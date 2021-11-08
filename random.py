import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Zlata"]

random_first = random.choice(people)
random_second = random.choice(people)

random_bar = random.choice(bars)

print(f'How about you go to {random_bar} with {random_first} and {random_second}')