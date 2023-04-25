
# A’rosa-je

**Préambule** : Ce projet est réalisé dans le cadre d'une MSPR. Le but de ce projet est de concevoir et tester
des solutions applicatives en suivant un cahier des charges. L’entreprise choisie pour cette MSPR est fictive.

A'rosa-je est une application web qui permet la mise en relation de particuliers afin de faire garder ses plantes
en cas d'absence prolongées. A'rosa-je permet aussi à des professionels de prodiguer des conseils d'entretien
afin que les propriétaires s’occupent de mieux en mieux de leurs plantes.


## Features

- Soon™


## Lancer en local

Créer un nouveau dossier ``projet_arosaje`.

```bash
mkdir projet_arosaje
```

Se déplacer dans ce dossier et y cloner le projet.

```bash
cd projet_arosaje
git clone https://gitlab.com/aurock/projet_mspr_arosaje.git
```

Se déplacer dans le dossier du projet.

```bash
cd projet_mspr-arosaje
```

Je cherche toujours une solution propre pour lancer proprement un serveur Django avec un ficheir env.
En attendant, il faut modifier le fichier `settings.py` en suivant la section
[Variables d'Environnement](##Variables d'Environnement).

Démarrer le serveur.
```bash
python manage.py runserver 8000
```


## Déploiement

Placer le `Dockerfile` dans le dossier `projet_arosaje`.

Build le projet depuis ce dossier.

```bash
docker build -t lorispercin/arosaje:version .
```

Push le projet sur DockerHub.

```bash
docker push lorispercin/arosaje:version
```

Le reste du déploiement est pour le moment géré manuellement par l'administrateur du serveur de production.


## Variables d'Environnement

Pour lancer ce projet, certaines valeurs du fichier `settings.py` doivent être modifiées. Ceci est normalement réalisé
à l'aide d'un fichier .env mais aucune solution fiable et simple d'implémentation n'a encore été trouvée.

**ATTENTION:** Ces changements réalisés en local ne devraient pas être push sur le git !

`SECRET_KEY =` trouvable dans le `env`

`DEBUG = True`


## Auteurs

- Jeremy
- Juliette
- Brice
- Loris
- Flavien


## Acknowledgements

 - [How to Build a Django and Gunicorn Application with Docker](https://www.digitalocean.com/community/tutorials/how-to-build-a-django-and-gunicorn-application-with-docker)
 - [How to Set Up a Scalable Django App with DigitalOcean Managed Databases and Spaces](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-scalable-django-app-with-digitalocean-managed-databases-and-spaces)
