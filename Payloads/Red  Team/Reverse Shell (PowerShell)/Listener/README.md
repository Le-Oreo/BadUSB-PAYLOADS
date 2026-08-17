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

# 🎧 ATTP Listener

A standalone Python listener for catching reverse shells from BadUSB payloads.

## ⚠️ Disclaimer

For **authorized penetration testing and education only.** Unauthorized use is illegal.

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Install

If you don't have Python:
1. Download from https://python.org/downloads/
2. **Check "Add Python to PATH"** during install
3. Restart CMD

## Run

**Easy way (Windows):**
```batch
listener.bat 4444
```

**Direct way:**
```bash
python listener.py 4444
```

Default port is `4444`. Use any port you want.

## Features

- 🎨 Colored output
- 📝 Auto session logging
- 📂 Loot folder for downloads
- 🔄 Multi-session support
- ⏯️ Background sessions
- 📥 File transfer (download)
- 🔍 Session management

## Commands

```
sessions       List active sessions
interact <id>  Connect to session
kill <id>      Kill session
killall        Kill all sessions
clear          Clear screen
exit           Stop listener
```

## Usage With BadUSB

1. Run listener: `python listener.py 4444`
2. Note the IP address shown (e.g., `192.168.1.100:4444`)
3. Update your payload to use that IP
4. Plug in USB / run payload
5. When connection comes in, type `interact 1`

## License

MIT
