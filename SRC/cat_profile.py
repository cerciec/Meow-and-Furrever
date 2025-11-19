# cat_profile.py
# common cat breeds
COMMON_BREEDS = ["Domestic Shorthair", "American Shorthair", "Domestic Longhair", "Siamese", "Ragdoll", "Maine Coon", "I don't see my cat's breed (type my own)"]

#Common cat color/pattern categories
COLOR_PATTERNS = ["Tuxedo", "Tabby", "Calico", "Tortie", "Solid", "Bi-Color", "type my own"]

def choose_with_custom(options, prompt_text, custom_default_label):

print(f"\n{prompt_text}")
for i, item in enumerate(options, start=1):
  print(f"{i}. {item}")

choice = input("\nEnter the number of your choice: ").strip()

if choice.isdigit():
  index = int(choice) - 1
  if 0 <= index < len(options)
    selected = options[index]
# If they picked the "type my own" option (last item)
if index == len(options) - 1:
  custom = input("Type your own value"
