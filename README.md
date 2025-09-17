## 🌊 FloodSense - AI-Powered Flood Early Warning System

[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Twilio](https://img.shields.io/badge/Twilio-SMS-blue.svg)](https://www.twilio.com/)

**FloodSense** is an automated early warning system that predicts flash floods using real-time river data and disseminates life-saving alerts via SMS, Email, and Telegram, empowering communities to act before disaster strikes.

> **Built for:** Smart India Hackathon 2025 | **Theme:** Disaster Management & Clean Tech

---

## 🚀 Inspiration

Every year, floods cause unprecedented damage to life and property in India. The critical gap we identified is not the lack of data, but the **delay in communicating actionable warnings** to the right people at the right time. FloodSense bridges this gap by automating the entire pipeline from data to decision.

## ⚡ What It Does

1.  **Data Ingestion:** Continuously monitors real-time water level and rainfall data from simulated government APIs (CWC/IMD).
2.  **Risk Prediction:** Employs a rule-based AI model (designed for easy replacement with ML) to assess flood risk.
3.  **Multi-Channel Alerting:** Instantly triggers alerts via:
    *   **SMS** (using Twilio/TextLocal API)
    *   **Email**
    *   **Telegram**
4.  **Real-time Dashboard:** Provides a live web dashboard for authorities to monitor river conditions and alert statuses.

## 🛠️ Tech Stack

*   **Backend:** Python, Flask, Flask-SocketIO
*   **Frontend:** HTML5, CSS3, JavaScript, Chart.js, Leaflet.js
*   **Notifications:** Twilio API, TextLocal API, SMTP (Gmail), Telegram Bot API
*   **Data:** Simulated CWC/IMD API data (ready for real API integration)
*   **Deployment:** Ready for deployment on Replit, Heroku, or any Linux server.

## 📦 Installation & Setup

Follow these steps to run FloodSense locally.

### Prerequisites

*   Python 3.8 or higher
*   `pip` (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/floodsense.git
cd floodsense
```
### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
Create a .env file in the root directory and add your credentials:
```bash
# Twilio Credentials (Optional)
TWILIO_SID=your_account_sid
TWILIO_AUTH=your_auth_token
TWILIO_PHONE=your_twilio_phone_number

# TextLocal Credentials (Optional - for India)
TEXTLOCAL_API_KEY=your_textlocal_api_key

# Email Credentials (Gmail - use App Password)
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_specific_password

# Telegram Bot Credentials (Optional)
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT=your_chat_id

# Test Recipients
TEST_SMS_TO=+91XXXXXXXXXX
TEST_EMAIL_TO=test@example.com
```
### 5. Run the Application
```bash
python app.py
The backend API server will start at http://localhost:5000.
Open your browser and navigate to http://localhost:5000 to view the dashboard.
```

**🎮 Usage**
View Dashboard: The home page shows the current river data, risk level, and a history chart.

Send Test Alert: Use the dashboard form to send a test alert via all configured channels.

Simulate Emergency: Click "Simulate Emergency" to trigger a high-risk scenario and see the alert system in action.

API Endpoints: The system exposes a clean REST API for integration:

GET /api/station-data - Fetch current river data and risk assessment.

POST /api/send-alert - Trigger an alert manually (accepts message, sms_to, email_to in JSON body).

GET /api/health - Check API status.




