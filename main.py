space = " "
#Adding Room 2D Array
MAX_CAP = 300
roomCount = 0
#here -1 = RoomNO, HD = Type, -11 = Price
hotelData = [[-1,"HD",-11] for _ in range(MAX_CAP)]


#Adding UserData 2D Array
MAX_USER = 50
userCount = 1
#Here U = Username, P = Username, R= Role
#Format: [usercount, Username, Username, Role]
userData= [[-1,"U","P","R"] for _ in range(MAX_USER)]

userData[0][0] = -1
userData[0][1] = "admin"
userData[0][2] = "1122"
userData[0][3] = "Admin"

#Adding Task 2D Array
MAX_TASK = 1000
taskCount = 0
#Format: [TaskID, StaffName, Description, Status]
assignTask = [[0,"SN","TD","Pending"] for _ in range(MAX_TASK)]


#Adding Guest Data Array
MAX_GUEST = 10000
guest_count = 0
#Formate = [id,GuestName, Room NO, Phoneno, Status,CheckIn Timem, Check Out Time]
guest_data = [[0,'GN','RN','PN','S','CI','CO'] for _ in range(MAX_GUEST)]

#Admin Login
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
        workerDuties()
    elif option == 5:
        viewBooking()
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
#Manage Rooms Function
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
#Manage Staff Members
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
#Add New Staff Member 
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
            userrole = input("[3] Ty Rpeole:(Admin  | Receptionist | Manager | Worker)")
            
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
                
#List Of all Users 
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
#Manage Staff Members
def managestaff():
    global userCount
    header("Manage Staff")
    element("-")
    print(f"{space:<4} {'Sr.':<10} {'Username':<10} {'Password':<10} {'Role':<10}")
    element("-")
    for i in range(userCount):
        print(f"{space:<4} {userData[i][0]:<10} {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")
    element("-")

    
    Search_User_name = input("Enter User Name: ")
    
    for i in range(userCount):
        if userData[i][1] == Search_User_name:
            print("\n[User FOUND!]\n")
            print(f"Current User: Name= {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")
            element("-")
            print("[1] Edit Data")
            print("[2] Delete")
            print("[0] Cancel")
            option = int(input("Enter Option: "))
            if option == 1:
                print(f"{space:<4} {'Sr.':<10} {'Username':<10} {'Password':<10} {'Role':<10}")
                print(f"{space:<4} {userData[i][0]:<10} {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")
   
                print("\n--- UPDATE DETAILS ---")

                new_username = input("Enter New Username (press Enter to skip): ")
                
                if new_username != "":
                    userData[i][1] = new_username

                new_password = input("Enter New Password (press Enter to skip): ")
                if new_password != "":
                    userData[i][2] = new_password

                new_role = input("Enter New Role (press Enter to skip): ")
                if new_role != "":
                    userData[i][3] = new_role

                print("\n[SUCCESS] User details updated successfully!")
                print(f"{space:<4} {userData[i][0]:<10} {userData[i][1]:<10} {userData[i][2]:10} {userData[i][3]:20}")

            elif option == 2:
                confirm = input(f"Are you sure you want to DELETE User {Search_User_name}? [Y/N]").upper()
                confirm = confirm.upper()
                if confirm.upper() == "Y":
                    for j in range(new_username,userCount-1):
                        userData[j][0] = -1
                        userData[j][1] = "U"
                        userData[j][2] = "P"
                        userData[j][2] = "R"
                    userCount = userCount-1
                    print("\n[SUCCESS] USER deleted successfully.")
                    viewallUser()
                else:
                    print("\n[CANCELLED] Deletion cancelled.")
                    viewAllRooms()
            else:
                print("\n[INFO] Returned to menu.")
                viewAllRooms()

        else:
            print(f"\n[ERROR] User {Search_User_name} not found in List.")
            break
   
def workerDuties():
    header("WORKER DUTIES & TASK ASSIGNMENT")
    element("-")
    print(f"{'Option':<10} {'Function':<20}")
    element("-")
    print(f"{'[1]':<10} {'Assign New Task':<20}")
    print(f"{'[2]':<10} {'View All Task':<20}")
    print(f"{'[3]':<10} {'Complete a Task':<20}")
    print(f"{'[0]':<10} {'Back':<20}")
    element("-")
    option =  int(input("Enter Option: "))
    if option == 1:
        assignNewTask()
    elif option == 2:
        viewAllTask()
    elif option == 3:
        completeTask()
    elif option == 0:
        administratordashboard()
    else:
        print("Invalid Opiton!")

  
#Assign Task To Worker
def assignNewTask():
    global taskCount
    global userCount
    header("Assign New Task")
    print("[Available Staff]")
    found_worker = False
    for i in range(userCount):
        if userData[i][3] == "Worker":
            print(f"{userData[i][1]:<10} {userData[i][3]:<3}")
            found_worker = True
        if not found_worker:
            print("No Staff with Role 'Worker' found")
        print("")

    staffName= input("Enter Staff Name to Assign: ")
    taskDetail = input("Enter Task Description: ")
    
    assignTask[i][0] = taskCount+1
    assignTask[i][1] = staffName
    assignTask[i][2] = taskDetail
    assignTask[i][3] = "Pending"
    
    print(f"[SUCCESS] Task Assigned to {staffName}")
    input("\nPress Enter To Reture...")
    workerDuties()

