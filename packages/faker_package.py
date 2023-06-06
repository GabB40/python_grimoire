# py -m pip install faker

import numbers
from faker import Faker

fake = Faker(locale="fr_FR")
print(fake.name())
print(fake.address())
print(fake.email())

# unicité
random_unique_numbers: list[int] = [fake.unique.random_int() for n in range(500)]
print(len(random_unique_numbers) == len(set(random_unique_numbers)))

# parenthèse sur les sets = liste non-ordonnée avec des éléments uniques
print((set((1, 2, 3, 3))))
print({1, 2, 3, 3})

# autres exemples de chose utile à faker
for i in range(10):
    print(fake.file_path(depth=5, category="video"))
    print(
        fake.credit_card_number(),
        fake.credit_card_expire(),
        fake.credit_card_security_code(),
    )
    print(fake.rgb_color(), fake.hex_color())
    print()

# égalemnt numerify() ou botify()
