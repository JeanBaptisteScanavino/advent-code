# Advent of Code

Ce mini projet est un template pour répondre aux énigmes journalières du advent of code (mais peut être détourné).

## Technos

Ce template vous permet de répondre aux énigmes en utilisant, au choix :
- JS
- TS
- Tests unitaires (en route vers le TDD)

## Utilisation

- Récupérez le template localement

```bash
$ git@github.com:thetribeio/template-ts-tdd.git
$ mv template-ts-tdd template
$ cd template
```

- Installer les dépendances

```bash
$ yarn install
```

- Copier le template pour démarrer une nouvelle journée

```bash
$ cp -r template day01
```

- Le fichier `input.txt` est destiné à recevoir les données des problèmes posés.

## Commandes

- Lancer le code

```bash
$ yarn start
```

- Lancer les tests

```bash
$ yarn test         # Une seul fois
$ yarn test:watch   # En continue
```

- Tests lint et typage

```bash
$ yarn lint
$ yarn type-check
```

## Template collaboratif

Si vous voyez des améliorations à apporter à ce template, sentez vous libre d'y apporter des modifications ! :) 




Happy Advent of Code !
