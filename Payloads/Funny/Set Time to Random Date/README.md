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

# ⏰ Random Time Prank

A BadUSB prank that sets the system clock to a random date between 1990 and 2050.

## ⚠️ Disclaimer

**Friendly prank only.** Setting the wrong time can break:
- SSL/TLS certificates (browser warnings)
- Authentication tokens
- Scheduled tasks
- File timestamps

Use carefully.

## 📋 What It Does

- Sets system clock to a random year/month/day/hour/minute/second
- Range: 1990-01-01 to 2049-12-31
- Persistent until fixed manually

## 🛑 How to Fix

1. Right-click clock in taskbar → "Adjust date and time"
2. Toggle "Set time automatically" off and back on
3. Or run: `w32tm /resync`

## 📜 License

MIT
