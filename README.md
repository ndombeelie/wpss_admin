# Script d'Activation WPS Routeur

## Description
Ce script Python active le WPS (Wi-Fi Protected Setup) sur votre routeur via HTTP/HTTPS en utilisant l'authentification Digest.

## Prérequis
- Python 3.x
- Bibliothèque `requests`

### Installation des dépendances
```bash
pip install requests
```

## Configuration

Avant d'exécuter le script, modifiez les paramètres dans `main.py` :

```python
ROUTER_IP = "192.168.1.1"  # IP de votre routeur
USERNAME = "admin"         # Nom d'utilisateur
PASSWORD = "admin"         # Mot de passe
```

### Valeurs par défaut courantes
| Paramètre | Valeur par défaut |
|-----------|------------------|
| IP Routeur | 192.168.1.1 |
| Nom d'utilisateur | admin |
| Mot de passe | admin |

## Utilisation

Exécutez le script :
```bash
python main.py
```

### Résultat attendu
```
Activation du WPS...
✓ GET /cgi-bin/wps -> 200
✓ POST /cgi-bin/wps -> 200

✓✓ WPS activé avec succès!
Appuyez sur le bouton WPS du routeur dans les 2 minutes.
```

## Endpoint utilisé
- **URL** : `http://{ROUTER_IP}/cgi-bin/wps`
- **Méthodes** : GET et POST
- **Authentification** : HTTP Digest Auth

## Paramètres POST (optionnels)
```python
{
    "method": "set",
    "wpsEnable": "1",
    "wpsStatus": "1"
}
```

## Dépannage

### Erreur 404
L'endpoint `/cgi-bin/wps` n'existe pas sur votre routeur. Vérifiez le modèle du routeur.

### Erreur d'authentification
Vérifiez les identifiants (USERNAME et PASSWORD).

### Connexion refusée
Vérifiez que :
- L'IP du routeur est correcte
- Le routeur est accessible depuis votre réseau
- Aucun pare-feu ne bloque la connexion

### WPS activé mais pas de connexion
Appuyez physiquement sur le bouton WPS du routeur dans les 2 minutes suivant l'exécution du script.

## Fichiers du projet
- `main.py` : Script principal d'activation WPS
- `1.py` : Fichier alternatif (même code)
- `README.md` : Ce fichier

## Notes importantes
⚠️ Le WPS n'est pas recommandé pour la sécurité à long terme. Désactivez-le après l'appairage du dispositif.
