#!/usr/bin/env python3
"""
Script to generate Pyrogram session string for DAXXMUSIC bot
"""
import asyncio
from pyrogram import Client

print("🎵 DAXXMUSIC Bot - Session String Generator 🎵")
print("=" * 50)
print("This will generate a session string for your Telegram account.")
print("⚠️  IMPORTANT: Use a separate Telegram account for the music bot!")
print("=" * 50)

async def generate_session():
    try:
        # Get user inputs
        api_id = input("Enter your API_ID: ").strip()
        api_hash = input("Enter your API_HASH: ").strip()
        
        if not api_id or not api_hash:
            print("❌ API_ID and API_HASH cannot be empty!")
            return
        
        api_id = int(api_id)
        
        print("\n📱 You will receive an OTP on your Telegram account.")
        print("📱 If you have 2FA enabled, you'll need your password too.")
        
        # Create client
        client = Client(
            "music_bot_session",
            api_id=api_id,
            api_hash=api_hash,
            in_memory=True
        )
        
        # Start client and generate session
        await client.start()
        session_string = await client.export_session_string()
        
        print("\n🎉 SUCCESS! Session string generated:")
        print("=" * 50)
        print(f"STRING_SESSION: {session_string}")
        print("=" * 50)
        
        # Get user info
        me = await client.get_me()
        print(f"\n👤 Account Info:")
        print(f"Name: {me.first_name} {me.last_name or ''}")
        print(f"Username: @{me.username or 'No username'}")
        print(f"User ID: {me.id}")
        print("=" * 50)
        
        print("\n📝 Save this information:")
        print(f"OWNER_ID={me.id}")
        print(f"STRING_SESSION={session_string}")
        
        await client.stop()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure you have:")
        print("- Correct API_ID and API_HASH")
        print("- Active internet connection")
        print("- The account can receive SMS/calls")

if __name__ == "__main__":
    asyncio.run(generate_session())