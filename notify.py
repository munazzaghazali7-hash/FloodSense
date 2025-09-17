# notifier.py
import os
import requests
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# Load environment variables
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
TEXTLOCAL_KEY = os.getenv("TEXTLOCAL_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT = os.getenv("TELEGRAM_CHAT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_sms_twilio(to, message):
    """Send SMS using Twilio"""
    if not (TWILIO_SID and TWILIO_AUTH and TWILIO_PHONE):
        raise RuntimeError("Twilio config missing")
    client = Client(TWILIO_SID, TWILIO_AUTH)
    return client.messages.create(body=message, from_=TWILIO_PHONE, to=to)

def send_sms_textlocal(to, message):
    """Send SMS using TextLocal (India focused)"""
    if not TEXTLOCAL_KEY:
        raise RuntimeError("TextLocal key missing")
    url = "https://api.textlocal.in/send/"
    data = {
        "apikey": TEXTLOCAL_KEY,
        "numbers": to,
        "sender": "TXTLCL",
        "message": message
    }
    resp = requests.post(url, data=data)
    return resp.json()

def send_email(to, subject, message):
    """Send email using SMTP (Gmail)"""
    if not (EMAIL_USER and EMAIL_PASS):
        raise RuntimeError("Email credentials missing")
    
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to, msg.as_string())
    return True

def send_telegram(message):
    """Send message to Telegram channel"""
    if not (TELEGRAM_TOKEN and TELEGRAM_CHAT):
        raise RuntimeError("Telegram config missing")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT, "text": message}
    return requests.post(url, data=data).json()

def notify_all(message, sms_to=None, email_to=None, use_twilio=True):
    """
    Send notifications through all configured channels
    Returns: dict with results from each channel
    """
    results = {}
    
    # SMS Notification
    if sms_to:
        try:
            if use_twilio and TWILIO_SID:
                results['sms'] = send_sms_twilio(sms_to, message)
            elif TEXTLOCAL_KEY:
                results['sms'] = send_sms_textlocal(sms_to, message)
        except Exception as e:
            results['sms_error'] = str(e)
    
    # Email Notification
    if email_to:
        try:
            results['email'] = send_email(email_to, "🌊 Flood Alert", message)
        except Exception as e:
            results['email_error'] = str(e)
    
    # Telegram Notification
    try:
        if TELEGRAM_TOKEN:
            results['telegram'] = send_telegram(message)
    except Exception as e:
        results['telegram_error'] = str(e)
    
    return results