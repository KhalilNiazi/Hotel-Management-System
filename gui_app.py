
import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
import main as backend
import datetime

# --- THEME CONFIG ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Brand Colors matching Web
COLOR_BG = "#050505"       
COLOR_SURFACE = "#121212"  
COLOR_GOLD = "#d4af37"     
COLOR_GOLD_HOVER = "#c5a028"
COLOR_TEXT = "#ffffff"
COLOR_TEXT_MUTED = "#a1a1aa"

backend.load_data()

class HotelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Luxe Stay | Admin Suite")
        self.root.geometry("1000x700")
        self.root.configure(fg_color=COLOR_BG)
        
        self.current_user = None
        self.current_role = None
        
        self.create_auth_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- AUTH ---
    def create_auth_screen(self):
        self.clear_screen()
        
        card = ctk.CTkFrame(self.root, fg_color=COLOR_SURFACE, corner_radius=20, border_width=1, border_color="#333", width=500, height=450)
        card.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(card, text="♦ Luxe Stay", font=("Times New Roman", 32, "bold"), text_color=COLOR_GOLD).place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(card, text="PREMIUM HOTEL MANAGEMENT SYSTEM", font=("Arial", 10), text_color=COLOR_TEXT_MUTED).place(relx=0.5, rely=0.28, anchor="center")
        
        grid_frame = ctk.CTkFrame(card, fg_color="transparent", width=400, height=200)
        grid_frame.place(relx=0.5, rely=0.6, anchor="center")
        
        btn_config = {
            "font": ("Arial", 13, "bold"), "fg_color": "transparent", 
            "border_width": 1, "border_color": "#444", "text_color": "#fff", 
            "hover_color": "#222", "height": 50, "corner_radius": 8, "width": 190
        }
        
        ctk.CTkButton(grid_frame, text="Administrator", command=lambda: self.login_form("Admin"), **btn_config).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(grid_frame, text="Receptionist", command=lambda: self.login_form("Receptionist"), **btn_config).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(grid_frame, text="Manager", command=lambda: self.login_form("Manager"), **btn_config).grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkButton(grid_frame, text="Staff / Worker", command=lambda: self.login_form("Worker"), **btn_config).grid(row=1, column=1, padx=5, pady=5)
        
        ctk.CTkButton(card, text="Exit Application", fg_color="transparent", text_color="#ef4444", hover_color="#330000", command=self.root.quit).place(relx=0.5, rely=0.9, anchor="center")

    def login_form(self, role):
        self.clear_screen()
        card = ctk.CTkFrame(self.root, fg_color=COLOR_SURFACE, corner_radius=20, border_width=1, border_color=COLOR_GOLD, width=400, height=500)
        card.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(card, text="♦ Luxe Stay", font=("Times New Roman", 24), text_color=COLOR_GOLD).place(relx=0.5, rely=0.15, anchor="center")
        ctk.CTkLabel(card, text=f"{role} Portal Login", font=("Arial", 12), text_color=COLOR_TEXT_MUTED).place(relx=0.5, rely=0.22, anchor="center")
        
        ctk.CTkLabel(card, text="IDENTITY", font=("Arial", 10, "bold"), text_color=COLOR_TEXT_MUTED).place(x=40, y=160)
        user_entry = ctk.CTkEntry(card, height=40, border_color="#333", bg_color="transparent", fg_color="#000", width=320)
        user_entry.place(x=40, y=185)
        
        ctk.CTkLabel(card, text="CREDENTIAL", font=("Arial", 10, "bold"), text_color=COLOR_TEXT_MUTED).place(x=40, y=240)
        pass_entry = ctk.CTkEntry(card, show="*", height=40, border_color="#333", bg_color="transparent", fg_color="#000", width=320)
        pass_entry.place(x=40, y=265)
        
        def attempt():
            u = user_entry.get()
            p = pass_entry.get()
            valid = False
            for i in range(backend.userCount):
                if backend.userData[i][1] == u and backend.userData[i][2] == p:
                    u_role = backend.userData[i][3]
                    if u_role == role or u_role == "Admin": # Admin override
                        valid = True
            
            if valid:
                self.current_user = u
                self.current_role = role
                self.load_dashboard()
            else:
                messagebox.showerror("Access Denied", "Invalid Credentials")

        ctk.CTkButton(card, text="AUTHENTICATE", fg_color=COLOR_GOLD, text_color="#000", hover_color=COLOR_GOLD_HOVER, height=45, font=("Arial", 12, "bold"), width=320, command=attempt).place(x=40, y=360)
        ctk.CTkButton(card, text="← Return", fg_color="transparent", text_color=COLOR_TEXT, hover_color="#222", command=self.create_auth_screen).place(relx=0.5, rely=0.9, anchor="center")

    # --- MAIN DASHBOARD ---
    def load_dashboard(self):
        self.clear_screen()
        
        # Sidebar
        sidebar = ctk.CTkFrame(self.root, width=240, corner_radius=0, fg_color=COLOR_SURFACE)
        sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(sidebar, text="♦ Luxe Stay", font=("Times New Roman", 20), text_color=COLOR_GOLD).pack(pady=40)
        ctk.CTkLabel(sidebar, text=f"Welcome, {self.current_user}", font=("Arial", 12, "bold"), text_color="#fff").pack(pady=(0,5))
        ctk.CTkLabel(sidebar, text=self.current_role.upper(), font=("Arial", 10), text_color=COLOR_TEXT_MUTED).pack(pady=(0,30))
        
        self.btn_map = {} # To toggle active state
        
        def nav(txt, func):
            btn = ctk.CTkButton(sidebar, text=txt, fg_color="transparent", text_color="#ccc", hover_color="#222", anchor="w", command=func, height=40)
            btn.pack(fill="x", pady=2, padx=10)
            self.btn_map[txt] = btn

        # Role-Based Menu
        if self.current_role in ["Admin", "Manager"]:
            nav("Dashboard", lambda: self.show_view("Stats"))
        
        if self.current_role in ["Admin", "Receptionist", "Manager"]:
            nav("Rooms", lambda: self.show_view("Rooms"))
            nav("Guests / Bookings", lambda: self.show_view("Guests"))

        if self.current_role in ["Admin", "Manager"]:
            nav("Staff", lambda: self.show_view("Staff"))
            nav("Tasks", lambda: self.show_view("Tasks"))
            nav("Financials", lambda: self.show_view("Reports"))
        
        if self.current_role == "Worker":
            nav("My Tasks", lambda: self.show_view("MyTasks"))
            nav("Mark Attendance", lambda: self.show_view("MarkAttendance"))
            
        nav("Logout", self.create_auth_screen)
        
        # Main Area
        self.main_area = ctk.CTkFrame(self.root, fg_color=COLOR_BG, corner_radius=0)
        self.main_area.pack(side="right", fill="both", expand=True)
        
        # Default View
        start_view = "Stats" if self.current_role == "Admin" else "Guests" if self.current_role == "Receptionist" else "MyTasks"
        self.show_view(start_view)

    def show_view(self, view_name):
        for w in self.main_area.winfo_children(): w.destroy()
        
        # Title
        header = ctk.CTkFrame(self.main_area, fg_color="transparent", height=60)
        header.pack(fill="x", padx=30, pady=20)
        ctk.CTkLabel(header, text=view_name.upper(), font=("Playfair Display", 28), text_color=COLOR_GOLD).pack(side="left")
        
        content = ctk.CTkFrame(self.main_area, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=30, pady=(0, 20))
        
        if view_name == "Stats": self.render_stats(content)
        elif view_name == "Rooms": self.render_rooms(content)
        elif view_name == "Staff": self.render_staff(content)
        elif view_name == "Guests": self.render_guests(content)
        elif view_name == "Tasks": self.render_tasks(content)
        elif view_name == "MyTasks": self.render_my_tasks(content)
        elif view_name == "MarkAttendance": self.render_attendance(content)
        elif view_name == "Reports": self.render_reports(content)

    # --- VIEWS ---

    def render_stats(self, parent):
        grid = ctk.CTkFrame(parent, fg_color="transparent")
        grid.pack(fill="x")
        
        # Metrics
        rev = 0
        for i in range(backend.guest_count):
            if backend.guest_data[i][4] == "CheckedOut": rev += backend.guest_data[i][7]
        
        # Occupied
        occ = 0
        for i in range(backend.guest_count):
            if backend.guest_data[i][4] == "Active": occ += 1
            
        def card(t, v):
            f = ctk.CTkFrame(grid, fg_color=COLOR_SURFACE, border_width=1, border_color="#333", height=100)
            f.pack(side="left", fill="x", expand=True, padx=5)
            ctk.CTkLabel(f, text=t, text_color=COLOR_TEXT_MUTED, font=("Arial", 11)).pack(pady=(15,0))
            ctk.CTkLabel(f, text=str(v), font=("Times New Roman", 24), text_color=COLOR_GOLD).pack()

        card("REVENUE", f"Rs. {rev}")
        card("OCCUPANCY", f"{occ} / {backend.roomCount}")
        card("STAFF", str(backend.userCount))

    def render_rooms(self, parent):
        # Actions
        controls = ctk.CTkFrame(parent, fg_color="transparent")
        controls.pack(fill="x", pady=(0,10))
        if self.current_role == "Admin":
            ctk.CTkButton(controls, text="+ ADD ROOM", fg_color=COLOR_GOLD, text_color="black", width=100, command=self.modal_add_room).pack(side="right")
        
        # List
        sf = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sf.pack(fill="both", expand=True)
        
        # Header
        h = ctk.CTkFrame(sf, fg_color="#222", height=30)
        h.pack(fill="x")
        ctk.CTkLabel(h, text="ROOM NO", width=100, anchor="w").pack(side="left", padx=10)
        ctk.CTkLabel(h, text="TYPE", width=100, anchor="w").pack(side="left", padx=10)
        ctk.CTkLabel(h, text="PRICE", width=100, anchor="w").pack(side="left", padx=10)
        
        for i in range(backend.roomCount):
            r = backend.hotelData[i]
            row = ctk.CTkFrame(sf, fg_color=COLOR_SURFACE)
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(row, text=str(r[0]), width=100, anchor="w", font=("Arial", 12, "bold")).pack(side="left", padx=10)
            ctk.CTkLabel(row, text=r[1], width=100, anchor="w").pack(side="left", padx=10)
            ctk.CTkLabel(row, text=f"{r[2]}", width=100, anchor="w", text_color=COLOR_GOLD).pack(side="left", padx=10)
            # Delete Button
            if self.current_role == "Admin":
                ctk.CTkButton(row, text="DEL", width=40, fg_color="#ef4444", command=lambda idx=i: self.delete_room(idx)).pack(side="right", padx=10, pady=5)

    def delete_room(self, idx):
        if messagebox.askyesno("Confirm", "Delete this room?"):
             # Shift logic (quick hack: set to last and reduce count to avoid list shift loops for GUI)
             # Better: rebuild list.
             # Actually backend uses array replacement logic.
             # Simple removal:
             for j in range(idx, backend.roomCount - 1):
                backend.hotelData[j] = backend.hotelData[j+1][:]
             backend.roomCount -= 1
             backend.save_data()
             self.show_view("Rooms")

    def modal_add_room(self):
        d = ctk.CTkToplevel(self.root)
        d.geometry("300x300")
        d.title("Add Room")
        ctk.CTkLabel(d, text="Room No").pack(pady=5)
        e1 = ctk.CTkEntry(d); e1.pack(pady=5)
        ctk.CTkLabel(d, text="Type (S/D/T/ST)").pack(pady=5)
        e2 = ctk.CTkEntry(d); e2.pack(pady=5)
        ctk.CTkLabel(d, text="Price").pack(pady=5)
        e3 = ctk.CTkEntry(d); e3.pack(pady=5)
        
        def save():
            try:
                rn = int(e1.get())
                rt = e2.get().upper()
                rp = int(e3.get())
                # Add
                backend.hotelData[backend.roomCount] = [rn, rt, rp]
                backend.roomCount += 1
                backend.save_data()
                d.destroy()
                self.show_view("Rooms")
            except: messagebox.showerror("Error", "Invalid Input")
            
        ctk.CTkButton(d, text="Save", command=save, fg_color=COLOR_GOLD, text_color="black").pack(pady=20)

    def render_staff(self, parent):
        controls = ctk.CTkFrame(parent, fg_color="transparent")
        controls.pack(fill="x", pady=(0,10))
        ctk.CTkButton(controls, text="+ ADD STAFF", fg_color=COLOR_GOLD, text_color="black", width=100, command=self.modal_add_staff).pack(side="right")
        
        sf = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sf.pack(fill="both", expand=True)
        
        for i in range(backend.userCount):
            u = backend.userData[i]
            row = ctk.CTkFrame(sf, fg_color=COLOR_SURFACE)
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(row, text=u[1], width=150, anchor="w", font=("Arial", 12, "bold")).pack(side="left", padx=10)
            ctk.CTkLabel(row, text=u[3], width=100, anchor="w", text_color=COLOR_TEXT_MUTED).pack(side="left", padx=10)
            ctk.CTkLabel(row, text=f"Salary: {u[4] if len(u)>4 else 0}", width=100, anchor="w").pack(side="left", padx=10)

    def modal_add_staff(self):
        d = ctk.CTkToplevel(self.root)
        d.geometry("300x400")
        d.title("Add Staff")
        
        def entry(lbl): ctk.CTkLabel(d, text=lbl).pack(pady=2); e=ctk.CTkEntry(d); e.pack(pady=2); return e
        e_user = entry("Username")
        e_pass = entry("Password")
        e_role = entry("Role (Admin/Manager/Receptionist/Worker)")
        e_sal = entry("Salary")
        
        def save():
            backend.userData[backend.userCount] = [backend.userCount, e_user.get(), e_pass.get(), e_role.get(), e_sal.get()]
            backend.userCount += 1
            backend.save_data()
            d.destroy()
            self.show_view("Staff")
            
        ctk.CTkButton(d, text="Save", command=save, fg_color=COLOR_GOLD, text_color="black").pack(pady=20)

    def render_guests(self, parent):
        controls = ctk.CTkFrame(parent, fg_color="transparent")
        controls.pack(fill="x", pady=(0,10))
        ctk.CTkButton(controls, text="+ New Booking", fg_color=COLOR_GOLD, text_color="black", width=100, command=self.modal_booking).pack(side="right")
        
        sf = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sf.pack(fill="both", expand=True)
        
        # Header
        h = ctk.CTkFrame(sf, fg_color="#222", height=30)
        h.pack(fill="x")
        cols = ["Name", "Room", "Status", "Action"]
        for c in cols: ctk.CTkLabel(h, text=c, width=120, anchor="w").pack(side="left", padx=5)

        for i in range(backend.guest_count):
            g = backend.guest_data[i]
            # Show Active Only mostly, or all? Let's show all but sort active first
            if g[4] == "Active":
                row = ctk.CTkFrame(sf, fg_color="#1a1a1a", border_width=1, border_color="#333")
                row.pack(fill="x", pady=2)
                ctk.CTkLabel(row, text=g[1], width=120, anchor="w").pack(side="left", padx=5)
                ctk.CTkLabel(row, text=str(g[2]), width=120, anchor="w", text_color=COLOR_GOLD).pack(side="left", padx=5)
                ctk.CTkLabel(row, text=g[4], width=120, anchor="w", text_color="#4ade80").pack(side="left", padx=5)
                
                ctk.CTkButton(row, text="Check Out", width=80, fg_color="#333", command=lambda idx=i: self.checkout(idx)).pack(side="left", padx=5, pady=5)

    def modal_booking(self):
        d = ctk.CTkToplevel(self.root)
        d.geometry("400x500"); d.title("New Booking")
        
        ctk.CTkLabel(d, text="Guest Name").pack(pady=5); name = ctk.CTkEntry(d); name.pack()
        ctk.CTkLabel(d, text="Phone").pack(pady=5); phone = ctk.CTkEntry(d); phone.pack()
        ctk.CTkLabel(d, text="Room No (Check Availability First)").pack(pady=5); rno = ctk.CTkEntry(d); rno.pack()
        
        def save():
            try:
                rid = int(rno.get())
                # validate
                available = True
                for i in range(backend.guest_count):
                    if backend.guest_data[i][2] == rid and backend.guest_data[i][4] == "Active": available = False
                
                if not available:
                    messagebox.showerror("Error", "Room Occupied!")
                    return
                
                backend.guest_data[backend.guest_count] = [
                    backend.guest_count, name.get(), rid, phone.get(), "Active", datetime.datetime.now().strftime("%Y-%m-%d"), "", 0
                ]
                backend.guest_count += 1
                backend.save_data()
                d.destroy(); self.show_view("Guests")
            except: messagebox.showerror("Err", "Invalid Input")

        ctk.CTkButton(d, text="Confirm Booking", command=save, fg_color=COLOR_GOLD, text_color="black").pack(pady=20)

    def checkout(self, idx):
        # Calculate Bill (Simple days * price)
        g = backend.guest_data[idx]
        rid = g[2]
        price = 0
        for i in range(backend.roomCount):
            if backend.hotelData[i][0] == rid: price = backend.hotelData[i][2]
        
        # Assume 1 day for demo if dates complex
        bill = price 
        
        if messagebox.askyesno("Confirm CheckOut", f"Guest: {g[1]}\nRoom: {rid}\nTotal Bill: {bill}"):
            backend.guest_data[idx][4] = "CheckedOut"
            backend.guest_data[idx][6] = datetime.datetime.now().strftime("%Y-%m-%d")
            backend.guest_data[idx][7] = bill
            backend.save_data()
            self.show_view("Guests")

    def render_tasks(self, parent):
        controls = ctk.CTkFrame(parent, fg_color="transparent")
        controls.pack(fill="x", pady=(0,10))
        ctk.CTkButton(controls, text="Assign Task", fg_color=COLOR_GOLD, text_color="black", width=120, command=self.modal_assign).pack(side="right")
        
        sf = ctk.CTkScrollableFrame(parent)
        sf.pack(fill="both", expand=True)
        
        for i in range(backend.taskCount):
            t = backend.assignTask[i]
            row = ctk.CTkFrame(sf, fg_color=COLOR_SURFACE)
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(row, text=t[1], width=100, anchor="w").pack(side="left", padx=10) # Staff
            ctk.CTkLabel(row, text=t[2], width=200, anchor="w").pack(side="left", padx=10) # Desc
            ctk.CTkLabel(row, text=t[3], width=100, anchor="w", text_color="#fbbf24").pack(side="left", padx=10)

    def modal_assign(self):
        d = ctk.CTkToplevel(self.root); d.geometry("300x300")
        ctk.CTkLabel(d, text="Staff Name").pack(); s=ctk.CTkEntry(d); s.pack()
        ctk.CTkLabel(d, text="Task Description").pack(); desc=ctk.CTkEntry(d); desc.pack()
        
        def save():
            backend.assignTask[backend.taskCount] = [backend.taskCount, s.get(), desc.get(), "Pending"]
            backend.taskCount += 1; backend.save_data(); d.destroy(); self.show_view("Tasks")
        ctk.CTkButton(d, text="Assign", command=save).pack(pady=20)

    def render_my_tasks(self, parent):
        sf = ctk.CTkScrollableFrame(parent)
        sf.pack(fill="both", expand=True)
        ctk.CTkLabel(sf, text="My Pending Tasks", font=("Arial", 16)).pack(pady=10)
        
        for i in range(backend.taskCount):
            t = backend.assignTask[i]
            if t[1] == self.current_user and t[3] == "Pending":
                row = ctk.CTkFrame(sf, fg_color="#222")
                row.pack(fill="x", pady=5)
                ctk.CTkLabel(row, text=t[2]).pack(side="left", padx=20)
                ctk.CTkButton(row, text="Done", width=60, command=lambda idx=i: self.complete_task(idx)).pack(side="right", padx=10)

    def complete_task(self, idx):
        backend.assignTask[idx][3] = "Completed"
        backend.save_data()
        self.show_view("MyTasks")

    def render_attendance(self, parent):
        def mark(type):
            backend.attendanceData[backend.attendance_count] = [
                backend.attendance_count, self.current_user, datetime.datetime.now().strftime("%Y-%m-%d"),
                type, datetime.datetime.now().strftime("%H:%M"), ""
            ]
            backend.attendance_count += 1
            backend.save_data()
            messagebox.showinfo("Success", f"Marked {type}")
            
        ctk.CTkButton(parent, text="CLOCK IN", font=("Arial", 18), height=60, command=lambda: mark("In")).pack(fill="x", padx=100, pady=20)
        ctk.CTkButton(parent, text="CLOCK OUT", font=("Arial", 18), height=60, fg_color="#ef4444", command=lambda: mark("Out")).pack(fill="x", padx=100, pady=20)

    def render_reports(self, parent):
        sf = ctk.CTkScrollableFrame(parent)
        sf.pack(fill="both", expand=True)
        
        ctk.CTkLabel(sf, text="Financial Report", font=("Times", 20)).pack(pady=10)
        total = 0
        for i in range(backend.guest_count):
            if backend.guest_data[i][4] == "CheckedOut":
                amt = backend.guest_data[i][7]
                ctk.CTkLabel(sf, text=f"{backend.guest_data[i][1]} - Rs. {amt}").pack()
                total += amt
        
        ctk.CTkLabel(sf, text="-"*30).pack(pady=10)
        ctk.CTkLabel(sf, text=f"TOTAL REVENUE: Rs. {total}", font=("Arial", 16, "bold"), text_color=COLOR_GOLD).pack()

if __name__ == "__main__":
    app = ctk.CTk()
    gui = HotelGUI(app)
    app.mainloop()
