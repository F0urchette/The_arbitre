# The_arbitre

- Serveur :
    - Se connecte à interval régulier à la caméra de l'arbitre
      - Répertorie la pos des robots (Baliser le terrain pour pouvoir situer les robots sur celui-ci; QrCode sur les robots avec id du robot; Détection des QrCode, récup des id et stockage id-pos dans la BD), OpenCV
    - Arbitrage :
      - (Vérifier qu'ils respectent les règles)
      - Donner les renseignements qu'ils demandent (Bluetooth : Robot - arbitre puis arbitre - serveur)
      - Serveur : Google Cloud Platform (Python)
      
- Application :
    - Prend des photos à intervalles réguliers, et envoie ces photos au serveur
    - Récupère les requêtes des robots et les envoie au serveur, puis renvoie la réponse du serveur au robot

- Objectifs :
    - Faire application qui prend des photos à interval régulier
    - Faire en sorte que l'application envoie les photos au serveur et que celui-ci les recoit
    - Lire un QrCode sur une image (1 robot)
    - Trouver la position d'1 robot
    - Lire plusieurs QrCode sur une image
    - Trouver la position de plusieurs robots

- Données :
    - Robot :
        - int : id
        - (float, float) : position
        - (int, int) : (score enfants transportés, score adultes transportés)
        - (int, int) : (score enfants sauvés, score adultes sauvés)
        - Lorsqu'un robot arrive un un hopital, le score x transportés correspondant est additionné au score x sauvés et reset
            - Par exemple : Un robot transporte 1 enfant et 2 adultes, le score transporté est (1 x 10, 2 x 10) et le score sauvé (0, 0). Il passe par un hopital pour enfant, le score transporté passe à (0, 20) et le score sauvé à (10, 0). Puis lorsque le robot passe sur un hopital général, le score transporté passe à (0, 0) et le score sauvé à (10, 20).
    - Victime :
        - int : type (0 : enfant, 1 : adulte | par exemple)
    - Hopital
        - int : type (0 : enfant, 1 : adulte | par exemple)
