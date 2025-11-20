# cat_profile.py
# common cat breeds
COMMON_BREEDS = [
    "Domestic Shorthair",
    "American Shorthair",
    "Domestic Longhair",
    "Siamese",
    "Ragdoll",
    "Maine Coon",
    "I don't see my cat's breed (type my own)",
]

# Common cat color/pattern categories
COLOR_PATTERNS = [
    "Tuxedo",
    "Tabby",
    "Calico",
    "Tortie",
    "Solid",
    "Bi-Color",
    "type my own",
]


def choose_with_custom(options, prompt_text, custom_default_label):
    """Let the user choose from options; if they pick the last option, allow typing custom value."""
    print(f"\n{prompt_text}")
    for i, item in enumerate(options, start=1):
        print(f"{i}. {item}")

    choice = input("\nEnter the number of your choice: ").strip()

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(options):
            selected = options[index]
            # If they picked the "type my own" option (last item)
            if index == len(options) - 1:
                custom = input("Type your own value: ").strip()
                return custom if custom else custom_default_label
            return selected

    print("Invalid choice. Using default value.\n")
    return custom_default_label


def choose_breed():
    return choose_with_custom(COMMON_BREEDS, "Choose your cat's breed:", custom_default_label="Breed not specified")


def choose_color_pattern():
    return choose_with_custom(COLOR_PATTERNS, "Choose your cat's color or pattern:", custom_default_label="Color/pattern not specified")


def create_cat_profile(name, age, indoor=True):
    """Create a cat profile dict using interactive selection for breed and color/pattern."""
    breed = choose_breed()
    color_pattern = choose_color_pattern()

    return {
        "name": name,
        "age": age,
        "breed": breed,
        "color_pattern": color_pattern,
        "indoor": indoor,
    }


def format_cat_profile(profile):
    """Return a nicely formatted string of the cat profile."""
    living_style = "Indoor" if profile.get("indoor", True) else "Outdoor"
    return (
        "\nCat Profile\n"
        f"Name: {profile.get('name', '')}\n"
        f"Age: {profile.get('age', '')} years\n"
        f"Breed: {profile.get('breed', '')}\n"
        f"Color / Pattern: {profile.get('color_pattern', '')}\n"
        f"Living Style: {living_style}\n"
    )
