# Fort Boyard Simulator/ Projet Python

*Contributeurs:*

- Aurélien Devaux-Riviere(mise en forme, fonctions principales)
- Ivan Perez(fonctions secondaires et enigmes)


Ce projet simule une partie d'un jeu inspiré de Fort Boyard. Trois clés sont attendues pour accéder à la salle finale et réussir le jeu. les épreuves sont diverses. Il y des énigmes, des épreuves aléatoires ou résultant de l'hasard, des épreuves de mathématiques et de
logique.





## les fonctions principales sont :

- la fonction jeu() qui permet de lancer la partie
- enigme_pere_fourras qui choisi et lance une énigme au hasard
- epreuve_finale qui se lance apres avoir récupérée les trois clés et lance une enigme 
- les fonctions épreuves maths/hasard/logique qui consituent le jeu en lui-même.

Puis les fonction_utiles sont l'ensemble des fonctions qui sont nécéssaires au bon fonctionnement du programme


Le langage de programmation utilisé est python et les bibliotheques qui ont été utilisées sont "random" pour la génération aléatoire et "json" pour l'exctraction et l'utilisation des données. De plus Pycharm a été utilisé afin de réaliser ce projet



Pour cloner ce dépot Git, il suffit simplement de copier le lien suivant: https://github.com/Aurel1dr/pyfort-perez-devauxriviere-D 
Ensuite il faut ouvrir Gitbash et écrire 'git clone' suivi de l'url du lien que l'on souhaite copier


Pour lancer ce programme il suffit de lancer le programme 'main'.

#### Algorithme de jeu():

1. Lancement de la fonction introduction qui donne les règles du jeu et composer_équipes qui crée l'équipe qui vas participer.

2. initialisation des variables pour suivre le nombre de clés.

#### lancement du jeu:

3. tant que les clés obtenues sont inférieur au nombre de clés voulues on lance un jeu.

4. on lance le choix des épreuves via menu_epreuves

5. on choisi un joueur avec choisir_joueur

6. Selection des épreuves (entre épreuve logique/épreuve hasard/ épreuve maths/énigme Pere Fouras), si nombre choisi est supérieur à 4
alors: "Choix d'épreuve invalide"

#### Vérification des clés:

7. Si le joueur à réussi alors: Clés prend +1 et le message 'Félicitation' s'affiche

8. Sinon: le message 'joueur n'as pas réussi' s'affiche

9. enregistrer historique

10. si clés obtenues sont égales à 3 alors: le message s'affiche 'bravo' et cela lance salle_de_trésor()

## Fonctions implémentées:

### Jeu d'Énigmes et Épreuves

Ce projet contient plusieurs modules permettant de jouer à un jeu d'énigmes et d'épreuves variées. Le jeu propose des défis sous forme de logique, de mathématiques, de hasard, et d'énigmes pour tester les joueurs.

## Modules du jeu

### Module `enigme_pere_Fouras`

- **`charger_enigme`** : Cette fonction prend en paramètre le nom d'un fichier JSON et retourne une liste d'énigmes extraites du fichier.
  
- **`enigme_pere_fourras`** : Cette fonction ne prend aucun paramètre. Elle choisit une énigme aléatoire grâce à **`charger_enigme`**, la pose au joueur et lui donne trois chances pour y répondre. Elle renvoie un booléen qui indique si la réponse du joueur est correcte.

### Module `epreuve_finale`

- **`salle_de_tresor`** : Cette fonction ne prend aucun paramètre. Elle ouvre un fichier d'indices, choisit une énigme et permet au joueur de tenter de résoudre l'énigme avec trois essais. Si le joueur trouve la réponse, il gagne le jeu.

### Module `fonctions_utiles`

- **`Introduction`** : Affiche les règles du jeu sans prendre de paramètre.
  
- **`composer_equipe`** : Cette fonction ne prend aucun paramètre et renvoie une liste contenant les joueurs (maximum de 3).
  
- **`menu_épreuve`** : Demande au joueur de choisir parmi 4 types d'épreuves disponibles. Si le choix est incorrect (supérieur à 4), un message d'erreur est affiché.
  
- **`choisir_joueur`** : Prend en paramètre la liste des joueurs (générée par **`composer_equipe`**) et demande au joueur de choisir un membre pour l'épreuve.

- **`enregistrer_historique`** : Cette fonction prend en paramètre le joueur choisi, l'épreuve sélectionnée, et le résultat de l'épreuve (booléen).

### Module `mathématiques`

- **`factorielle`** : Calcule la factorielle d'un nombre donné.

