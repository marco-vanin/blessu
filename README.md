# blessu

À chaque éternuement, une façon de dire "À tes souhaits" dans une nouvelle langue.

```
  Gesundheit
  Allemand
```

Le mot est automatiquement copié dans le presse-papier.

---

## Installation

```bash
git clone https://github.com/ton-user/bless-u.git
cd bless-u
pip3 install -e .
```

Ajoute ça dans ton `~/.zshrc` si la commande n'est pas trouvée :

```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

---

## Commandes

| Commande | Description |
|---|---|
| `blessu` | Traduction aléatoire + copie dans le presse-papier |
| `blessu --history` | Langues déjà utilisées |
| `blessu --reset` | Vider l'historique |
| `blessu --help` | Afficher l'aide |

---

## Langues

20 langues : anglais, espagnol, allemand, italien, japonais, arabe, russe, portugais, néerlandais, suédois, polonais, turc, coréen, chinois, hindi, finnois, hébreu, grec, tchèque, hongrois.

Pour en ajouter, édite `bless/translations.json` :

```json
{ "code": "fr", "language": "Français", "text": "À tes souhaits" }
```

---

## Stockage

L'historique est sauvegardé dans `~/.config/blessu/history.json`.
