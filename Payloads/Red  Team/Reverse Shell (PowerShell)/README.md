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

# 💻 PowerShell Reverse Shell

A BadUSB payload that establishes a PowerShell reverse shell from the target to an attacker's listener.

## ⚠️ Legal Warning

**CRITICAL: For authorized penetration testing and educational use only.**

Unauthorized use is **illegal** and violates:
- Computer Fraud and Abuse Act (CFAA) in the US
- Computer Misuse Act (CMA) in the UK
- Similar laws worldwide

You are fully responsible for your actions.

## 📋 Description

This payload opens a PowerShell process that connects back to your listener, giving you full interactive access to the target's command line.

## Requirements

- Windows 10/11
- PowerShell 5+
- A netcat listener (or equivalent) on your machine
- Direct network path to target (or via port forwarding)

## Setup

### 1. Start Your Listener

On your machine (Linux/Mac):
```bash
nc -lvp 4444
```

On Windows:
```bash
ncat -lvp 4444
```

### 2. Configure Payload

Replace `YOUR_IP` with your listener's IP:
- Use your **public IP** if target is external
- Use **localhost/tailscale IP** for internal pentests

Replace `YOUR_PORT` with your listener port (default: 4444).

### 3. Deployment

**CMD (one-liner):**
```batch
powershell -WindowStyle Hidden -NoExit -Command "[paste payload]"
```

**Rubber Ducky:**
1. Encode `payload.txt` at https://hak5.github.io/usbrubberducky-payloads/
2. Copy `inject.bin` to Ducky
3. Plug into target

## Why `-NoExit`?

The `-NoExit` flag keeps the PowerShell window open after the command runs, allowing the reverse shell to stay alive.

## Limitations

- **Two-way interactive shell** requires your listener to send commands
- **No file transfer** built in — you'd need additional commands
- **Modern Windows Defender** blocks this exact signature
- May need bypass: `-ExecutionPolicy Bypass`, AMSI bypass, etc.

## Detection

Defenders should monitor for:
- PowerShell with `-WindowStyle Hidden -NoExit`
- Outbound TCP connections on non-standard ports
- `System.Net.Sockets.TCPClient` creation
- Long-running hidden PowerShell processes

## License

MIT — use at your own risk.
