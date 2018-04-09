# The_arbitre

- Serveur :
    - Se connecte à intervalle régulier à la caméra de l'arbitre
      - Répertorie la pos des robots (Baliser le terrain pour pouvoir situer les robots sur celui-ci; QrCode sur les robots avec id du robot; Détection des QrCode, récup des id et stockage id-pos dans la BD), OpenCV
    - Arbitrage :
      - (Vérifier qu'ils respectent les règles)
      - Donner les renseignements qu'ils demandent (Bluetooth : Robot - arbitre puis arbitre - serveur)
      - Serveur : Google Cloud Platform (Python)
      
- Application :
    - Prend des photos à intervalles réguliers, et envoi ces photos au serveur
    - Récupère les requêtes des robots et les envoi au serveur, puis renvoit la réponse du serveur au robot
