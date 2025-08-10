# 🎵 DAXX MUSIC BOT - Ultimate Telegram Music Bot

<p align="center">
  <img src="https://telegra.ph/file/cfbdee8103102bcb2e5da.jpg" alt="DAXX Music Logo" width="300">
</p>

<p align="center">
  <a href="https://github.com/DAXXTEAM/DAXXMUSIC/stargazers"><img src="https://img.shields.io/github/stars/DAXXTEAM/DAXXMUSIC?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/DAXXTEAM/DAXXMUSIC/network/members"><img src="https://img.shields.io/github/forks/DAXXTEAM/DAXXMUSIC?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/DAXXTEAM/DAXXMUSIC/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-v3.10-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Python"></a>
</p>

## 🚀 Deploy to Railway (Recommended)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/daxxmusic)

## ✨ Features

### 🎵 Music Features
- **Multi-Platform Support**: YouTube, Spotify, SoundCloud, Apple Music, Resso
- **High Quality Streaming**: Crystal clear audio up to 320kbps
- **Video Support**: Stream videos in voice chats
- **Live Streams**: Support for YouTube live streams
- **Queue Management**: Advanced queue with shuffle, loop, and seek
- **Lyrics Display**: Auto-fetch and display song lyrics
- **Playlist Support**: Create and manage playlists

### 🛠️ Bot Features
- **Multi-Language**: Support for English, Hindi, Arabic, Punjabi
- **Multi-Assistant**: Up to 5 assistant accounts for lag-free music
- **Auto-Leave**: Automatically leaves inactive voice chats
- **Channel Play**: Play music in channels
- **Force Play**: Priority queue for admins
- **Clean Mode**: Auto-delete bot messages
- **Broadcast**: Send messages to all users
- **Statistics**: Track bot usage and stats

### 👮 Admin Features
- **Full Control**: Pause, Resume, Skip, Stop, Shuffle
- **Volume Control**: Adjust playback volume
- **Auth Users**: Authorize users to use admin commands
- **Blacklist**: Ban users from using the bot
- **Maintenance Mode**: Temporary disable bot for updates

## 📋 Prerequisites

Before deploying, you need:

1. **Telegram API Credentials**
   - Get `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org)

2. **Bot Token**
   - Create a bot via [@BotFather](https://t.me/BotFather)
   - Get your bot token

3. **MongoDB Database**
   - Create free account at [MongoDB Atlas](https://cloud.mongodb.com)
   - Create a cluster and get connection URI

4. **Pyrogram Session String**
   - Run the session generator script (see below)

## 🚂 Railway Deployment Guide

### Step 1: Prepare Your Repository

1. Fork this repository to your GitHub account
2. Clone to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/DAXXMUSIC.git
cd DAXXMUSIC
```

### Step 2: Generate Session String

Run the session generator:
```bash
python generate_session.py
```

Enter your API credentials when prompted. Save the generated session string.

### Step 3: Configure Environment Variables

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Fill in all required variables:
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
OWNER_ID=your_user_id
STRING_SESSION=your_session_string
LOGGER_ID=your_logger_group_id
```

### Step 4: Deploy to Railway

#### Method 1: Using Railway CLI

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login to Railway:
```bash
railway login
```

3. Initialize project:
```bash
railway init
```

4. Link to Railway project:
```bash
railway link
```

5. Deploy:
```bash
railway up
```

#### Method 2: Using GitHub Integration

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your forked repository
4. Railway will auto-detect the Dockerfile
5. Add environment variables in Railway dashboard
6. Click "Deploy"

### Step 5: Configure Environment in Railway

1. Go to your project in Railway Dashboard
2. Click on "Variables" tab
3. Add all required environment variables:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `MONGO_DB_URI`
   - `OWNER_ID`
   - `STRING_SESSION`
   - `LOGGER_ID`

4. Optional variables for enhanced features:
   - `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` for Spotify
   - `SUPPORT_CHANNEL` and `SUPPORT_CHAT` for support links

### Step 6: Monitor Deployment

1. Check deployment logs in Railway dashboard
2. Wait for the build to complete
3. Your bot should automatically start

## 🔧 Local Development

### Setup Local Environment

1. Install Python 3.10+
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file with your credentials
4. Run the bot:
```bash
python -m DAXXMUSIC
```

## 📝 Commands

### 🎵 Play Commands
- `/play [song name/url]` - Play a song
- `/vplay [song name/url]` - Play video
- `/playlist` - Show queue
- `/lyrics` - Get song lyrics

### ⏸️ Control Commands
- `/pause` - Pause playback
- `/resume` - Resume playback
- `/skip` - Skip current song
- `/stop` - Stop playback
- `/volume [1-100]` - Set volume

### 👤 User Commands
- `/start` - Start the bot
- `/help` - Show help menu
- `/ping` - Check bot latency
- `/stats` - Bot statistics

### 👮 Admin Commands
- `/auth` - Authorize a user
- `/unauth` - Unauthorize a user
- `/shuffle` - Shuffle queue
- `/loop` - Loop current song
- `/seek [seconds]` - Seek to position

## 🐛 Troubleshooting

### Bot Not Starting?
- Check all environment variables are set correctly
- Verify MongoDB URI is valid
- Ensure bot token is correct
- Check session string is valid

### Music Not Playing?
- Ensure assistant account has joined the chat
- Check if bot has admin permissions
- Verify the assistant can access voice chat

### Railway Specific Issues
- Check deployment logs for errors
- Ensure Dockerfile builds successfully
- Verify all dependencies are installed
- Check memory usage (upgrade if needed)

## 🔒 Security Best Practices

1. **Never share your session string**
2. **Use environment variables for sensitive data**
3. **Regularly update dependencies**
4. **Use separate Telegram account for assistant**
5. **Enable 2FA on all accounts**

## 📊 Performance Optimization

### For Railway:
- Start with 512MB RAM (upgrade if needed)
- Enable auto-restart on failure
- Use health checks for monitoring
- Configure proper logging

### Database:
- Use MongoDB Atlas with proper indexing
- Enable connection pooling
- Regular backups

## 🤝 Support

- **Support Chat**: [Join Here](https://t.me/DAXXMUSIC_SUPPORT)
- **Updates Channel**: [Join Here](https://t.me/DAXXMUSIC_UPDATES)
- **Issues**: [GitHub Issues](https://github.com/DAXXTEAM/DAXXMUSIC/issues)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Py-TgCalls](https://github.com/pytgcalls/pytgcalls)
- [Railway](https://railway.app)
- All contributors and supporters

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/DAXXTEAM">DAXX TEAM</a>
</p>

<p align="center">
  <i>If you like this project, please star ⭐ the repository!</i>
</p>