
# WhatsApp Automatic Message Sender

This Python project allows you to automatically send messages to a list of contacts through **WhatsApp Web** using **Selenium**.

---

## Features

- Saves WhatsApp Web browser session (no need to scan QR code every time)
- Sends automatic messages to multiple numbers
- Shows detailed error messages if sending fails

---

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

---

## Installation

1. **Clone or Download the Project**

```bash
git clone https://github.com/yourusername/whatsapp-message-bot.git
cd whatsapp-message-bot
```

2. **Install Python Packages**

```bash
pip install selenium
```

3. **Download ChromeDriver**

- Find your Chrome version:  
  Chrome → Settings → About Chrome.
- Download the matching ChromeDriver version:  
  👉 [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

4. **Edit Configuration**

- Update `chrome_driver_path` in `yeni.py` to your own ChromeDriver path:

```python
chrome_driver_path = "C:/Path/To/chromedriver.exe"
```

5. **Prepare Your Files**

- **`numbers.txt`** → List of phone numbers (country code included, no spaces, no plus sign)
- **`text.txt`** → The message you want to send

---

## Usage

Run the script:

```bash
python yeni.py
```

1. Chrome will open WhatsApp Web.
2. Scan the QR code if prompted.
3. Script sends the message to each number from the list.
4. Done!

✅ Your session will be saved, and no need to scan QR again next time.

---

## Simple Flow Diagram

---

## Important Notes

- If you send too many messages too quickly, WhatsApp may temporarily block you. Use responsibly!
- If WhatsApp Web changes, you may need to update XPath or CSS selectors in the script.
- Files must be saved in **UTF-8** encoding.

---

## License

This project is intended for **personal use only**.  
Commercial use or spam activities are **NOT recommended** and are your own responsibility.
