from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
import random
from flask import render_template


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for our mock station
MOCK_STATION = {
    "station_id": "GRB-062",
    "station_name": "Godavari at Nashik",
    "river_name": "Godavari",
    "location": "Nashik, Maharashtra",
    "basin": "Godavari Basin",
    "normal_water_level": 2.8,
    "danger_water_level": 4.5,
    "max_water_level": 7.2,
    "normal_rainfall": 40,
    "danger_rainfall": 100
}

# Global variable to store current readings
current_reading = {
    "water_level": 2.8,
    "rainfall": 35,
    "timestamp": datetime.now().isoformat(),
    "risk_level": "NORMAL"
}

def calculate_risk(water_level, rainfall):
    """Calculate flood risk level based on thresholds"""
    if water_level > 4.5 and rainfall > 100:
        return "HIGH"
    elif water_level > 3.8 or rainfall > 70:
        return "MEDIUM"
    elif water_level > 3.2 or rainfall > 50:
        return "LOW"
    else:
        return "NORMAL"

def get_mock_data():
    """Get current mock data with gradual changes"""
    global current_reading
    
    # Update readings with small changes (simulate real sensors)
    current_reading["water_level"] += random.uniform(-0.1, 0.2)
    current_reading["rainfall"] += random.uniform(-2, 5)
    
    # Ensure values stay within realistic ranges
    current_reading["water_level"] = max(1.0, min(7.0, round(current_reading["water_level"], 2)))
    current_reading["rainfall"] = max(0, min(200, round(current_reading["rainfall"], 1)))
    
    # Update timestamp and risk level
    current_reading["timestamp"] = datetime.now().isoformat()
    current_reading["risk_level"] = calculate_risk(
        current_reading["water_level"], 
        current_reading["rainfall"]
    )
    
    return {**MOCK_STATION, **current_reading}

def simulate_emergency():
    """Force dangerous levels for demo purposes"""
    global current_reading
    current_reading.update({
        "water_level": 5.8,
        "rainfall": 150,
        "timestamp": datetime.now().isoformat(),
        "risk_level": "HIGH"
    })
    return get_mock_data()

def reset_to_normal():
    """Reset to normal levels"""
    global current_reading
    current_reading.update({
        "water_level": 2.8,
        "rainfall": 35,
        "timestamp": datetime.now().isoformat(),
        "risk_level": "NORMAL"
    })
    return get_mock_data()

# API Routes
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "OK", 
        "message": "FloodSense API is running",
        "station_monitored": MOCK_STATION["station_id"],
        "station_name": MOCK_STATION["station_name"],
        "data_source": "Mock CWC/IMD Data (Stable Demo Version)"
    })

@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/api/station-data', methods=['GET'])
def get_station_data():
    """
    Main endpoint: Returns realistic mock CWC data
    """
    try:
        data = get_mock_data()
        return jsonify(data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/risk-assessment', methods=['GET'])
def get_risk_assessment():
    """
    Returns only the risk assessment
    """
    try:
        data = get_mock_data()
        return jsonify({
            "station_id": data["station_id"],
            "station_name": data["station_name"],
            "risk_level": data["risk_level"],
            "water_level": data["water_level"],
            "rainfall": data["rainfall"],
            "timestamp": data["timestamp"],
            "alert_threshold_water": 4.5,
            "alert_threshold_rain": 100
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/send-alert', methods=['POST'])
def send_alert():
    """
    Send alert based on current risk level
    """
    try:
        # Get current data
        current_data = get_mock_data()
        
        # Get request data
        request_data = request.get_json() or {}
        phone_number = request_data.get('phone', '+91XXXXXXXXXX')
        custom_message = request_data.get('message', '')
        
        # Create alert message
        if not custom_message:
            alert_message = (
                f"🌊 FloodSense Alert: {current_data['station_name']}\n"
                f"⚠️ Risk Level: {current_data['risk_level']}\n"
                f"💧 Water Level: {current_data['water_level']}m (Danger: 4.5m)\n"
                f"🌧️ Rainfall: {current_data['rainfall']}mm/24h (Danger: 100mm)\n"
                f"🕒 Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            )
        else:
            alert_message = custom_message

        # Simulate SMS sending - This will print to console
        print("🔴" * 50)
        print("📱 SMS ALERT SENT:")
        print(f"   To: {phone_number}")
        print(f"   Message: {alert_message}")
        print("🔴" * 50)

        return jsonify({
            "status": "success",
            "message": "Alert sent successfully",
            "risk_level": current_data["risk_level"],
            "recipient": phone_number,
            "alert_message": alert_message,
            "timestamp": datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/simulate-emergency', methods=['POST'])
def trigger_emergency():
    """
    Force a HIGH risk scenario for demo purposes
    """
    try:
        emergency_data = simulate_emergency()
        
        # Auto-send alert for emergency
        alert_message = (
            f"🚨 CRITICAL FLOOD ALERT: {emergency_data['station_name']}\n"
            f"💧 Water Level: {emergency_data['water_level']}m (DANGER!)\n"
            f"🌧️ Rainfall: {emergency_data['rainfall']}mm/24h (DANGER!)\n"
            f"⚠️ Immediate action required!"
        )
        
        print("🚨" * 50)
        print("🔥 EMERGENCY SIMULATION ACTIVATED")
        print(f"   {alert_message}")
        print("🚨" * 50)

        return jsonify({
            "status": "emergency_activated",
            "risk_level": "HIGH",
            "message": "Emergency scenario simulated",
            "data": emergency_data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reset-data', methods=['POST'])
def reset_data():
    """
    Reset to normal conditions
    """
    try:
        normal_data = reset_to_normal()
        
        return jsonify({
            "status": "data_reset",
            "message": "Data reset to normal conditions",
            "risk_level": "NORMAL",
            "data": normal_data
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/station-info', methods=['GET'])
def get_station_info():
    """Returns information about the monitored station"""
    return jsonify({
        "station": MOCK_STATION,
        "alert_thresholds": {
            "water_level": {
                "normal": "< 3.2m",
                "low_risk": "3.2m - 3.8m", 
                "medium_risk": "3.8m - 4.5m",
                "high_risk": "> 4.5m"
            },
            "rainfall": {
                "normal": "< 50mm",
                "low_risk": "50mm - 70mm",
                "medium_risk": "70mm - 100mm", 
                "high_risk": "> 100mm"
            }
        }
    })

if __name__ == '__main__':
    print("🚀 Starting FloodSense Mock API Server")
    print("✅ Using stable mock data - No API dependencies")
    print(f"📡 Monitoring: {MOCK_STATION['station_name']}")
    print("\n📋 API Endpoints:")
    print("   GET  /api/health            - Health check")
    print("   GET  /api/station-data      - Get mock CWC data")
    print("   GET  /api/risk-assessment   - Get risk assessment") 
    print("   GET  /api/station-info      - Get station info")
    print("   POST /api/send-alert        - Send SMS alert")
    print("   POST /api/simulate-emergency - Force high risk scenario")
    print("   POST /api/reset-data        - Reset to normal")
    print("\n🌐 Server running on http://localhost:5000")
    print("📧 Alerts will be printed to this console")
    
    app.run(debug=True, host='0.0.0.0', port=5000)