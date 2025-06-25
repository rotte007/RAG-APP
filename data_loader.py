import json
from typing import List, Dict

def load_docs(path: str) -> List[Dict]:
    """Load JSON docs: expect a list of {"id": str, "text": str}."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
