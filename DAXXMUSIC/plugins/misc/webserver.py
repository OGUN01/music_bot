"""
Simple HTTP server for health checks
Runs alongside the bot for Render compatibility
"""
import asyncio
import json
from aiohttp import web
from DAXXMUSIC.utils.health import get_health_status
from DAXXMUSIC import LOGGER

async def health_handler(request):
    """Health check endpoint for Render"""
    try:
        status = await get_health_status()
        return web.json_response(status, status=200 if status["status"] == "healthy" else 503)
    except Exception as e:
        LOGGER(__name__).error(f"Health check failed: {e}")
        return web.json_response({"status": "error", "message": str(e)}, status=500)

async def root_handler(request):
    """Root endpoint"""
    return web.json_response({
        "name": "DAXX Music Bot",
        "status": "running",
        "endpoints": {
            "/": "Bot information",
            "/health": "Health check"
        }
    })

async def start_webserver():
    """Start the web server"""
    try:
        app = web.Application()
        app.router.add_get('/', root_handler)
        app.router.add_get('/health', health_handler)
        
        runner = web.AppRunner(app)
        await runner.setup()
        
        # Use port from environment or default to 8000
        import os
        port = int(os.environ.get('PORT', 8000))
        
        site = web.TCPSite(runner, '0.0.0.0', port)
        await site.start()
        
        LOGGER(__name__).info(f"Health check server started on port {port}")
        return runner
    except Exception as e:
        LOGGER(__name__).error(f"Failed to start web server: {e}")
        return None

# Auto-start web server when module loads
asyncio.create_task(start_webserver())