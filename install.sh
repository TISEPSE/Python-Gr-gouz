#!/bin/bash

# Script d'installation pour le Scanner de Ports IP
# Ce script configure automatiquement l'alias 'portscan'

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/scan.py"

echo "╔══════════════════════════════════════╗"
echo "║     Installation Scanner de Ports    ║"
echo "╚══════════════════════════════════════╝"
echo

# Vérifier que Python 3 est installé et obtenir sa version
if ! command -v python3 &> /dev/null; then
    echo "❌ Erreur: Python 3 n'est pas installé"
    echo ""
    echo "Pour installer Python 3 :"
    echo "  • Ubuntu/Debian : sudo apt update && sudo apt install python3"
    echo "  • Fedora/RHEL   : sudo dnf install python3"
    echo "  • macOS         : brew install python3"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python $PYTHON_VERSION détecté"

# Vérifier que le script scan.py existe
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "❌ Erreur: scan.py non trouvé dans $SCRIPT_DIR"
    exit 1
fi

# Rendre le script exécutable
chmod +x "$SCRIPT_PATH"
echo "✅ Script rendu exécutable"

# Déterminer le fichier de configuration du shell
SHELL_CONFIG=""
if [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    if [ -f "$HOME/.bashrc" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    else
        SHELL_CONFIG="$HOME/.bash_profile"
    fi
else
    # Essayer de détecter le shell par défaut
    if [ -f "$HOME/.zshrc" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    elif [ -f "$HOME/.bashrc" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    else
        SHELL_CONFIG="$HOME/.bash_profile"
    fi
fi

echo "📁 Fichier de configuration: $SHELL_CONFIG"

# Créer le fichier de config s'il n'existe pas
touch "$SHELL_CONFIG"

# Vérifier si l'alias existe déjà
if grep -q "alias portscan=" "$SHELL_CONFIG" 2>/dev/null; then
    echo ""
    echo "⚠️  L'alias 'portscan' existe déjà dans $SHELL_CONFIG"
    echo "   Voulez-vous le remplacer ? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "❌ Installation annulée"
        exit 0
    fi
    # Supprimer l'ancien alias (compatible macOS et Linux)
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS (BSD sed)
        sed -i '' '/alias portscan=/d' "$SHELL_CONFIG"
        sed -i '' '/# Scanner de Ports IP - Alias automatique/d' "$SHELL_CONFIG"
    else
        # Linux (GNU sed)
        sed -i '/alias portscan=/d' "$SHELL_CONFIG"
        sed -i '/# Scanner de Ports IP - Alias automatique/d' "$SHELL_CONFIG"
    fi
    echo "✅ Ancien alias supprimé"
fi

# Ajouter l'alias
echo "" >> "$SHELL_CONFIG"
echo "# Scanner de Ports IP - Alias automatique" >> "$SHELL_CONFIG"
echo "alias portscan='$SCRIPT_PATH'" >> "$SHELL_CONFIG"

echo "✅ Alias 'portscan' ajouté à $SHELL_CONFIG"
echo ""
echo "╔══════════════════════════════════════╗"
echo "║    ✓ Installation terminée !         ║"
echo "╚══════════════════════════════════════╝"
echo ""
echo "🔄 Pour utiliser immédiatement, exécutez :"
echo "   source $SHELL_CONFIG"
echo ""
echo "   Ou redémarrez votre terminal."
echo ""
echo "📖 Exemples d'utilisation :"
echo "   portscan -i 192.168.1.1 -p 80"
echo "   portscan -i 127.0.0.1 -r 20-100"
echo "   portscan -i example.com -p 22 80 443"
echo ""
echo "ℹ️  Pour tester : portscan -i 127.0.0.1 -p 80"
echo ""