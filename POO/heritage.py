class User:
    def __init__(self, firstname, lastname) -> None:
        self.firstname: str = firstname
        self.lastname: str = lastname

    def get_authorizations(self) -> list[str]:
        return ["n1", "n2"]

    # exemple heritage
    def user_created(self):
        print("un utilisateur a été créé")


class Admin(User):
    def __init__(self, firstname, lastname) -> None:
        super().__init__(firstname, lastname)

    def get_authorizations(self) -> list[str]:
        return super().get_authorizations() + ["n3", "n4", "n5"]

    # exemple heritage
    def user_created(self):
        super().user_created()
        print("Son rôle est 'ADMIN'")


class Owner(User):
    def __init__(self, firstname, lastname) -> None:
        super().__init__(firstname, lastname)

    def get_authorizations(self) -> list[str]:
        return super().get_authorizations() + ["n3", "n4", "n6"]

    # exemple heritage
    def user_created(self):
        super().user_created()
        print("Son rôle est 'OWNER'")


print("-" * 50)
user1 = User("Paul", "Dupond")
user1.user_created()
print(user1.get_authorizations())
print("-" * 50)

admin1 = Admin("Jean", "Durand")
admin1.user_created()
print(admin1.get_authorizations())

print("-" * 50)
owner1 = Owner("Patrick", "Grand")
owner1.user_created()
print(owner1.get_authorizations())
