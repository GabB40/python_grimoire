import dateparser
from datetime import datetime

print(dateparser.parse("aujourd'hui"))
print(dateparser.parse("Il y a un an six mois et deux jours"))
print(dateparser.parse("dans trois heures et dix minutes"))
print(dateparser.parse("three days and two hours ago", settings={'RELATIVE_BASE': datetime(2023, 12, 4)}))