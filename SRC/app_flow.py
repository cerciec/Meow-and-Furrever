# Connects all project features

from cat_profile import create_cat_profile, format_cat_profile
from myths import load_myths, get_random_myth
from vet_reminder import yearly_checkup, dental_health_reminder, indoor_cat_reminder, senior_cat_checkup

def run_app():
  print("\nWelcome to Meow and Furrever!")
  print("Because cats deserve care.\n")

# Create Cat Profile
print("Let's create your cat's profile!")
name = input("What is your cat's name? ")
age_input = input("How old is your cat (in years)? ")

# Validate Age
try:
  age = int(age_input)
except ValueError:
  age = 0
  print("Invalid age. Setting age to 0.")

indoor_choice = input("Is your cat an indoor cat? (yes/no): ").strip().lower()
indoor = indoor_choice.startswith("y")

# Build profile dictionary
profile = create_cat_profile(name, age, indoor)
print("\nYour Cat's Profile")
print(format_cat_profile(profile))

# Myth of the Day
myths = load_myths()
myth = get_random_myth(myths)

if myth:
  print("\nMyth of the Day")
  print("~~~~~~~~~~~~~~~~~~~~")
  print("Myth:  ", myth["myth"])
  print("Truth:  ", myth["truth"])
else:
  print("\nNo myths available.")
