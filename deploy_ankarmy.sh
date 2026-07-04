#!/bin/bash

SOURCE=~/Documents/AnkArmy
TARGET=~/.local/share/Anki2/addons21/AnkArmy

echo "🪖 AnkArmy deployment started..."
git add .
git commit -m "modif"
git push

# Création du dossier cible si besoin
mkdir -p "$TARGET"

# Copie en excluant git et fichiers inutiles
rsync -av \
  --exclude ".git" \
  --exclude "__pycache__" \
  --exclude "*.pyc" \
  "$SOURCE/" "$TARGET/"

echo "✅ AnkArmy deployed successfully!"