- **`epreuve_math_factorielle`** : Lance une épreuve demandant de calculer la factorielle d'un nombre. Elle renvoie un booléen qui indique si la réponse est correcte.

- **`epreuve_roulette_mathematique`** : Lance une épreuve aléatoire de roulette mathématique et renvoie un booléen en fonction de la réussite du joueur.

- **`epreuve_math_premier`** : Lance une épreuve demandant de vérifier si un nombre est premier. Utilise les fonctions **`est_premier`** (pour vérifier la primalité) et **`premier_plus_proche`** (pour trouver le premier nombre premier supérieur ou égal à un nombre donné). Elle renvoie un booléen.

- **`epreuve_math`** : Lance aléatoirement une des trois épreuves disponibles : **`epreuve_math_factorielle`**, **`epreuve_roulette_mathematique`**, ou **`epreuve_math_premier`**.

### Module `hasard`

- **`bonneteau`** : Jeu de bonneteau, qui renvoie un booléen en fonction de la victoire ou défaite du joueur.

- **`jeu_de_des`** : Jeu de dés, qui renvoie un booléen pour indiquer si le joueur a gagné ou non.

- **`epreuve_hasard`** : Choisit aléatoirement entre les épreuves de bonneteau et de jeu de dés.

### Module `logique`

- **`jeu_bataille_navale`** : Regroupe toutes les fonctions nécessaires pour jouer à la bataille navale, un jeu de logique où deux joueurs s'affrontent en tirant des projectiles sur une grille.

- **`suiv`** : Prend en paramètre le joueur qui vient de jouer et renvoie celui qui doit jouer ensuite.

