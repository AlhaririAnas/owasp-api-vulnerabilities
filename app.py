from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 1. Unrestricted Resource Consumption
@app.route('/heavy', methods=['GET'])
def heavy_resource():
    # Endpunkt ohne Begrenzung - Ressource intensiv
    large_list = [x**2 for x in range(10**6)]
    return jsonify({"message": "Processed a large request", "data_size": len(large_list)})

# 2. Server Side Request Forgery (SSRF)
@app.route('/proxy', methods=['GET'])
def proxy_request():
    target_url = request.args.get('url')  # Keine Validierung der Eingabe
    response = requests.get(target_url)  # Leitet die Anfrage direkt weiter
    return jsonify({"proxied_response": response.text[:100]})

# 3. Security Misconfiguration
@app.route('/admin', methods=['GET'])
def admin_area():
    # Simulierte Standardanmeldeinformationen
    admin_password = "admin123"  # Schwachstelle: Standardpasswort
    return jsonify({"message": "Admin area accessed", "default_password": admin_password})

# 4. Unsafe Consumption of APIs
@app.route('/external', methods=['POST'])
def unsafe_external():
    # Daten von der Anfrage werden direkt verwendet
    user_data = request.get_json()
    return jsonify({"unsafe_response": f"Hello, {user_data['name']}!"})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Insecure API for educational purposes!"})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
