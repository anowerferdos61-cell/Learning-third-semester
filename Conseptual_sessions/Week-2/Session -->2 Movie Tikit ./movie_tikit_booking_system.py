class Hall:
    def __init__(self,hall_no,row,collam):
        self.hall_no = hall_no
        self.row = row
        self.collam = collam
        self.seat = {}
        self.movie_list = []
    
    def add_show(self,show_code,movie_name,show_time):
        self.tuple = (show_code,movie_name,show_time)
        self.movie_list.append(self.tuple)
        self.seat_list= []
        for i in range(self.row):
            row = []
            for j in range(self.collam):
                row.append("free")
            self.seat_list.append(row)
        self.seat[show_code] = self.seat_list

    def view_show_list(self):
        for value in self.movie_list:
            print(f"Code : {value[0]}\tMovie : {value[1]}\tTime : {value[2]}\n")

    def show_avilable_seats(self,show_code):
        if show_code in self.seat:
            for i in self.movie_list:
                if i[0] == show_code:
                    print(f"Movie : {i[1]}-\t-Time : {i[2]}\n")
            for x in range(self.row):
                for y in range(self.collam):
                    if(self.seat[show_code][x][y] == 'free'):
                        print(f'{chr(x+65)}{y+1}',end='\t')
                    else:
                        print("X",end='\t')
                print("\n")
        else:
            print("Wrong Show code.\n")
    
    def book_tickets(self,id,name,phone,booking_seats):
        flag = 0
        self.booked_tickets = []

        if id not in self.seat:
            print("Wrong id. try again.\n")
        else:
            for x in booking_seats:
                r = ord(x[0])-65
                c = ord(x[1])-49
                if r>=self.row or c>=self.collam or c<0 or r<0:
                    print("Seat dose\'nt exist\n")
                elif self.seat[id][r][c] != "free":
                    print(x,"is already booked.\n")
                else:
                    self.seat[id][r][c] = "X"
                    self.booked_tickets.append(x)
                    flag = 1

            if flag == 1:
                print('*----------------------------------------*')
                print("Ticket Booked Sucessfully.")
                print('*----------------------------------------*')
                print(f"Name : {name}\tPhone : {phone}\tHall_no : {hall.hall_no}")
                print('*----------------------------------------*')
                for i in self.movie_list:
                    if i[0] == id:
                        print(f"Movie : {i[1]}\tTime : {i[2]}")
                print("Your tickets : ",end=" ")
                for i in self.booked_tickets:
                    print(i,end="\t")
                print(f"\nPrice : {500*len(self.booked_tickets)} TK")
            




hall = Hall(2,6,6)
hall.add_show(150,'Avengers\t','10:00 AM')
hall.add_show(250,'Avengers infinity war','01:00 PM')
hall.add_show(350,'Avengers End game','04:00 PM')
hall.add_show(450,'Avengers Civil War','09:00 PM')


while True:
    print('*----------------------------------------*')
    print("1.View all show.")
    print("2.View avilable tikits.")
    print("3.Book tikit")
    print("4. Exit")
    print('*----------------------------------------*')

    option = int(input("Enter Your choice : "))

    if option == 1:
        print('*----------------------------------------*')
        hall.view_show_list()
    elif option ==2:
        id = int(input("Enter show id: "))
        hall.show_avilable_seats(id)
    elif option ==3:
        print('*----------------------------------------*')
        hall.view_show_list()
        print('*--------------------------------------*')
        id = int(input("Enter Movie Code : "))
        hall.show_avilable_seats(id)
        name = input("Enter Your Name : ")
        phone = input("Enter your Phone No : ")
        tickets = int(input("Enter number of tickets: "))
        booking_seats = []
        for i in range(tickets):
            booking_seats.append(input("Enter your seat no. "))
        hall.book_tickets(id,name,phone,booking_seats)

    elif option ==4:
        print("Thanks for Watching.")
        break
    else:
        print("\nInvalid option - try again.\n")
    