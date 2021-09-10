# [Microservice partenaire]()

[![pipeline status](https://gitlab.com/biomedical/backend/microservice-partenaires/badges/develop/pipeline.svg)](https://gitlab.com/biomedical/backend/microservice-partenaires/-/commits/develop)
[![coverage report](https://gitlab.com/biomedical/backend/microservice-partenaires/badges/develop/coverage.svg)](https://gitlab.com/biomedical/backend/microservice-partenaires/-/commits/develop)

## Description

Microservice de gestion des partenaires.

## Documentation

La documentation est disponible [ici](CONTRIBUTING.md).

## Contribuer

Veuillez prendre un moment pour lire le [guide sur la contribution](CONTRIBUTING.md).

## Environement de travail

Nous avons configuré trois types d'environement de travail

```
     - Environement de test (--env DJANGO_SETTINGS_MODULE=core.settings.test )
     - Environement de dev (--env DJANGO_SETTINGS_MODULE=core.settings.dev )
     - Environement de prod (--env DJANGO_SETTINGS_MODULE=core.settings.prod )
```

## Docker

Pour pouvoir build l'image Docker

```
     docker-composer up --build
```

## Changelog

[CHANGELOG.md](CHANGELOG.md) liste tous les changements effectués lors de chaque release.
