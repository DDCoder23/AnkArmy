# Game Engine (Pseudo-logique)

Version : 0.1
Statut : Spécification technique

---

# 1. Objectif

Le Game Engine est le cœur logique d’AnkArmy.

Il est responsable de :

* l’analyse des réponses Anki ;
* la mise à jour des missions ;
* le calcul de l’XP ;
* la gestion de la discipline ;
* la validation des promotions ;
* la génération des événements.

Il est la seule source de logique métier du système.

---

# 2. Principe fondamental

Toutes les actions suivent un flux unique :

> Entrée (événement Anki) → Traitement → Mise à jour état → Sortie (terminal + sauvegarde)

Aucune logique ne doit exister en dehors de ce flux.

---

# 3. Événements d’entrée

Le moteur réagit uniquement à 4 événements :

## 1. START_SESSION

Déclenché à l’ouverture d’une session Anki.

Actions :

* charger l’état joueur ;
* générer mission ;
* afficher ordre de mission.

---

## 2. CARD_REVIEWED

Déclenché après chaque carte.

Données :

* correct / incorrect
* temps de réponse

Actions :

* mise à jour score mission ;
* calcul XP partiel ;
* ajustement discipline léger.

---

## 3. END_SESSION

Déclenché à la fin d’une session.

Actions :

* finaliser mission ;
* calcul XP final ;
* calcul discipline ;
* génération du rapport ;
* déclenchement promotions éventuelles.

---

## 4. APP_CLOSE

Déclenché à la fermeture d’Anki.

Actions :

* sauvegarde complète ;
* vérification intégrité état ;
* clôture session.

---

# 4. Pipeline principal

```text id="g7m2xq"
EVENT INPUT
     │
     ▼
Load State
     │
     ▼
Update Mission System
     │
     ▼
Update Progression System
     │
     ▼
Update Discipline System
     │
     ▼
Check Promotions
     │
     ▼
Generate Terminal Output
     │
     ▼
Save State
```

---

# 5. Calcul XP

## 5.1 Carte individuelle

```text id="xp1"
if correct:
    base_xp = 1
else:
    base_xp = 0
```

Multiplicateurs appliqués :

* discipline
* série
* difficulté mission

---

## 5.2 Fin de mission

```text id="xp2"
mission_xp = base_xp_total
mission_xp *= discipline_multiplier
mission_xp += bonus_mission
```

---

# 6. Gestion de la discipline

## Mise à jour par carte

```text id="d1"
if correct:
    discipline += small_gain
else:
    discipline -= small_loss
```

---

## Mise à jour fin de session

```text id="d2"
if session_success:
    discipline += bonus
else:
    discipline -= penalty
```

---

# 7. Validation mission

Une mission est validée si :

* objectif atteint ;
* taux de réussite minimum respecté ;
* contraintes non violées.

Sinon :

* mission échouée ;
* XP réduit ;
* discipline impactée.

---

# 8. Promotions

À la fin de session :

```text id="p1"
if xp >= threshold AND discipline >= required_level:
    promote_player()
```

---

# 9. Déclenchement des événements

## Promotion

* affichage terminal
* sauvegarde grade
* mise à jour missions futures

---

## Sanction

```text id="s1"
if discipline < critical:
    apply_penalty()
    restrict_missions()
```

---

# 10. Résolution des conflits

Priorité stricte :

1. Intégrité des données
2. Discipline
3. XP
4. Missions
5. Interface

---

# 11. Règle de stabilité

Le Game Engine doit être :

* déterministe ;
* prévisible ;
* testable ;
* sans effets secondaires cachés.

---

# 12. Règle d’or

Le Game Engine ne décide jamais “quoi montrer”.

Il décide uniquement “ce qui est vrai”.

Le Terminal décide de la présentation.
