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

# 🔓 UAC Bypass — Fodhelper Method

A BadUSB payload that attempts to bypass User Account Control (UAC) using the Fodhelper hijack technique.

## ⚠️ Legal Warning

**For authorized penetration testing only.** Unauthorized use is illegal.

## 📋 Description

The Fodhelper UAC bypass exploits the way Windows handles `ms-settings` URI scheme. By:
1. Adding a registry entry under `HKCU\Software\Classes\ms-settings\shell\open\command`
2. Setting the value to a custom command (e.g., elevated cmd)
3. Triggering the `ms-settings:` protocol via `fodhelper.exe`
4. Windows runs the custom command **with elevated privileges** without UAC prompt

This is a well-documented technique (CVE-2017-8464 & similar).

## Requirements

- Windows 10/11 (works on most versions, **patched in newer builds**)
- Target must be in a **high UAC level** (default)
- Target must have Fodhelper (most do)
- **No admin required** — that's the point of the bypass

## How It Works

```
1. Attacker's command stored in HKCU registry
2. fodhelper.exe runs auto-elevated (it has a UAC manifest)
3. Windows reads the registry value instead of the legitimate setting
4. Attacker's command executes AS ADMIN
```

## Cleanup

The payload cleans up after itself by deleting the registry key.

## Detection

Defenders should monitor for:
- `fodhelper.exe` execution from non-elevated processes
- Registry writes to `HKCU\Software\Classes\ms-settings`
- New elevated processes spawned after non-elevated application

## Limitations

- **Patched in Windows 10 1709+**
- Many EDRs detect this exact technique
- May trigger Defender alerts
- Requires `fodhelper.exe` to exist (can be disabled)

## License

MIT — use at your own risk.
