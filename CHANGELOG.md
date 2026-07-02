# CHANGELOG

Ce fichier décrit les mises à jour (release notes / journal des modifications) du projet wpss_admin.

Règles et conventions

- Suivre la versionnage sémantique (SemVer) : MAJOR.MINOR.PATCH
  - MAJOR : changements incompatibles
  - MINOR : ajout de fonctionnalité rétrocompatible
  - PATCH : corrections de bugs rétrocompatibles
- Chaque version doit avoir une date et un court résumé des changements.
- Regrouper les changements par catégories : Added, Changed, Fixed, Deprecated, Removed, Security.
- Garder les entrées concises et orientées utilisateur (ce que le changement apporte).

Format recommandé (exemple)

## [Unreleased]
- Work in progress pour la prochaine version.

## [1.2.0] - 2026-07-01
### Added
- Ajout d'une interface d'administration pour gérer les utilisateurs.
- Export CSV des rapports.

### Changed
- Mise à jour de la dépendance Django vers 4.2.x.

### Fixed
- Correction d'un bug provoquant l'interruption du service sur certaines requêtes.

## [1.1.2] - 2026-05-15
### Fixed
- Correction de l'affichage des champs dans la vue des profils.

Bonnes pratiques pour l'équipe

- Mettre à jour le CHANGELOG.md lors de la préparation d'une release (avant le tag).
- Utiliser des commits clairs (ex: `fix: corrige la validation du formulaire`) pour faciliter la génération automatique si nécessaire.
- Pour les petites équipes, tenir à jour la section [Unreleased] et la basculer lors du tagging.

Exemple de workflow rapide

1. Travailler sur une branche feature/bugfix.
2. Fusionner dans main (ou la branche de release) via PR avec description claire.
3. Mettre à jour le CHANGELOG.md : ajouter les lignes sous [Unreleased] ou directement créer une nouvelle section versionnée.
4. Tagger la version git : `git tag -a v1.2.0 -m "Release 1.2.0"`
5. Pousser le tag et publier la release (GitHub Releases).

Checklist de release

- [ ] Tests unitaires et d'intégration OK
- [ ] Changelog mis à jour
- [ ] Version dans le fichier de configuration (si applicable) mise à jour
- [ ] Tag git créé
- [ ] Release GitHub créée avec notes et binaires (si nécessaire)

Génération automatique (optionnel)

- Possibilité d'utiliser des outils comme `github-changelog-generator` ou `auto-changelog` pour générer le changelog à partir des commits et des PRs.
- Si vous utilisez une génération automatique, conservez une section manuelle pour les remarques particulières.

Traductions

- Le fichier principal est en français. Pour des publics internationaux, ajouter un CHANGELOG_en.md ou traduire les entrées clés dans la page GitHub Releases.

Contact

- Pour toute question sur le format du changelog, contacter l'équipe technique ou l'auteur des releases.
