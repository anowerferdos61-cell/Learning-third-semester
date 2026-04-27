from menu import Menu
class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu = Menu()
    
    def add_employee (self,employe):
        self.employees.append(employe)
    
    def view_employe(self):
        print("--Employe ditels--")
        for emp in self.employees:
            print(emp.name,emp.age, emp.email, emp.address)