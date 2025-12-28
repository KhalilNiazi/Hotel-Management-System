from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import main as backend
import datetime

# Initialize Flask App
# Serve static files from 'web' folder

# Initialize Flask App
# Serve static files from current directory since 'web' folder was removed
app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')

CORS(app) # Enable CORS for all routes (to support port 5500 if needed)

# Load data on start (Force reload to get new generated data)
backend.load_data()

@app.route('/')
def home():
    return render_template('index.html')

# --- AUTHENTICATION ---

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    
    # Validation against backend.userData
    # userData format: [userCount, Username, Password, Role]
    for i in range(backend.userCount):
        u_name = backend.userData[i][1]
        u_pass = backend.userData[i][2]
        u_role = backend.userData[i][3]
        
        if u_name == username and u_pass == password:
            # Check role hierarchy logic or exact match
            # "Admin" can access any portal usually, but here we enforce role match or Admin override
            if u_role == role or u_role == "Admin":
                return jsonify({"status": "success", "username": u_name, "role": u_role})
    
    return jsonify({"status": "error", "message": "Invalid Credentials"})

# --- DATA ENDPOINTS ---

@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    # Helper to clean data for JSON
    rooms = []
    # Occupied for guests
    occupied = [backend.guest_data[k][2] for k in range(backend.guest_count) if backend.guest_data[k][4] == "Active"]
    
    for i in range(backend.roomCount):
        r = {
            "id": backend.hotelData[i][0],
            "type": backend.hotelData[i][1],
            "price": backend.hotelData[i][2],
            "status": "Occupied" if backend.hotelData[i][0] in occupied else "Available"
        }
        rooms.append(r)
    return jsonify(rooms)

@app.route('/api/staff', methods=['GET'])
def get_staff():
    staff = []
    for i in range(backend.userCount):
        salary = "0"
        if len(backend.userData[i]) > 4:
             salary = backend.userData[i][4]

        staff.append({
            "id": backend.userData[i][0],
            "username": backend.userData[i][1],
            "role": backend.userData[i][3],
            "salary": salary
        })
    return jsonify(staff)

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    bookings = []
    for i in range(backend.guest_count):
        bookings.append({
            "id": backend.guest_data[i][0],
            "name": backend.guest_data[i][1],
            "room": backend.guest_data[i][2],
            "phone": backend.guest_data[i][3],
            "status": backend.guest_data[i][4],
            "checkin": backend.guest_data[i][5],
            "bill": backend.guest_data[i][7]
        })
    return jsonify(bookings)

@app.route('/api/attendance', methods=['GET'])
def get_attendance():
    att = []
    for i in range(backend.attendance_count):
        # Format: [ID, WorkerName, Date, Status, TimeIn, TimeOut]
        att.append({
            "name": backend.attendanceData[i][1],
            "date": backend.attendanceData[i][2],
            "status": backend.attendanceData[i][3],
            "time_in": backend.attendanceData[i][4],
            "time_out": backend.attendanceData[i][5]
        })
    return jsonify(att)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    for i in range(backend.taskCount):
        tasks.append({
            "id": backend.assignTask[i][0],
            "staff": backend.assignTask[i][1],
            "desc": backend.assignTask[i][2],
            "status": backend.assignTask[i][3]
        })
    return jsonify(tasks)

@app.route('/api/my_tasks', methods=['POST'])
def get_my_tasks():
    data = request.json
    username = data.get('username')
    tasks = []
    for i in range(backend.taskCount):
        if backend.assignTask[i][1] == username:
             tasks.append({
                "id": backend.assignTask[i][0],
                "desc": backend.assignTask[i][2],
                "status": backend.assignTask[i][3]
            })
    return jsonify(tasks)

# --- ACTION ENDPOINTS ---



@app.route('/api/checkout', methods=['POST'])
def checkout():
    data = request.json
    gid = int(data.get('id'))
    
    found = False
    bill = 0
    
    for i in range(backend.guest_count):
        if backend.guest_data[i][0] == gid:
            if backend.guest_data[i][4] == "Active":
                # Mark Checked Out
                backend.guest_data[i][4] = "CheckedOut"
                backend.guest_data[i][6] = datetime.datetime.now().strftime("%Y-%m-%d") # Checkout Date
                
                # Calculate Bill (Simple: Price * 1 for now, or could store days)
                rid = backend.guest_data[i][2]
                price = 0
                for r in range(backend.roomCount):
                    if backend.hotelData[r][0] == rid:
                         price = backend.hotelData[r][2]
                         break
                
                bill = price # Default 1 day charge for simplicity
                backend.guest_data[i][7] = bill
                
                backend.save_data()
                found = True
                break
    
    if found:
        return jsonify({"status": "success", "message": f"Guest Checked Out. Bill: Rs. {bill}", "bill": bill})
    else:
        return jsonify({"status": "error", "message": "Guest not found or already checked out."})

