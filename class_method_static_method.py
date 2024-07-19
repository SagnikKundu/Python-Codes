from datetime import date 

class Person() :
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
    @classmethod
    def calc_age(cls, name, dob) :
        return cls(name,  (date.today().year - int(dob.split('-')[-1])) ) 
    
    @staticmethod
    def age_check(age): 
        if age < 18 : return 'Minor.'
        else : return 'Not a Minor.'
        
person1 = Person('Amit', 21)
person2 = Person('Amit', '19-06-2001')

print(person1.age)
print(person2.age)

print(Person.age_check(16))