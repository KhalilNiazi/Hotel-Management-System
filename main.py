
import datetime
import os
import colorama
from colorama import Fore, Back, Style

# Auto-reset colors after each print
colorama.init(autoreset=True)

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
userData[0] = [0, "admin", "admin123", "Admin"]

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
attendanceData = [[0, 'WN', 'D', 'S', 'TI', 'TO'] for _ in range(MAX_ATTENDANCE)]

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


import requests
import json
import requests.exceptions

# Config to switch betwen local and cloud

# Config to switch betwen local and cloud
APPS_SCRIPT_URL = "" 
USE_CLOUD = False    # Set to True to enable

def load_data():
    global roomCount, userCount, taskCount, guest_count, attendance_count
    load_settings()
    
    # --- FILE LOAD (Existing Code) ---
    # Load Rooms

    # --- FILE LOAD (Existing Code) ---
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
    # Use fallback if attendance.txt missing or empty
    if not os.path.exists("data/attendance.txt"):
        pass 
    else:
         with open("data/attendance.txt", "r") as f:
            lines = f.readlines()
            idx = 0
            for line in lines:
                data = line.strip().split(',')
                # Ensure data row has at least 6 columns
                # ID, Name, Date, Status, TimeIn, TimeOut
                if len(data) >= 6 and idx < MAX_ATTENDANCE:
                    try:
                        attendanceData[idx][0] = int(data[0])
                        attendanceData[idx][1] = str(data[1])
                        attendanceData[idx][2] = str(data[2])
                        attendanceData[idx][3] = str(data[3])
                        attendanceData[idx][4] = str(data[4])
                        attendanceData[idx][5] = str(data[5])
                        idx += 1
                    except Exception as e:
                        print(f"Error parsing attendance line {idx}: {e}")
            attendance_count = idx


def save_data():
    save_settings()
    
    if USE_CLOUD and APPS_SCRIPT_URL:
        # --- CLOUD SAVE ---
        try:
            payload = {
                "Rooms": [hotelData[i][:3] for i in range(roomCount)],
                "Users": [userData[i][:5] for i in range(userCount)],
                "Tasks": [assignTask[i][:4] for i in range(taskCount)],
                "Guests": [guest_data[i][:8] for i in range(guest_count)],
                "Attendance": [attendanceData[i][:6] for i in range(attendance_count)],
                "Settings": [[hotel_config["name"]]]
            }
            # Send Async if possible, but here we sync wait
            requests.post(APPS_SCRIPT_URL, json=payload)
        except Exception as e:
            print(f"Cloud Save Error: {e}")

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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_console_size():
    if os.name == 'nt':
        try:
            # Attempt to maximize the console window
            import ctypes
            kernel32 = ctypes.WinDLL('kernel32')
            user32 = ctypes.WinDLL('user32')
            
            hwnd = kernel32.GetConsoleWindow()
            if hwnd:
                user32.ShowWindow(hwnd, 3) # SW_MAXIMIZE = 3
        except Exception:
            pass # Fail silently if not supported

# Note: 'header' is redefined below in the main loop area so this one is redundant or shadowed.
# We will update it to match the colorful one anyway to be safe.
def header(name=None):
    if name is None or name == "Hostel Management System": 
        name = hotel_config.get("name", "Luxe Stay")
        
    print(Fore.CYAN + "=" * 55)
    print(Fore.YELLOW + Style.BRIGHT + f"{name:^55}")
    print(Fore.CYAN + "=" * 55)
    
def element(dash):
    print(Fore.CYAN + dash * 55)

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
    header()
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



