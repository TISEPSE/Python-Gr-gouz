import argparse
import socket
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, nargs="+", help="Port(s) à scanner")
parser.add_argument("-r", "--range", type=str, help="Range de ports à scanner, ex: 20-30")
parser.add_argument("-i", "--ip", type=str, required=True, help="IP sélectionnée pour le scan")
args = parser.parse_args()

#===============================Fonction pour le Scan===============================
def scan(ip_target, port_target):

    # Essaie de convertir la chaîne en adresse binaire
    try:
        socket.inet_aton(ip_target)
    except socket.error:
        print(f"{ip_target} — Adresse IP invalide, veuillez saisir une IPv4 correcte")
        return

    # Vérifie que le port indiqué est dans la gamme des ports valide
    if port_target < 0 or port_target > 65535:
        print(f"{port_target} — Port invalide, veuillez saisir un port valide (0 - 65535)")
        return

    # Contexte pour tester et afficher les résultats
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        try:
            s.connect((ip_target, port_target))
            print(f"{ip_target}:{port_target} — Connexion valide")
        except (socket.timeout, ConnectionRefusedError):
            print(f"{ip_target}:{port_target} — fermé / pas de connexion")
        except OSError as e:
            print(f"{ip_target}:{port_target} — erreur réseau: {e}")
#===================================================================================

if __name__ == "__main__":
    try:
        ports_to_scan = []

        # Ports manuels
        if args.port:
            #Si l'argument est "-p / --port" alors on ajoute les ports de la commande dans "ports_to_scan"
            ports_to_scan.extend(args.port)

        # Range
        if args.range: #ex: 25-106
            try:
                start, end = map(int, args.range.split('-')) #ex: ["20", "106"] => 20, 106
                ports_to_scan.extend(range(start, end+1)) #On attribue start = 20 et end = 25
                
                #Si ya une erreur on print() et on sort du programme
            except ValueError:
                print("Erreur : range invalide, ex: 20-30")
                sys.exit(1)

        for port in ports_to_scan: #Boucle sur tout les ports de "ports_to_scan"
            scan(args.ip, port)

    except KeyboardInterrupt:
        sys.exit(0)