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

# 📁 Desktop/Documents ZIP Extractor

A BadUSB payload that zips up the user's Desktop, Documents, and Downloads folders and uploads them to a Discord webhook.

## ⚠️ Legal Warning

**For authorized penetration testing and educational use only.** Unauthorized use is illegal and unethical.

## 📋 Description

This payload:
1. Creates a ZIP file containing:
   - Desktop contents
   - Documents contents
   - Downloads contents
2. Uploads to a Discord webhook (if under 24MB)
3. Cleans up the temp ZIP

## Requirements

- Windows 10/11
- PowerShell 5+
- .NET Framework
- Discord webhook URL
- Target must have files in Desktop/Documents/Downloads

## Setup

1. Create Discord webhook
2. Replace `YOUR_DISCORD_WEBHOOK_URL`
3. **Never commit real webhook**

## Deployment

**CMD (as Admin):**
```batch
powershell -NoProfile -ExecutionPolicy Bypass -Command "[paste payload]"
```

**Rubber Ducky:**
1. Encode `payload.txt` at https://hak5.github.io/usbrubberducky-payloads/
2. Copy `inject.bin` to Ducky
3. Plug into target

## Limitations

- Discord has a **24MB file upload limit** — large file collections will fail
- Some files (locked, in use) won't be included
- Files outside Desktop/Documents/Downloads are not collected

## Detection

Defenders should monitor for:
- PowerShell with `System.IO.Compression.FileSystem` loaded
- ZIP file creation in `%TEMP%`
- File system reads of Desktop/Documents/Downloads
- Outbound Discord traffic with large attachments

## License

MIT — use at your own risk.