def checkOutGuest():
    global guest_count
    header("GUEST CHECKOUT & BILLING")
    
    # List Active
    print(Fore.CYAN + "ACTIVE GUESTS:")
    foundAny = False
    for i in range(guest_count):
        if guest_data[i][4] == "Active":
            print(f"ID:{guest_data[i][0]:<4} | Name:{guest_data[i][1]:<15} | Room:{guest_data[i][2]:<5} | In:{guest_data[i][5]}")
            foundAny = True
            
    if not foundAny:
        print(Fore.RED + "No active guests.")
        return

    try:
        val = input(Fore.YELLOW + "Enter Guest ID to Checkout (X to back): " + Fore.RESET)
        if val.upper() == 'X': return
        
        gid = int(val)
        idx = -1
        for i in range(guest_count):
            if guest_data[i][0] == gid and guest_data[i][4] == "Active":
                 idx = i
                 break
        
        if idx == -1:
             print(Fore.RED + "Guest ID not found or not active.")
             return

        # Found Guest
        # 1. Calculate Days
        checkin_str = guest_data[idx][5]
        checkout_now = datetime.datetime.now()
        
        try:
            checkin_dt = datetime.datetime.strptime(checkin_str, "%d/%m/%Y %H:%M")
        except ValueError:
            # Fallback if format is just date or invalid
            try:
                checkin_dt = datetime.datetime.strptime(checkin_str, "%d/%m/%Y")
            except:
                checkin_dt = checkout_now
        
        duration = checkout_now - checkin_dt
        days = duration.days
        if days < 1: days = 1  # Charge minimum 1 day
        
        # 2. Get Room Price
        room_price = 0
        rno = guest_data[idx][2]
        for i in range(roomCount):
            if hotelData[i][0] == rno:
                room_price = hotelData[i][2]
                break
                
        base_bill = days * room_price
        
        # 3. Interactive Billing
        print(Fore.GREEN + "\n--- BILL CALCULATION ---")
        print(f"Guest Name: {guest_data[idx][1]}")
        print(f"Stay Duration: {days} Days")
        print(f"Room Charge: {base_bill} (Rate: {room_price}/night)")
        

        try:
            extra_input = input("Add Extra Charges (Food/Services) [0]: ").strip()
            if not extra_input: 
                extra = 0
            else: 
                extra = int(extra_input)
        except ValueError:
            extra = 0
            
        total_bill = base_bill + extra
        

        print(Fore.YELLOW + f"TOTAL BILL AMOUNT: Rs. {total_bill}")
        
        conf = input("Confirm Checkout & Save? (Y/N): ")
        if conf.upper() == 'Y':
            guest_data[idx][4] = "CheckedOut"
            guest_data[idx][6] = checkout_now.strftime("%d/%m/%Y %H:%M")
            guest_data[idx][7] = total_bill
            save_data()
            print(Fore.GREEN + "[SUCCESS] Guest Checked Out.")
            

            # Print/PDF Option
            if input("Generate Invoice? (Y/N): ").upper() == 'Y':
                h_name = hotel_config.get("name", "Luxe Stay").upper()
                invoice_text = f"""
                    ===================================================
                                {h_name:^35}
                    ===================================================
                    INVOICE ID: #{int(datetime.datetime.now().timestamp())}
                    DATE      : {checkout_now.strftime("%d-%b-%Y %I:%M %p")}
                    ---------------------------------------------------
                    GUEST NAME  : {guest_data[idx][1]}
                    ROOM NO     : {guest_data[idx][2]} 
                    DURATION    : {days} Night(s)
                    ---------------------------------------------------
                    Room Charge : Rs. {base_bill}
                    Extra       : Rs. {extra}
                    ---------------------------------------------------
                    TOTAL       : Rs. {total_bill}
                    ===================================================
                    Thank you for choosing {h_name.title()}!
                    """
                fname = f"invoice_{gid}_{int(datetime.datetime.now().timestamp())}.txt"
                with open(fname, "w") as f:
                    f.write(invoice_text)
                print(Fore.CYAN + f"Invoice saved to {fname}")
                # Try to open file (simulating print/pdf view)
                try:
                    os.startfile(fname)
                except:
                    pass
        else:
            print(Fore.RED + "Cancelled.")

    except ValueError:
        print(Fore.RED + "Invalid Input.")

