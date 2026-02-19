# Mémo 1 page — Git & GitHub (débutant)

> Objectif : avoir **le minimum vital** sous la main (concepts + commandes).

## Les 2 endroits
- **Local** : ton dossier + `.git/` (historique). Tu peux tout faire sans internet.
- **Distant** (GitHub) : copie du repo + outils (PR, review, CI).

## Les 3 zones (cycle)
```
Working directory --(git add)--> Staging --(git commit)--> Commits
```
- **Working dir** : fichiers sur disque
- **Staging** : sélection précise de ce qui va entrer dans le prochain commit
- **Commits** : historique (snapshots)

## Les mots clés
- **Commit** : une “photo” versionnée (snapshot) + message.
- **Branche** : un **pointeur nommé** vers une suite de commits (ex: `master`/`main`, `feat/...`).
- **HEAD** : où tu es (branche/commit courant).
- **Remote** : adresse du dépôt distant (souvent `origin`).
- **Push** : envoyer tes commits/branches vers GitHub.
- **Fetch** : récupérer les nouveautés du distant **sans** modifier tes fichiers (safe).
- **Pull** : fetch + intégration (merge ou rebase).
- **Merge** : intégrer une branche dans une autre.
- **Pull Request (PR)** : sur GitHub, demande de fusion `branche A -> branche B`.

## Les 10 commandes qui servent tout le temps
- Où j’en suis : `git status -sb`
- Historique : `git log --oneline --graph --decorate --all`
- Diff : `git diff` (et `git diff --staged`)
- Staging : `git add <fichier>` / `git add -A`
- Commit : `git commit -m "message"`
- Changer de branche : `git switch <branche>`
- Créer une branche : `git switch -c feat/xxx`
- Publier : `git push -u origin <branche>`
- Récupérer infos : `git fetch --prune`
- Mettre à jour : `git pull --rebase`

## “Anti-panique”
- Retirer du staging : `git restore --staged <fichier>`
- Annuler modifs locales d’un fichier : `git restore <fichier>`
- Voir ce qui est en staging : `git diff --staged`

## Routine pro (simple)
1. Partir de `main/master` à jour  
2. `git switch -c feat/xxx`  
3. coder → tests → commit  
4. `git push -u origin feat/xxx`  
5. PR sur GitHub vers `main/master` → merge  
6. retour : `git switch main` + `git pull --rebase`

## Note “master vs main”
`master` et `main` = juste un **nom** pour la branche principale. L’important : une branche stable.
