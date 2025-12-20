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
        if username == "admin" and password == 1122:
            administratordashoard()
            break
        else:
            attempts = attempts-1
            if attempts == 0:
                print("No More Attempts Left")
                break
            else:
                print(f"Invalid Credention! Try Agian\n Remaining Attempts: {attempts}")
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
            break
        else:
            print("Invalid Option")

print(main())


