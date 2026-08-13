# 🥚 The Unclosable Egg Prank

A harmless BadUSB prank that opens Notepad and floods it with 🥚 eggs. If the user closes Notepad, it respawns. Lasts until the script is killed or the computer is restarted.

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
2. Fills it with a wall of 🥚 emojis
3. Starts a hidden PowerShell loop that:
   - Closes any Notepad window after 5 seconds
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

- Replace 🥚 with 💀, 🐸, 🍆, 🦆, or any emoji
- Add a custom message:
  ```
  STRING Hey {name}! You got egged! 🥚
  ```
- Change the respawn timer (currently 5 seconds)
- Add a rickroll URL in the text

## ⚖️ Legal

For pranks among consenting friends only. Don't be a jerk.

## 📜 License

MIT — prank responsibly.
