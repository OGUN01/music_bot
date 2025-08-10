@echo off
title DAXX Music Bot - Railway Deployment

echo ======================================
echo    DAXX Music Bot - Railway Deploy    
echo ======================================
echo.

REM Check if Railway CLI is installed
where railway >nul 2>nul
if %errorlevel% neq 0 (
    echo Railway CLI is not installed!
    echo Installing Railway CLI...
    npm install -g @railway/cli
    
    if %errorlevel% neq 0 (
        echo Failed to install Railway CLI
        echo Please install manually: npm install -g @railway/cli
        pause
        exit /b 1
    )
)

REM Check if .env file exists
if not exist .env (
    echo No .env file found!
    echo Running setup script...
    python setup_bot.py
    
    if %errorlevel% neq 0 (
        echo Setup failed! Please run manually: python setup_bot.py
        pause
        exit /b 1
    )
)

REM Validate deployment
echo.
echo Validating deployment configuration...
python validate_deployment.py

if %errorlevel% neq 0 (
    echo Validation failed! Please fix the errors above.
    pause
    exit /b 1
)

echo.
echo Configuration validated successfully!
echo.

REM Railway deployment
echo Starting Railway deployment...
echo.

REM Login to Railway
echo Logging in to Railway...
railway login

if %errorlevel% neq 0 (
    echo Railway login failed!
    pause
    exit /b 1
)

REM Initialize Railway project
echo.
echo Initializing Railway project...
railway init

REM Link to project
echo.
echo Linking to Railway project...
railway link

REM Deploy
echo.
echo Deploying to Railway...
railway up

if %errorlevel% equ 0 (
    echo.
    echo ======================================
    echo    Deployment Successful! 
    echo ======================================
    echo.
    echo Your bot is being deployed to Railway!
    echo.
    echo Next steps:
    echo 1. Go to your Railway dashboard
    echo 2. Add environment variables if not already set
    echo 3. Monitor the deployment logs
    echo 4. Your bot will start automatically!
    echo.
    echo Dashboard: https://railway.app/dashboard
) else (
    echo.
    echo Deployment failed!
    echo Please check the error messages above.
)

pause