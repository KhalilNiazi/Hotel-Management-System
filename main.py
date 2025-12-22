space = " "
#Adding Room 2D Array
MAX_CAP = 300
roomCount = 0
#here -1 = RoomNO, HD = Type, -11 = Price
hotelData = [[-1,"HD",-11] for _ in range(MAX_CAP)]


#Adding UserData 2D Array
MAX_USER = 50
userCount = 1
#Here U = Username, P = Password, R= Role
userData= [[-1,"U","P","R"] for _ in range(MAX_USER)]

userData[0][0] = -1
userData[0][1] = "admin"
userData[0][2] = "1122"
userData[0][3] = "Admin"

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

        for i in range(userCount):
            if username == userData[i][1] and password == userData[i][2]:
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
        ManageStaff()
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
    while True:
        try:
            New_RoomNO = int(input(f"Room No[1-to-{MAX_CAP}]: "))
            
            if is_valid_room_number(New_RoomNO):
                exists = False
                for i in range(roomCount):
                    if hotelData[i][0] == New_RoomNO:
                        print(f"[ERROR] Room {New_RoomNO} Already Exists!")
                        exists = True
                        break
                if not exists:
                    break
        except ValueError:
            print("[ERROR] Invalid Input. Please enter a number.")
    Room_Type = ""
    while True:
        New_RoomType = input("Enter Room Type (S/D/T/ST): ").upper()
        New_RoomType= New_RoomType.upper()
        result = get_room_type_name(New_RoomType)
        if result != None:
            Room_Type = result
            break  
       
    New_RoomPrice = int(input("Enter Price Per Night (PKR): "))
   
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

def is_valid_room_number(room):
    if room > int(MAX_CAP):
        print(f"[ERROR] Room No Must Be Less Than {MAX_CAP}")
        return False
    elif room < 1:
        print(f"[ERROR] Room No cannot be zero or negative.")
        return False
    else:
        return True
def get_room_type_name(type):
    if type == 'S':
        return "Single"
    elif  type == 'D':
       return "Double"
    elif  type == 'T':
        return "Triple"
    elif type== 'ST':
        return "Suite"
    else:
       print("[ERROR] Invalid Room Type. Please use S, D, T, or ST.")
       return None
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
        option= input("Enter Option: ").upper()
        if option.upper() == 'M':
            manageRooms()
            break
            
        elif option.upper() == 'X':
            administratordashboard()
            break
            
        else:
            print("Invalid Option! Try Again")
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
    for i in range(roomCount):
        if hotelData[i][0] == Search_Room_No:
            found_index = i
            break
    if found_index == -1:
        print(f"\n[ERROR] Room {Search_Room_No} not found in List.")
        return
    print("\n[ROOM FOUND!]")
    print(f"Current Data: TYPE={hotelData[found_index][1]:<4}| PRICE={hotelData[found_index][2]}")
    element("-")
    print("[1] Edit Data")
    print("[2] Delete")
    print("[0] Cancel")
    option = int(input("Enter Option: "))
    if option == 1:
        print("\n--- UPDATE DETAILS ---")
        roomtypes()
        New_RoomType = input("Enter New Type (S/D/T/ST) or Press Enter To Skip")
        if (New_RoomType != ""):
            if New_RoomType.upper() == 'S':
                hotelData[found_index][1] = "Single"
            elif  New_RoomType.upper() == 'D':
                hotelData[found_index][1] = "Double"
            elif  New_RoomType.upper() == 'T' :
                hotelData[found_index][1] = "Triple"
            elif New_RoomType.upper() == 'ST':
                hotelData[found_index][1] = "Suite"
        New_Room_Price = int(input("Enter New Price Or Press Enter To Skip"))
        if (New_Room_Price != 0):
            hotelData[found_index][2] = New_Room_Price

        
        print("\n[SUCCESS] Room details updated successfully!")
        print(f"{space:<4} {hotelData[found_index][0]:<10} {hotelData[found_index][1]:<20} {hotelData[i][2]}")
    

    elif option == 2:
        confirm = input(f"Are you sure you want to DELETE Room {Search_Room_No}? [Y/N]").upper()
        if confirm.upper() == "Y":
            for j in range(found_index,roomCount-1):

                hotelData[j][0] = -1
                hotelData[j][1] = "HD"
                hotelData[j][2] = -11
            roomCount = roomCount-1
            
            print("\n[SUCCESS] Room deleted successfully.")
            viewAllRooms()
        else:
            print("\n[CANCELLED] Deletion cancelled.")
            viewAllRooms()
    else:
        print("\n[INFO] Returned to menu.")
        viewAllRooms()

    
