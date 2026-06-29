# Terminal

Version : 0.1
Statut : En cours de conception

---

# 1. Objectif

Le terminal est l’interface principale d’AnkArmy.

Il remplace toute interface classique par un affichage textuel inspiré d’un centre de commandement militaire.

Il doit transmettre des informations rapidement, sans ralentir les révisions.

---

# 2. Philosophie

Le terminal repose sur trois principes :

* sobriété ;
* clarté ;
* immersion.

Le joueur ne doit jamais se sentir dans un jeu lourd, mais dans un système de commande efficace.

---

# 3. Apparence générale

Le terminal est affiché en texte brut stylisé.

Exemple :

```text id="1kq8zm"
========================================
     AIR COMMAND - TERMINAL SYSTEM
========================================

STATUS : CONNECTED
USER   : AVIATOR
RANK   : SERGENT
DISCIPLINE : STABLE

----------------------------------------
```

---

# 4. Couleurs (optionnel selon support)

* Vert : validation / succès
* Orange : avertissement
* Rouge : alerte / discipline faible
* Blanc : information neutre

---

# 5. Sections principales

## 5.1 Connexion

Affichage à l’ouverture d’Anki.

Exemple :

```text id="9xq2aa"
Connexion au Commandement...

Vérification du dossier...

Accès autorisé.

Bienvenue, Recrue.
```

---

## 5.2 Ordre de mission

Affiché avant chaque session.

```text id="3mncqk"
MISSION 248

OBJECTIF :
Réviser 32 cartes

PRIORITÉ :
Normale

STATUS :
VALIDÉ
```

---

## 5.3 Pendant la mission

Affichage minimal (ou invisible selon configuration).

Optionnel :

* progression
* cartes restantes
* discipline actuelle

---

## 5.4 Rapport de mission

Affiché à la fin.

```text id="7vpl1a"
MISSION TERMINÉE

RÉSULTATS :
- Cartes : 32
- Réussite : 91%
- Temps : 14 min

ÉVALUATION :
SATISFAISANT

XP : +280
```

---

## 5.5 Rapport disciplinaire

Affiché uniquement si nécessaire.

```text id="4qz8ld"
RAPPORT DU COMMANDEMENT

ATTENTION :
Baisse de discipline détectée

RECOMMANDATION :
Reprise régulière des missions
```

---

## 5.6 Promotion

Affichage spécial.

```text id="8vld9c"
========================================
PROMOTION OFFICIELLE
========================================

Vous êtes promu au grade de :

CAPORAL

Félicitations.
========================================
```

---

# 6. Ton du système

Le terminal utilise un langage :

* direct ;
* militaire ;
* factuel ;
* jamais émotionnellement excessif.

Exemples :

* ❌ “Incroyable performance !!!”
* ✔ “Performance excellente.”

---

# 7. Règle de rapidité

Aucune interaction du terminal ne doit dépasser :

* 1 seconde pour l’affichage initial ;
* 5 secondes pour les rapports.

---

# 8. Minimalisme obligatoire

Le terminal ne doit jamais :

* afficher trop d’informations en même temps ;
* interrompre une révision ;
* forcer des interactions longues ;
* ralentir Anki.

---

# 9. Cohérence globale

Tous les messages du jeu doivent passer par ce terminal :

* missions ;
* XP ;
* discipline ;
* promotions ;
* sanctions.

Il est la seule voix du Commandement.

---

# 10. Règle fondamentale

Le terminal n’est pas une interface.

C’est le Commandement.
