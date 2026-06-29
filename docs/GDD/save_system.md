# Save System

Version : 0.1
Statut : En cours de conception

---

# 1. Objectif

Le système de sauvegarde d’AnkArmy garantit la persistance de toutes les données du joueur :

* progression ;
* XP ;
* discipline ;
* grades ;
* missions ;
* statistiques ;
* équipements ;
* historique.

Aucune perte de données ne doit être possible en utilisation normale.

---

# 2. Philosophie

Le système de sauvegarde doit respecter trois principes :

* fiabilité ;
* simplicité ;
* autonomie locale.

Le système doit fonctionner sans serveur externe.

---

# 3. Stockage local

Toutes les données sont stockées localement sur la machine de l’utilisateur via Anki.

Formats possibles :

* JSON (principal)
* fichiers internes Anki (fallback)

---

# 4. Structure des données

## 4.1 Profil joueur

```json id="p1x9aa"
{
  "name": "player",
  "rank": "Recrue",
  "xp": 0,
  "discipline": 100,
  "reputation": 0,
  "days_in_service": 0
}
```

---

## 4.2 Statistiques

```json id="k9v3bd"
{
  "cards_reviewed": 0,
  "correct_answers": 0,
  "incorrect_answers": 0,
  "sessions_completed": 0,
  "best_streak": 0
}
```

---

## 4.3 Missions

```json id="x7q2lp"
{
  "current_mission": null,
  "mission_history": []
}
```

---

## 4.4 Grades

```json id="m3ld91"
{
  "current_rank": "Recrue",
  "promotion_history": []
}
```

---

## 4.5 Équipements

```json id="q8z1ka"
{
  "unlocked_items": [],
  "active_items": []
}
```

---

# 5. Cycle de sauvegarde

La sauvegarde se déclenche automatiquement :

* après chaque mission ;
* après chaque session Anki ;
* lors de la fermeture d’Anki ;
* à intervalles réguliers.

---

# 6. Sécurité des données

Le système doit garantir :

* aucune corruption de fichier ;
* écriture atomique (éviter les sauvegardes partielles) ;
* récupération automatique en cas d’erreur.

---

# 7. Versionnement

Chaque sauvegarde contient une version du système :

```text id="v7m2aa"
save_version : 0.1
```

Cela permet :

* compatibilité future ;
* migration des données ;
* évolution du système sans perte.

---

# 8. Récupération

En cas de problème :

* le système tente de charger la dernière sauvegarde valide ;
* sinon, création d’un profil vierge ;
* aucune suppression automatique sans confirmation.

---

# 9. Performance

Le système doit être :

* rapide (< 50ms d’écriture) ;
* non bloquant pour Anki ;
* asynchrone si possible.

---

# 10. Règle fondamentale

La progression du joueur est sacrée.

Aucune erreur logicielle ne doit effacer une carrière.
