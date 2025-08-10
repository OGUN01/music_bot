#!/bin/bash

# DAXX Music Bot - Quick Railway Deployment Script

echo "======================================"
echo "   DAXX Music Bot - Railway Deploy    "
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo -e "${RED}Railway CLI is not installed!${NC}"
    echo "Installing Railway CLI..."
    npm install -g @railway/cli
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to install Railway CLI${NC}"
        echo "Please install manually: npm install -g @railway/cli"
        exit 1
    fi
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}No .env file found!${NC}"
    echo "Running setup script..."
    python setup_bot.py
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}Setup failed! Please run manually: python setup_bot.py${NC}"
        exit 1
    fi
fi

# Validate deployment
echo ""
echo "Validating deployment configuration..."
python validate_deployment.py

if [ $? -ne 0 ]; then
    echo -e "${RED}Validation failed! Please fix the errors above.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}Configuration validated successfully!${NC}"
echo ""

# Railway deployment
echo "Starting Railway deployment..."
echo ""

# Login to Railway
echo "Logging in to Railway..."
railway login

if [ $? -ne 0 ]; then
    echo -e "${RED}Railway login failed!${NC}"
    exit 1
fi

# Initialize Railway project
echo ""
echo "Initializing Railway project..."
railway init

# Link to project
echo ""
echo "Linking to Railway project..."
railway link

# Deploy
echo ""
echo "Deploying to Railway..."
railway up

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}======================================"
    echo "   Deployment Successful! 🎉"
    echo "======================================${NC}"
    echo ""
    echo "Your bot is being deployed to Railway!"
    echo ""
    echo "Next steps:"
    echo "1. Go to your Railway dashboard"
    echo "2. Add environment variables if not already set"
    echo "3. Monitor the deployment logs"
    echo "4. Your bot will start automatically!"
    echo ""
    echo "Dashboard: https://railway.app/dashboard"
else
    echo ""
    echo -e "${RED}Deployment failed!${NC}"
    echo "Please check the error messages above."
    exit 1
fi