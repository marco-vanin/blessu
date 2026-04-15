"""
Génère bless/translations.json via l'API officielle Google Cloud Translate.
Récupère automatiquement TOUTES les langues supportées par Google.
Lance une seule fois (ou quand tu veux mettre à jour).

Prérequis :
    → créer une clé API sur console.cloud.google.com
    → activer "Cloud Translation API"

Usage :
    export GOOGLE_API_KEY=ta_cle
    python3 generate.py
"""

import json
import os
import time
import urllib.request
import urllib.parse
from pathlib import Path

API_KEY = os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    raise SystemExit("⚠️  Définis d'abord : export GOOGLE_API_KEY=ta_cle")

SOURCE = "À tes souhaits"
OUT = Path(__file__).parent / "bless" / "translations.json"

def api(endpoint, params):
    url = f"https://translation.googleapis.com/language/translate/v2/{endpoint}?" + urllib.parse.urlencode({**params, "key": API_KEY})
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())

# Récupère toutes les langues avec noms en français
print("Récupération des langues...")
langs_data = api("languages", {"target": "fr"})
languages = {l["language"]: l["name"] for l in langs_data["data"]["languages"]}
print(f"{len(languages)} langues trouvées\n")

results = []
for code, language in languages.items():
    try:
        data = api("", {"q": SOURCE, "target": code, "format": "text"})
        text = data["data"]["translations"][0]["translatedText"]
        results.append({"code": code, "language": language, "text": text})
        print(f"  ✓  {language:<30} {text}")
        time.sleep(0.05)
    except Exception as e:
        print(f"  ✗  {language:<30} erreur : {e}")

OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2))
print(f"\n→ {OUT} mis à jour ({len(results)} langues)")
