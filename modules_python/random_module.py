import random

# nb aléatoire entre 1 et 5
print(f"random.randint(1,5) : {random.randint(1,5)}")

# nb aléatoire entre 0 et 4 (!)
print(f"random.randrange(5) : {random.randrange(5)}")

# nb aléatoire entre 0 et 100 (!) avec un pas de 10
print(f"random.randrange(0, 101, 10) : {random.randrange(0, 101, 10)}")

# nb aléatoire à virgule entre 0 et 4 (!)
print(f"random.uniform(1,5) : {random.uniform(1,5)}")