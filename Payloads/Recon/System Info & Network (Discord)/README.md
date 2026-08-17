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

# 🔍 System & Network Recon

A BadUSB payload that gathers comprehensive system and network information and uploads it to a Discord webhook.

## ⚠️ Legal Warning

**For authorized penetration testing and educational use only.**

## Description

This payload extracts:
- **System Info**: hostname, user, OS, CPU, RAM
- **Network Info**: local IPs, public IP, adapters, ARP table
- **Wi-Fi**: saved profiles
- **Routes & DNS**: routing table, DNS servers
- **Connections**: active network connections
- **USB Devices**: connected USB hardware

## Requirements

- Windows 10/11
- PowerShell 5+
- Internet connection (for public IP)
- Discord webhook URL

## Setup

1. Create Discord webhook
2. Replace `YOUR_DISCORD_WEBHOOK_URL` in payload
3. **Never commit the real webhook**

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

**Discord message:**
```
Recon Bot
System & Network Recon from ANTHONYSPC
```

**File (`recon.txt`):**
```
=== SYSTEM INFO ===
Hostname: ANTHONYSPC
User: antma
OS: Microsoft Windows 11 Pro
Arch: AMD64
CPU: AMD Ryzen 7 5800X
RAM: 32 GB

=== NETWORK INFO ===

Local IPs:
  - 192.168.1.100 (Wi-Fi)
  - 10.0.0.50 (Ethernet)

Public IP: 73.42.18.99

=== ADAPTERS ===
...
```

## Detection

Defenders should monitor for:
- Multiple WMI/CIM queries in quick succession
- `ipconfig /all`, `arp -a`, `route print` execution
- Outbound IP lookup queries (ipify.org)
- Discord webhook traffic

## License

MIT — use at your own risk.
