# OneSignal Notifier

[![Build](https://github.com/ebalolo-bigbandconcept/onesignalnotif/actions/workflows/docker.yml/badge.svg)](https://github.com/ebalolo-bigbandconcept/onesignalnotif/actions/workflows/docker.yml)
[![GHCR](https://img.shields.io/badge/GHCR-ghcr.io%2Febalolo--bigbandconcept%2Fonesignalnotif-blue?logo=docker&logoColor=white)](https://ghcr.io/ebalolo-bigbandconcept/onesignalnotif:latest)

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3120/)
[![Docker](https://img.shields.io/badge/Docker-20.10+-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/engine/install/)
[![Docker Compose](https://img.shields.io/badge/Docker_Compose-2.0+-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/engine/install/)
[![SQLite](https://img.shields.io/badge/SQLite-Persistent-003B57?logo=sqlite&logoColor=white)](https://www.geeksforgeeks.org/python/python-sqlite/)
[![OneSignal](https://img.shields.io/badge/OneSignal-Push_Notifications-FAFBFB?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEwIiBmaWxsPSJub25lIiB2aWV3Qm94PSIwIDAgNTEyIDUxMCI+CiAgPHBhdGggZmlsbD0iIzA1MUIyQyIgZD0iTTI1NS40OTIgMEMxMTQuMjUyLjI3NS0uOCAxMTYuMDgzLjAwNCAyNTcuMTMzLjcxIDM4OC44NjggMTAxLjMwNSA0OTcuMDE3IDIyOS45OSA1MDkuOTg1YTIuOTUzIDIuOTUzIDAgMCAwIDIuMjc0LS43NDkgMi45NDMgMi45NDMgMCAwIDAgLjk2My0yLjE4OVYyNTUuNjU0aC0xOS44MzJhMi45NDUgMi45NDUgMCAwIDEtMi45NDMtMi45Mzl2LTM5LjYzMWEyLjkzOCAyLjkzOCAwIDAgMSAyLjk0My0yLjkzOGg2Mi40NGEyLjk0NCAyLjk0NCAwIDAgMSAyLjk0MiAyLjkzOHYyOTMuOTYzYTIuOTM3IDIuOTM3IDAgMCAwIDMuMjI3IDIuOTM4QzQxMS4xNyA0OTYuOTY4IDUxMiAzODguMDc1IDUxMiAyNTUuNjU0IDUxMiAxMTQuMjkgMzk3LjEwNS0uMjc0IDI1NS40OTIgMFptNzIuODE3IDQ1My4wMjZhMi45NSAyLjk1IDAgMCAxLTIuNjgtLjM3MSAyLjk1IDIuOTUgMCAwIDEtMS4yNDMtMi40MDF2LTQxLjk2MmE0LjQgNC40IDAgMCAxIDIuNTMtMy45NzcgMTY1LjAwOSAxNjUuMDA5IDAgMCAwIDY4LjQ4LTYwLjc3OSAxNjQuNyAxNjQuNyAwIDAgMCAyNS40ODQtODcuODgyYzAtOTEuNjUzLTc1LjM2Ny0xNjYuMDQ3LTE2Ny40NDgtMTY0LjYzNy04Ny41ODggMS4zMzItMTU5LjQzNCA3MS44NDgtMTYyLjIzIDE1OS4yNzlhMTY0LjY0OSAxNjQuNjQ5IDAgMCAwIDIzLjk5MiA5MC45NzEgMTY0Ljk2MiAxNjQuOTYyIDAgMCAwIDY5LjkxMyA2My4wNDggNC40MTYgNC40MTYgMCAwIDEgMi41NDEgMy45Nzd2NDEuOTcyYTIuOTQ3IDIuOTQ3IDAgMCAxLTEuMjQzIDIuNDAxIDIuOTQ4IDIuOTQ4IDAgMCAxLTIuNjgxLjM3MUMxMDIuNjE5IDQyMy4zMjggNDQuNzQgMzQ1LjA4NCA0NS41NzQgMjUzLjY5NWMxLjAzLTExNC4xNjMgOTQuNDE1LTIwNy4zMDUgMjA4Ljc3LTIwOC4xODYgMTE2Ljc4OC0uOTAxIDIxMi4wODYgOTMuNzIgMjEyLjA4NiAyMTAuMTQ1IDAgOTAuNTM3LTU3LjYyNCAxNjcuODc5LTEzOC4xMjEgMTk3LjM3MloiPjwvcGF0aD4KPC9zdmc+Cg==)](https://onesignal.com/)

Service Python qui surveille un flux JSON d'articles et envoie automatiquement une notification push via OneSignal pour chaque nouvel élément détecté.

---

## Sommaire

* [Présentation](#présentation)
* [Fonctionnement](#fonctionnement)
* [Prérequis](#prérequis)
* [Configuration](#configuration)

  * [Variables d'environnement](#variables-denvironnement)
* [Format du flux attendu](#format-du-flux-attendu)
* [Développement](#développement)
* [Production](#production)
* [Base de données](#base-de-données)
* [Structure du projet](#structure-du-projet)
* [Dépannage](#dépannage)
* [Licence](#licence)

---

## Présentation

One signal notif surveille périodiquement un flux JSON contenant des articles.

Lorsqu'un nouvel article est détecté :

1. Son identifiant est enregistré dans une base SQLite locale.
2. Une notification push est envoyée via OneSignal.
3. L'article ne sera plus traité lors des exécutions suivantes.

Le stockage est persistant dans :

```text
/data/feed.db
```

---

## Fonctionnement

Le service exécute la boucle suivante :

```text
Flux JSON
    │
    ▼
Lecture des items
    │
    ▼
Vérification SQLite
    │
    ├── Déjà traité → Ignoré
    │
    └── Nouveau
            │
            ▼
     Notification OneSignal
            │
            ▼
      Enregistrement SQLite
```

### Comportement

* Lecture du flux défini par `FEED_URL`
* Extraction du tableau `items`
* Détection des nouveaux articles via SQLite
* Envoi des notifications OneSignal
* Attente de 60 secondes entre deux notifications
* Vérification répétée toutes les `CHECK_INTERVAL` secondes

---

## Prérequis

### Système

* Python **3.12+**
* Docker **20.10+**
* Docker Compose **2.0+**

### Services externes

#### OneSignal

Vous devez disposer :

* d'une application active
* d'un `App ID`
* d'une `REST API Key`
* d'au moins un abonnement push actif

Compte gratuit disponible sur :

```text
https://onesignal.com
```

---

## Configuration

Créer un fichier `.env` à la racine du projet :

```env
FEED_URL=https://www.example.com/feed.json
CHECK_INTERVAL=300

ONESIGNAL_APP_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
ONESIGNAL_API_KEY=xxxxxxxx
```

## Variables d'environnement

| Variable            | Description                            |
| ------------------- | -------------------------------------- |
| `FEED_URL`          | URL du flux JSON à surveiller          |
| `CHECK_INTERVAL`    | Intervalle de vérification en secondes |
| `ONESIGNAL_APP_ID`  | Identifiant de l'application OneSignal |
| `ONESIGNAL_API_KEY` | Clé API REST OneSignal                 |

---

## Format du flux attendu

Le flux doit retourner un JSON contenant un tableau `items`.

Exemple :

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

### Champs recommandés

| Champ            | Description                        |
| ---------------- | ---------------------------------- |
| `id`             | Identifiant unique de l'article    |
| `title`          | Titre affiché dans la notification |
| `url`            | Lien vers l'article                |
| `content_html`   | Contenu HTML                       |
| `date_published` | Date de publication                |

---

## Développement

Le mode développement utilise le fichier :

```text
docker-compose.dev.yml
```

Lancement :

```bash
docker compose -f docker-compose.dev.yml up --build
```

### Caractéristiques

* Construction locale de l'image
* Montage du code source
* Rechargement rapide des modifications
* Base SQLite persistante dans `./data`

Arborescence :

```text
.
├── app/
├── data/
├── .env
├── docker-compose.dev.yml
└── Dockerfile
```

---

## Production

Le mode production utilise l'image publiée sur GitHub Container Registry :

```text
ghcr.io/ebalolo-bigbandconcept/onesignalnotif:latest
```

## Déploiement

Le projet ce site sur le serveur `180.149.198.204` dans `/opt/notificationOneSignal/phytosol/`

```bash
docker compose pull
docker compose up -d
```

### Caractéristiques

* Image précompilée
* Déploiement simplifié
* Persistance des données via volume Docker
* Redémarrage automatique possible selon la configuration du compose

Le volume :

```text
./data:/data
```

permet de conserver l'historique des notifications même après redémarrage du conteneur.

---

## Base de données

Les articles déjà notifiés sont stockés dans :

```text
/data/feed.db
```

Table principale :

```sql
sent_news
```

Cette table contient les identifiants déjà envoyés afin d'éviter les doublons.

### Réinitialiser l'historique

Supprimer simplement :

```text
/data/feed.db
```

Au prochain démarrage, tous les articles du flux seront considérés comme nouveaux.

---

## Structure du projet

```text
app/
├── feeds.py
├── main.py
├── models.py
├── onesignal.py
├── storage.py
├── utils.py
└── worker.py
```

### Description des modules

| Fichier        | Rôle                               |
| -------------- | ---------------------------------- |
| `main.py`      | Point d'entrée                     |
| `worker.py`    | Boucle principale                  |
| `feeds.py`     | Lecture du flux JSON               |
| `onesignal.py` | Communication avec l'API OneSignal |
| `storage.py`   | Gestion SQLite                     |
| `models.py`    | Modèles de données                 |
| `utils.py`     | Fonctions utilitaires              |

---

## Dépannage

### Aucune notification reçue

Vérifier :

* les variables `ONESIGNAL_APP_ID` et `ONESIGNAL_API_KEY`
* la présence d'abonnements actifs dans OneSignal
* que chaque article possède un `id` unique
* les logs du conteneur

```bash
docker logs <container_name>
```

### Trop de notifications au premier lancement

C'est le comportement attendu.

Tous les articles absents de la base SQLite sont considérés comme nouveaux et déclenchent donc un envoi.

---

## Configuration OneSignal

Notifications envoyées via :

```text
https://api.onesignal.com/notifications?c=push
```

Paramètres utilisés :

| Paramètre | Valeur                |
| --------- | --------------------- |
| Canal     | `push`                |
| Segment   | `Total Subscriptions` |
| Langues   | Français + Anglais    |
| URL       | Article détecté       |

---

## Licence

Aucune licence n'est actuellement définie.
