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

# 💀 Full-Screen Fake BSOD Prank

A BadUSB prank that downloads an image of a fake Blue Screen of Death and displays it fullscreen with no way to close it normally.

## ⚠️ Disclaimer

**This is a joke payload for friends who'll find it funny.**

- Do **NOT** use on work/school computers
- The image requires internet to download (first time)
- **Ctrl + Alt + Del** to Task Manager closes it (this is the escape hatch)
- No permanent damage, no files left behind

## 📋 What It Does

1. Downloads a fake BSOD image from the configured URL to `%TEMP%\bsod.png`
2. Opens a fullscreen window with **no borders, title bar, or close button**
3. **Blocks Alt+F4** so they can't close it with the keyboard shortcut
4. Scales the image to fit the screen while keeping aspect ratio
5. Centers it perfectly
6. Always on top (covers taskbar)
7. **Only Ctrl+Alt+Del works** — opens Task Manager, which can close it

## 🛠️ Requirements

- Windows 10/11
- USB Rubber Ducky (or compatible HID device)
- Internet connection (for the image)
- PowerShell (built-in)
- .NET Framework (built-in)

## 🔧 Setup

1. Save as `payload.txt`
2. Encode at https://hak5.github.io/usbrubberducky-payloads/
3. Copy `inject.bin` to your Ducky
4. Plug into target
5. Watch the panic

## 🎨 Image Source

Default image: A classic fake BSOD from `silicon.co.uk`

**To change the image:**
Replace the URL in the payload with any direct link to a PNG/JPG:
```powershell
$u='https://your-image-url.com/something.png'
```

Good image sources for fake BSODs:
- Google "fake blue screen of death png"
- Use any image hosting (Imgur, GitHub, etc.)
- Even a screenshot of a real BSOD works

## 🛑 How to Stop It

**Only one way:** Press **Ctrl + Alt + Del** to open Task Manager.

In Task Manager:
1. Find "Windows PowerShell" in the Processes tab
2. Right-click → End Task
3. The fake BSOD will close

Or just **reboot** the computer.

## ⚖️ Legal

For pranks among consenting friends only. Don't be a jerk.

## 📜 License

MIT — prank responsibly.
