class Resume:
    def __init__(self, name, surname, age, tel, linkedin, github):
        self.name = name
        self.surname = surname
        self.age = age
        self.tel = tel
        self.linkedin = linkedin
        self.github = github

    def fav_prog_lang(self):
        print("Python")

    def last_work(self):
        print("VitSpetsConsult LLC")

    def study(self):
        print("Belarussian State Economic University")

    def family_status(self):
        print("married")

    def language(self):
        print("English - intermediate")

    def hobby(self):
        print("books, bysicle")


i_am = Resume("Viktar", "Makeichyk", "42", "80297098422", "www.linkedin.com/in/viktar-makeichyk-3aa477180", "https://github.com/ViktarMak")


print("Имя: " + i_am.name)
print("Фамилия: " + i_am.surname)
print("Возраст: " + i_am.age)
print("Телефон: " + i_am.tel)
print("Профиль в Linkedin: " + i_am.linkedin)
print("Github: " + i_am.github)


