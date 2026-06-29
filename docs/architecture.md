# Architecture

Version : 0.1
Statut : En cours de conception

---

# 1. Objectif

Définir l’architecture technique d’AnkArmy afin de transformer le Game Design Document en système fonctionnel dans Anki.

Ce document sert de pont entre :

* le design du jeu ;
* le code de l’addon ;
* le moteur Anki.

---

# 2. Philosophie technique

L’architecture doit respecter quatre principes :

* compatibilité totale avec Anki ;
* simplicité de maintenance ;
* modularité forte ;
* absence de dépendances externes inutiles.

---

# 3. Vue d’ensemble

AnkArmy est composé de 5 modules principaux :

```text id="a1x9dd"
Anki Addon Core
        │
        ├── Game Engine
        ├── Mission System
        ├── Progression System
        ├── Save System
        └── Terminal UI
```

---

# 4. Intégration avec Anki

Le système s’intègre via :

* hooks Anki (révisions, réponses, sessions) ;
* API interne d’Anki ;
* interception des événements de carte.

---

# 5. Modules principaux

---

## 5.1 Game Engine

Cœur logique du système.

Responsable de :

* calcul XP ;
* gestion discipline ;
* validation des missions ;
* déclenchement des promotions.

Aucune logique métier ne doit exister en dehors de ce module.

---

## 5.2 Mission System

Responsable de :

* génération des missions ;
* adaptation selon discipline ;
* définition des objectifs ;
* validation des résultats.

---

## 5.3 Progression System

Responsable de :

* gestion des grades ;
* calcul de l’évolution carrière ;
* déblocages.

---

## 5.4 Save System

Responsable de :

* stockage local ;
* chargement des données ;
* versionnement ;
* récupération des erreurs.

---

## 5.5 Terminal UI

Responsable de :

* affichage des missions ;
* rapports ;
* messages du Commandement ;
* promotions.

Aucune logique métier.

---

# 6. Flux de données

```text id="b2x8ff"
Anki Event (card review)
        │
        ▼
Game Engine analyse
        │
        ▼
Mission System met à jour l’état
        │
        ▼
Progression System calcule XP / grade
        │
        ▼
Save System enregistre
        │
        ▼
Terminal UI affiche le résultat
```

---

# 7. Hooks Anki

Le système repose sur des événements :

* début de session ;
* réponse à une carte ;
* fin de session ;
* fermeture d’Anki.

Chaque événement déclenche une mise à jour du Game Engine.

---

# 8. Gestion des états

Le système fonctionne avec un état global :

```json id="c3l9aa"
{
  "player_state": {},
  "mission_state": {},
  "session_state": {},
  "global_stats": {}
}
```

Cet état est la seule source de vérité.

---

# 9. Règle d’or

Aucune logique métier ne doit être dispersée dans l’interface ou les hooks.

Tout doit passer par le Game Engine.

---

# 10. Extensibilité

Le système est conçu pour permettre :

* ajout de nouvelles missions ;
* nouveaux grades ;
* nouveaux systèmes de récompenses ;
* évolution sans casser les sauvegardes.

---

# 11. Contraintes Anki

Le système doit :

* être rapide (< 50ms traitement) ;
* ne jamais bloquer une révision ;
* fonctionner offline ;
* rester léger en mémoire.

---

# 12. Règle fondamentale

AnkArmy doit toujours être perçu comme une couche invisible au-dessus d’Anki.

Anki reste l’outil principal. AnkArmy est un système de lecture et de progression.
