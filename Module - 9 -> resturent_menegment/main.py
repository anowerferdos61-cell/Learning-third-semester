from users import user,Admin,Employee,Customer
from fooditem import FoodItem
from menu import Menu
from restaurent import Restaurent

mama = Restaurent('MAMA Hotel')
print(mama.name)

def customer_menu():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    Phone = input('Enter Your Phone : ')
    address = input('Enter Your Adress : ')

    customer = Customer(name=name,email=email,phone=Phone,address=address)

    while True:
        print(f"\nWellCome {customer.name}")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter Your Choice : ")
        
        if choice == '1':
            customer.view_menu(mama)
        
        elif choice == '2':
            item_name = input("Enter Item Name : ")
            quantity = int(input("Enter Quantity : "))
            customer.add_to_cart(mama, item_name, quantity)
        
        elif choice == '3':
            customer.view_cart()
        
        elif choice == '4':
            print(f"Total Price : {customer.cart.total_price()}")
            print("Thank you for ordering!")
            customer.pay_bill()
            customer.cart.clear()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice")

def admin_menu():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    Phone = input('Enter Your Phone : ')
    address = input('Enter Your Adress : ')
    
    admin = Admin(name=name, email=email, phone=Phone, address=address)
    
    while True:
        print(f"\nWellCome {admin.name}")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Menu")
        print("4. Add Employee")
        print("5. View Employees")
        print("6. Exit")
        choice = input("Enter Your Choice : ")
        
        if choice == '1':
            item_name = input("Enter Item Name : ")
            price = float(input("Enter Price : "))
            quantity = int(input("Enter Quantity : "))
            item = FoodItem(item_name, price, quantity)
            admin.add_new_item(mama, item)
            print("Item added successfully!")
        
        elif choice == '2':
            item_name = input("Enter Item Name : ")
            admin.delet_item(mama, item_name)
        
        elif choice == '3':
            admin.show_menu(mama)
        
        elif choice == '4':
            emp_name = input("Enter Employee Name : ")
            phone = input("Enter Phone : ")
            email = input("Enter Email : ")
            address = input("Enter Address : ")
            age = int(input("Enter Age : "))
            salary = float(input("Enter Salary : "))
            designetion = input("Enter Designation : ")
            employee = Employee(emp_name, phone, email, address, age, salary, designetion)
            admin.add_employee(mama, employee)
            print("Employee added successfully!")
        
        elif choice == '5':
            admin.view_employe(mama)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice")

while True:
        print("\n===== MAMA Hotel =====")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        choice = input("Enter Your Choice : ")
        
        if choice == '1':
            customer_menu()
        
        elif choice == '2':
            admin_menu()
        
        elif choice == '3':
            print("Thank you for visiting!")
            break
        
        else:
            print("Invalid choice")    