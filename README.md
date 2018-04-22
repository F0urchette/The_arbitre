# The_arbitre

## Cahier des charges et journal de bord

- Serveur :
    - Se connecte à interval régulier à la caméra de l'arbitre
      - Arbitre la partie (<del>Baliser le terrain pour pouvoir situer les robots sur celui-ci</del>; QrCode sur les robots avec id du robot; Détection des QrCode, récup des id et stockage id-pos dans la BD), OpenCV
    - Arbitrage :
      - Vérifier qu'ils respectent les règles et appliquer les malus
        - Ne pas quitter la ligne
        - Ne pas rentrer en collision avec un obstacle
        - Amener les victimes dans le bon hopital
        - Compter les points du robot
      - <del>Donner les renseignements qu'ils demandent (Bluetooth : Robot-arbitre puis arbitre-serveur)</del>
      
- Application :
    - Prend des photos à intervalles réguliers, et envoie ces photos au serveur
    - Envoie au serveur le signal de début et de fin de partie
    - <del>Récupère les requêtes des robots et les envoie au serveur, puis renvoie la réponse du serveur au robot)</del>

- Objectifs :
    1. Faire application qui prend des photos à interval régulier
        - 12/04 : Fonctionnel & interface
    2. Faire en sorte que l'application envoie les photos au serveur et que celui-ci les recoit
        - 11/04 : Serveur python qui peut recevoir plusieurs images à la suite à partir d'un client python
        - 13/04 : Difficultés à faire communiquer 2 programmes python autrement qu'en localhost
        - 16/04-22/04 Travail sur protocole TCP pour faire communiquer l'application et le serveur, des difficultés.
    3. Lire un QrCode sur une image (1 robot)
        1. Lire plusieurs QrCode sur une image
    4. <del>Lire plusieurs QrCode sur une image</del>
    5. <del>Trouver la position d'1 robot</del>
    6. <del>Trouver la position de plusieurs robots</del>
    4. Identifier un robot sur le terrain et le rentrer dans la BD
    5. Identifier un robot qui quitte la ligne
    6. Identifier un robot qui récupère une victime
    7. Identifier un robot qui s'arrête sur un hôpital
    8. Différencier les types de victime et tester si celui-ci correspond avec celui de l'hôpital
    9. Identifier la collision de 2 robots
    10. Etapes 4, 5, 6, 7 et 8 avec plusieurs robots
    11. Communiquer le terrain aux robot (par ondes sonores si bluetooth non disponible)

- Données :
    - Robot :
        - int : id
        - <del>(float, float) : position</del>
        - (int, int) : (score enfants transportés, score adultes transportés)
        - (int, int) : (score enfants sauvés, score adultes sauvés)
        - (int, int) : (malus sortie ligne, malus collision)
        - Lorsqu'un robot arrive un un hopital, le score x transportés correspondant est additionné au score x sauvés et reset
            > Par exemple : Un robot transporte 1 enfant et 2 adultes, le score transporté est (1 x 10, 2 x 10) et le score sauvé (0, 0). Il passe par un hopital pour enfant, le score transporté passe à (0, 20) et le score sauvé à (10, 0). Puis lorsque le robot passe sur un hopital général, le score transporté passe à (0, 0) et le score sauvé à (10, 20). Pour calculer le score final du robot, il suffit d'additionner les 2 composantes du score sauvé et de soustraires les 2 composantes du malus. Ici, supposons que le robot soit sorti 2 fois de la ligne et qu'il est percuté un robot, son malus serait (4, 8). Son score final serait donc : 10 + 20 - 4 - 8 = 18.
    - Victime :
        - int : type (0 : enfant, 1 : adulte *par exemple*)
        - <del>(float, float) : position</del>
    - Hopital
        - int : type (0 : enfant, 1 : adulte *par exemple*)
        - <del>(float, float) : position</del>

## Infos supplémentaires

Ceci est le repository du serveur du projet, voici le lien du repository de l'application mobile :
https://github.com/Ravelator/Arbiter_Android
