class Human():
    def __init__(self,name,father_name,cnic): 
        self.name = name
        self.father_name = father_name
        self.cnic = cnic
    def printer(self,type):
        print("This is a ",type)
    def showdetails(self):
        print("Name: ",self.name,"\nFather Name: ",self.father_name,"\nCnic no.: ",self.cnic)

class Student(Human): #Human parent ko idhar pass kradia as a parameter 
    # def __init__(self,name):
    #   self.name = name  #constructor overloading nhi horhi
    def __init__(self,name,father_name,cnic,rollno):
        super().__init__(name,father_name,cnic)
        self.rollno = rollno
    def showdetails(self):
        ##function overriding
        print("Name: ",self.name,"\nFather Name: ",self.father_name,"\nCnic no.: ",self.cnic,"\nRoll no.: ",self.rollno)
    # def eat(self):
    #     print(self.name, 'is eating Biryani')

class Teacher(Human):
    def __init__(self,name,father_name,cnic,Id):
        super().__init__(name,father_name,cnic)
        self.Id = Id
    def showdetails(self):
        print("Name: ",self.name,"\nFather Name: ",self.father_name,"\nCnic no.: ",self.cnic,"\nID: ",self.Id)


class Admin(Human):
    def __init__(self,name,father_name,cnic,designation):
        super().__init__(name,father_name,cnic)
        self.designation = designation
    def showdetails(self):
        print("Name: ",self.name,"\nFather Name: ",self.father_name,"\nCnic no.: ",self.cnic,"\nDesignation: ",self.designation)
    # def eat(self):
    #     print(self.name, 'is eating Biryani')


# st1 = Student(father_name="Tahir",name= "Midha",program="AI")
# st = Student("Midha","Tahir","BE")
# st.eat()
# st1.eat()
stud = Student("Mids","Khan","42101-233",87)
stud.showdetails()
stud.printer("student")
print("###")
teach = Teacher("Hashy","Khan","42101-2347","s2")
teach.showdetails()
print("###")
ad = Admin("Mids","Tahir","42101-233","BE")
ad.showdetails()


