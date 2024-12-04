class Animal:
    def __init__(self, type, age, name):
        self.type = type
        self.name = name
        self.age = age
an1 = Animal ('dog', 10, 'Burek')
an2 = Animal ('cat', '22', 'Honda')

print(an1.type)
print(an1.age)
print(an1.name)
print(an2.name, an2.age, an2.type)