import requests
from requests.auth import HTTPDigestAuth

ROUTER_IP = "192.168.1.1"  # IP de votre routeur
USERNAME = "admin"
PASSWORD = "admin" 

url = f"http://{ROUTER_IP}/cgi-bin/wps"
auth = HTTPDigestAuth(USERNAME, PASSWORD)

try:
    print("Activation du WPS...")
    
    # Essayer en GET
    response = requests.get(url, auth=auth, timeout=10)
    print(f"✓ GET /cgi-bin/wps -> {response.status_code}")
    
    # Essayer en POST avec paramètres
    params = {
        "method": "set",
        "wpsEnable": "1",
        "wpsStatus": "1"
    }
    
    response_post = requests.post(url, auth=auth, data=params, timeout=10)
    print(f"✓ POST /cgi-bin/wps -> {response_post.status_code}")
    
    if response.status_code == 200 or response_post.status_code == 200:
        print("\n✓✓ WPS activé avec succès!")
        print("Appuyez sur le bouton WPS du routeur dans les 2 minutes.")
    else:
        print("Vérifiez les paramètres WPS.")
        
except Exception as e:
    print(f"Erreur: {e}")
