import datetime
import os

space = " "

# --- GLOBAL DATA STRUCTURES ---

# Room Data
MAX_CAP = 300
roomCount = 0
# Format: [RoomNO, Type, Price]
hotelData = [[-1, "HD", -11] for _ in range(MAX_CAP)]

# User Data
MAX_USER = 50
userCount = 1
# Format: [UserID, Username, Password, Role]
userData = [[-1, "U", "P", "R"] for _ in range(MAX_USER)]
# Default Admin (will be overwritten if file exists)
userData[0] = [0, "admin", "1122", "Admin"]

# Task Data
MAX_TASK = 1000
taskCount = 0
# Format: [TaskID, StaffName, Description, Status]
assignTask = [[0, "SN", "TD", "Pending"] for _ in range(MAX_TASK)]

# Guest Data
MAX_GUEST = 10000
guest_count = 0
# Format: [id, GuestName, RoomNO, Phone, Status, CheckIn, CheckOut, BillAmount]
guest_data = [[0, 'GN', 'RN', 'PN', 'S', 'CI', 'CO', 0] for _ in range(MAX_GUEST)]

# Attendance Data
MAX_ATTENDANCE = 10000
attendance_count = 0
# Format: [ID, WorkerName, Date, Status, TimeIn, TimeOut]

# Settings
hotel_config = {"name": "Luxe Stay"}