def ManageStaff():
    global userCount
    header("STAFF MANAGEMENT PORTAL")
    print(f"[Total Users={userCount}]")
    element("-")
    print("[1] Add New Staff Member")
    print("[2] View All Users")
    print("[0] Go Back")
    option = int(input("Enter Option: "))
    if option == 1:
        addNewStaff()
    elif option == 2:
        viewallUser()
    else:
        administratordashboard()


def addNewStaff():
    global userCount
    header("REGISTER NEW USER")
    element("-")
    
    while True:
        username = input("[1] Enter New Username:")
        if userData[userCount][1] == username:
                print(f"[ERROR] UserName {username} Already Exists!")
                break   
        else:
            password = input("[2] Enter Password:")
            userrole = input("[3] Ty Rpeole:(Admin [A]/Receptionist [R] | Manager [M] | Worker[W])")
            userData[userCount][0] = userCount
            userData[userCount][1] = username
            userData[userCount][2] = password
            userData[userCount][3] = userrole
            print(f"[SUCCESS] User= {username} Role= ({username}) created successfully!\n")
            userCount += 1

            print("[1] Add Another")
            print("[0] Go Back")
            element("-")
            option = int(input("Select Option: "))
            if option == 1:
                addNewStaff()
                break
            else:
                ManageStaff()
                break
                
    
def viewallUser():
    header("Hostel Management System")
    print(f"{'[View All Staff]':^55}\n")
    element("-")
    print(f"{space:<4} {'Sr.':<10} {'Username':<10} {'Password':<10} {'Role':<10}")
    element("-")
    for i in range(userCount):
        print(f"{space:<4} {userData[i][0]:<10} {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")
    element("-")

    print("")
    print(f"[Total Users: {userCount}]")
    print("")
    element("=")


    while(True):
        print("[1] Press [M] to Manage Staff")
        print("[2] Press [X] to Go Back")    
        option= input("Enter Option: ").upper()
        if option.upper() == 'M':
            managestaff()
            break
            
        elif option.upper() == 'X':
            administratordashboard()
            break
            
        else:
            print("Invalid Option! Try Again")

def managestaff():
    global roomCount
    header("Manage Staff")
    element("-")
    print(f"{space:<4} {'Sr.':<10} {'Username':<10} {'Password':<10} {'Role':<10}")
    element("-")
    for i in range(userCount):
        print(f"{space:<4} {userData[i][0]:<10} {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")
    element("-")

    
    Search_User_name = input("Enter User Name: ")
    
    for i in range(userCount):
        if hotelData[i][1] == Search_User_name:
            print("\n[User FOUND!]\n")
            print(f"Current User: Name= {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")
            element("-")

            element("-")
            print("[1] Edit Data")
            print("[2] Delete")
            print("[0] Cancel")
            option = int(input("Enter Option: "))
            if option == 1:
                print("\n--- UPDATE DETAILS ---")
                New_username = input("Enter New Name) or Press Enter To Skip")
                userData[i][1] = New_username
                New_Role = int(input("Enter New Role Or Press Enter To Skip"))
                userData[i][3] = New_Role
                New_Password = int(input("Enter New Password Or Press Enter To Skip"))
                userData[i][3] = New_Password

                
                print("\n[SUCCESS] Room details updated successfully!")
                print(f"{space:<4} {userData[i][0]:<10} {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")
   

            elif option == 2:
                confirm = input(f"Are you sure you want to DELETE User {Search_User_name}? [Y/N]").upper()
                if confirm.upper() == "Y":
                    for j in range(New_username,roomCount-1):

                        hotelData[j][0] = -1
                        hotelData[j][1] = "HD"
                        hotelData[j][2] = -11
                    roomCount = roomCount-1
                    
                    print("\n[SUCCESS] Room deleted successfully.")
                    viewAllRooms()
                else:
                    print("\n[CANCELLED] Deletion cancelled.")
                    viewAllRooms()
            else:
                print("\n[INFO] Returned to menu.")
                viewAllRooms()

        else:
            print(f"\n[ERROR] Room {Search_User_name} not found in List.")
            return
   

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