#View All Task
def viewAllTask():
    
    global taskCount
    header("TASK LIST")
    element("-")
    print(f"{'ID':<10} {'Staff Name':<10} {'TASK':<30} {'STATUS':<10}")
    element("-")
    for i in range(taskCount):
        print(f"{assignTask[i][0]:<10} {assignTask[i][1]:<10} {assignTask[i][2]:<30} {assignTask[i][3]:<10}")
    element("-")
    input("Press Enter to return...")
    workerDuties()

def completeTask():
    header("UPDATE TASK STATUS")
    print(f"{'ID':<10} {'Staff Name':<10} {'TASK':<30} {'STATUS':<10}")
    element("-")
    for i in range(taskCount):
        print(f"{assignTask[i][0]:<10} {assignTask[i][1]:<10} {assignTask[i][2]:<30} {assignTask[i][3]:<10}")
        
    element("-")
    taskid = input("Enter Task ID to Complete:...")
    if taskid == assignTask[i][0]:
        assignTask[i][3] = "COMPLETED"
    input("Press Enter to return...")
    workerDuties()

def viewBooking():
    header("GUEST BOOKING RECORDS")
    element("-")
    print(f"{'ID':<5} {'GUEST NAME':<30} {'ROOM NO':<10} {'PHONE NO':<10} {'STATUS':<10} {'Check IN':<5} {'Check OUt'}")
    element('-')
    for i in range(guest_count):
        print(f" {' ':<3} {guest_data[i][0]:<5} {guest_data[i][1]:<30} {guest_data[i][2]:<10} {guest_data[i][3]:<10} {guest_data[i][4]:<10} {guest_data[i][5]:<5} {guest_data[i][6]}")
    element

    print(f"Total Active Guests: {guest_count}")
    element("-")
    print("[1] Add New Booking")
    print("[0] Go Back")
    element("-")
    while True:
        option = int(input("Enter the Option [1-or-0]"))
        if option == 1:
            addNewBooking()
            break
        elif option == 2:
            administratordashboard()
            break
        else:
            print("Invalid Option")

def addNewBooking():

    global guest_count
    global roomCount
    
    header("Add New Booking")
    print("[Avalible Rooms]")
    element("-")
    print(f"{'ROOM NO':<10} {'TYPE':<10} {'Price' :<10}")
    element('-')
    occupied_room = []

    for k in range(guest_count):
        #Formate = [id,GuestName, Room NO, Phoneno, Status,CheckIn Timem, Check Out Time]
        #guest_data = [[0,'GN','RN','PN','S','CI','CO']
        if guest_data[k][4] == "Active":
            occupied_room.append(guest_data[k][2])
       
    element("-")
    available_room_found = False
    for i in range(roomCount):
        current_room_No = hotelData[i][0]
        if current_room_No != occupied_room:
            print(f"{hotelData[i][0]:<10} {hotelData[i][1]:<10} {hotelData[i][2]:<10}")
            available_room_found = True
    if not available_room_found:
        print("\n[!] No rooms are currently available.")
        input("Press Enter to go back...")
        return

    element("-")
    print("Enter '0' to Cancel")
    guestName = input("Enter Guest Name: ")
    if guestName == '0': return

    guestPhoneNo = input("Enter Mobile Number: ")
    guestCheckInTime = input("Enter CheckIn Date (e.g., 12/01/2026): ")

    # --- STEP 3: SELECT AND VALIDATE ROOM ---
    selected_room = -1
    while True:
        try:
            room_input = int(input("Enter Room No to Book: "))
            
            # Check 1: Does the room exist in hotelData?
            room_exists = False
            for i in range(roomCount):
                if hotelData[i][0] == room_input:
                    room_exists = True
                    break
            
            # Check 2: Is the room already occupied?
            if room_input in occupied_rooms:
                print(f"[ERROR] Room {room_input} is already occupied!")
            elif not room_exists:
                print(f"[ERROR] Room {room_input} does not exist in the hotel!")
            else:
                selected_room = room_input
                break # Room is valid and free
                
        except ValueError:
            print("[ERROR] Please enter a valid number.")

    # --- STEP 4: SAVE DATA TO ARRAY ---
    # Format: [id, GuestName, Room NO, Phoneno, Status, CheckIn Time, Check Out Time]
    
    guest_data[guest_count][0] = guest_count + 1        # ID
    guest_data[guest_count][1] = guestName              # Name
    guest_data[guest_count][2] = selected_room          # Room No
    guest_data[guest_count][3] = guestPhoneNo           # Phone
    guest_data[guest_count][4] = "Active"               # Status
    guest_data[guest_count][5] = guestCheckInTime       # Check In
    guest_data[guest_count][6] = "-"                    # Check Out (Pending)

    guest_count += 1
    
    print("\n[SUCCESS] Booking Confirmed!")
    print(f"Guest {guestName} assigned to Room {selected_room}")
    
    input("\nPress Enter to return...")
    viewBooking()



def main():
    while(True):
        header("Hostel Management System")
        print("\nWelcome! Please select your role to access the system\n")
        print("-" * 55)
        print(f"[1] ADMINISTRATOR{space:<10} [2] RECEPTIONIST")
        print(f"[3] MANAGER{space:<16} [4] WORKER / STAFF")
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

main()