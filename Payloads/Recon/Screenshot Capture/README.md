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

# 📸 Screenshot Capture Payload

A BadUSB payload that captures a screenshot of the target's desktop and uploads it to a Discord webhook.

## ⚠️ Legal Warning

**For authorized penetration testing and educational use only.**

Unauthorized use is illegal. You are responsible for your own actions.

## Description

When executed, this payload:
1. Captures the entire primary screen
2. Saves as PNG to temp folder
3. Sends a Discord notification message
4. Uploads the screenshot as a file attachment
5. Cleans up

## Requirements

- Windows 10/11
- PowerShell (built-in)
- .NET Framework (built-in)
- A Discord webhook URL

## Setup

1. Create a Discord webhook (Server Settings → Integrations)
2. Replace `YOUR_DISCORD_WEBHOOK_URL` with your webhook
3. **Never commit the real webhook to git**

## Deployment

**Direct CMD (as Admin):**
```batch
powershell -NoProfile -ExecutionPolicy Bypass -Command "[paste payload here]"
```

**For Rubber Ducky:**
1. Encode `payload.txt` at https://hak5.github.io/usbrubberducky-payloads/
2. Copy `inject.bin` to Ducky
3. Plug into target

## Testing

Test in a VM first:
1. Open VirtualBox/VMware
2. Create Windows 10 VM
3. Set up some visible content on desktop
4. Run the payload
5. Verify Discord receives the screenshot

## Detection

Defenders should monitor for:
- PowerShell with `System.Windows.Forms` and `System.Drawing` loaded
- `CopyFromScreen` API calls
- Outbound Discord traffic
- `screen.png` in temp folders

## License

MIT — use at your own risk.
