# Scanner de Ports IP

Un scanner de ports simple et efficace en Python pour analyser les ports ouverts sur une adresse IP donnée.

## 🚀 Fonctionnalités

- Scan de ports individuels ou par plages
- Identification automatique des services associés aux ports (80+ services)
- Interface en ligne de commande intuitive
- Timeout configurable pour éviter les blocages
- Aucune dépendance externe requise

## 📋 Prérequis

- **Python 3.6 ou supérieur** (vérifiez avec `python3 --version`)
- **Git** (pour cloner le projet)
- Système Linux/macOS ou Windows avec WSL/Git Bash

## ⚡ Installation rapide (recommandée)

### Sur Linux/macOS

```bash
# 1. Cloner le projet
git clone https://github.com/votre-username/Scanner-IP-PORTS.git
cd Scanner-IP-PORTS

# 2. Rendre le script d'installation exécutable
chmod +x install.sh

# 3. Lancer l'installation
./install.sh

# 4. Recharger votre shell
source ~/.bashrc  # ou source ~/.zshrc si vous utilisez zsh

# 5. Tester l'installation
portscan -i 127.0.0.1 -p 80
```

**L'installation automatique configure :**
- ✅ Permissions d'exécution sur `scan.py`
- ✅ Alias global `portscan` dans votre shell
- ✅ Compatible bash/zsh
- ✅ Vérification de Python 3

### Sur Windows

```powershell
# 1. Cloner le projet
git clone https://github.com/votre-username/Scanner-IP-PORTS.git
cd Scanner-IP-PORTS

# 2. Utiliser directement avec Python
python scan.py -i 127.0.0.1 -p 80

# Ou créer un alias PowerShell (optionnel)
# Ajouter cette ligne à votre $PROFILE :
# Set-Alias portscan "C:\chemin\vers\Scanner-IP-PORTS\scan.py"
```

## 📦 Installation manuelle

Si le script d'installation automatique ne fonctionne pas :

### Linux/macOS

```bash
# 1. Cloner le projet
git clone https://github.com/votre-username/Scanner-IP-PORTS.git
cd Scanner-IP-PORTS

# 2. Rendre le script exécutable
chmod +x scan.py

# 3. Ajouter l'alias à votre configuration shell
# Pour Bash :
echo "alias portscan='$(pwd)/scan.py'" >> ~/.bashrc
source ~/.bashrc

# Pour Zsh :
echo "alias portscan='$(pwd)/scan.py'" >> ~/.zshrc
source ~/.zshrc

# 4. Vérifier l'installation
portscan -i 127.0.0.1 -p 80
```

### Windows (sans alias)

```bash
# Utiliser directement Python
python scan.py -i 192.168.1.1 -p 80
```

## 💻 Utilisation

### ⭐ Avec l'alias portscan (après installation)

```bash
# Scanner un port spécifique
portscan -i 192.168.1.1 -p 80

# Scanner plusieurs ports
portscan -i 192.168.1.1 -p 22 80 443

# Scanner une plage de ports
portscan -i 192.168.1.1 -r 20-100

# Combiner ports spécifiques et plage
portscan -i 192.168.1.1 -p 22 443 -r 8000-8080

# Scanner des ports communs sur localhost
portscan -i 127.0.0.1 -p 80 443 3306 5432 8080
```

### Avec Python directement (sans installation)

```bash
# Scanner un port
python3 scan.py -i 192.168.1.1 -p 80

# Scanner une plage
python3 scan.py -i 192.168.1.1 -r 1-1000

# Exécution directe (si chmod +x a été fait)
./scan.py -i 192.168.1.1 -p 80
```

## 📖 Options disponibles

| Option | Description | Exemple |
|--------|-------------|---------|
| `-i, --ip` | Adresse IP cible (obligatoire) | `-i 192.168.1.1` |
| `-p, --port` | Port(s) spécifique(s) à scanner | `-p 80 443 22` |
| `-r, --range` | Plage de ports à scanner | `-r 20-100` |

**Notes :**
- Les options `-p` et `-r` peuvent être combinées
- Le timeout par défaut est de 3 secondes par port
- Les ports valides vont de 0 à 65535

## 🔍 Services détectés

Le scanner reconnaît automatiquement plus de 80 services courants :
- **Web :** HTTP (80), HTTPS (443), HTTP-Alt (8000, 8080)
- **Base de données :** MySQL (3306), PostgreSQL (5432), MongoDB (27017), Redis (6379)
- **Admin système :** SSH (22), Telnet (23), RDP (3389), VNC (5900)
- **Mail :** SMTP (25), POP3 (110), IMAP (143)
- **Et bien d'autres...**

## 🐛 Dépannage

### L'alias ne fonctionne pas après installation

```bash
# Recharger votre configuration shell
source ~/.bashrc   # Pour Bash
source ~/.zshrc    # Pour Zsh

# Ou redémarrer votre terminal
```

### Permission denied lors de l'exécution

```bash
# Rendre le script exécutable
chmod +x scan.py
chmod +x install.sh
```

### Python non trouvé

```bash
# Vérifier que Python 3 est installé
python3 --version

# Sur Debian/Ubuntu, installer Python 3
sudo apt update && sudo apt install python3

# Sur macOS avec Homebrew
brew install python3
```

### Le script install.sh ne s'exécute pas

```bash
# Vérifier les fins de ligne (problème Windows/Linux)
dos2unix install.sh   # Si disponible
# Ou utiliser sed
sed -i 's/\r$//' install.sh

# Puis réessayer
chmod +x install.sh
./install.sh
```

## ⚠️ Avertissement

**Utilisation légale uniquement :** Cet outil est destiné à des fins éducatives et de test sur vos propres systèmes ou avec autorisation explicite. Le scan de ports non autorisé peut être illégal selon votre juridiction.

## 📄 Licence

Ce projet est libre d'utilisation pour des fins éducatives et personnelles.
