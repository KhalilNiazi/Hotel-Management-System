
import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
import main as backend

# --- THEME CONFIG ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Brand Colors matching Web
COLOR_BG = "#050505"       # Deep Black content background
COLOR_SURFACE = "#121212"  # Card background
COLOR_GOLD = "#d4af37"     # Gold Text/Accent
COLOR_GOLD_HOVER = "#c5a028"
COLOR_TEXT = "#ffffff"
COLOR_TEXT_MUTED = "#a1a1aa"

backend.load_data()

class HotelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Luxe Stay | Admin Suite")
        self.root.geometry("900x600")
        self.root.configure(fg_color=COLOR_BG)
        
        # Load fonts if possible (CustomTkinter uses standard fonts but we can spec names)
        # We'll use Times for Serif-like headings and Roboto/Arial for sans
        self.font_head = ("Times New Roman", 32, "bold") 
        self.font_sub = ("Arial", 12)
        self.font_btn = ("Arial", 13, "bold")
        
        self.create_auth_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- AUTH / ROLE SELECTION ---
    def create_auth_screen(self):
        self.clear_screen()
        
        # Central Card
        card = ctk.CTkFrame(self.root, fg_color=COLOR_SURFACE, corner_radius=20, border_width=1, border_color="#333")
        card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=450)
        
        # Logo Area
        # We can't easily do ionicons in tkinter without images, so we use text
        ctk.CTkLabel(card, text="♦ Luxe Stay", font=self.font_head, text_color=COLOR_GOLD).pack(pady=(40, 5))
        ctk.CTkLabel(card, text="PREMIUM HOTEL MANAGEMENT SYSTEM", font=("Arial", 10), text_color=COLOR_TEXT_MUTED).pack(pady=(0, 40))
        
        # Grid of roles
        # Grid Frame
        grid_frame = ctk.CTkFrame(card, fg_color="transparent")
        grid_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        btn_config = {
            "font": self.font_btn, 
            "fg_color": "transparent", 
            "border_width": 1, 
            "border_color": "#444", 
            "text_color": "#fff", 
            "hover_color": "#222", 
            "height": 50,
            "corner_radius": 8
        }
        
        # Buttons
        ctk.CTkButton(grid_frame, text="Administrator", command=lambda: self.login_form("Admin"), **btn_config).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(grid_frame, text="Receptionist", command=lambda: self.login_form("Receptionist"), **btn_config).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(grid_frame, text="Manager", command=lambda: self.login_form("Manager"), **btn_config).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(grid_frame, text="Staff / Worker", command=lambda: self.login_form("Worker"), **btn_config).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        
        # Exit
        ctk.CTkButton(card, text="Exit Application", fg_color="transparent", text_color="#ef4444", hover_color="#330000", command=self.root.quit).pack(pady=20)

    def login_form(self, role):
        self.clear_screen()
        
        # Central Card
        card = ctk.CTkFrame(self.root, fg_color=COLOR_SURFACE, corner_radius=20, border_width=1, border_color=COLOR_GOLD)
        card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)
        
        # Header
        ctk.CTkLabel(card, text="♦ Luxe Stay", font=("Times New Roman", 24), text_color=COLOR_GOLD).pack(pady=(40, 5))
        ctk.CTkLabel(card, text=f"{role} Portal Login", font=("Arial", 12), text_color=COLOR_TEXT_MUTED).pack(pady=(0, 40))
        
        # Inputs
        ctk.CTkLabel(card, text="IDENTITY", font=("Arial", 10, "bold"), text_color=COLOR_TEXT_MUTED, anchor="w").pack(fill="x", padx=40)
        user_entry = ctk.CTkEntry(card, height=40, border_color="#333", bg_color="transparent", fg_color="#000")
        user_entry.pack(fill="x", padx=40, pady=(5, 20))
        
        ctk.CTkLabel(card, text="CREDENTIAL", font=("Arial", 10, "bold"), text_color=COLOR_TEXT_MUTED, anchor="w").pack(fill="x", padx=40)
        pass_entry = ctk.CTkEntry(card, show="*", height=40, border_color="#333", bg_color="transparent", fg_color="#000")
        pass_entry.pack(fill="x", padx=40, pady=(5, 30))
        
        # Auth Function
        def attempt():
            u = user_entry.get()
            p = pass_entry.get()
            valid = False
            for i in range(backend.userCount):
                if backend.userData[i][1] == u and backend.userData[i][2] == p:
                    # Role Check (Simplified: Admin allows all, else exact match)
                    u_role = backend.userData[i][3]
                    if u_role == role or u_role == "Admin":
                        valid = True
            
            if valid:
                self.load_dashboard(role, u)
            else:
                self.show_error("Access Denied", "Invalid Credentials")

        # Action Buttons
        ctk.CTkButton(card, text="AUTHENTICATE", fg_color=COLOR_GOLD, text_color="#000", hover_color=COLOR_GOLD_HOVER, height=45, font=("Arial", 12, "bold"), command=attempt).pack(fill="x", padx=40)
        
        ctk.CTkButton(card, text="← Return", fg_color="transparent", text_color=COLOR_TEXT, hover_color="#222", command=self.create_auth_screen).pack(pady=15)

    def show_error(self, title, msg):
        # Custom modal or simple messagebox
        messagebox.showerror(title, msg)

    # --- DASHBOARD (Generic for GUI) ---
    def load_dashboard(self, role, username):
        self.clear_screen()
        
        # Sidebar
        sidebar = ctk.CTkFrame(self.root, width=240, corner_radius=0, fg_color=COLOR_SURFACE)
        sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(sidebar, text="♦ Luxe Stay", font=("Times New Roman", 20), text_color=COLOR_GOLD).pack(pady=40)
        
        ctk.CTkLabel(sidebar, text=f"Welcome, {username}", font=("Arial", 12, "bold"), text_color="#fff").pack(pady=(0,5))
        ctk.CTkLabel(sidebar, text=role, font=("Arial", 10), text_color=COLOR_TEXT_MUTED).pack(pady=(0,30))
        
        # Menu Helper
        def menu_btn(txt, cmd):
            ctk.CTkButton(sidebar, text=txt, fg_color="transparent", text_color="#ccc", hover_color="#222", anchor="w", command=cmd).pack(fill="x", pady=2, padx=10)
            
        if role == "Admin":
            menu_btn("Dashboard", lambda: self.show_view("Stats"))
            menu_btn("Manage Rooms", lambda: self.show_view("Rooms"))
            menu_btn("Manage Staff", lambda: self.show_view("Staff"))
            menu_btn("Settings", lambda: self.show_view("Settings"))

        if role == "Receptionist":
             menu_btn("New Booking", lambda: self.show_view("Booking"))
             menu_btn("View Rooms", lambda: self.show_view("Rooms"))
             menu_btn("Check Out", lambda: self.show_view("CheckOut"))
             
        menu_btn("Logout", self.create_auth_screen)
        
        # Main Area
        self.main_area = ctk.CTkFrame(self.root, fg_color="#111", corner_radius=0)
        self.main_area.pack(side="right", fill="both", expand=True)
        
        self.show_view("Default")

    def show_view(self, view_name):
        # Clear main area
        for w in self.main_area.winfo_children(): w.destroy()
        
        # Header
        ctk.CTkLabel(self.main_area, text=view_name.upper(), font=("Arial", 24, "bold"), text_color=COLOR_TEXT).pack(anchor="w", padx=30, pady=30)
        
        content = ctk.CTkFrame(self.main_area, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=30)

        if view_name == "Rooms":
            self.render_rooms(content)
        elif view_name == "Staff":
            self.render_staff(content)
        elif view_name == "Stats":
            self.render_stats(content)
        else:
            ctk.CTkLabel(content, text="Select an option from the sidebar.").pack()

    def render_rooms(self, parent):
        # Scrollable list
        sf = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sf.pack(fill="both", expand=True)
        
        for i in range(backend.roomCount):
            r = backend.hotelData[i]
            # Card for Room
            row = ctk.CTkFrame(sf, fg_color="#222")
            row.pack(fill="x", pady=5)
            ctk.CTkLabel(row, text=f"Room {r[0]} ({r[1]})", font=("Arial", 14, "bold")).pack(side="left", padx=10, pady=10)
            ctk.CTkLabel(row, text=f"Rs.{r[2]}", text_color=COLOR_GOLD).pack(side="right", padx=10)

    def render_staff(self, parent):
        sf = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sf.pack(fill="both", expand=True)
        for i in range(backend.userCount):
            u = backend.userData[i]
            row = ctk.CTkFrame(sf, fg_color="#222")
            row.pack(fill="x", pady=5)
            ctk.CTkLabel(row, text=f"{u[1]}", font=("Arial", 14, "bold")).pack(side="left", padx=10, pady=10)
            ctk.CTkLabel(row, text=f"{u[3]}").pack(side="right", padx=10)

    def render_stats(self, parent):
        # Stats Cards
        grid = ctk.CTkFrame(parent, fg_color="transparent")
        grid.pack(fill="x")
        
        def stat_card(title, value, col):
            f = ctk.CTkFrame(grid, fg_color="#222", border_width=1, border_color="#333")
            f.pack(side="left", fill="both", expand=True, padx=5)
            ctk.CTkLabel(f, text=title, text_color=COLOR_TEXT_MUTED).pack(pady=(15,0))
            ctk.CTkLabel(f, text=value, font=("Times New Roman", 24), text_color=COLOR_GOLD).pack(pady=(5,15))
            
        stat_card("Total Guests", str(backend.guest_count), 0)
        stat_card("Total Rooms", str(backend.roomCount), 1)

if __name__ == "__main__":
    app = ctk.CTk()
    gui = HotelGUI(app)
    app.mainloop()