- **`affiche_grille`** : Affiche une grille (par exemple, la grille de tir d'un joueur) avec un message personnalisé.

- **`tour`** : Simule un tour du jeu en prenant en paramètre la grille de tir d'un joueur et celle de son adversaire. Le joueur tire, et un message annonce si le tir a touché ou non.

- **`gagne`** : Vérifie si un joueur a gagné la partie en fonction de sa grille de tir. Si le joueur a coulé deux bateaux (indiqués par deux 'X'), il remporte la partie.


### Gestion des Entrées et Erreurs

### Traitement des Valeurs et des Intervalles

Le code gère les valeurs et les intervalles en vérifiant que les entrées de l'utilisateur respectent des conditions préalablement définies. Par exemple, pour les choix de l'utilisateur dans le menu d'épreuves, le code s'assure que l'entrée est un nombre entier compris entre 1 et 4. Si l'utilisateur entre une valeur en dehors de cet intervalle, une erreur est générée et un message explicatif est affiché, demandant à l'utilisateur de réessayer avec une valeur valide.

De même, lors de la saisie des réponses aux énigmes, le code vérifie que les réponses sont sous forme de texte ou de chiffres, selon le type d'énigme, et que celles-ci respectent les critères définis (longueur de la chaîne, caractères autorisés, etc.).

## Méthodes de Gestion des Erreurs

Les principales méthodes utilisées pour gérer les erreurs potentielles sont les suivantes :

- **Validation des Entrées** : Avant chaque saisie de l'utilisateur, le code vérifie si la donnée est conforme au format attendu. Par exemple, si l'on attend un nombre entier, une vérification est effectuée pour s'assurer que l'utilisateur n'entre pas de texte ou de valeurs non numériques.

- **Boucles de Réessai** : Lorsqu'une erreur est détectée, une boucle de réessai permet à l'utilisateur de tenter une nouvelle entrée, jusqu'à ce qu'une entrée valide soit fournie. Ceci est utilisé, par exemple, lorsque l'utilisateur fait un mauvais choix d'épreuve ou répond mal à une énigme.

- **Messages d'Erreur** : Des messages clairs et informatifs sont affichés lorsque des erreurs surviennent, expliquant à l'utilisateur ce qui a échoué et comment il peut corriger son erreur. Ces messages sont rédigés de manière à être compréhensibles pour l'utilisateur, afin qu'il sache exactement ce qu'il doit faire.

### Liste des Bugs Connus

- **Erreurs dans l'épreuve de mathématiques (factorielle)** : Si l'utilisateur entre un nombre trop élevé pour calculer la factorielle (par exemple, 1000!), le programme peut rencontrer un dépassement de mémoire ou une erreur d'exécution. 

- **Erreur de calcul dans les épreuves de logique** : Lors des épreuves de logique, notamment la bataille navale, si les grilles sont corrompues ou mal initialisées, le jeu peut planter ou ne pas fonctionner correctement. 

---

### Tests et Validation

### Stratégies de Test

Les stratégies de test sont cruciales pour s'assurer que toutes les fonctionnalités du jeu fonctionnent comme prévu et que les erreurs potentielles sont identifiées et corrigées avant la mise en production. Les tests sont réalisés à la fois manuellement et automatiquement pour vérifier la validité du code et la stabilité du jeu.

### Cas de Test Spécifiques et Résultats

1. **Test de Validation des Choix d'Épreuve**  
   **Objectif** : Vérifier que le joueur peut correctement choisir une épreuve parmi les 4 proposées et que des erreurs sont levées pour des choix invalides.  
   **Cas de test** :  
- Entrée valide : Choix de "1" pour l'épreuve de logique  
- Entrée invalide : Choix de "5" ou "0"  
   **Résultat attendu** :  
- Pour un choix valide, l'épreuve correspondante est lancée.  
- Pour un choix invalide, un message d'erreur est affiché et l'utilisateur est invité à entrer un nombre entre 1 et 4.  
   **Résultat obtenu** : Conformité avec les attentes. Le test est passé avec succès.

2. **Test de Réponse aux Énigmes**  
   **Objectif** : Vérifier que le joueur peut répondre correctement aux énigmes et que trois tentatives sont autorisées.  
   **Cas de test** :  
- Réponse correcte à la première tentative  
- Réponse incorrecte suivie de deux réponses incorrectes supplémentaires  
   **Résultat attendu** :  
- Si la réponse est correcte au premier essai, l'énigme est validée et le joueur peut passer à l'épreuve suivante.  
- Si les trois réponses sont incorrectes, un message de fin d'épreuve est affiché et le joueur est informé qu'il a perdu l'épreuve.  
   **Résultat obtenu** : Conformité avec les attentes. Le test est passé avec succès.

3. **Test de la Factorielle (Épreuve Mathématique)**  
   **Objectif** : Vérifier le bon fonctionnement de l'épreuve demandant de calculer la factorielle d'un nombre.  
   **Cas de test** :  
- Entrée valide : Calcul de la factorielle de "5" (résultat attendu : 120)  
- Entrée invalide : Tentative de calcul de la factorielle d'un nombre trop grand (par exemple, "1000")  
   **Résultat attendu** :  
- Pour une entrée valide, le résultat est correctement calculé et affiché.  
- Pour une entrée invalide, une gestion d'exception empêche le plantage du programme et un message d'erreur est affiché.  
   **Résultat obtenu** : Le test a échoué pour les très grands nombres, une gestion d'exception est à mettre en place pour éviter les dépassements de mémoire.

4. **Test de la Bataille Navale**  
   **Objectif** : Vérifier que le jeu de bataille navale fonctionne correctement, avec un joueur qui réussit à couler des bateaux et un autre qui perd.  
   **Cas de test** :  
- Un joueur gagne en coulant les deux bateaux adverses.  
- Un joueur perd en n'ayant pas coulé ses deux bateaux avant que l'adversaire ne les ait coulés.  
   **Résultat attendu** :  
- Le joueur qui coule les deux bateaux remporte la partie.  
- Si la partie se termine avant, un message de "victoire" ou "défaite" est affiché.  
   **Résultat obtenu** : Le test a passé avec succès, mais des améliorations peuvent être apportées pour les cas où la grille est corrompue.

5. **Test de Réponse au Jeu de Dés**  
   **Objectif** : Vérifier que l'épreuve de jeu de dés fonctionne correctement, avec une probabilité aléatoire de victoire ou de défaite.  
   **Cas de test** :
 - Lancer du dé et obtenir un résultat supérieur à une certaine valeur pour gagner (par exemple, un jet supérieur ou égal à 4).  
   **Résultat attendu** :  
- Si le résultat est supérieur ou égal à 4, le joueur gagne.  
- Si le résultat est inférieur à 4, le joueur perd.  
   **Résultat obtenu** : Conformité avec les attentes. Le test a passé avec succès.

## Installation et Lancement

Pour jouer au jeu, vous devez d'abord charger les modules nécessaires. Ensuite, vous pouvez suivre les étapes dans le jeu pour choisir un joueur, participer à des épreuves, et tenter de résoudre les énigmes.

1. **Charger les modules** : Importez les modules nécessaires dans votre environnement Python.
2. **Lancer le jeu** : Utilisez la fonction d'introduction pour comprendre les règles et commencer à jouer.
3. **Participer aux épreuves** : Choisissez les épreuves auxquelles vous souhaitez participer et répondez correctement pour avancer.

---

Ce jeu offre une expérience interactive avec des énigmes, des épreuves mathématiques, de logique et de hasard pour défier vos compétences et obtenir des points. Préparez-vous à relever le défi !


