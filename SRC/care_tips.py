# care_tips.py
# Simple grooming and enrichment tips for the Meow and Furrever project.

import random


GROOMING_TIPS = [
    "Brush long-haired cats daily to prevent mats and hairballs.",
    "Use a soft brush and go slowly if your cat is nervous about grooming.",
    "Check around the ears and tail base for tangles or debris.",
    "Introduce grooming in short, positive sessions with treats."
]

ENRICHMENT_TIPS = [
    "Short, daily play sessions are better than one long session once a week.",
    "Rotate toys so your cat doesn’t get bored of the same ones.",
    "Provide vertical spaces like cat trees or shelves for climbing and observing.",
    "Offer puzzle feeders or treat balls to encourage foraging behavior."
]


def random_grooming_tip():
    """Return a random grooming-related tip."""
    return random.choice(GROOMING_TIPS)


def random_enrichment_tip():
    """Return a random enrichment-related tip."""
    return random.choice(ENRICHMENT_TIPS)


# Optional testing
if __name__ == "__main__":
    print("Grooming tip:", random_grooming_tip())
    print("Enrichment tip:", random_enrichment_tip())
