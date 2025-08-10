"""
Health check system for DAXXMUSIC bot
Provides status monitoring and validation
"""
import asyncio
import time
from datetime import datetime
from pyrogram import Client
from pyrogram.errors import FloodWait
import config
from DAXXMUSIC import app
from DAXXMUSIC.core.mongo import mongodb

class HealthCheck:
    def __init__(self):
        self.start_time = time.time()
        self.checks = {
            "bot": False,
            "database": False,
            "assistants": False,
            "apis": False
        }
    
    async def check_bot_status(self):
        """Check if bot is running and responsive"""
        try:
            me = await app.get_me()
            self.checks["bot"] = True if me else False
            return self.checks["bot"]
        except Exception as e:
            print(f"Bot check failed: {e}")
            self.checks["bot"] = False
            return False
    
    async def check_database(self):
        """Check MongoDB connection"""
        try:
            # Test database connection
            await mongodb.server_info()
            self.checks["database"] = True
            return True
        except Exception as e:
            print(f"Database check failed: {e}")
            self.checks["database"] = False
            return False
    
    async def check_assistants(self):
        """Check if at least one assistant is configured"""
        try:
            if config.STRING1:
                self.checks["assistants"] = True
                return True
            self.checks["assistants"] = False
            return False
        except Exception as e:
            print(f"Assistant check failed: {e}")
            self.checks["assistants"] = False
            return False
    
    async def check_apis(self):
        """Check if required APIs are configured"""
        try:
            required = [
                config.API_ID,
                config.API_HASH,
                config.BOT_TOKEN,
                config.MONGO_DB_URI
            ]
            self.checks["apis"] = all(required)
            return self.checks["apis"]
        except Exception as e:
            print(f"API check failed: {e}")
            self.checks["apis"] = False
            return False
    
    async def get_status(self):
        """Get complete health status"""
        await self.check_bot_status()
        await self.check_database()
        await self.check_assistants()
        await self.check_apis()
        
        uptime = time.time() - self.start_time
        hours, remainder = divmod(int(uptime), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return {
            "status": "healthy" if all(self.checks.values()) else "unhealthy",
            "uptime": f"{hours}h {minutes}m {seconds}s",
            "checks": self.checks,
            "timestamp": datetime.now().isoformat()
        }
    
    async def validate_deployment(self):
        """Validate deployment configuration"""
        errors = []
        warnings = []
        
        # Check required environment variables
        required_vars = {
            "API_ID": config.API_ID,
            "API_HASH": config.API_HASH,
            "BOT_TOKEN": config.BOT_TOKEN,
            "MONGO_DB_URI": config.MONGO_DB_URI,
            "OWNER_ID": config.OWNER_ID,
            "STRING_SESSION": config.STRING1,
            "LOGGER_ID": config.LOGGER_ID
        }
        
        for var_name, var_value in required_vars.items():
            if not var_value:
                errors.append(f"Missing required: {var_name}")
        
        # Check optional but recommended
        if not config.SPOTIFY_CLIENT_ID:
            warnings.append("Spotify integration not configured")
        
        # Validate bot token format
        if config.BOT_TOKEN and not ":" in config.BOT_TOKEN:
            errors.append("Invalid BOT_TOKEN format")
        
        # Validate MongoDB URI
        if config.MONGO_DB_URI and not config.MONGO_DB_URI.startswith(("mongodb://", "mongodb+srv://")):
            errors.append("Invalid MONGO_DB_URI format")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }

# Initialize health checker
health_checker = HealthCheck()

async def get_health_status():
    """Get current health status"""
    return await health_checker.get_status()

async def validate_config():
    """Validate configuration"""
    return await health_checker.validate_deployment()