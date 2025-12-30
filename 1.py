import requests
from requests.auth import HTTPDigestAuth

ROUTER_IP = "192.168.1.1"  # IP de votre routeur
USERNAME = "admin"
PASSWORD = "admin" 

url = f"http://{ROUTER_IP}/userRpm/StatusRpm.htm?homeWlanSwitch=1&wps=1"
auth = HTTPDigestAuth(USERNAME, PASSWORD)

try:
    response = requests.get(url, auth=auth, timeout=10)
    if response.status_code == 200:
        print("WPS activé avec succès. Appuyez sur le bouton WPS du routeur dans 2 min.")
    else:
        print(f"Erreur: {response.status_code}. Vérifiez login/IP.")
except Exception as e:
    print(f"Erreur connexion: {e}")
