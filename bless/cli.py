import json
import random
import subprocess
import sys
from pathlib import Path
from bless.storage import load, save

TRANSLATIONS = {
    e["code"]: e
    for e in json.loads((Path(__file__).parent / "translations.json").read_text())
}

B = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
R = "\033[0m"

HELP = f"""
  {B}blessu{R}             traduction aléatoire (copiée dans le presse-papier)
  {B}blessu --history{R}   langues déjà utilisées
  {B}blessu --reset{R}     vider l'historique
"""

def copy(text):
    try:
        subprocess.run(["pbcopy"], input=text.encode(), check=True)
    except Exception:
        pass

def cmd_history():
    used = load()
    if not used:
        print(f"\n  {DIM}Aucun historique{R}\n")
        return
    print()
    for i, code in enumerate(used, 1):
        e = TRANSLATIONS.get(code)
        if e:
            print(f"  {DIM}{i:>2}.{R}  {CYAN}{e['text']}{R}  {DIM}{e['language']}{R}")
    print()

def main():
    args = sys.argv[1:]

    if "--help" in args:
        print(HELP)
        return
    if "--reset" in args:
        save([])
        print(f"\n  {GREEN}Historique réinitialisé{R}\n")
        return
    if "--history" in args:
        cmd_history()
        return

    used = load()
    available = [code for code in TRANSLATIONS if code not in used]

    if not available:
        used = []
        available = list(TRANSLATIONS.keys())
        print(f"\n  {DIM}Tour complet — on recommence{R}")

    code = random.choice(available)
    e = TRANSLATIONS[code]
    copy(e["text"])

    print(f"\n  {B}{CYAN}{e['text']}{R}\n  {DIM}{e['language']}{R}\n")

    used.append(code)
    save(used)
