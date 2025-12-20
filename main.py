space = " "
#Adding Room 2D Array
MAX_CAP = 300
roomCount = 0
#here -1 = RoomNO, HD = Type, -11 = Price
hotelData = [[-1,"HD",-11] for _ in range(MAX_CAP)]


#Adding UserData 2D Array
MAX_USER = 50
userSount = 1
#Here U = Username, P = Password, R= Role
userData= [["U","P","R"] for _ in range(MAX_USER)]
userData[0][0] = "admin"
userData[0][1] = "1122"
userData[0][2] = "Admin"

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

        if username == userData[0][0] and password == userData[0][1]:
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

def header(name):
    print("=" * 55)
    print(f"{name:^55}")
    print("=" * 55)

def element(dash):
    print(dash * 55)
#Admin Login Funciton
def roomtypes():
    print("AVAILABLE ROOM TYPES:")
    print("Single[S]  (1 Bed,  Max 1 Person)")
    print("Double[D]  (1 Bed,  Max 2 Persons)")
    print("Twin[T]    (2 Beds, Max 2 Persons)")
    print("Suite[ST]  (Luxury, Max 4 Persons)")
#Admin Dashboard
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

#Adding Rooms Function
def addroom():
    global roomCount
    header("Hostel Management System")
    print(f"{'[ADD NEW ROOM]':^55}\n")
    print('"Enter the details below to register a new room in the system."')    
    element("-")
    roomtypes()
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
    hotelData[roomCount][1] = Room_Type
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
#list of All room
def viewAllRooms():
    global roomCount
    header("Hostel Management System")
    print(f"{'[ROOM INVENTORY LIST]':^55}\n")
    element("-")
    print(f"{space:<4} {'ROOM NO':<10} {'TYPE':<20} PRICE (PKR)")
    element("-")
    for i in range(roomCount):
        print(f"{space:<4} {hotelData[i][0]:<10} {hotelData[i][1]:<20} {hotelData[i][2]}")
    element("-")

    print("")
    print(f"[Total Rooms: {roomCount}]")
    print("")
    element("=")


    while(True):
        print("[1] Press [M] to Manage Rooms")
        print("[2] Press [X] to Go Back")    
        option= input("Enter Option: ")
        if option.upper() == 'M' or option.upper() == 'm':
            manageRooms()
            return
        elif option.upper() == 'X' or option.upper() == 'x':
            administratordashboard()
            return
        else:
            print("InValid Option! Try Again")
     
def manageRooms():
    global roomCount
    header("Manage Rooms")
    element("-")
    print(f"{space:<4} {'ROOM NO':<10} {'TYPE':<20} PRICE (PKR)")
    element("-")
    for i in range(roomCount):
        print(f"{space:<4} {hotelData[i][0]:<10} {hotelData[i][1]:<20} {hotelData[i][2]}")
    element("-")
    
    Search_Room_No = input("Enter Room No: ")
    
    found_index = -1
    for i in roomCount:
        if hotelData[i][0] == Search_Room_No:
            found_index = i
            break
    if found_index == -1:
        print(f"\n[ERROR] Room {Search_Room_No} not found in List.")
        return
    print("\n[ROOM FOUND!]")
    print(f"Current Data: TYPE >>{hotelData[found_index][1]:<20} << |  PRICE >>{found_index[i][2]}<<")
    element("-")
    print("[1] Edit Data")
    print("[2] Delete")
    print("[0] Cancel")
    option = int(input("Enter Option: "))
    if option == 1:
        print("\n--- UPDATE DETAILS ---")
        roomtypes()
        New_RoomType = input("Enter New Type (S\D\T\ST) or Press Enter To Skip")
        if (New_RoomType != ""):
            if New_RoomType.upper() == 'S' or New_RoomType.lower() == "s":
                hotelData[found_index][1] = "Single"
            elif  New_RoomType.upper() == 'D' or New_RoomType.lower() == "d":
                hotelData[found_index][1] = "Double"
            elif  New_RoomType.upper() == 'T' or New_RoomType.lower() == "t":
                hotelData[found_index][1] = "Triple"
            elif New_RoomType.upper() == 'ST' or New_RoomType.lower() == "st":
                hotelData[found_index][1] = "Suite"
        New_Room_Price = int(input("Enter New Price Or Press Enter To Skip"))


    
def ManageStaff():
    header("STAFF MANAGEMENT PORTAL")
    
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