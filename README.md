# blessu

À chaque éternuement, une nouvelle façon de dire "À tes souhaits" — dans une des 195 langues du monde.

```
  Gesundheit.
  Allemand
```

La traduction est automatiquement copiée dans le presse-papier. blessu parcourt toutes les langues sans répétition avant de recommencer un nouveau cycle.

---

## Installation

```bash
git clone https://github.com/marcovanin/bless-u.git
cd bless-u
pip3 install -e .
```

Si la commande n'est pas trouvée, ajouter le chemin Python à `~/.zshrc` :

```bash
export PATH="$HOME/Library/Python/3.x/bin:$PATH"
```

---

## Usage

```
blessu              traduction aléatoire, copiée dans le presse-papier
blessu --history    afficher les langues déjà utilisées dans le cycle
blessu --reset      réinitialiser l'historique
blessu --help       afficher l'aide
```

---

## Langues

195 langues couvertes — abkhaze, afrikaans, albanais, allemand, anglais, arabe, arménien, basque, bengali, breton, bulgare, catalan, chinois, coréen, croate, danois, espagnol, estonien, finnois, français, gallois, grec, gujarati, hébreu, hindi, hongrois, indonésien, irlandais, islandais, italien, japonais, kazakh, letton, lituanien, luxembourgeois, malais, maltais, marathi, mongol, néerlandais, norvégien, ourdou, perse, polonais, portugais, punjabi, roumain, russe, serbe, slovaque, slovène, suédois, swahili, tamoul, tchèque, thaï, turc, ukrainien, vietnamien, yoruba, zoulou, et bien d'autres.

Pour ajouter une langue, éditer `bless/translations.json` :

```json
{ "code": "xx", "language": "Nom de la langue", "text": "À tes souhaits en xx" }
```

---

## Stockage

L'historique du cycle est sauvegardé dans `~/.config/blessu/history.json`.
