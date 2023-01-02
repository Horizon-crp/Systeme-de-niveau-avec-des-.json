from os import path
import json
from .math import get_level_max
def get_xp(member_id: int) -> tuple:
  fi = f"db/{member_id}.json"
  if path.isfile(fi) is False:
    with open(fi, 'x') as f:
      json.dump({'xp': 1}, f, indent=2)
    xp = 1
    level, max = get_level_max(xp)
    return xp, level, max
  with open(fi, 'r') as f:
    data = json.load(f)
  xp = data['xp']
  level, max = get_level_max(xp)
  return xp, level, max

def save(xp, id):
  with open(f"db/{id}.json", 'w') as f:
    json.dump({"xp": xp}, f, indent=2)
  return
