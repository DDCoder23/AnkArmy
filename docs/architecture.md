# 🪖 AnkArmy — Architecture du projet

## 🎯 Vision du projet

AnkArmy transforme Anki en un jeu de progression militaire.

L’utilisateur commence comme **soldat simple** et progresse dans les grades en fonction de sa régularité et de ses performances de révision.

Chaque carte Anki devient un **ordre militaire** à exécuter.

---

## 🧩 Concept central

### 🔁 Boucle de gameplay
1. Réviser des cartes Anki
2. Réussir / échouer des réponses
3. Gagner de l’expérience (XP)
4. Monter en grade
5. Débloquer de nouveaux rôles / missions

---

## 🪖 Système de progression

| Grade | Rôle | Débloque |
|------|------|----------|
| Recrue | Débutant | Missions simples |
| Soldat | Utilisateur actif | Streak bonus |
| Caporal | Régularité | Missions quotidiennes |
| Sergent | Discipline | Défis chronométrés |
| Lieutenant | Maîtrise | Missions stratégiques |
| Capitaine | Haut niveau | Gestion de “unités de cartes” |

---

## ⚙️ Architecture technique

### 📁 Structure du projet
AnkArmy/
│
├── manifest.json
├── main.py
├── config.py
│
├── core/
│ ├── xp_system.py
│ ├── rank_system.py
│ ├── missions.py
│ ├── stats_tracker.py
│
├── ui/
│ ├── dashboard.py
│ ├── overlays.py
│
├── hooks/
│ ├── on_card_review.py
│ ├── on_deck_complete.py
│
├── data/
│ ├── player.json
│ ├── progress.json
│
├── assets/
│ ├── icons/
│ ├── sounds/
│
└── docs/
├── architecture.md
├── README.md

---

## 🧠 Logique du système

### 📌 1. Hooks Anki
Le plugin écoute :
- réponse carte
- réussite/échec
- temps de réponse

👉 déclenche XP + events

---

### 📌 2. XP System
- bonne réponse → +XP
- mauvaise réponse → peu ou pas XP
- série → bonus multiplicateur

---

### 📌 3. Rank System
- seuils d’XP définissent les grades
- chaque grade débloque des mécaniques

---

### 📌 4. Missions
Exemples :
- “Réviser 20 cartes sans erreur”
- “3 jours de streak”
- “Deck complet en mode rapide”

---

## 🎮 Boucle de motivation

Le système doit toujours répondre à 3 besoins :

- 📈 progression visible
- 🎯 objectifs courts
- 🪖 immersion (ordre militaire, hiérarchie)

---

## ⚠️ Contraintes importantes

- ne jamais bloquer Anki (plugin léger)
- sauvegarde locale obligatoire
- pas de dépendance serveur au début

---

## 🚀 Étapes futures

- UI type “table de commandement”
- missions dynamiques
- système d’unités (groupes de cartes)
- ranking global optionnel
