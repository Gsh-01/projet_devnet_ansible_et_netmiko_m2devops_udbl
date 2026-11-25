# Projet d'Automatisation Réseau avec Ansible et Netmiko

Projet académique (**M2 DevOps**) consacré à l'automatisation de la configuration, de la gestion et de la vérification d'une infrastructure réseau multiservices simulée sous **GNS3** à l'aide d'**Ansible** et de **Netmiko**.

## Architecture et Topologie Réseau

La topologie GNS3 (`Projet_Automatisation_Infra_Multiservices_Ansible`) s'articule autour des éléments suivants[cite: 12, 14] :

* **R1** : Routeur central gérant le routage et l'interconnexion des segments réseau[cite: 12].
* **IOU1 et IOU2** : Commutateurs Layer 2 / Layer 3 assurant la segmentation (VLANs) et la connectivité des postes clients[cite: 12].
* **PC1 – PC4** : Hôtes VPCS de test et de validation réseau[cite: 12].
* **Cloud1** : Interface d'interconnexion entre la topologie simulée et l'environnement hôte / contrôleur d'automatisation[cite: 12].

### Plan d'adressage et VLANs (à compléter)

| Équipement / Zone | Interface / VLAN | Adresse IP / Masque | Rôle |
| :--- | :--- | :--- | :--- |
| `R1` | `[ex: Gi0/0]` | `[ex: 192.168.1.1/24]` | `[ex: Passerelle / Inter-VLAN]` |
| `IOU1` | `[ex: VLAN 10]` | `[ex: 192.168.10.2/24]` | `[ex: Commutation accès]` |
| `IOU2` | `[ex: VLAN 20]` | `[ex: 192.168.20.2/24]` | `[ex: Commutation accès]` |
| `PC1 – PC4` | `[ex: Eth0]` | `[ex: DHCP / Statique]` | `[ex: Tests connectivité]` |

## Prérequis et Stack Technique

* **Système d'exploitation** : Linux (Ubuntu / Debian)
* **Simulation réseau** : GNS3 (avec images IOS/IOU configurées localement)[cite: 12, 14]
* **Automatisation** : Ansible (`ansible-core`, collections réseau appropriées) et Python 3 avec **Netmiko**
* **Gestion de versions** : Git et GitHub

## Structure du Dépôt

```text
Projet_Ansible/
├── Projet_Automatisation_Infra_Multiservices_Ansible/  # Projet GNS3
├── [inventaire/ ou hosts.ini]                          # Inventaire des équipements réseau
├── [playbooks/]                                         # Playbooks Ansible
├── [scripts/ ou netmiko/]                               # Scripts Python basés sur Netmiko
├── .gitignore                                           # Exclusion des images et archives lourdes
└── README.md
