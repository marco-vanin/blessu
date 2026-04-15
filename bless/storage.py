import json
from pathlib import Path

FILE = Path.home() / ".config" / "blessu" / "history.json"

def load():
    try:
        return json.loads(FILE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save(data):
    FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(data))
    tmp.replace(FILE)