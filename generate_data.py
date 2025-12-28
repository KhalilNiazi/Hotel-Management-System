import random
import datetime
from datetime import timedelta

# --- CONFIG ---
NUM_ROOMS = 300
NUM_GUESTS = 240 # Leaving ~60 available
NUM_WORKERS = 30
NUM_TASKS = 50
SALARY_BASE = 30000

# --- PAKISTANI NAMES ---
first_names = [
    "Muhammad", "Ahmed", "Ali", "Raza", "Hassan", "Hussain", "Bilal", "Usman", "Umar", "Zain",
    "Fatima", "Ayesha", "Zainab", "Maryam", "Sana", "Sadia", "Hina", "Khadija", "Noor", "Amna"
]
last_names = [
    "Khan", "Ahmed", "Ali", "Malik", "Chaudhry", "Sheikh", "Butt", "Raja", "Shah", "Bhatti",
    "Cheema", "Jat", "Qureshi", "Abbasi", "Mirza", "Siddiqui", "Baig", "Akram"
]

def get_pakistani_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_date(start_year=2024):
    start = datetime.datetime(start_year, 1, 1)
    end = datetime.datetime.now()
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# --- GENERATE ROOMS ---
rooms = []
for i in range(1, NUM_ROOMS + 1):
    r_type = "Single"
    price = 4000
    if i > 100: 
        r_type = "Double"
        price = 7000
    if i > 200: 
        r_type = "Triple"
        price = 10000
    if i > 280: 
        r_type = "Suite"
        price = 25000
    rooms.append(f"{i},{r_type},{price}\n")

with open("data/rooms.txt", "w") as f:
    f.writelines(rooms)

# --- GENERATE USERS ---
users = []
# 0: Admin
users.append("0,admin,1122,Admin,100000\n")
# 1-2: Receptionist
users.append("1,recept1,123,Receptionist,45000\n")
users.append("2,recept2,123,Receptionist,45000\n")
users.append("3,recept3,123,Receptionist,45000\n")
# Managers
users.append("4,manager1,123,Manager,80000\n")
users.append("5,manager2,123,Manager,80000\n")

# Workers
current_id = 6
workers_list = []
for i in range(1, NUM_WORKERS + 1):
    w_name = f"worker{i}"
    workers_list.append(w_name)
    salary = SALARY_BASE + random.choice([0, 2000, 5000, 8000])
    users.append(f"{current_id},{w_name},123,Worker,{salary}\n")
    current_id += 1

with open("data/users.txt", "w") as f:
    f.writelines(users)

# --- GENERATE GUESTS ---
guests = []
# Occupy rooms 1 to NUM_GUESTS
for i in range(1, NUM_GUESTS + 1):
    g_name = get_pakistani_name()
    room_no = i 
    phone = f"03{random.randint(0,4)}{random.randint(0,9)}-{random.randint(1000000, 9999999)}"
    
    # Randomize timestamps
    checkin_dt = random_date(2025)
    checkin_str = checkin_dt.strftime("%d/%m/%Y %H:%M")
    
    status = "Active"
    checkout_str = "-"
    bill = 0
    
    # 30% are checked out (History)
    if random.random() < 0.3:
        status = "CheckedOut"
        # Checkout 1-5 days after checkin
        checkout_dt = checkin_dt + timedelta(days=random.randint(1, 5))
        checkout_str = checkout_dt.strftime("%d/%m/%Y %H:%M")
        
        # Calculate bill approx
        r_price = 4000
        if room_no > 100: r_price = 7000
        if room_no > 200: r_price = 10000
        if room_no > 280: r_price = 25000
        days = (checkout_dt - checkin_dt).days
        if days < 1: days = 1
        bill = days * r_price
    
    guests.append(f"{i},{g_name},{room_no},{phone},{status},{checkin_str},{checkout_str},{bill}\n")

with open("data/guests.txt", "w") as f:
    f.writelines(guests)

# --- GENERATE ATTENDANCE ---
attendance = []
att_id = 1
today = datetime.datetime.now().strftime("%Y-%m-%d")

for i in range(1, NUM_WORKERS + 1):
    w_name = f"worker{i}"
    h_in = random.randint(7, 10)
    m_in = random.randint(0, 59)
    time_in = f"{h_in:02}:{m_in:02}"
    
    status = "Present"
    time_out = "-"
    
    if random.random() < 0.8: # 80% Checked out
        h_out = h_in + 9
        time_out = f"{h_out:02}:{m_in:02}"
        
    attendance.append(f"{att_id},{w_name},{today},{status},{time_in},{time_out}\n")
    att_id += 1

with open("data/attendance.txt", "w") as f:
    f.writelines(attendance)

# --- GENERATE TASKS ---
tasks = []
task_descs = [
    "Clean Room", "Fix Leakage", "Serve Breakfast", "Ironing Service", 
    "Guest Luggage", "Pool Maintenance", "Garden Watering", "Security Check"
]
for i in range(1, NUM_TASKS + 1):
    w_name = random.choice(workers_list)
    desc = f"{random.choice(task_descs)} #{random.randint(1,300)}"
    status = random.choice(["Pending", "Completed", "In Progress", "Completed"])
    tasks.append(f"{i},{w_name},{desc},{status}\n")

with open("data/tasks.txt", "w") as f:
    f.writelines(tasks)

print("Data Generated Successfully in data/ folder with Pakistani Context")