@app.route('/api/stats', methods=['GET'])

def get_stats():
    # Calculate Total Revenue
    revenue = 0
    for i in range(backend.guest_count):
        revenue += backend.guest_data[i][7]
        
    occupied_count = len([k for k in range(backend.guest_count) if backend.guest_data[k][4] == "Active"])
    
    stats = {
        "rooms": backend.roomCount,
        "staff": backend.userCount,
        "guests": backend.guest_count,
        "occupied": occupied_count,
        "revenue": revenue
    }
    return jsonify(stats)

@app.route('/api/add_room', methods=['POST'])
def add_room():
    data = request.json
    try:
        r_no = int(data.get('room'))
        r_type = data.get('type')
        r_price = int(data.get('price'))
        
        # Check exists
        for i in range(backend.roomCount):
            if backend.hotelData[i][0] == r_no:
                 return jsonify({"status": "error", "message": "Room ID exists"})
        
        backend.hotelData[backend.roomCount][0] = r_no
        backend.hotelData[backend.roomCount][1] = r_type
        backend.hotelData[backend.roomCount][2] = r_price
        backend.roomCount += 1
        backend.save_data()
        return jsonify({"status": "success", "message": "Room Added"})
    except:
        return jsonify({"status": "error", "message": "Invalid Data"})

@app.route('/api/add_staff', methods=['POST'])
def add_staff():
    data = request.json
    username = data.get('username')
    
    # Check exists
    for i in range(backend.userCount):
        if backend.userData[i][1] == username:
             return jsonify({"status": "error", "message": "User exists"})
             
    backend.userData[backend.userCount][0] = backend.userCount
    backend.userData[backend.userCount][1] = username
    backend.userData[backend.userCount][2] = data.get('password')
    backend.userData[backend.userCount][3] = data.get('role')
    backend.userData[backend.userCount][4] = data.get('salary', "0")
    backend.userCount += 1
    backend.save_data()
    return jsonify({"status": "success", "message": "Staff Added"})


@app.route('/api/delete_room', methods=['POST'])
def delete_room():
    data = request.json
    try:
        rid = int(data.get('id'))
        
        # Determine index
        for i in range(backend.roomCount):
             if backend.hotelData[i][0] == rid:
                 # Shift logic (simple array replacement for persistent lists)
                 # In python lists: pop or del. But backend uses fixed size arrays logic?
                 # No, backend.hotelData is list of lists
                 # In main.py:
                 # for j in range(idx, roomCount - 1): hotelData[j] = hotelData[j+1]
                 # hotelData[roomCount-1] = [-1, "HD", -11]
                 
                 for j in range(i, backend.roomCount - 1):
                     backend.hotelData[j] = backend.hotelData[j+1][:]
                 
                 backend.hotelData[backend.roomCount - 1] = [-1, "HD", -11]
                 backend.roomCount -= 1
                 backend.save_data()
                 return jsonify({"status": "success", "message": "Room Deleted"})
        
        return jsonify({"status": "error", "message": "Room Not Found"})
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": "Delete Failed"})

@app.route('/api/delete_staff', methods=['POST'])
def delete_staff():
    data = request.json
    try:
        uid = int(data.get('id'))
        
        for i in range(backend.userCount):
             if backend.userData[i][0] == uid:
                 # Shift
                 for j in range(i, backend.userCount - 1):
                     backend.userData[j] = backend.userData[j+1][:]
                 
                 # Reset last
                 backend.userData[backend.userCount - 1] = [-1, "U", "P", "R", "0"]
                 backend.userCount -= 1
                 backend.save_data()
                 return jsonify({"status": "success", "message": "Staff Deleted"})
                 
        return jsonify({"status": "error", "message": "Staff Not Found"})
    except:
        return jsonify({"status": "error", "message": "Delete Failed"})