def load_settings():
    global hotel_config
    if os.path.exists("data/settings.txt"):
        with open("data/settings.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("name="):
                    hotel_config["name"] = line.strip().split("=")[1]

def save_settings():
    with open("data/settings.txt", "w") as f:
        f.write(f"name={hotel_config['name']}\n")

def load_data():
    global roomCount, userCount, taskCount, guest_count, attendance_count
    load_settings()
    
    # Load Rooms

    if os.path.exists("data/rooms.txt"):
        with open("data/rooms.txt", "r") as f:
            lines = f.readlines()
            idx = 0
            for line in lines:
                data = line.strip().split(',')
                if len(data) >= 3 and idx < MAX_CAP:
                    hotelData[idx][0] = int(data[0])
                    hotelData[idx][1] = data[1]
                    hotelData[idx][2] = int(data[2])
                    idx += 1
            roomCount = idx


    # Load Users
    if os.path.exists("data/users.txt"):
        with open("data/users.txt", "r") as f:
            lines = f.readlines()
            idx = 0
            for line in lines:
                data = line.strip().split(',')
                # Format: ID,Username,Password,Role,Salary
                if len(data) >= 4 and idx < MAX_USER:
                    userData[idx][0] = int(data[0])
                    userData[idx][1] = data[1]
                    userData[idx][2] = data[2]
                    userData[idx][3] = data[3]
                    
                    # Ensure the inner list is big enough or append
                    # Original init was [-1, "U", "P", "R"] length 4
                    # We extend it to length 5 for salary if needed
                    while len(userData[idx]) < 5:
                        userData[idx].append("0")
                    
                    if len(data) > 4:
                        userData[idx][4] = data[4]
                    else:
                        userData[idx][4] = "0"
                    
                    idx += 1
            userCount = idx


    # Load Tasks
    if os.path.exists("data/tasks.txt"):
        with open("data/tasks.txt", "r") as f:
            lines = f.readlines()
            idx = 0
            for line in lines:
                data = line.strip().split(',')
                if len(data) >= 4 and idx < MAX_TASK:
                    assignTask[idx][0] = int(data[0])
                    assignTask[idx][1] = data[1]
                    assignTask[idx][2] = data[2]
                    assignTask[idx][3] = data[3]
                    idx += 1
            taskCount = idx

    # Load Guests
    if os.path.exists("data/guests.txt"):
        with open("data/guests.txt", "r") as f:
            lines = f.readlines()
            idx = 0
            for line in lines:
                data = line.strip().split(',')
                # Support legacy/shorter lines just in case
                if len(data) >= 7 and idx < MAX_GUEST:
                    guest_data[idx][0] = int(data[0])
                    guest_data[idx][1] = data[1]
                    guest_data[idx][2] = int(data[2])
                    guest_data[idx][3] = data[3]
                    guest_data[idx][4] = data[4]
                    guest_data[idx][5] = data[5]
                    guest_data[idx][6] = data[6]
                    if len(data) > 7:
                        guest_data[idx][7] = int(data[7])
                    else:
                        guest_data[idx][7] = 0
                    idx += 1
            guest_count = idx
            
    # Load Attendance
    if os.path.exists("data/attendance.txt"):
        with open("data/attendance.txt", "r") as f:
            lines = f.readlines()
            idx = 0
            for line in lines:
                data = line.strip().split(',')
                if len(data) >= 6 and idx < MAX_ATTENDANCE:
                    attendanceData[idx][0] = int(data[0])
                    attendanceData[idx][1] = data[1]
                    attendanceData[idx][2] = data[2]
                    attendanceData[idx][3] = data[3]
                    attendanceData[idx][4] = data[4]
                    attendanceData[idx][5] = data[5]
                    idx += 1
            attendance_count = idx

def save_data():
    # Save Rooms
    with open("data/rooms.txt", "w") as f:
        for i in range(roomCount):
            f.write(f"{hotelData[i][0]},{hotelData[i][1]},{hotelData[i][2]}\n")


    # Save Users
    with open("data/users.txt", "w") as f:
        for i in range(userCount):
            # Check length for salary
            salary = "0"
            if len(userData[i]) > 4:
                salary = str(userData[i][4])
            f.write(f"{userData[i][0]},{userData[i][1]},{userData[i][2]},{userData[i][3]},{salary}\n")


    # Save Tasks
    with open("data/tasks.txt", "w") as f:
        for i in range(taskCount):
            f.write(f"{assignTask[i][0]},{assignTask[i][1]},{assignTask[i][2]},{assignTask[i][3]}\n")

    # Save Guests
    with open("data/guests.txt", "w") as f:
        for i in range(guest_count):
            f.write(f"{guest_data[i][0]},{guest_data[i][1]},{guest_data[i][2]},{guest_data[i][3]},{guest_data[i][4]},{guest_data[i][5]},{guest_data[i][6]},{guest_data[i][7]}\n")
            
    # Save Attendance
    with open("data/attendance.txt", "w") as f:
        for i in range(attendance_count):
            f.write(f"{attendanceData[i][0]},{attendanceData[i][1]},{attendanceData[i][2]},{attendanceData[i][3]},{attendanceData[i][4]},{attendanceData[i][5]}\n")

# --- UTILS ---

def header(name):
    print("=" * 55)
    print(f"{name:^55}")
    print("=" * 55)

def element(dash):
    print(dash * 55)

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
    if type == 'S': return "Single"
    elif type == 'D': return "Double"
    elif type == 'T': return "Triple"
    elif type == 'ST': return "Suite"
    else:
        print("[ERROR] Invalid Room Type. Please use S, D, T, or ST.")
        return None

# --- ADMIN FUNCTIONS ---

def administratorlogin():
    header("Hostel Management System")
    print(f"{'[ AUTHENTICATION REQUIRED ]':^55}\n")
    element("-")
    attempts = 3 
    while True:
        print("Enter X to go back\n")
        username = input("Enter UserName: ")
        if username.lower() == 'x': return
        
        password = input("Enter Password: ")
        if password.lower() == 'x': return

        for i in range(userCount):
            if username == userData[i][1] and password == userData[i][2] and userData[i][3] == "Admin":
                element("-")
                print("\nLogin Successful!\n")
                administratordashboard()
                return   
        
        attempts -= 1
        if attempts == 0:
            print("No More Attempts Left")
            break
        print(f"Invalid Credentials or Access Denied! Remaining Attempts: {attempts}\n")

def administratordashboard():
    while True:
        header("ADMINISTRATOR DASHBOARD")
        element("-")
        print(f"{'[1]':<8} {'Add Rooms':<20} {'[2]':<8} {'View All Rooms':<20}")
        print(f"{'[3]':<8} {'Manage Staff':<20} {'[4]':<8} {'Worker Duties':<20}")
        print(f"{'[5]':<8} {'View Booking':<20} {'[6]':<8} {'Financials/Bill Report':<20}")
        print(f"{'[7]':<8} {'Attendance':<20} {'[8]':<8} {'System Stats':<20}")
        print(f"{'[0]':<8} {'Logout':<20}")
        element("-")
        
        try:
            option = int(input("Enter the Option (0-to-8): "))
            if option == 1: addroom()
            elif option == 2: viewAllRooms()
            elif option == 3: ManageStaff()
            elif option == 4: workerDuties()
            elif option == 5: viewBooking()
            elif option == 6: viewBillingReport()
            elif option == 7: viewAttendanceReport()
            elif option == 8: viewSystemStats()
            elif option == 0: return
            else: print("Invalid Option")
        except ValueError:
            print("Invalid Input")

def roomtypes():
    print("AVAILABLE ROOM TYPES:")
    print("Single[S]  (1 Bed,  Max 1 Person)")
    print("Double[D]  (1 Bed,  Max 2 Persons)")
    print("Twin[T]    (2 Beds, Max 2 Persons)")
    print("Suite[ST]  (Luxury, Max 4 Persons)")

def addroom():
    global roomCount
    header("ADD NEW ROOM")
    roomtypes()
    
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
                if not exists: break
        except ValueError:
            print("Invalid number.")
            
    Room_Type = ""
    while True:
        rt = input("Enter Room Type (S/D/T/ST): ").upper()
        res = get_room_type_name(rt)
        if res:
            Room_Type = res
            break
            
    try:
        New_RoomPrice = int(input("Enter Price Per Night (PKR): "))
    except ValueError:
        New_RoomPrice = 0
        
    hotelData[roomCount][0] = New_RoomNO
    hotelData[roomCount][1] = Room_Type
    hotelData[roomCount][2] = New_RoomPrice
    roomCount += 1
    save_data() 
    print(f"[SUCCESS] Room {New_RoomNO} Created!")
    
    if input("[1] Add Another / [Any] Go Back: ") == '1':
        addroom()

def viewAllRooms():
    header("ROOM INVENTORY LIST")
    print(f"{'ROOM NO':<10} {'TYPE':<20} PRICE (PKR)")
    element("-")
    for i in range(roomCount):
        print(f"{hotelData[i][0]:<10} {hotelData[i][1]:<20} {hotelData[i][2]}")
    element("-")
    
    opt = input("[M] Manage Rooms / [X] Back: ").upper()
    if opt == 'M': manageRooms()

def manageRooms():
    global roomCount
    s_room = int(input("Enter Room No to Manage: "))
    idx = -1
    for i in range(roomCount):
        if hotelData[i][0] == s_room:
            idx = i
            break
    
    if idx == -1:
        print("Room not found.")
        return
        
    print(f"Found: {hotelData[idx]}")
    opt = input("[1] Edit / [2] Delete / [0] Cancel: ")
    
    if opt == '1':
        rt = input("New Type (S/D/T/ST) or Enter to skip: ").upper()
        if rt:
            res = get_room_type_name(rt)
            if res: hotelData[idx][1] = res
            
        rp = input("New Price or Enter to skip: ")
        if rp: hotelData[idx][2] = int(rp)
        save_data()
        print("Updated.")
        
    elif opt == '2':
        if input("Confirm Delete (Y/N): ").upper() == 'Y':
            # Shift elements
            for j in range(idx, roomCount - 1):
                hotelData[j] = hotelData[j+1]
                # Assuming simple copy is enough for list of lists if we don't hold refs
                # Actually better to invoke manual copy if deepcopy needed, but integers/strings are fine
                hotelData[j] = hotelData[j+1][:] 

            # Clear last
            hotelData[roomCount-1] = [-1, "HD", -11]
            roomCount -= 1
            save_data()
            print("Deleted.")

def ManageStaff():
    header("STAFF MANAGEMENT")
    print(f"[1] Add Staff  [2] View Staff  [0] Back")
    opt = input("Option: ")
    if opt == '1': addNewStaff()
    elif opt == '2': viewallUser()

def addNewStaff():
    global userCount
    username = input("Enter New Username: ")
    # Check exist
    for i in range(userCount):
        if userData[i][1] == username:
            print("User exists.")
            return

    password = input("Enter Password: ")
    print("Roles: Admin, Receptionist, Manager, Worker")
    role = input("Enter Role: ")
    
    userData[userCount][0] = userCount
    userData[userCount][1] = username
    userData[userCount][2] = password
    userData[userCount][3] = role
    userCount += 1
    save_data()
    print("User Added.")

def viewallUser():
    header("ALL USERS")
    print(f"{'ID':<5} {'Username':<15} {'Role':<15}")
    element("-")
    for i in range(userCount):
        print(f"{userData[i][0]:<5} {userData[i][1]:<15} {userData[i][3]:<15}")
    element("-")
    input("Press Enter...")

def workerDuties():
    header("WORKER DUTIES")
    print(f"[1] Assign Task  [2] View Tasks  [3] Complete Task  [0] Back")
    opt = input("Option: ")
    if opt == '1': assignNewTask()
    elif opt == '2': viewAllTask()
    elif opt == '3': completeTask()

def assignNewTask():
    global taskCount
    staff = input("Enter Staff Name: ")
    desc = input("Task Description: ")
    
    assignTask[taskCount][0] = taskCount + 1
    assignTask[taskCount][1] = staff
    assignTask[taskCount][2] = desc
    assignTask[taskCount][3] = "Pending"
    taskCount += 1
    save_data()
    print("Task Assigned.")

def viewAllTask():
    header("TASKS")
    for i in range(taskCount):
        print(f"ID:{assignTask[i][0]} | Staff:{assignTask[i][1]} | {assignTask[i][2]} | [{assignTask[i][3]}]")
    input("Press Enter...")

def completeTask():
    tid = int(input("Enter Task ID to complete: "))
    for i in range(taskCount):
        if assignTask[i][0] == tid:
            assignTask[i][3] = "Completed"
            save_data()
            print("Updated.")
            return
    print("Not found.")

def viewBooking():
    header("BOOKINGS")
    print(f"{'ID':<5} {'Name':<20} {'Room':<5} {'Status':<10} {'CheckIn'}")
    for i in range(guest_count):
        print(f"{guest_data[i][0]:<5} {guest_data[i][1]:<20} {guest_data[i][2]:<5} {guest_data[i][4]:<10} {guest_data[i][5]}")
    
    if input("[1] New Booking / [0] Back: ") == '1':
        addNewBooking()

def addNewBooking():
    global guest_count
    name = input("Guest Name: ")
    phone = input("Phone: ")
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Show available
    occupied = [guest_data[k][2] for k in range(guest_count) if guest_data[k][4] == "Active"]
    print("Available Rooms:")
    for i in range(roomCount):
        if hotelData[i][0] not in occupied:
            print(f"Room {hotelData[i][0]} ({hotelData[i][1]}) - {hotelData[i][2]}")
            
    try:
        rno = int(input("Enter Room No: "))
    except ValueError:
        return

    # Validate
    valid = False
    for i in range(roomCount):
        if hotelData[i][0] == rno:
            valid = True
            break
    if not valid or rno in occupied:
        print("Invalid or Occupied.")
        return

    guest_data[guest_count][0] = guest_count + 1
    guest_data[guest_count][1] = name
    guest_data[guest_count][2] = rno
    guest_data[guest_count][3] = phone
    guest_data[guest_count][4] = "Active"
    guest_data[guest_count][5] = now
    guest_data[guest_count][6] = "-"
    guest_data[guest_count][7] = 0
    guest_count += 1
    save_data()
    print("Booked.")


def viewBillingReport():
    print("="*55)
    print(f"{'Financials':^55}")
    print("="*55)
    # print(f"{'Guest Name':<30} | {'Bill (PKR)':>15}")
    # print("="*55)
    total = 0
    for i in range(guest_count):
        if guest_data[i][4] == "CheckedOut":
            print(f"Guest: {guest_data[i][1]} | Bill: {guest_data[i][7]}")
            total += int(guest_data[i][7])
    print("="*55)
    print(f"Total Revenue: {total}")
    print("="*55)
    input("Press Enter...")


def viewAttendanceReport():
    header("Attendance Log")
    for i in range(attendance_count):
        print(f"{attendanceData[i][1]} | {attendanceData[i][2]} | {attendanceData[i][3]} | In: {attendanceData[i][4]} | Out: {attendanceData[i][5]}")
    input("Press Enter...")

def viewSystemStats():
    print(f"Total Rooms: {roomCount}")
    print(f"Total Staff: {userCount}")
    print(f"Total Bookings: {guest_count}")
    input("Press Enter...")

# --- RECEPTIONIST FUNCTIONS ---

def receptionist():
    header("RECEPTIONIST PORTAL")
    while True:
        username = input("Username: ")
        password = input("Password: ")
        # Validate
        valid = False
        for i in range(userCount):
            if userData[i][1] == username and userData[i][2] == password and (userData[i][3] == "Receptionist" or userData[i][3] == "Admin"):
                valid = True
                break
        if valid:
            receptionist_dashboard()
            return
        else:
            print("Invalid.")
            if input("Try again? (y/n): ") != 'y': return

def receptionist_dashboard():
    while True:
        header("RECEPTIONIST DASHBOARD")
        print("[1] Available Rooms")
        print("[2] Register Entry (Book)")
        print("[3] Guest Checkout & Bill")
        print("[4] View Bookings")
        print("[0] Logout")
        
        opt = input("Option: ")
        if opt == '1': viewAvailableRooms()
        elif opt == '2': addNewBooking()
        elif opt == '3': checkOut()
        elif opt == '4': viewBooking()
        elif opt == '0': return

def viewAvailableRooms():
    header("AVAILABLE ROOMS")
    occupied = [guest_data[k][2] for k in range(guest_count) if guest_data[k][4] == "Active"]
    for i in range(roomCount):
        if hotelData[i][0] not in occupied:
            print(f"Room {hotelData[i][0]} | {hotelData[i][1]} | {hotelData[i][2]}")
    input("Press Enter...")

def checkOut():
    header("CHECKOUT")
    rno = int(input("Enter Room Number to Checkout: "))
    found = -1
    for i in range(guest_count):
        if guest_data[i][2] == rno and guest_data[i][4] == "Active":
            found = i
            break
            
    if found != -1:
        # Calculate Bill
        print(f"Checking out Guest: {guest_data[found][1]}")
        days = int(input("Enter Total Days Stayed: "))
        
        # Find room price
        price = 0
        for r in range(roomCount):
            if hotelData[r][0] == rno:
                price = hotelData[r][2]
                break
        
        bill = days * price
        print(f"Total Bill: {bill} PKR")
        confirm = input("Confirm Checkout (y/n)? ")
        if confirm.lower() == 'y':
            guest_data[found][4] = "CheckedOut"
            guest_data[found][6] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            guest_data[found][7] = bill
            save_data()
            print("Checked Out Successfully.")
    else:
        print("No active booking found for this room.")

# --- MANAGER FUNCTIONS ---

def manager():
    header("MANAGER PORTAL")
    # Simplify login for brevity - in real app, duplicate the logic or make a shared login func
    username = input("Username: ")
    password = input("Password: ")
    # Validate
    valid = False
    for i in range(userCount):
        if userData[i][1] == username and userData[i][2] == password and (userData[i][3] == "Manager" or userData[i][3] == "Admin"):
            valid = True
            break
    if valid:
        manager_dashboard()
    else:
        print("Invalid.")

def manager_dashboard():
    while True:
        header("MANAGER DASHBOARD")
        print("[1] View Rooms")
        print("[2] View Bookings")
        print("[3] Billing Reports")
        print("[4] Staff Attendance")
        print("[0] Logout")
        
        opt = input("Option: ")
        if opt == '1': viewAllRooms() # Reuse
        elif opt == '2': viewBooking() # Reuse
        elif opt == '3': viewBillingReport() # Reuse
        elif opt == '4': viewAttendanceReport() # Reuse
        elif opt == '0': return

# --- WORKER FUNCTIONS ---

def worker():
    header("WORKER PORTAL")
    username = input("Username: ")
    password = input("Password: ")
    # Validate
    valid = False
    for i in range(userCount):
        if userData[i][1] == username and userData[i][2] == password and (userData[i][3] == "Worker" or userData[i][3] == "Admin"):
            valid = True
            break
    if valid:
        worker_dashboard(username)
    else:
        print("Invalid.")

def worker_dashboard(name):
    while True:
        header(f"WORKER: {name}")
        print("[1] Check-In (Attendance)")
        print("[2] Check-Out (Attendance)")
        print("[3] View My Tasks")
        print("[0] Logout")
        
        opt = input("Option: ")
        if opt == '1': mark_attendance(name, "In")
        elif opt == '2': mark_attendance(name, "Out")
        elif opt == '3': viewMyTasks(name)
        elif opt == '0': return

def mark_attendance(name, type):
    global attendance_count
    now = datetime.datetime.now().strftime("%H:%M")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    if type == "In":
        attendanceData[attendance_count][0] = attendance_count + 1
        attendanceData[attendance_count][1] = name
        attendanceData[attendance_count][2] = date
        attendanceData[attendance_count][3] = "Present"
        attendanceData[attendance_count][4] = now
        attendanceData[attendance_count][5] = "-"
        attendance_count += 1
        save_data()
        print("Checked In.")
    else:
        # Find last checkin today
        for i in range(attendance_count-1, -1, -1):
            if attendanceData[i][1] == name and attendanceData[i][2] == date and attendanceData[i][5] == "-":
                attendanceData[i][5] = now
                save_data()
                print("Checked Out.")
                return
        print("You haven't checked in yet today.")

def viewMyTasks(name):
    header("MY TASKS")
    for i in range(taskCount):
        if assignTask[i][1] == name:
            print(f"{assignTask[i][2]} - [{assignTask[i][3]}]")
    input("Press Enter...")


# --- MAIN ---

def main():
    load_data()
    while True:
        header("Hostel Management System")
        print("\nWelcome! Please select your role to access the system\n")
        print("-" * 55)
        print(f"[1] ADMINISTRATOR{space:<10} [2] RECEPTIONIST")
        print(f"[3] MANAGER{space:<16} [4] WORKER / STAFF")
        print(f"[5] Exit")
        print("-"*55)
        
        try:
            option_str = input("Enter the Option (1-to-5): ")
            if not option_str.isdigit(): continue
            option = int(option_str)
            
            if option == 1: administratorlogin()
            elif option == 2: receptionist()
            elif option == 3: manager()
            elif option == 4: worker()
            elif option == 5:
                save_data()
                print("Goodbye!")
                return
            else:
                print("Invalid Option")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
else:
    load_data()
