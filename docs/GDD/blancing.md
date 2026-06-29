# Balancing

Version : 0.1
Statut : En cours de conception

---

# 1. Objectif

Le fichier de balancing définit toutes les valeurs numériques du système AnkArmy :

* gain d’XP ;
* perte ou gain de discipline ;
* conditions de promotion ;
* multiplicateurs ;
* sanctions ;
* bonus.

Il sert de référence centrale pour ajuster l’équilibre du jeu.

---

# 2. Philosophie

L’équilibrage repose sur trois principes :

* la progression doit être lente mais visible ;
* les efforts réguliers doivent être fortement récompensés ;
* les irrégularités doivent avoir un impact mesurable mais récupérable.

---

# 3. XP (Expérience)

## 3.1 Gain de base

* Carte correcte : +1 XP
* Série de 10 cartes correctes : +5 XP bonus
* Mission complétée : +20 à +100 XP selon difficulté

---

## 3.2 Multiplicateurs

### Discipline élevée

* Discipline excellente : x1.2 XP
* Discipline stable : x1.0 XP

---

### Discipline faible

* Discipline fragile : x0.8 XP
* Discipline critique : x0.6 XP

---

# 4. Discipline

## 4.1 Gain

* Mission complétée : +2 à +10 discipline
* Série de 3 jours : +5 discipline bonus

---

## 4.2 Perte

* Jour sans révision : -10 discipline
* Mission abandonnée : -5 discipline
* Performance très faible : -3 discipline

---

# 5. Seuils de progression

## Grades (approximation initiale)

* Recrue → Caporal : 0 à 500 XP
* Caporal → Sergent : 500 à 1200 XP
* Sergent → Adjudant : 1200 à 2500 XP
* Adjudant → Officier : 2500 à 5000 XP
* Officier → Commandement : 5000+ XP

---

# 6. Difficulté des missions

## Mission facile

* 10 à 20 cartes
* XP : faible
* discipline neutre

---

## Mission normale

* 20 à 40 cartes
* XP : standard

---

## Mission difficile

* 40 à 80 cartes
* XP : élevé
* discipline influencée fortement

---

## Mission critique

* 80+ cartes
* XP : très élevé
* discipline fortement impactée

---

# 7. Sanctions

## Avertissement

* aucun impact mécanique direct

---

## Surveillance

* -10% XP global temporaire

---

## Restriction

* -25% XP
* missions simplifiées uniquement

---

# 8. Bonus

## Série de jours consécutifs

* 3 jours : +5% XP
* 7 jours : +10% XP
* 14 jours : +20% XP

---

# 9. Promotions

Une promotion nécessite :

* XP minimum atteint
* discipline ≥ stable
* activité régulière

Le système privilégie la régularité sur les performances ponctuelles.

---

# 10. Règle fondamentale

Le système doit :

* récompenser la constance ;
* éviter les “rush” de progression ;
* maintenir une sensation de carrière longue.

---

# 11. Ajustabilité

Toutes les valeurs de ce fichier sont :

* modifiables ;
* testables ;
* ajustables sans modifier le code.

Ce fichier est la base de l’équilibrage global du jeu.
