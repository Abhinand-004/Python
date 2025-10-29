from abc import ABC, abstractmethod
class user(ABC):
    def __init__(self, username, year):
        self.username = username
        self.year = year
    def account_age(self, current_year):
        current_year=2025
        return current_year - self.year
    @abstractmethod
    def get_role(self):
        pass
class Admin(user):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"Admin User: {self.username}, Year: {self.year}"
class Guest(user):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"Guest User: {self.username}, Year: {self.year}"

Admin1 = Admin("Alice", 2020)
Guest1 = Guest("Bob", 2022)
print("Role:", Admin1.get_role())
print("Account Age:", Admin1.account_age(2025), "Years")
print(Admin1)
print("Role:", Guest1.get_role())
print("Account Age:", Guest1.account_age(2025), "Years")
print(Guest1)