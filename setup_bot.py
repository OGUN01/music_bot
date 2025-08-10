#!/usr/bin/env python3
"""
Interactive setup script for DAXXMUSIC bot deployment
"""
import os
import re

def validate_bot_token(token):
    """Validate Telegram bot token format"""
    pattern = r'^\d+:[A-Za-z0-9_-]{35}$'
    return bool(re.match(pattern, token))

def validate_mongo_uri(uri):
    """Validate MongoDB URI format"""
    return uri.startswith(('mongodb://', 'mongodb+srv://'))

def get_user_input(prompt, validator=None, required=True):
    """Get and validate user input"""
    while True:
        value = input(prompt).strip()
        
        if not value and required:
            print("❌ This field is required!")
            continue
        
        if validator and value and not validator(value):
            print("❌ Invalid format!")
            continue
        
        return value

def main():
    print("🎵 DAXXMUSIC Bot Setup Wizard 🎵")
    print("=" * 50)
    
    env_vars = {}
    
    # Get API credentials
    print("\n📡 Telegram API Credentials:")
    print("Get these from: https://my.telegram.org")
    env_vars['API_ID'] = get_user_input("Enter API_ID: ", lambda x: x.isdigit())
    env_vars['API_HASH'] = get_user_input("Enter API_HASH: ")
    
    # Get bot token
    print("\n🤖 Bot Configuration:")
    print("Get bot token from: @BotFather")
    env_vars['BOT_TOKEN'] = get_user_input(
        "Enter BOT_TOKEN: ", 
        validate_bot_token
    )
    
    # Get session string
    print("\n👤 User Session:")
    print("Generate using: python generate_session.py")
    env_vars['STRING_SESSION'] = get_user_input("Enter STRING_SESSION: ")
    
    # Get owner ID
    env_vars['OWNER_ID'] = get_user_input(
        "Enter OWNER_ID (your Telegram user ID): ",
        lambda x: x.isdigit()
    )
    
    # Get MongoDB URI
    print("\n🗄️ Database Configuration:")
    print("Get free MongoDB from: https://cloud.mongodb.com")
    env_vars['MONGO_DB_URI'] = get_user_input(
        "Enter MONGO_DB_URI: ",
        validate_mongo_uri
    )
    
    # Get logger ID
    print("\n📋 Logging Configuration:")
    print("Create a Telegram group, add bot as admin, get group ID")
    env_vars['LOGGER_ID'] = get_user_input(
        "Enter LOGGER_ID (group ID with -): ",
        lambda x: x.startswith('-') and x[1:].isdigit()
    )
    
    # Optional configurations
    print("\n⚙️ Optional Configurations:")
    env_vars['HEROKU_APP_NAME'] = get_user_input(
        "Enter HEROKU_APP_NAME (optional): ", 
        required=False
    )
    env_vars['HEROKU_API_KEY'] = get_user_input(
        "Enter HEROKU_API_KEY (optional): ", 
        required=False
    )
    
    # Create .env file
    env_content = ""
    for key, value in env_vars.items():
        if value:
            env_content += f"{key}={value}\n"
    
    # Write to .env file
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n✅ Configuration saved to .env file!")
    print("\n📋 Next Steps:")
    print("1. Push code to GitHub repository")
    print("2. Deploy on Railway: https://railway.app")
    print("3. Import environment variables from .env")
    print("4. Start deployment!")
    
    # Display Railway deployment commands
    print("\n🚂 Railway Commands:")
    print("railway login")
    print("railway link")
    print("railway up")
    
    print("\n🎉 Setup Complete! Your bot is ready for deployment.")

if __name__ == "__main__":
    main()