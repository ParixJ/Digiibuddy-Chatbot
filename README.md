# Tech Helper Chatbot

A user-friendly Streamlit chatbot designed to help elderly and non-tech-savvy users understand technology in simple terms.

## Features

- 🤖 **Simple Chat Interface**: Easy-to-use chat interface with large, readable text
- 👋 **Personalized Experience**: Greets users by name for a friendly experience
- 💡 **Helpful Examples**: Pre-loaded example questions to get started
- 🎯 **Clear Explanations**: Technology concepts explained in simple, everyday language
- 📱 **Accessible Design**: Large fonts, clear colors, and intuitive layout
- 🔒 **Safe & Secure**: No data collection, runs locally on your computer

## Topics Covered

The chatbot can help explain:
- What is the internet?
- How to use email
- What is a smartphone?
- How to stay safe online
- What is social media?
- How to take photos with your phone
- What are passwords?
- How to connect to WiFi
- And many more...

## Installation & Setup

1. **Install Python** (if you haven't already):
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Add api key for openrouter in .env file**:
   - Create a .env file in the main directory.
   - Create a api key at openrouter's website if you haven't.
   - Add the api key in the .env file with name API_KEY

4. **Run the app**:
   ```bash
   streamlit run App.py
   ```

5. **Open your browser**:
   - The app will automatically open in your default web browser
   - If it doesn't, go to: http://localhost:8501

## How to Use

1. **Type your question** in the chat box at the bottom
2. **Click "Send"** or press Enter to get an answer
3. **Try the example questions** in the sidebar for quick start
4. **Ask follow-up questions** if you need more clarification

## System Requirements

- Python 3.7 or higher
- Windows, Mac, or Linux
- Web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (for initial package installation)

## Troubleshooting

- **If the app doesn't start**: Make sure Python is installed and in your PATH
- **If packages aren't found**: Run `pip install streamlit` manually
- **If the browser doesn't open**: Manually go to http://localhost:8501

## Support

This chatbot is designed to be simple and user-friendly. If you have technical issues, try:
1. Restarting the app
2. Refreshing your browser
3. Checking that all files are in the same folder

---

**Note**: This is a local application that runs on your computer. No data is sent to external servers, ensuring your privacy and security. 