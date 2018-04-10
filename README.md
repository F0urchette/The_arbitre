# The_arbitre

- Serveur :
    - Se connecte à interval régulier à la caméra de l'arbitre
      - Répertorie la pos des robots (Baliser le terrain pour pouvoir situer les robots sur celui-ci; QrCode sur les robots avec id du robot; Détection des QrCode, récup des id et stockage id-pos dans la BD), OpenCV
    - Arbitrage :
      - Vérifier qu'ils respectent les règles et appliquer les malus
      - Donner les renseignements qu'ils demandent (Bluetooth : Robot-arbitre puis arbitre-serveur)
      - Serveur : Google Cloud Platform (Python)
      
- Application :
    - Prend des photos à intervalles réguliers, et envoie ces photos au serveur
    - Récupère les requêtes des robots et les envoie au serveur, puis renvoie la réponse du serveur au robot

- Objectifs :
    1) Faire application qui prend des photos à interval régulier
    2) Faire en sorte que l'application envoie les photos au serveur et que celui-ci les recoit
    3) Lire un QrCode sur une image (1 robot)
    4) Trouver la position d'1 robot
    5) Lire plusieurs QrCode sur une image
    6) Trouver la position de plusieurs robots
    7) Communication robot-arbitre par ondes sonores

- Données :
    - Robot :
        - int : id
        - (float, float) : position
        - (int, int) : (score enfants transportés, score adultes transportés)
        - (int, int) : (score enfants sauvés, score adultes sauvés)
        - (int, int) : (malus sortie ligne, malus collision)
        - Lorsqu'un robot arrive un un hopital, le score x transportés correspondant est additionné au score x sauvés et reset
            - Par exemple : Un robot transporte 1 enfant et 2 adultes, le score transporté est (1 x 10, 2 x 10) et le score sauvé (0, 0). Il passe par un hopital pour enfant, le score transporté passe à (0, 20) et le score sauvé à (10, 0). Puis lorsque le robot passe sur un hopital général, le score transporté passe à (0, 0) et le score sauvé à (10, 20). Pour calculer le score final du robot, il suffit d'additionner les 2 composantes du score sauvé et de soustraires les 2 composantes du malus. Ici, supposons que le robot soit sorti 2 fois de la ligne et qu'il est percuté un robot, son malus serait (4, 8). Son score final serait donc : 10 + 20 - 4 - 8 = 18.
    - Victime :
        - int : type (0 : enfant, 1 : adulte | par exemple)
        - (float, float) : position
    - Hopital
        - int : type (0 : enfant, 1 : adulte | par exemple)
        - (float, float) : position
