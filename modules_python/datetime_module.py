from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

print(date(year=2023, month=4, day=30))
print(time(hour=10, minute=40, second=50))
print(datetime(year=2023, month=4, day=30, hour=10, minute=40, second=50))
print(datetime(2023, 4, 30))
print()
print(datetime.now())
print(date.today())
print()
print(date.fromisoformat("2023-04-30"))

# cheatsheet : https://strftime.org/
print(datetime.strptime("30 Apr 2023", "%d %b %Y"))
print(datetime.now().strftime("%d %b %Y"))
print(datetime.strptime("2023-05-16T09:24:24", "%Y-%m-%dT%H:%M:%S"))
""" 
## package extraordinaire : dateparser --> voir fichier dédié !

## les TIMEZONES (cf: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) 
# NB: les dates sans tz sont dîtes 'naive', celles avec une tz 'aware'
print("\nTIMEZONE")
now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))
now_in_montreal = datetime.now(tz=ZoneInfo("America/Montreal"))
print(f"now_in_vancouver = {now_in_vancouver}")
print(f"now_in_montreal = {now_in_montreal}")
now_in_paris = now_in_vancouver.astimezone(ZoneInfo("Europe/Paris"))
print(f"now_in_paris = {now_in_paris}")
print(f"now_in_montreal.tzinfo = {now_in_montreal.tzinfo}") # aware
print(f"datetime.now().tzinfo = {datetime.now().tzinfo}") # naive

## voir tous les problèmes et solutions sur les timezones dans section 54 vidéo 319 du cours udemy

## TIMEDELTA : soustraire ou ajout aux dates
print("\nTIMEDELTA")
now_in_15_days_minus_5hours = datetime.now() + timedelta(days=15, hours=-5)
print(f"now_in_15_days_minus_5hours = {now_in_15_days_minus_5hours}")
## voir égalemnet la librairie dateutil

 """