@app.route('/api/assign_task', methods=['POST'])

def assign_task():
    data = request.json
    try:
        backend.assignTask[backend.taskCount][0] = backend.taskCount + 1
        backend.assignTask[backend.taskCount][1] = data.get('staff')
        backend.assignTask[backend.taskCount][2] = data.get('desc')
        backend.assignTask[backend.taskCount][3] = "Pending"
        backend.taskCount += 1
        backend.save_data()
        return jsonify({"status": "success", "message": "Task Assigned"})
    except:
         return jsonify({"status": "error", "message": "Error assigning task"})


@app.route('/api/edit_room', methods=['POST'])
def edit_room():
    data = request.json
    try:
        rid = int(data.get('id'))
        price = data.get('price')
        
        found = False
        for i in range(backend.roomCount):
            if backend.hotelData[i][0] == rid:
                backend.hotelData[i][2] = price
                found = True
                break
        
        if found:
            backend.save_data()
            return jsonify({"status": "success", "message": "Room Updated"})
        else:
            return jsonify({"status": "error", "message": "Room Not Found"})
    except:
        return jsonify({"status": "error", "message": "Invalid ID"})

@app.route('/api/edit_staff', methods=['POST'])
def edit_staff():
    data = request.json
    try:
        sid = int(data.get('id'))
        salary = data.get('salary')
        
        found = False
        for i in range(backend.userCount):
            if backend.userData[i][0] == sid:
                if len(backend.userData[i]) < 5: backend.userData[i].append("0")
                backend.userData[i][4] = salary
                found = True
                break
        
        if found:
            backend.save_data()
            return jsonify({"status": "success", "message": "Staff Updated"})
    except:
         return jsonify({"status": "error", "message": "Error"})
    
    return jsonify({"status": "error", "message": "Not Found"})


@app.route('/api/edit_guest', methods=['POST'])
def edit_guest():
    data = request.json
    try:
        gid = int(data.get('id'))
        name = data.get('name')
        
        found = False
        for i in range(backend.guest_count):
            if backend.guest_data[i][0] == gid:
                backend.guest_data[i][1] = name
                found = True
                break
        
        if found:
            backend.save_data()
            return jsonify({"status": "success", "message": "Guest Updated"})
    except:
         return jsonify({"status": "error", "message": "Error"})
    
    return jsonify({"status": "error", "message": "Not Found"})

@app.route('/api/book', methods=['POST'])

def book_room():


    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    try:
        room = int(data.get('room'))
    except:
        return jsonify({"status": "error", "message": "Invalid Room"}), 400

    # Logic mirror from main.py
    valid = False
    for i in range(backend.roomCount):
        if backend.hotelData[i][0] == room:
            valid = True
            break
            
    occupied = [backend.guest_data[k][2] for k in range(backend.guest_count) if backend.guest_data[k][4] == "Active"]
    
    if not valid: return jsonify({"status": "error", "message": "Room not found"})
    if room in occupied: return jsonify({"status": "error", "message": "Room occupied"})

    backend.guest_data[backend.guest_count][0] = backend.guest_count + 1
    backend.guest_data[backend.guest_count][1] = name
    backend.guest_data[backend.guest_count][2] = room
    backend.guest_data[backend.guest_count][3] = phone
    backend.guest_data[backend.guest_count][4] = "Active"
    backend.guest_data[backend.guest_count][5] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    backend.guest_data[backend.guest_count][6] = "-"
    backend.guest_data[backend.guest_count][7] = 0
    backend.guest_count += 1
    backend.save_data()
    
    return jsonify({"status": "success"})


@app.route('/api/settings', methods=['GET', 'POST'])
def handle_settings():
    if request.method == 'POST':
        data = request.json
        new_name = data.get('name')
        if new_name:
            backend.hotel_config['name'] = new_name
            backend.save_settings()
            return jsonify({"status": "success", "message": "Settings Updated"})
        return jsonify({"status": "error", "message": "Invalid Name"})
    else:
        return jsonify(backend.hotel_config)

@app.route('/api/mark_attendance', methods=['POST'])

def mark_attendance():
    data = request.json
    name = data.get('username')
    atype = data.get('type') # In or Out
    backend.mark_attendance(name, atype)
    return jsonify({"status": "success", "message": f"Checked {atype}"})


if __name__ == '__main__':
    print("SERVER STARTED - ACCESS VIA: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)

