# ScaProj


## Projet Ydays - 2020 - Melvin Aubert


### Présentation du projet


Dans un but de développement de compétence personnel, étant nouveau dans le milieu de la cybersécurité j'ai fais 
le choix de découvrir deux nouvelles technologies afin de réaliser un programme capable de réaliser des attaques 
sur des protocoles réseaux de basse couche. Mon premier choix étant de découvrir la programmation et sachant que 
Python est une technologie très utilisée de nos jours, j'ai donc choisi de développer un outil grâce à ce language. 
Ayant découvert Scapy quelques jours avant, et sachant que celui-ci était exploitable via Python. J'ai donc 
rapidement décidé de réaliser mon projet là dessus.


### Choix Technologique


On utilisera le language python afin d'interagir avec la librairie Scapy.

* [Python 2.7](https://www.python.org/)

* [Scapy](https://scapy.net/)

* [IDE Visual Studio Code](https://code.visualstudio.com/)
* [CodeAcademy](https://www.codecademy.com/learn)
* l'outil Scapy installé sur une machine joignable sur mon réseau local. ( OS Debian 10.4)

Mes sources : 
* Des vidéos YouTube
* http://www.secdev.org/conf/scapy_csw05.pdf ( un cours Scapy)
* https://scapy.net/ - Le site de l'outil Scapy


### Déroulement

Dans un premier temps je me suis formé sur le site de CodeAcademy, j'ai passé quelques heures à découvrir le language et intégrer quelques notions d'algorithmes que je n'avais jamais vu auparavant.

Par la suite j'ai commencé à  me renseigner sur la formation d'un menu à choix multiple , pour moi il était important que l'utilisateur puisse faire le choix entre différentes attaques.

Après quelques recherches j'ai défini le fait d'avoir unquement 2 attaques possibles:
* CAM_Overflow
* ARP_Spoofing

La première consiste à  envoyer un maximum de paquet en modifiant l'adresse source ainsi que l'adresse mac du paquet afin de saturer la table CAM d'un switch de niveau 2. Une fois cette table saturée , l'attaquant est en capacité d'écouter tout ce qui passe par le switch qui se comporte désormais comme un hub.

La seconde attaque consiste à rediriger le traffic de la machine cible vers le pc de l'attaquant afin qu'il puisse écouter les différentes requêtes de la victime. On appelle alors cela du MiTM (ou Man in the middle )

### Voie d'amélioration
Afin d'améliorer mon code , je souhaiterais dans les jours a venir réaliser une interface graphique afin de rendre mon programme plus user-friendly.
Dans un second temps , je pense qu'il serais possible d'ajouter des attaques un peu plus complexe à mon outil.
