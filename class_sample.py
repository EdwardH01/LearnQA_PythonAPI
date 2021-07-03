class User():
    def __init__(self, name, age):  # Метод __init__ автоматически выполняется при создании каждого экземпляра класса
        self.name = name            # (выполяется сразу при обращении к данному классу
        self.age = age
        print("Создан новый юзер" + ' ' + name + ' ' + str(age))

    def login(self):    # Метод - юзер залогинился
        print(self.name.title() + " logged in")

    def logout(self):   # Метод - юзер вылогинился
        print(self.name.title() + " log out")

New_user_0 = User('Jonny', 32)    # Создан объект (экземпляр класса) юзер Jonny, 32 года

print(New_user_0.name)
print(New_user_0.age)

New_user_1 = User('Mick', 40)    # Создан объект (экземпляр класса) юзер Mick, 40 лет

New_user_0.logout()
New_user_1.login()
Tom = User('Tom', 27)    # Создан объект (экземпляр класса) юзер Tom, 27 лет

New_user_1.logout()
Tom.login()

