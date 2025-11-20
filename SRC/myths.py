import json
import random

def load_myths(filepath="data/myth_data.json"):
  try:
    with open(filepath, "r") as file:
      myths = json.load(file)
    return myths
  except FileNotFoundError:
    print("Error: myth_data.json not found.")
    return []
  except json.JSONDecodeError:
    print("Error: Could not read myth_data.json.")

def get_random_myth(myths):
  if not myths:
    return None
  return random.choice(myths)
