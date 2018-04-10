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
