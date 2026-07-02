# WPSS Admin — Script d'activation WPS

Ce dépôt contient des scripts Python légers pour activer le WPS (Wi‑Fi Protected Setup) sur certains routeurs via leurs interfaces HTTP/HTTPS en utilisant l'authentification Digest.

---

# WPSS Admin — WPS Activation Script (EN)

This repository contains small Python scripts to activate WPS (Wi‑Fi Protected Setup) on some routers via their HTTP/HTTPS interfaces using Digest authentication.

---

## Français — Présentation

### À quoi ça sert
Automatiser l'activation du WPS d'un routeur compatible depuis la ligne de commande, par exemple pour des besoins temporaires d'appairage d'appareils.

### Contenu principal
- `main.py` : script principal qui tente un GET puis un POST vers `/cgi-bin/wps` avec HTTP Digest Auth.
- `1.py` : variante qui cible un endpoint différent (`/userRpm/StatusRpm.htm`) pour certains modèles de routeurs.
- `wps_clok` : script plus avancé qui enchaîne plusieurs POST et attend entre les requêtes pour simuler l'activation automatique.
- `CHANGELOG.md` : journal des modifications.
- `README.md` : documentation (vous lisez la version étendue).

### Prérequis
- Python 3.7+
- Paquet `requests`

Installation rapide :

```bash
python -m pip install --user requests
```

### Configuration
Modifiez les variables en haut des scripts (ou préférez les variables d'environnement) :

```python
ROUTER_IP = "192.168.1.1"
USERNAME = "admin"
PASSWORD = "admin"
```

Exemple sécurisé (recommandé) : exporter des variables d'environnement avant exécution et modifier les scripts pour lire `os.environ` :

```bash
export ROUTER_IP=192.168.1.1
export ROUTER_USER=admin
export ROUTER_PASS=supersecret
python main.py
```

ou ajoutez un petit wrapper :

```python
import os
ROUTER_IP = os.getenv('ROUTER_IP', '192.168.1.1')
USERNAME = os.getenv('ROUTER_USER', 'admin')
PASSWORD = os.getenv('ROUTER_PASS', 'admin')
```

### Utilisation
Exécutez directement l'un des scripts :

```bash
python main.py
# ou
python 1.py
# ou
python wps_clok
```

Sortie attendue :

```
Activation du WPS...
✓ GET /cgi-bin/wps -> 200
✓ POST /cgi-bin/wps -> 200

✓✓ WPS activé avec succès!
Appuyez sur le bouton WPS du routeur dans les 2 minutes.
```

### Remarques de sécurité (FR)
- WPS présente des faiblesses connues ; son activation doit rester temporaire et contrôlée.
- Ne commitez jamais d'identifiants réels dans le dépôt.
- Utilisez des variables d'environnement, un gestionnaire de secrets ou un fichier de configuration exclu via `.gitignore`.
- Limitez l'accès réseau au poste qui exécute ces scripts.

### Dépannage (FR)
- 404 sur `/cgi-bin/wps` : l'endpoint n'existe pas sur votre routeur — vérifier modèle et pages d'administration.
- Erreur d'authentification : vérifier username/password et la méthode d'auth (Digest vs Basic).
- Connexion refusée : IP incorrecte, routeur non accessible ou pare-feu.
- WPS activé mais pas d'appairage : appuyez sur le bouton WPS physique du routeur si requis.

---

## English — Overview

### What this does
Small CLI scripts to trigger WPS on compatible routers by sending HTTP requests (GET/POST) with HTTP Digest authentication.

### Files
- `main.py` — tries GET then POST to `/cgi-bin/wps` with Digest auth.
- `1.py` — alternate endpoint used by some router models.
- `wps_clok` — sequence of POSTs with waits to attempt "automatic" WPS activation.
- `CHANGELOG.md` — changelog.

### Requirements
- Python 3.7+
- requests

Install dependency:

```bash
python -m pip install --user requests
```

### Configuration
Edit the top of each script or export environment variables instead (recommended):

```bash
export ROUTER_IP=192.168.1.1
export ROUTER_USER=admin
export ROUTER_PASS=supersecret
```

Suggested code to read env vars inside scripts:

```python
import os
ROUTER_IP = os.getenv('ROUTER_IP', '192.168.1.1')
USERNAME = os.getenv('ROUTER_USER', 'admin')
PASSWORD = os.getenv('ROUTER_PASS', 'admin')
```

### Usage
Run one of the scripts:

```bash
python main.py
python 1.py
python wps_clok
```

Expected output (example):

```
Activating WPS...
✓ GET /cgi-bin/wps -> 200
✓ POST /cgi-bin/wps -> 200

✓✓ WPS successfully activated!
Press the router WPS button within 2 minutes.
```

### Security notes (EN)
- WPS is generally insecure — only enable temporarily for pairing.
- Never store real credentials in the repo. Use env vars or secret manager.
- Consider running these scripts from an isolated host on the same LAN.

### Troubleshooting (EN)
- 404 on `/cgi-bin/wps`: the endpoint is not available on that router model.
- Auth errors: confirm credentials and that the router expects HTTP Digest.
- Connection refused: wrong IP, network isolation, or firewall.
- WPS activated but devices don't pair: some routers still require pressing the physical WPS button.

---

## Contributing
- Fork the repo, create a branch, open a PR.
- For code changes: add tests where possible and document behavior in the README.
- If you add support for a new router model, include the tested endpoint and firmware version.

## Improving this project — suggestions I can implement for you
- Replace hardcoded credentials with env var support across all scripts.
- Add a CLI interface (click/argparse) to choose router IP, mode, and dry-run.
- Add logging and optional verbose / debug output.
- Add a pyproject.toml and make a package/console script.

Si vous voulez que je mette en place l'une de ces améliorations, dites laquelle et je la commiterai.
