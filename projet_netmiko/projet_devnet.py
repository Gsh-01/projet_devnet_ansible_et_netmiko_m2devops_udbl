from netmiko import ConnectHandler
import re

# Paramètres de connexion pour TON routeur GNS3
cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.10.10",
    "username": "admin",
    "password": "Kernel@2026",
    "fast_cli": False,
}

def main():
    print(f"🔌 Connexion au routeur {cisco1['host']}...")
    
    try:
        net_connect = ConnectHandler(**cisco1)
        print("✅ Connexion réussie !\n")

        # TÂCHE 1 : Nom, Version, Modèle
        print("--- 1. INFORMATIONS DU ROUTEUR ---")
        output_version = net_connect.send_command('show version')
        
        # Extraction avec Regex
        hostname = re.search(r'(\S+)\s+uptime', output_version)
        version = re.search(r'Version\s+(\S+),', output_version)
        
        # Extraction du modèle (méthode robuste par ligne)
        model = "Non trouvé"
        for line in output_version.splitlines():
            if "processor" in line and "cisco" in line.lower():
                parts = line.split()
                if len(parts) >= 2:
                    model = parts[1]
                break
        
        # Affichage
        print(f"Nom du routeur : {hostname.group(1) if hostname else 'Non trouvé'}")
        print(f"Version OS     : {version.group(1) if version else 'Non trouvée'}")
        print(f"Modèle         : {model}")
        print()

        # TÂCHES 2, 3, 4 : Analyse des interfaces
        print("--- 2, 3, 4. ANALYSE DES INTERFACES ---")
        output_interfaces = net_connect.send_command('show ip interface brief')
        
        interfaces_up = []
        interfaces_down = []
        count_fast = 0
        count_giga = 0

        for line in output_interfaces.splitlines():
            if 'Interface' in line or '---' in line or not line.strip():
                continue
            
            parts = line.split()
            if len(parts) >= 2:
                intf_name = parts[0]
                status = parts[-2]
                protocol = parts[-1]

                if 'FastEthernet' in intf_name:
                    count_fast += 1
                elif 'GigabitEthernet' in intf_name:
                    count_giga += 1

                if 'up' in status.lower() and 'up' in protocol.lower():
                    interfaces_up.append(intf_name)
                else:
                    interfaces_down.append(intf_name)

        print(f"Interfaces UP   : {', '.join(interfaces_up) if interfaces_up else 'Aucune'}")
        print(f"Interfaces DOWN : {', '.join(interfaces_down) if interfaces_down else 'Aucune'}")
        print(f"Nombre de FastEthernet    : {count_fast}")
        print(f"Nombre de GigabitEthernet : {count_giga}")
        print()

        # TÂCHE 5 : Table de routage
        print("--- 5. TABLE DE ROUTAGE ---")
        output_route = net_connect.send_command('show ip route')
        print(output_route)

        net_connect.disconnect()
        print("\n🔌 Connexion fermée.")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    main()
