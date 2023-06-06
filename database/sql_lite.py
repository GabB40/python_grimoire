import sqlite3

conn = sqlite3.connect("./database/database.db")
c = conn.cursor()
c.execute(
    """
        CREATE TABLE IF NOT EXISTS employes
        (
            prenom text,
            nom text,
            salaire int
        )
    """
)

# employe = {"prenom": "Paul", "nom": "Dupond", "salaire": 10000}
# c.execute("INSERT INTO employes VALUES (:prenom, :nom, :salaire)", employe)

search: dict[str, str] = {"prenom": "Paul"}
c.execute("SELECT * FROM employes WHERE prenom=:prenom", search)
results: list[tuple] = c.fetchall()
print(f"results = {results}")

employe = {"prenom": "Paul", "nom": "Dupond", "salaire": 12000}
c.execute("""
    UPDATE employes SET salaire=:salaire WHERE prenom=:prenom AND nom=:nom
""", employe)


conn.commit()
conn.close()