def administratordashboard():

    while True:
        clear()
        header("ADMINISTRATOR DASHBOARD")
        element("-")
        print(Fore.WHITE + f"{'[1]':<8} {Fore.YELLOW}{'Add Rooms':<25} {Fore.WHITE}{'[2]':<8} {Fore.YELLOW}{'View All Rooms':<25}")
        print(Fore.WHITE + f"{'[3]':<8} {Fore.YELLOW}{'Manage Staff':<25} {Fore.WHITE}{'[4]':<8} {Fore.YELLOW}{'Worker Duties':<25}")
        print(Fore.WHITE + f"{'[5]':<8} {Fore.YELLOW}{'View Booking':<25} {Fore.WHITE}{'[6]':<8} {Fore.YELLOW}{'Financials/Bill Report':<25}")
        print(Fore.WHITE + f"{'[7]':<8} {Fore.YELLOW}{'Attendance':<25} {Fore.WHITE}{'[8]':<8} {Fore.YELLOW}{'System Stats':<25}")
        print(Fore.WHITE + f"{'[9]':<8} {Fore.YELLOW}{'Check Out Guest':<25} {Fore.WHITE}{'[10]':<8} {Fore.YELLOW}{'Settings':<25}")
        print(Fore.RED   + f"{'[0]':<8} {'Logout':<25}")
        element("-")
        
        try:
            option_str = input(Fore.CYAN + "Enter Option (0-10): " + Fore.RESET)
            if not option_str.isdigit(): continue
            option = int(option_str)
            if option == 1: addroom()
            elif option == 2: viewAllRooms()
            elif option == 3: ManageStaff()
            elif option == 4: workerDuties()
            elif option == 5: viewBooking()
            elif option == 6: viewBillingReport()
            elif option == 7: viewAttendanceReport()
            elif option == 8: viewSystemStats()
            elif option == 9: checkOutGuest()
            elif option == 10: system_settings()
            elif option == 0: return
            else: print(Fore.RED + "Invalid Option")
        except ValueError:
            print(Fore.RED + "Invalid Input")

def system_settings():
    clear()
    header("SYSTEM SETTINGS")
    print(f"Current Hotel Name: {hotel_config['name']}")
    print("-" * 30)
    print("[1] Change Hotel Name")
    print("[0] Back")
    
    opt = input("Option: ")
    if opt == '1':
        new_name = input("Enter New Hotel Name: ")
        if new_name.strip():
            hotel_config["name"] = new_name.strip()
            save_settings()
            print("Settings Saved.")
    

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
            val = input(f"Room No[1-to-{MAX_CAP}] (X to back): ")
            if val.lower() == 'x': return
            
            New_RoomNO = int(val)
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
    print(Fore.CYAN + f"{'ROOM NO':<10} {'TYPE':<20} {'PRICE (PKR)'}")
    element("-")
    for i in range(roomCount):
        print(Fore.WHITE + f"{hotelData[i][0]:<10} {hotelData[i][1]:<20} {hotelData[i][2]}")
    element("-")
    
    opt = input(Fore.YELLOW + "[M] Manage Rooms / [X] Back: " + Fore.RESET).upper()
    if opt == 'M': manageRooms()

def manageRooms():
    global roomCount
    try:
        s_room = int(input(Fore.YELLOW + "Enter Room No to Manage: " + Fore.RESET))
    except ValueError: return
    
    idx = -1
    for i in range(roomCount):
        if hotelData[i][0] == s_room:
            idx = i
            break
    
    if idx == -1:
        print(Fore.RED + "Room not found.")
        return
        
    print(Fore.GREEN + f"Found: {hotelData[idx]}")
    opt = input(Fore.YELLOW + "[1] Edit / [2] Delete / [0] Cancel: " + Fore.RESET)
    
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
    print(Fore.CYAN + f"{'ID':<5} {'Username':<15} {'Role':<15}")
    element("-")
    for i in range(userCount):
        print(Fore.WHITE + f"{userData[i][0]:<5} {userData[i][1]:<15} {userData[i][3]:<15}")
    element("-")
    input(Fore.YELLOW + "Press Enter..." + Fore.RESET)

