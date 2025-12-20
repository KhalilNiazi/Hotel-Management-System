space = " "
MAX_CAP = 300
roomCount = 0
hotelData = [[-1,"HD",-11] for _ in range(MAX_CAP)]

def header(name):
    print("=" * 55)
    print(f"{name:^55}")
    print("=" * 55)

def element(dash):
    print(dash * 55)

def administratorlogin():
    header("Hostel Management System")
    print(f"{'[ AUTHENTICATION REQUIRED ]':^55}")
    print("\n")
    element("-")
    attempts = 3 
    while(True):
        print("Enter X to go back\n")
        username = input("Enter UserName: ")
        if username.lower() == 'x':
            print("Returning to previous menu...")
            main()
            return
        
        password = input("Enter Password: ")
        
        if password.lower() == 'x':
            print("Returning to previous menu...")
            main()
            return

        if username == "admin" and password == "1122":
            element("-")
            print("\nLogin Successful!\n")
            administratordashboard()
            return   
        else:
            attempts = attempts-1
            if attempts == 0:
                print("No More Attempts Left")
                break
            else:
                print(f"Invalid Credentials! Try Again")
                print(f"Remaining Attempts: {attempts}\n")


def administratordashboard():
    header("ADMINISTRATOR DASHBOARD")
    element("-")
    print(f"{'Option':<8} {'Function':<20}{'Option':<9} {'Function':<20}")
    
    element("-")
    print(f"{'[1]':<8} {'Add Rooms':<20} {'[2]':<8} {'View All Rooms':<20}")
    print(f"{'[3]':<8} {'Manage Staff':<20} {'[4]':<8} {'Worker Duties':<20}")
    print(f"{'[5]':<8} {'View Booking':<20} {'[6]':<8} {'Financials':<20}")
    print(f"{'[7]':<8} {'Attendance':<20} {'[8]':<8} {'System Stats':<20}")
    print(f"{'[0]':<8} {'Logout':<20}")


    element("-")
    option = int(input("Enter the Option (0-to-8): "))
    if option == 1:
        addroom()
    elif option == 2:
        viewAllRooms()
    elif option == 3:
        print("Manage Staff")
    elif option == 4:
        print("Worder Duties")
    elif option == 5:
        print("View Booking")
    elif option == 6:
        print("Financials")
    elif option == 7:
        print("Attendance")
    elif option == 8:
        print("System Stats")
    elif option == 0:
        return
    else:
        print("Invalid Option")

def addroom():
    global roomCount
    header("Hostel Management System")
    print(f"{'[ADD NEW ROOM]':^55}\n")
    print('"Enter the details below to register a new room in the system."')    
    element("-")
    print("AVAILABLE ROOM TYPES:")
    print("Single[S]  (1 Bed,  Max 1 Person)")
    print("Double[D]  (1 Bed,  Max 2 Persons)")
    print("Twin[T]    (2 Beds, Max 2 Persons)")
    print("Suite[ST]  (Luxury, Max 4 Persons)")
    element("-")
    New_RoomNO = input(f"Room No[1-to-{MAX_CAP}]: ")
    New_RoomType = input("Enter Room Type(S/D/T/ST): ")
    New_RoomPrice = int(input("Enter Price Per Night (PKR): "))
    element("-")
    print("[System Check...]")
    
    for i in range(roomCount):
        if hotelData[i][0] == New_RoomNO:
            print(f"[ERROR] Room {New_RoomNO} Already Exists!")
            return
    Room_Type = "Standard"
    if New_RoomType.upper() == 'S' or New_RoomType.lower() == "s":
        Room_Type = "Single"
    elif  New_RoomType.upper() == 'D' or New_RoomType.lower() == "d":
        Room_Type = "Double"
    elif  New_RoomType.upper() == 'T' or New_RoomType.lower() == "t":
        Room_Type = "Triple"
    elif New_RoomType.upper() == 'ST' or New_RoomType.lower() == "st":
        Room_Type = "Suite"

    hotelData[roomCount][0] = New_RoomNO
    hotelData[roomCount][1] = New_RoomType
    hotelData[roomCount][2] = New_RoomPrice
    print(f"[SUCCESS] Room {New_RoomNO} ({Room_Type}) created successfully!\n")
    roomCount += 1

    print("[1] Add Another")
    print("[0] Go Back")
    element("-")
    option = int(input("Select Option: "))
    if option == 1:
        addroom()
    else:
        administratordashboard()



def main():
    while(True):
        header("Hostel Management System")
        print("\nWelcome! Please select your role to access the system\n")
        print("-" * 55)
        print(f"[1] ADMINISTRATOR{space:>10} [2] RECEPTIONIST")
        print(f"[3] MANAGER{space:>16} [4] WORKER / STAFF")
        print(f"[5] Exit")
        print("-"*55)
        option = int(input("Enter the Option (1-to-5): "))
        if option == 1:
            administratorlogin()
        elif option == 2:
            receptionist()
        elif option == 3:
            manager()
        elif option == 4:
            worker()
        elif option == 5:
            print("[System Shutting Down... Goodbye!]")
            return
        else:
            print("Invalid Option")

print(main())