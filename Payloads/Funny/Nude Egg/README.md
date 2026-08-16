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

# 🥚 Naked Egg Prank

A harmless BadUSB prank that opens Notepad with a naked egg and respawns it as fast as possible when closed.

## ⚠️ Disclaimer

**This is a joke payload for friends who'll find it funny.**

- Do **NOT** use on:
  - Work computers
  - School computers  
  - Anyone who won't laugh
  - Strangers
  - Yourself when you have unsaved work (seriously)
- The respawn loop runs until killed via Task Manager
- No permanent damage, no data theft, no system changes
- Just eggs. Lots of eggs.

## 📋 What It Does

1. Opens Notepad
2. Fills it with an ASCII egg message
3. Starts a hidden PowerShell loop that:
   - Closes any Notepad window after a few seconds
   - Opens a new one immediately
   - Repeats forever (until killed)

## 🛠️ Requirements

- Windows 10/11
- USB Rubber Ducky (or compatible HID device)
- A friend with a sense of humor

## 🔧 Setup

1. Save as `payload.txt`
2. Encode at https://hak5.github.io/usbrubberducky-payloads/
3. Copy `inject.bin` to your Ducky
4. Plug into victim's computer
5. Run away

## 🛑 How to Stop It

The victim needs to:
1. Press `Ctrl + Shift + Esc` to open Task Manager
2. Find "Windows PowerShell" in the Processes tab
3. Right-click → End Task
4. Close any remaining Notepad windows
5. **Reboot** to be safe

Or just unplug the Ducky quickly and pretend nothing happened.

## 🎨 Variations

- Replace the message with anything funny
- Adjust the respawn timer (currently a few hundred milliseconds)
- Combine with other pranks

## ⚖️ Legal

For pranks among consenting friends only. Don't be a jerk.

## 📜 License

MIT — prank responsibly.