def workerDuties():
    header("WORKER DUTIES")
    print(Fore.CYAN + f"[1] Assign Task  [2] View Tasks  [3] Complete Task  [0] Back")
    opt = input(Fore.WHITE + "Option: ")
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
    print(Fore.CYAN + f"{'ID':<5} {'Name':<20} {'Room':<5} {'Status':<10} {'CheckIn'}")
    element("-")
    for i in range(guest_count):
        row_color = Fore.WHITE
        if guest_data[i][4] == "CheckedOut": row_color = Fore.RED
        elif guest_data[i][4] == "Active": row_color = Fore.GREEN
        
        print(row_color + f"{guest_data[i][0]:<5} {guest_data[i][1]:<20} {guest_data[i][2]:<5} {guest_data[i][4]:<10} {guest_data[i][5]}")
    element("-")
    
    if input(Fore.YELLOW + "[1] New Booking / [0] Back: " + Fore.RESET) == '1':
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
    clear()
    header("FINANCIAL REPORT")
    print(Fore.CYAN + f"{'GUEST NAME':<30} | {'BILL (PKR)':>15}")
    element("-")
    total = 0
    for i in range(guest_count):
        if guest_data[i][4] == "CheckedOut":
            print(Fore.WHITE + f"{guest_data[i][1]:<30} | {Fore.GREEN}{guest_data[i][7]:>15}")
            total += int(guest_data[i][7])
    element("-")
    print(Fore.YELLOW + Style.BRIGHT + f"{'TOTAL REVENUE':<30} | {total:>15}")
    element("-")
    input(Fore.YELLOW + "Press Enter..." + Fore.RESET)



def viewAttendanceReport():
    clear()
    header("ATTENDANCE LOG")
    if attendance_count == 0:
        print(Fore.RED + "No Attendance Records Found.")
    else:
        # Table Header
        print(Fore.CYAN + f"{'NAME':<15} {'DATE':<12} {'STATUS':<10} {'IN':<8} {'OUT':<8}")
        element("-")
        
        for i in range(attendance_count):
            name = attendanceData[i][1]
            date = attendanceData[i][2]
            status = attendanceData[i][3]
            time_in = attendanceData[i][4]
            time_out = attendanceData[i][5]
            
            # Color coding status
            status_color = Fore.GREEN if status == "Present" else Fore.RED
            
            print(Fore.WHITE + f"{name:<15} {date:<12} {status_color}{status:<10} {Fore.WHITE}{time_in:<8} {time_out:<8}")
            
    element("-")
    input(Fore.YELLOW + "Press Enter to Back..." + Fore.RESET)

def viewSystemStats():
    clear()
    header("SYSTEM STATISTICS")
    print(Fore.WHITE + f"Total Rooms    : {Fore.YELLOW}{roomCount}")
    print(Fore.WHITE + f"Total Staff    : {Fore.YELLOW}{userCount}")
    print(Fore.WHITE + f"Total Bookings : {Fore.YELLOW}{guest_count}")
    print(Fore.WHITE + f"Revenue        : {Fore.GREEN}{sum([int(guest_data[i][7]) for i in range(guest_count)])}")
    element("-")
    input(Fore.YELLOW + "Press Enter..." + Fore.RESET)

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
        clear()
        header("RECEPTIONIST DASHBOARD")
        print(Fore.WHITE + f"[1] {Fore.YELLOW}Available Rooms")
        print(Fore.WHITE + f"[2] {Fore.YELLOW}Register Entry (Book)")
        print(Fore.WHITE + f"[3] {Fore.YELLOW}Guest Checkout & Bill")
        print(Fore.WHITE + f"[4] {Fore.YELLOW}View Bookings")
        print(Fore.RED   + f"[0] Logout")
        
        opt = input(Fore.CYAN + "Option: " + Fore.RESET)
        if opt == '1': viewAvailableRooms()
        elif opt == '2': addNewBooking()
        elif opt == '3': checkOut()
        elif opt == '4': viewBooking()
        elif opt == '0': return

