# Feed Notifier

Service Python qui surveille un flux JSON d'articles et envoie une notification push OneSignal pour chaque nouvel élément.

## Fonctionnement

- Le service lit un flux défini par `FEED_URL`.
- Il extrait les éléments du tableau `items` du JSON.
- Chaque article déjà traité est mémorisé localement dans une base SQLite.
- Lorsqu'un nouvel article est trouvé, une notification push est envoyée via OneSignal.
- Un délai de 60 secondes est appliqué entre deux envois pour éviter les rafales si plusieurs articles arrivent en même temps.
- La vérification du flux est répétée toutes les `CHECK_INTERVAL` secondes.

Le stockage local est persistant dans `/data/feed.db`.

## Exemple de format attendu pour le flux

Le flux doit renvoyer un JSON avec une structure proche de celle-ci :

```json
{
  "items": [
    {
      "id": "article-1",
      "title": "Titre de l'article",
      "url": "https://example.com/article-1",
      "content_html": "<p>Contenu HTML</p>",
      "date_published": "2026-06-17T10:30:00Z"
    }
  ]
}
```

## Variables d'environnement

Créer un fichier `.env` à la racine du projet :

```env
FEED_URL=https://www.example.com/feed.json
CHECK_INTERVAL=300
ONESIGNAL_APP_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
ONESIGNAL_API_KEY=xxxxxxxx
```

### Détail

- `FEED_URL` : URL du flux JSON à surveiller.
- `CHECK_INTERVAL` : délai entre deux vérifications du flux, en secondes.
- `ONESIGNAL_APP_ID` : identifiant de l'application OneSignal.
- `ONESIGNAL_API_KEY` : clé API OneSignal.

## OneSignal

Le service envoie les notifications via l'API REST OneSignal :

- endpoint : `https://api.onesignal.com/notifications?c=push`
- canal ciblé : `push`
- segment ciblé : `Total Subscriptions`

Le message inclut :

- un titre (`headings`) en anglais et en français
- un contenu (`contents`) en anglais et en français
- l'URL de l'article

## Installation

### Développement

Le plus simple est de lancer le service avec le compose de développement :

```bash
docker compose -f docker-compose.dev.yml up --build
```

Ce mode construit l'image localement, monte le code source et garde la base SQLite dans `./data`.

### Production

En production, il suffit de récupérer l'image publiée puis de lancer le compose principal :

```bash
docker compose pull
docker compose up -d
```

Le fichier `docker-compose.yml` utilise l'image `ghcr.io/anakingig/feed-notifier:latest` et monte `./data` vers `/data` pour conserver la base SQLite.

## Base de données

Le fichier SQLite contient la liste des articles déjà envoyés.

- table `sent_news` : identifiants des notifications déjà traitées
- fichier : `/data/feed.db`

Supprimer ce fichier réinitialise l'historique des envois.

## Structure du projet

```text
app/
  feeds.py
  main.py
  models.py
  onesignal.py
  storage.py
  utils.py
  worker.py
```

## Dépannage

Si aucune notification n'apparaît dans OneSignal :

- vérifier que `ONESIGNAL_APP_ID` et `ONESIGNAL_API_KEY` sont corrects
- vérifier que des abonnements push existent bien dans l'application OneSignal
- vérifier que le flux renvoie bien des `id` uniques pour chaque article
- vérifier les logs du conteneur pour voir la réponse exacte de l'API OneSignal

Si le service renvoie trop d'articles d'un coup au premier lancement, c'est parce que tous les articles non présents dans la base locale sont considérés comme nouveaux.

## Licence

Aucune licence n'a été définie pour le moment.
