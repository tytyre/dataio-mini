# Exercices guidés — Git & GitHub avec le projet `dataio-mini`

> Objectif : apprendre par la pratique, avec des manipulations courtes et vérifiables.  
> Pré-requis : tu es dans le repo `dataio-mini` et tes tests passent (`pytest -q`).

---

## Exercice 0 — Comprendre où tu es
**But :** identifier branche courante, fichiers modifiés, historique.

1) Où je suis ?
```bash
git status -sb
```

2) Quelles branches j’ai ?
```bash
git branch -vv
```

3) Voir l’historique en “graph”
```bash
git log --oneline --graph --decorate --all
```

✅ Attendu : tu vois une branche principale (`master` ou `main`) et des branches `feat/...`.

---

## Exercice 1 — Faire un commit propre (staging)
**But :** comprendre la différence *working dir* vs *staging*.

1) Modifie `README.md` (ajoute 2 lignes “Usage CLI”).
```bash
echo "" >> README.md
echo "## Usage" >> README.md
echo "- NPZ: python -m dataio_mini write-demo /tmp/demo.npz --fmt npz" >> README.md
```

2) Observe ce qui a changé
```bash
git status -sb
git diff
```

3) Mets en staging **uniquement** README
```bash
git add README.md
git diff --staged
```

4) Commit
```bash
git commit -m "Docs: add quick CLI usage"
```

✅ Attendu : `git status -sb` ne montre plus README en modifié.

---

## Exercice 2 — Créer une branche feature
**But :** “1 feature = 1 branche”.

1) Depuis la branche principale :
```bash
git switch master  # ou main, selon ton repo
```

2) Créer une branche feature
```bash
git switch -c feat/better-cli-output
```

3) Vérifie
```bash
git status -sb
```

✅ Attendu : tu es sur `feat/better-cli-output`.

---

## Exercice 3 — Un petit changement + tests + commit
**But :** travailler en feature et garantir “tests verts”.

1) Améliore l’affichage du CLI (dans `src/dataio_mini/cli.py`) :  
Ajoute l’impression du nombre de clés lues, par exemple après la boucle `for`.

Exemple (à adapter) :
```python
print(f"Read {len(data)} arrays from {args.path}")
```

2) Lance les tests
```bash
pytest -q
```

3) Commit
```bash
git add src/dataio_mini/cli.py
git commit -m "Feat: improve CLI read output"
```

✅ Attendu : `pytest -q` passe et tu as un commit sur la branche feature.

---

## Exercice 4 — Publier sur GitHub (remote + push)
**But :** comprendre local vs distant.

1) Vérifie le remote
```bash
git remote -v
```

2) Push de ta branche feature
```bash
git push -u origin feat/better-cli-output
```

✅ Attendu : GitHub voit la branche. Tu peux ouvrir une PR.

---

## Exercice 5 — Pull Request (sur GitHub)
**But :** utiliser le workflow standard.

1) Sur GitHub, ouvre une PR :
- Base : `master` (ou `main`)
- Compare : `feat/better-cli-output`

2) Vérifie que les changements sont ceux attendus.
3) Merge la PR (bouton “Merge”).

✅ Attendu : la branche principale sur GitHub contient ta feature.

---

## Exercice 6 — Se resynchroniser en local après merge
**But :** mettre à jour la branche principale localement.

1) Revenir sur la branche principale
```bash
git switch master  # ou main
```

2) Mettre à jour depuis GitHub
```bash
git pull --rebase
```

3) Supprimer la branche feature localement (si la PR est mergée)
```bash
git branch -d feat/better-cli-output
```

✅ Attendu : ta branche principale locale contient le commit de la PR.

---

## Exercice 7 — Récupérer une erreur (restore / unstage)
**But :** savoir “annuler” sans paniquer.

1) Modifie un fichier puis annule
```bash
echo "# test" >> README.md
git status -sb
git restore README.md
git status -sb
```

2) Mets en staging par erreur, puis retire du staging
```bash
echo "# test2" >> README.md
git add README.md
git diff --staged
git restore --staged README.md
git status -sb
```

✅ Attendu : tu sais revenir à un état propre.

---

## Exercice 8 — Tagger une version
**But :** marquer une version stable.

1) Crée un tag (ex : v0.2.0)
```bash
git tag -a v0.2.0 -m "v0.2.0"
```

2) Pousse le tag
```bash
git push origin v0.2.0
```

✅ Attendu : GitHub affiche le tag (et tu peux faire une Release si tu veux).

---

## Exercice 9 — Commande “diagnostic”
**But :** savoir décrire l’état du repo en 10 secondes.

Exécute et garde ça dans ton réflexe :
```bash
git status -sb
git branch -vv
git log --oneline --graph --decorate --max-count=20
```

✅ Attendu : tu sais répondre à “où tu en es ?” sans hésiter.

---

## Bonus (si tu veux aller plus loin)
- **stash** : mettre de côté des modifs non committées
- **rebase interactif** : nettoyer/squasher des commits avant PR
- **.gitignore + data** : ne pas versionner les gros `.npz` / `.h5` (sauf échantillons)

Si tu veux, on fait ensemble un **stash** + un **rebase -i** sur une branche d’entraînement.
