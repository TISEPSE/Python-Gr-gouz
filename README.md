# Scanner de Ports IP

Un scanner de ports simple et efficace en Python pour analyser les ports ouverts sur une adresse IP donnée.

## 🚀 Fonctionnalités

- Scan de ports individuels ou par plages
- Identification automatique des services associés aux ports
- Interface en ligne de commande intuitive
- Gestion d'erreurs robuste
- Timeout configurable pour éviter les blocages

## 📋 Prérequis

- Python 3.6 ou supérieur
- Aucune dépendance externe (utilise uniquement les modules standards)

## ⚡ Installation automatique (recommandée)

```bash
# Cloner le projet
git clone https://github.com/votre-username/Scanner-IP-PORTS.git
cd Scanner-IP-PORTS

# Installation automatique avec alias 'portscan'
./install.sh
```

**L'installation automatique configure :**
- ✅ Permissions d'exécution
- ✅ Alias global `portscan`
- ✅ Compatible bash/zsh
- ✅ Configuration automatique du shell

## 📦 Installation manuelle

```bash
# Cloner le projet
git clone https://github.com/votre-username/Scanner-IP-PORTS.git
cd Scanner-IP-PORTS

# Rendre le script exécutable
chmod +x scan.py

# Ajouter l'alias manuellement à votre ~/.bashrc ou ~/.zshrc
echo "alias portscan='$(pwd)/scan.py'" >> ~/.bashrc
source ~/.bashrc
```

## 💻 Utilisation

### ⭐ Méthode recommandée : Avec l'alias portscan
```bash
# Scanner un port spécifique
portscan -i 192.168.1.1 -p 80

# Scanner plusieurs ports
portscan -i 192.168.1.1 -p 22 80 443

# Scanner une plage de ports
portscan -i 192.168.1.1 -r 20-100

# Combiner ports spécifiques et plage
portscan -i 192.168.1.1 -p 22 443 -r 8000-8080
```

### Autres méthodes
```bash
# Avec Python directement
python3 scan.py -i 192.168.1.1 -p 80

# Exécution directe du script
./scan.py -i 192.168.1.1 -p 80
```

## 📖 Options disponibles

| Option | Description | Exemple |
|--------|-------------|---------|
| `-i, --ip` | Adresse IP cible (obligatoire) | `-i 192.168.1.1` |
| `-p, --port` | Port(s) spécifique(s) à scanner | `-p 80 443 22` |
| `-r, --range` | Plage de ports à scanner | `-r 20-100` |

## 🔍 Services détectés

Le scanner identifie automatiquement plus de 70 services courants :
- **Web** : HTTP (80), HTTPS (443)
- **Administration** : SSH (22), RDP (3389), VNC (5900)
- **Base de données** : MySQL (3306), PostgreSQL (5432), MongoDB (27017)
- **Et bien d'autres...**

## 📝 Exemples d'utilisation

```bash
# Scan rapide des ports web
portscan -i example.com -p 80 443

# Audit de sécurité basique
portscan -i 192.168.1.100 -r 1-1000

# Vérification des services de base
portscan -i 10.0.0.1 -p 22 23 53 80 443
```

## ⚠️ Avertissement

Cet outil est destiné à des fins éducatives et de test sur vos propres systèmes ou avec autorisation explicite. L'utilisation non autorisée pour scanner des systèmes tiers peut être illégale.

## 📄 Licence

Ce projet est libre d'utilisation pour des fins éducatives et personnelles.