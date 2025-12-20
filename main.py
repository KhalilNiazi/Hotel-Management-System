space = " "
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
        username = input("Enter UserName: ")
        password = input("Enter Password: ")
        
        if username == "admin" and password == "1122":
            administratordashboard()
        else:
            attempts = attempts-1
            if attempts == 0:
                print("No More Attempts Left")
                break
            else:
                print(f"Invalid Credention! Try Agian\n Remaining Attempts: {attempts}")
def administratordashboard():
    header("ADMINISTRATOR DASHBOARD")
    print("\n")
    element("-")
    print(f"{'Option':<6} Function")
    print(f"{'[1]':<3} Add Rooms")
    print(f"{'[2]':<3} View All Rooms")
    print(f"{'[3]':<3} Manage Staff")
    print(f"{'[4]':<3} Worder Duties")
    print(f"{'[5]':<3} View Booking")
    print(f"{'[6]':<3} Financials")
    print(f"{'[7]':<3} Attendence")
    print(f"{'[8]':<3} System Stats")
    element("-")
    print(f"{'[0]':<3} Logout")
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
        if (option == 1):
            administratorlogin()
        elif (option == 2):
            receptionist()
        elif (option == 3):
            manager()
        elif (option == 4):
            worker()
        elif (option == 5):
            print("[System Shutting Down... Goodbye!]")
            1
        else:
            print("Invalid Option")

print(main())


