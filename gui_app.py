import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import main as backend

# Ensure data is loaded
backend.load_data()

class HotelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("600x500")
        
        self.create_main_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Hotel Management System", font=("Arial", 20, "bold")).pack(pady=20)
        
        tk.Button(self.root, text="Administrator", command=self.admin_login, width=30, height=2).pack(pady=10)
        tk.Button(self.root, text="Receptionist", command=self.receptionist_login, width=30, height=2).pack(pady=10)
        tk.Button(self.root, text="Manager", command=self.manager_login, width=30, height=2).pack(pady=10)
        tk.Button(self.root, text="Worker", command=self.worker_login, width=30, height=2).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=30, height=2, bg="#ffdddd").pack(pady=10)

    # --- LOGIN SCREENS ---
    
    def admin_login(self):
        self.login_screen("Admin", self.admin_dashboard)

    def receptionist_login(self):
        self.login_screen("Receptionist", self.receptionist_dashboard)

    def manager_login(self):
        self.login_screen("Manager", self.manager_dashboard)
        
    def worker_login(self):
        self.login_screen("Worker", self.worker_dashboard)

    def login_screen(self, role, success_callback):
        self.clear_screen()
        tk.Label(self.root, text=f"{role} Login", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Username").pack()
        user_entry = tk.Entry(self.root)
        user_entry.pack()
        
        tk.Label(self.root, text="Password").pack()
        pass_entry = tk.Entry(self.root, show="*")
        pass_entry.pack()
        
        def attempt_login():
            username = user_entry.get()
            password = pass_entry.get()
            
            # Validation Logic using backend data
            valid = False
            found_role = ""
            for i in range(backend.userCount):
                if backend.userData[i][1] == username and backend.userData[i][2] == password:
                     found_role = backend.userData[i][3]
                     # Admin can access everything, else exact match
                     if role == "Admin" and found_role == "Admin": valid = True
                     elif role == "Receptionist" and found_role in ["Receptionist", "Admin"]: valid = True
                     elif role == "Manager" and found_role in ["Manager", "Admin"]: valid = True
                     elif role == "Worker" and found_role in ["Worker", "Admin"]: valid = True
            
            if valid:
                if role == "Worker": success_callback(username)
                else: success_callback()
            else:
                messagebox.showerror("Error", "Invalid Credentials")

        tk.Button(self.root, text="Login", command=attempt_login).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    # --- DASHBOARDS ---

    def admin_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Add Room", command=self.add_room_ui).pack(fill="x")
        tk.Button(self.root, text="View Rooms", command=self.view_rooms_ui).pack(fill="x")
        tk.Button(self.root, text="Add Staff", command=self.add_staff_ui).pack(fill="x")
        tk.Button(self.root, text="View Staff", command=self.view_staff_ui).pack(fill="x")
        tk.Button(self.root, text="Reports", command=self.view_reports_ui).pack(fill="x")
        
        tk.Button(self.root, text="Logout", command=self.create_main_menu, bg="#ffdddd").pack(pady=20)

    def receptionist_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Receptionist Dashboard", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Book Room", command=self.book_room_ui).pack(fill="x")
        tk.Button(self.root, text="Check Out", command=self.checkout_ui).pack(fill="x")
        tk.Button(self.root, text="View Rooms", command=self.view_rooms_ui).pack(fill="x")
        tk.Button(self.root, text="Logout", command=self.create_main_menu, bg="#ffdddd").pack(pady=20)

    def manager_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Manager Dashboard", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="View Rooms", command=self.view_rooms_ui).pack(fill="x")
        tk.Button(self.root, text="View Reports", command=self.view_reports_ui).pack(fill="x")
        tk.Button(self.root, text="Logout", command=self.create_main_menu, bg="#ffdddd").pack(pady=20)

    def worker_dashboard(self, username):
        self.clear_screen()
        tk.Label(self.root, text=f"Worker: {username}", font=("Arial", 16)).pack(pady=10)
        
        def mark_in():
            backend.mark_attendance(username, "In")
            messagebox.showinfo("Info", "Checked In")
        def mark_out():
            backend.mark_attendance(username, "Out")
            messagebox.showinfo("Info", "Checked Out")
            
        tk.Button(self.root, text="Check In", command=mark_in).pack(fill="x")
        tk.Button(self.root, text="Check Out", command=mark_out).pack(fill="x")
        tk.Button(self.root, text="Logout", command=self.create_main_menu, bg="#ffdddd").pack(pady=20)

    # --- FUNCTIONAL UI ---

    def add_room_ui(self):
        rno = simpledialog.askinteger("Input", "Room Number:")
        if rno:
            rtype = simpledialog.askstring("Input", "Type (S/D/T/ST):")
            rprice = simpledialog.askinteger("Input", "Price:")
            
            if rtype and rprice:
                # Add to backend
                backend.hotelData[backend.roomCount][0] = rno
                backend.hotelData[backend.roomCount][1] = rtype.upper()
                backend.hotelData[backend.roomCount][2] = rprice
                backend.roomCount += 1
                backend.save_data()
                messagebox.showinfo("Success", "Room Added")

    def view_rooms_ui(self):
        win = tk.Toplevel(self.root)
        win.title("Rooms")
        text = tk.Text(win)
        text.pack()
        text.insert(tk.END, f"{'ROOM':<10}{'TYPE':<10}{'PRICE'}\n")
        text.insert(tk.END, "-"*30 + "\n")
        for i in range(backend.roomCount):
            text.insert(tk.END, f"{backend.hotelData[i][0]:<10}{backend.hotelData[i][1]:<10}{backend.hotelData[i][2]}\n")

    def add_staff_ui(self):
        name = simpledialog.askstring("Input", "Username:")
        pwd = simpledialog.askstring("Input", "Password:")
        role = simpledialog.askstring("Input", "Role (Admin/Receptionist/Manager/Worker):")
        if name and pwd and role:
            backend.userData[backend.userCount][0] = backend.userCount
            backend.userData[backend.userCount][1] = name
            backend.userData[backend.userCount][2] = pwd
            backend.userData[backend.userCount][3] = role
            backend.userCount += 1
            backend.save_data()
            messagebox.showinfo("Success", "Staff Added")

    def view_staff_ui(self):
        win = tk.Toplevel(self.root)
        text = tk.Text(win)
        text.pack()
        for i in range(backend.userCount):
             text.insert(tk.END, f"{backend.userData[i][1]} - {backend.userData[i][3]}\n")

    def book_room_ui(self):
        name = simpledialog.askstring("Data", "Guest Name:")
        room = simpledialog.askinteger("Data", "Room No:")
        if name and room:
            # Simple booking logic replicating 'addNewBooking'
            backend.guest_data[backend.guest_count][1] = name
            backend.guest_data[backend.guest_count][2] = room
            backend.guest_data[backend.guest_count][4] = "Active"
            backend.guest_data[backend.guest_count][7] = 0
            backend.guest_count += 1
            backend.save_data()
            messagebox.showinfo("Success", "Booked")

    def checkout_ui(self):
        room = simpledialog.askinteger("Data", "Room No to Checkout:")
        days = simpledialog.askinteger("Data", "Days Stayed:")
        if room and days:
            # Find and update
            found = False
            for i in range(backend.guest_count):
                if backend.guest_data[i][2] == room and backend.guest_data[i][4] == "Active":
                     backend.guest_data[i][4] = "CheckedOut"
                     # Find price
                     price = 1000 # Default
                     for r in range(backend.roomCount):
                         if backend.hotelData[r][0] == room:
                             price = backend.hotelData[r][2]
                     bill = price * days
                     backend.guest_data[i][7] = bill
                     backend.save_data()
                     messagebox.showinfo("Bill", f"Total Bill: {bill}")
                     found = True
                     break
            if not found:
                messagebox.showerror("Error", "Booking not found")

    def view_reports_ui(self):
        win = tk.Toplevel(self.root)
        text = tk.Text(win)
        text.pack()
        text.insert(tk.END, "BILLING REPORT\n")
        total = 0
        for i in range(backend.guest_count):
             if backend.guest_data[i][4] == "CheckedOut":
                 text.insert(tk.END, f"{backend.guest_data[i][1]}: {backend.guest_data[i][7]}\n")
                 total += backend.guest_data[i][7]
        text.insert(tk.END, f"TOTAL: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelGUI(root)
    root.mainloop()
