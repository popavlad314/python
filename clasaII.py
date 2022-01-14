class person:
    def __init__(self,gen ,name ,age , haircolor):
        self.gen = gen
        self.name = name
        self.age = age
        self.haircolor = haircolor
    
    def introduce_self(self):
        print("Numele meu este " + self.name , "genul " + self.gen ,"cu varsta de " + self.age , "ani" ,"si culoarea parului " + self.haircolor)

class student:
    def __init__(self,gen,name,age,haircolor):
        self.gen = gen
        self.name = name
        self.age = age
        self.haircolor = haircolor

    def introduce_self(self):
        print("Numele meu este " + self.name , "genul " + self.gen ,"cu varsta de " + self.age , "ani" ,"si culoarea parului " + self.haircolor)    

student = person("masculin", "Ion", "15", "rosu")

student.introduce_self()

class profesor:
    def __init__(self,gen,name,age,haircolor):
        self.gen = gen
        self.name = name
        self.age = age
        self.haircolor = haircolor

    def introduce_self(self):
            print("Numele meu este " + self.name , "genul " + self.gen ,"cu varsta de " + self.age , "ani" ,"si culoarea parului " + self.haircolor)

profesor = person ("feminin", "Maria", "45", "verde")

profesor.introduce_self()

class course:
    def __init__(self,nume,numar,timp):
        self.nume = nume
        self.numar = numar
        self.timp = timp

    def introduce_self(self):
        print("numele cursului este " + self.nume , "cu numarul " + self.numar , "si cu timpul de " +self.timp)

curs= course("Python", "1 ", "15h")  

curs.introduce_self()






    
    
    
