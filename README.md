# insta-chatbot-unofficial
# Instagram Bot - Automated Message Responder

## Overview
This Instagram bot automatically responds to direct messages (DMs) that start with "Q:" using AI-powered responses. It's designed to handle customer inquiries and provide intelligent responses using an integrated AI brain system.

## Features
- 🤖 **Automated Login**: Secure Instagram login with anti-detection measures
- 💬 **Smart Message Detection**: Automatically finds messages starting with "Q:"
- 🧠 **AI-Powered Responses**: Uses integrated brain system for intelligent replies
- 🔄 **Continuous Monitoring**: Runs continuously to check for new messages
- 🛡️ **Error Handling**: Robust error handling with automatic recovery
- 📱 **Anti-Detection**: Uses advanced Chrome options to avoid bot detection

## Prerequisites
- Python 3.7+
- Chrome browser installed
- ChromeDriver (automatically managed by Selenium)
- Instagram account credentials

## Required Dependencies
```bash
pip install selenium
pip install openai
```

## File Structure
```
├── instal_bot.py          # Main bot script
├── tempbrain.py           # AI brain integration
└── README_instal_bot.md  # This file
```

## 🔐 Instagram Login Setup

### **Step-by-Step Instructions:**
1. **Open instal_bot.py** - File kahan hai
2. **Find Login Section** - Line 111 pe credentials hain
3. **Replace Credentials** - Apne username/password daalo
4. **Save File** - Changes save karo

### **Clear Examples:**
```python
<code_block_to_apply_changes_from>
```

### **Security Guidelines:**
- ✅ Never share credentials publicly
- ✅ Use dedicated bot account
- ✅ Enable 2FA
- ✅ Keep credentials private

## How It Works

### 1. Login Process
```python
def login_to_instagram(username, password):
    # Sets up Chrome with anti-detection options
    # Navigates to Instagram login page
    # Enters credentials and logs in
    # Returns driver instance
```

### 2. Message Monitoring
```python
def check_and_reply(driver):
    # Navigates to Instagram DMs
    # Searches for messages starting with "Q:"
    # Processes each message individually
    # Sends AI-generated responses
```

### 3. Response System
- **Predefined Responses**: For common questions like "who are you"
- **AI Responses**: Uses `ask_brain()` for complex queries
- **Automatic Sending**: Sends responses and returns to inbox

## Usage

### Basic Usage
```bash
python instal_bot.py
```

### Expected Behavior
1. **Login Phase**: Bot logs into Instagram using your credentials
2. **Monitoring Phase**: Continuously checks for new messages
3. **Response Phase**: Automatically replies to "Q:" messages
4. **Loop Phase**: Repeats monitoring every 5 seconds

## Message Format
The bot responds to messages in this format:
```
Q: [Your question here]
```

## Response Types

### 1. Predefined Responses
- **"who are you"** → "I'm Igris develop by Ayush rana taking info from chatgpt database"

### 2. AI-Generated Responses
- All other questions are processed through the AI brain system
- Responses are generated using the integrated AI system

## Error Handling

### Login Failures
- Bot exits gracefully if login fails
- Clear error messages for debugging
- Check your username and password if login fails

### Message Processing Errors
- Individual message errors don't stop the bot
- Bot continues to next message
- Automatic navigation back to inbox

### Network Issues
- Robust retry mechanisms
- Graceful handling of connection problems

## Security Features

### Anti-Detection Measures
```python
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
```

### User Agent Spoofing
```python
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...'
})
```

## Console Output
- Login status messages
- Message processing updates
- Error notifications
- Check cycle completions

## Troubleshooting

### Common Issues

1. **Login Failed**
   - ✅ Check username/password spelling
   - ✅ Verify Instagram account status
   - ✅ Check internet connection
   - ✅ Ensure account is not locked

2. **No Messages Found**
   - ✅ Ensure messages start with "Q:"
   - ✅ Check Instagram DM access
   - ✅ Verify bot is running
   - ✅ Check if messages are in the correct format

3. **Chrome Driver Issues**
   - ✅ Update Chrome browser
   - ✅ Check ChromeDriver compatibility
   - ✅ Verify Selenium installation

### Debug Mode
Add debug prints for troubleshooting:
```python
print(f"Processing message: {question}")
print(f"AI Response: {answer}")
```

## Safety Guidelines

### Instagram Terms of Service
- Use responsibly and within Instagram's terms
- Avoid excessive automation
- Respect rate limits
- Don't spam or send too many messages

### Account Security
- Use dedicated bot account
- Enable 2FA for security
- Monitor account activity
- Keep credentials secure

## Customization

### Adding Predefined Responses
```python
if question.lower() == "your_question":
    answer = "Your predefined response"
```

### Modifying Check Intervals
```python
time.sleep(5)  # Change to desired interval (in seconds)
```

### Custom Message Detection
```python
messages = driver.find_elements(By.XPATH, "//span[contains(text(), 'Q:')]")
# Modify XPath for different message patterns
```

## Quick Setup Checklist

### Before Running:
- [ ] Python 3.7+ installed
- [ ] Chrome browser installed
- [ ] Dependencies installed (`pip install selenium openai`)
- [ ] Instagram credentials updated in `instal_bot.py`
- [ ] `tempbrain.py` properly configured
- [ ] Internet connection stable

### First Run:
- [ ] Run `python instal_bot.py`
- [ ] Check console for login success
- [ ] Verify bot is monitoring messages
- [ ] Test with a "Q:" message

## Support

### Getting Help
1. Check console output for error messages
2. Verify all dependencies are installed
3. Test with simple questions first
4. Ensure Instagram credentials are correct

### Common Error Messages
- **"Failed to log in"** → Check username/password
- **"No new messages found"** → Ensure messages start with "Q:"
- **"Chrome driver error"** → Update Chrome browser

## License
This project is for educational purposes. Use responsibly and in compliance with Instagram's terms of service.

---

**⚠️ Important**: This bot is for educational purposes. Always comply with Instagram's terms of service and use responsibly. 
