class User():
    def __init__(self, name, age):  # Метод __init__ автоматически выполняется при создании каждого экземпляра класса
        self.name = name            # (выполяется сразу при обращении к данному классу
        self.age = age
        print("Создан новый юзер")

    def login(self):    # Метод - юзер залогинился
        print(self.name.title() + " - User logged in")

    def logout(self):   # Метод - юзер вылогинился
        print(self.name.title() + " - User log out")

New_user_0 = User('Jonny', 32)    # Создан объект (экземпляр класса) юзер Jonny, 32 года

print(New_user_0.name)
print(New_user_0.age)

New_user_1 = User('Mick', 40)

New_user_0.logout()
New_user_1.login()
