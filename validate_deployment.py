#!/usr/bin/env python3
"""
Deployment validation script for DAXXMUSIC Bot
Run this before deploying to ensure everything is configured correctly
"""

import os
import sys
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def color_text(text, color):
    """Add color to terminal output"""
    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'end': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['end']}"

def validate_env_var(name, required=True, validator=None):
    """Validate a single environment variable"""
    value = os.getenv(name)
    
    if not value:
        if required:
            return False, f"{name} is not set"
        else:
            return True, f"{name} is optional and not set"
    
    if validator and not validator(value):
        return False, f"{name} has invalid format"
    
    return True, f"{name} is configured"

def validate_bot_token(token):
    """Validate Telegram bot token format"""
    pattern = r'^\d+:[A-Za-z0-9_-]{35}$'
    return bool(re.match(pattern, token))

def validate_mongo_uri(uri):
    """Validate MongoDB URI format"""
    return uri.startswith(('mongodb://', 'mongodb+srv://'))

def check_file_exists(filepath):
    """Check if a file exists"""
    return os.path.exists(filepath)

def main():
    print(color_text("=" * 50, 'blue'))
    print(color_text("DAXXMUSIC Bot - Deployment Validator", 'blue'))
    print(color_text("=" * 50, 'blue'))
    print()
    
    errors = []
    warnings = []
    success = []
    
    # Check required environment variables
    print(color_text("Checking Required Environment Variables:", 'yellow'))
    
    required_vars = [
        ('API_ID', lambda x: x.isdigit()),
        ('API_HASH', lambda x: len(x) == 32),
        ('BOT_TOKEN', validate_bot_token),
        ('MONGO_DB_URI', validate_mongo_uri),
        ('OWNER_ID', lambda x: x.lstrip('-').isdigit()),
        ('STRING_SESSION', lambda x: len(x) > 100),
        ('LOGGER_ID', lambda x: x.startswith('-') and x[1:].isdigit())
    ]
    
    for var_name, validator in required_vars:
        valid, message = validate_env_var(var_name, required=True, validator=validator)
        if valid:
            print(color_text(f"  ✓ {message}", 'green'))
            success.append(message)
        else:
            print(color_text(f"  ✗ {message}", 'red'))
            errors.append(message)
    
    print()
    
    # Check optional environment variables
    print(color_text("Checking Optional Environment Variables:", 'yellow'))
    
    optional_vars = [
        'SPOTIFY_CLIENT_ID',
        'SPOTIFY_CLIENT_SECRET',
        'SUPPORT_CHANNEL',
        'SUPPORT_CHAT',
        'STRING_SESSION2',
        'STRING_SESSION3'
    ]
    
    for var_name in optional_vars:
        valid, message = validate_env_var(var_name, required=False)
        if os.getenv(var_name):
            print(color_text(f"  ✓ {message}", 'green'))
            success.append(message)
        else:
            print(color_text(f"  ⚠ {message}", 'yellow'))
            warnings.append(message)
    
    print()
    
    # Check required files
    print(color_text("Checking Required Files:", 'yellow'))
    
    required_files = [
        'Dockerfile',
        'requirements.txt',
        'config.py',
        'start',
        'DAXXMUSIC/__main__.py',
        'DAXXMUSIC/__init__.py'
    ]
    
    for filepath in required_files:
        if check_file_exists(filepath):
            print(color_text(f"  ✓ {filepath} exists", 'green'))
            success.append(f"{filepath} exists")
        else:
            print(color_text(f"  ✗ {filepath} not found", 'red'))
            errors.append(f"{filepath} not found")
    
    print()
    
    # Check Railway configuration
    print(color_text("Checking Railway Configuration:", 'yellow'))
    
    railway_files = ['railway.json', 'railway.toml']
    railway_found = False
    
    for filepath in railway_files:
        if check_file_exists(filepath):
            print(color_text(f"  ✓ {filepath} exists", 'green'))
            success.append(f"{filepath} exists")
            railway_found = True
            break
    
    if not railway_found:
        print(color_text(f"  ⚠ No Railway configuration file found", 'yellow'))
        warnings.append("No Railway configuration file found (optional)")
    
    print()
    print(color_text("=" * 50, 'blue'))
    print(color_text("Validation Summary:", 'blue'))
    print(color_text("=" * 50, 'blue'))
    print()
    
    print(f"✅ Success: {len(success)} checks passed")
    print(f"⚠️  Warnings: {len(warnings)} warnings")
    print(f"❌ Errors: {len(errors)} errors")
    
    print()
    
    if errors:
        print(color_text("❌ Deployment validation FAILED!", 'red'))
        print(color_text("Please fix the following errors:", 'red'))
        for error in errors:
            print(color_text(f"  - {error}", 'red'))
        print()
        print(color_text("Run 'python setup_bot.py' to configure the bot", 'yellow'))
        sys.exit(1)
    else:
        print(color_text("✅ Deployment validation PASSED!", 'green'))
        print(color_text("Your bot is ready for deployment!", 'green'))
        print()
        
        if warnings:
            print(color_text("⚠️  Warnings (optional):", 'yellow'))
            for warning in warnings:
                print(color_text(f"  - {warning}", 'yellow'))
            print()
        
        print(color_text("Next steps:", 'blue'))
        print("1. Push your code to GitHub")
        print("2. Deploy on Railway using:")
        print("   - Railway CLI: railway up")
        print("   - Railway Dashboard: Connect GitHub repo")
        print("3. Add environment variables in Railway dashboard")
        print("4. Your bot will start automatically!")

if __name__ == "__main__":
    main()