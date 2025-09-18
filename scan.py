import argparse
import socket
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, nargs="+", help="Port(s) à scanner")
parser.add_argument("-r", "--range", type=str, help="Range de ports à scanner, ex: 20-30")
parser.add_argument("-i", "--ip", type=str, required=True, help="IP sélectionnée pour le scan")
args = parser.parse_args()

service = {
    7: "Echo",
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    37: "Time",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    79: "Finger",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "Microsoft RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "Microsoft SMB",
    465: "SMTPS",
    514: "Syslog",
    515: "LPR/LPD",
    587: "SMTP Submission",
    631: "IPP",
    636: "LDAPS",
    873: "Rsync",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1194: "OpenVPN",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    1723: "PPTP",
    1883: "MQTT",
    2049: "NFS",
    2181: "Apache Zookeeper",
    2222: "SSH Alternate",
    2375: "Docker REST API",
    2376: "Docker REST API (TLS)",
    3000: "TCP / UDP",
    3306: "MySQL",
    3389: "RDP",
    3690: "Subversion",
    4444: "Metasploit",
    5000: "Flask/Python Dev Server",
    5432: "PostgreSQL",
    5672: "AMQP",
    5900: "VNC",
    6379: "Redis",
    6667: "IRC",
    7000: "Cassandra",
    8000: "HTTP Alternate",
    8080: "HTTP Proxy/Alternate",
    8443: "HTTPS Alternate",
    8888: "Jupyter Notebook",
    9000: "SonarQube",
    9200: "Elasticsearch",
    9418: "Git",
    27017: "MongoDB"
}


#===========Affichage de l'en-tête============
def entete():
    print("╔══════════════════════════════════════╗")
    print("║          ▪ SCAN DE PORTS ▪           ║")
    print("╚══════════════════════════════════════╝ \n")

#===============================Fonction pour le Scan===============================
def scan(ip_target, port_target):
    global service

    # Essaie de convertir la chaîne en adresse binaire
    try:
        socket.inet_aton(ip_target)
    except socket.error:
        print(f"{ip_target} — Adresse IP invalide, veuillez saisir une IPv4 correcte")
        sys.exit(1)

    # Vérifie que le port indiqué est dans la gamme des ports valide
    if port_target < 0 or port_target > 65535:
        print(f"{port_target} — Port invalide, veuillez saisir un port valide (0 - 65535)")
        return

    # Contexte pour tester et afficher les résultats
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        try:
            s.connect((ip_target, port_target))
            
            # Si une connexion est valide on affiche son service 
            if port_target in service:
                print(f"[{ip_target}:{port_target}] | {service[port_target]} → Connexion établie [✓] \n")
            else:
                print(f"[{ip_target}:{port_target}] → Service inconnu\n")
            # Sinon rien et on continue
        except (socket.timeout, ConnectionRefusedError):
            return
        except OSError as e:
            print(f"{ip_target}:{port_target} — erreur réseau: {e}")
#===================================================================================

if __name__ == "__main__":
    entete()
    try:
        ports_to_scan = []

        # Ports manuels
        if args.port:
            ports_to_scan.extend(args.port)

        # Range
        if args.range:  # ex: 25-106
            try:
                start, end = map(int, args.range.split('-'))  # ex: ["20", "106"] => 20, 106
                if start < 0 or end > 65535 or start > end:
                    print("Erreur : range de ports invalide (0-65535)")
                    sys.exit(1)
                ports_to_scan.extend(range(start, end + 1))
            
            except ValueError:
                print("Erreur : range invalide, ex: 20-30")
                sys.exit(1)

        for port in ports_to_scan:  # Boucle sur tous les ports de "ports_to_scan"
            scan(args.ip, port)

    except KeyboardInterrupt:
        sys.exit(0)