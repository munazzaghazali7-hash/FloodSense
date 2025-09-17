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


**2. Create a Virtual Environment (Recommended)**