def viewAvailableRooms():
    header("AVAILABLE ROOMS")
    print(Fore.CYAN + f"{'ROOM NO':<10} {'TYPE':<20} {'PRICE'}")
    element("-")
    occupied = [guest_data[k][2] for k in range(guest_count) if guest_data[k][4] == "Active"]
    for i in range(roomCount):
        if hotelData[i][0] not in occupied:
            print(Fore.WHITE + f"{hotelData[i][0]:<10} {hotelData[i][1]:<20} {hotelData[i][2]}")
    element("-")
    input(Fore.YELLOW + "Press Enter..." + Fore.RESET)


def checkOut():
    # Reuse the robust checkout logic from Admin
    # But first we might want to support Room Number search?
    # For now, let's just alias it since checkOutGuest lists active guests anyway.
    checkOutGuest()

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
        clear()
        header("MANAGER DASHBOARD")
        print(Fore.WHITE + f"[1] {Fore.YELLOW}View Rooms")
        print(Fore.WHITE + f"[2] {Fore.YELLOW}View Bookings")
        print(Fore.WHITE + f"[3] {Fore.YELLOW}Billing Reports")
        print(Fore.WHITE + f"[4] {Fore.YELLOW}Staff Attendance")
        print(Fore.WHITE + f"[5] {Fore.YELLOW}System Stats")
        print(Fore.WHITE + f"[6] {Fore.YELLOW}Worker Duties (Tasks)")
        print(Fore.RED   + f"[0] Logout")
        
        opt = input(Fore.CYAN + "Option: " + Fore.RESET)
        if opt == '1': viewAllRooms() # Reuse
        elif opt == '2': viewBooking() # Reuse
        elif opt == '3': viewBillingReport() # Reuse
        elif opt == '4': viewAttendanceReport() # Reuse
        elif opt == '5': viewSystemStats() # Reuse from Admin
        elif opt == '6': workerDuties() # Reuse from Admin
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
        clear()
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




def header(name=None):
    if name is None or name == "Hostel Management System": 
        name = hotel_config.get("name", "Luxe Stay")

    print(Fore.CYAN + "=" * 55)
    print(Fore.YELLOW + Style.BRIGHT + f"{name:^55}")
    print(Fore.CYAN + "=" * 55)

def element(dash):
    print(Fore.CYAN + dash * 55)

# --- MAIN ---



def main():
    load_data()
    set_console_size()
    while True:
        clear()
        header()
        print(Fore.GREEN + "\nWelcome! Please select your role to access the system\n")
        print(Fore.CYAN + "-" * 55)
        print(Fore.WHITE + f"[{Fore.MAGENTA}1{Fore.WHITE}] ADMINISTRATOR{space:<10} [{Fore.MAGENTA}2{Fore.WHITE}] RECEPTIONIST")
        print(Fore.WHITE + f"[{Fore.MAGENTA}3{Fore.WHITE}] MANAGER{space:<16} [{Fore.MAGENTA}4{Fore.WHITE}] WORKER / STAFF")
        print(Fore.RED + f"[5] Exit")
        print(Fore.CYAN + "-"*55)
        
        try:
            option_str = input(Fore.YELLOW + "Enter the Option (1-to-5): " + Fore.RESET)
            if not option_str.isdigit(): continue
            option = int(option_str)
            
            if option == 1: administratorlogin()
            elif option == 2: receptionist()
            elif option == 3: manager()
            elif option == 4: worker()
            elif option == 5:
                save_data()
                print(Fore.RED + "Goodbye!")
                return
            else:
                print(Fore.RED + "Invalid Option")
                input("Press Enter...")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            input("Press Enter...")

if __name__ == "__main__":
    main()
else:
    load_data()
