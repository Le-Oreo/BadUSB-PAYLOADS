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

# 🛡️ Disable Windows Defender Payload

A BadUSB payload that disables Windows Defender real-time protection and related security features.

## ⚠️ Legal Warning

**For authorized penetration testing and educational use only.**

Unauthorized use against systems you don't own is illegal.

## Description

This payload disables:
- Real-time monitoring
- Behavior monitoring
- Cloud-delivered protection
- Sample submission to Microsoft
- Tamper Protection (via registry)
- Telemetry (MAPS reporting)

## ⚠️ Limitations

- **Tamper Protection** (Windows 10 1903+) may block registry changes
- Must run as **Administrator**
- **Group Policy** can override these settings
- Enterprise/managed Defender cannot be disabled this way

## Requirements

- Windows 10/11
- Administrator privileges
- USB Rubber Ducky (or compatible HID device)
- Target must have Tamper Protection disabled (manually) OR vulnerable Windows version

## Setup

1. Test on your own system first
2. Adjust payload for your target environment
3. **Only use on authorized targets**

## Deployment

**CMD (as Admin):**
```batch
powershell -NoProfile -ExecutionPolicy Bypass -Command "[paste payload]"
```

**Rubber Ducky:**
1. Encode `payload.txt` at https://hak5.github.io/usbrubberducky-payloads/
2. Copy `inject.bin` to Ducky
3. Plug into target

## Detection

Defenders should monitor for:
- `Set-MpPreference` cmdlet usage
- Registry changes to `HKLM:\SOFTWARE\Microsoft\Windows Defender`
- `WinDefend` service restarts
- Tamper Protection disabled events

## Cleanup / Re-Enable

To re-enable Defender:
```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows Defender\Features" -Name "TamperProtection" -Value 1
```

## License

MIT — use at your own risk.
