class NamewithAdress:
    def __init__(self , name , adress , phone_number):
        self.name = name
        self.adress = adress
        self.phone_number = phone_number

    def introduce_self(self):
        print("Numele meu este " +  self.name , "cu adresa in " + self.adress , " si avand nr.tel " + self.phone_number)  

class Person(NamewithAdress):
    def __init__(self , name , adress , phone_number):
        NamewithAdress.__init__(self , name , adress , phone_number)


class Seller(Person):
    def __init__(self, name , adress , phone_number):
        Person.__init__(self, name ,adress , phone_number)
      
ionica=Seller ("Ion  Ionescu " , "oradea" , "12345" ,)
ionica.introduce_self()


class Manager(Person):
    def __init__(self , name , adress , phone_number):
        Person.__init__(self ,name , adress , phone_number)

Popescu = Manager ("Popescu Vasile" , "Cluj " , "0359415")   
Popescu.introduce_self()


class Customer(Person):
    def __init__(self , name , adress , phone_number):
        Person.__init__(self , name , adress , phone_number)

client = Customer (" Palag Bogdan" , " Oradea " , " 93824")
client.introduce_self()


class Mall:
    def __init__(self , open , closing ):
        
        self.open = open 
        self.closing = closing

    def introduce_self(self):
        print("Program Mall Deschis de la " , self.open , " pana la " , self.closing)

Mal = Mall ("08:00" , " 22:00")
Mal.introduce_self()


class Department:
    def __init__(self , namedp):
        self.namedp = namedp

    def introduce_self(self):
        print("Departamentul de " , self.namedp)

Dep = Department ( "Electrocasnice")
Dep.introduce_self()


class Store(NamewithAdress):
    def __init__(self , name , adress , phone_number , variety ):
        NamewithAdress.__init__(self , name , adress , phone_number)

        self.variety = variety 

    def show_variety(self):
        print("Avand o varietate " , self.variety)    

Media = Store ( "Media " , "Nufaru " , " 0800800" , "vasta")

Media.introduce_self()
Media.show_variety()

class Product:
    def __init__ (self , type , price):
        self.type = type
        self.price = price 

    def introduce_self(self):
        print("Produsele sunt de mai multe tipuri , " , self.type , "pretul fiind afisat pe fiecare in parte de la " , self.price)

produs = Product("electrocasnice , menaj , IT , etc " , "300 RON") 
produs.introduce_self()                   


class Magazine:
    def __init__(self , type):
        self.type = type 

    def introduce_self(self):
        print("Revista magazin , " , self.type) 

Revista = Magazine("Aici se pot vedea articole ce nu sunt puse pe raft in magazin")
Revista.introduce_self()


class Storesite:
    def __init__(self , url , products , account):
        self.url = url 
        self.products = products
        self.account = account

    def introduce_self(self):
        print("Acceseaza  " , self.url , "pentru a vedea daca avem  " ,self.products , " pentru a comanda accesati account si signup" , self.account)     

site = Storesite(" www.mediagalaxy.ro" , "produsele dorite in stock " , "account" )
site.introduce_self() 


    

         
