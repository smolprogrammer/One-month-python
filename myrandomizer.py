import random

ice_cream = ["blueberry",
             "melon",
             "banana",
             "chocolate",
             "lemon"]

family = ["grandma",
          "father",
          "mother",
          "brother",
          "cousin"]

random_ice_cream = random.choice(ice_cream)

random_family = random.choice(family)

print(f'Maybe you want to eat {random_ice_cream} ice cream with your {random_family}?')
