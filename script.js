// --- INIT ---
(async function initSystem() {
  try {
    const res = await fetch(`${API_BASE}/api/settings`);
    const conf = await res.json();

    // Update Title and Brand
    document.title = conf.name + " System";
    const authBrand = document.getElementById("app-brand-auth");
    if (authBrand) authBrand.innerText = conf.name;

    const sideBrand = document.querySelector(".brand");
    if (sideBrand)
      sideBrand.innerHTML = `<ion-icon name="bed-outline"></ion-icon> ${conf.name}`;
  } catch (e) {
    console.log("Could not load settings");
  }
})();

// --- CONFIG ---
const API_BASE = window.location.port === "5500" ? "http://127.0.0.1:5000" : "";
let currentUser = null;
let currentRole = null;
let allRoomData = []; // Store for filtering

// --- AUTH LOGIC ---
function showLoginInfo(role) {
  // Hide the Role Grid
  document.getElementById("role-view").style.display = "none";
  // Show the Login Form
  document.getElementById("login-form").style.display = "block";

  document.getElementById("selected-role").value = role;

  // Update Header text to show which portal we are accessing
  const subtitle = document.querySelector(".auth-subtitle");
  if (subtitle) subtitle.innerText = `${role} Portal Login`;

  // Clear previous messages and focus
  document.getElementById("login-msg").innerText = "";
  document.getElementById("username").focus();
}

function backToRoles() {
  // Hide the Login Form
  document.getElementById("login-form").style.display = "none";
  // Show the Role Grid
  document.getElementById("role-view").style.display = "block";

  // Reset Header and Inputs
  const subtitle = document.querySelector(".auth-subtitle");
  if (subtitle) subtitle.innerText = "Premium Hotel Management System";

  document.getElementById("login-msg").innerText = "";
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
}

document.getElementById("login-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const role = document.getElementById("selected-role").value;
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;

  try {
    const res = await fetch(`${API_BASE}/api/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username: user, password: pass, role: role }),
    });
    const data = await res.json();

    if (data.status === "success") {
      currentUser = data.username;
      currentRole = role;
      setupDashboard(role);
    } else {
      document.getElementById("login-msg").innerText = data.message;
    }
  } catch {
    document.getElementById("login-msg").innerText = "Server Unreachable";
  }
});

function setupDashboard(role) {
  // Switch Screen
  document.getElementById("auth-screen").classList.remove("active");
  document.getElementById("main-dashboard").classList.add("active");
  if (type === "assign_task") {
    modalTitle.innerText = "Assign New Task";
    modalBody.innerHTML = `
            <form onsubmit="submitForm(event, 'assign_task')">
                <div class="form-group">
                    <label class="form-label">Staff Username</label>
                    <input type="text" name="staff" class="form-input" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Description</label>
                    <input type="text" name="desc" class="form-input" required>
                </div>
                <button type="submit" class="btn btn-primary" style="width:100%">Assign</button>
            </form>
        `;
  }

  // Sidebar Config
  document
    .querySelectorAll(".nav-menu")
    .forEach((el) => (el.style.display = "none"));
  if (role === "Admin")
    document.getElementById("admin-menu").style.display = "flex";
  if (role === "Receptionist")
    document.getElementById("recept-menu").style.display = "flex";
  if (role === "Worker")
    document.getElementById("worker-menu").style.display = "flex";
  if (role === "Manager")
    document.getElementById("manager-menu").style.display = "flex";

  // User Info
  document.getElementById("display-username").innerText = currentUser;
  document.getElementById("display-role").innerText = role;
  document.getElementById("user-initial").innerText = currentUser
    .charAt(0)
    .toUpperCase();

  // Initial View
  if (role === "Admin") loadStats();
  if (role === "Receptionist") loadView("newbooking");
  if (role === "Worker") loadWorkerTasks();
  if (role === "Manager") loadView("finance");
}

function logout() {
  location.reload(); // Simplest logout
}

// --- CORE VIEW LOGIC ---

async function loadView(viewType) {
  const area = document.getElementById("view-area");
  const searchCont = document.getElementById("search-container");
  const workerArea = document.getElementById("worker-area");
  const statsArea = document.getElementById("stats-area");

  // Reset View State
  area.innerHTML = '<div style="padding:20px">Loading...</div>';
  area.style.display = "block";
  workerArea.style.display = "none";
  statsArea.style.display = "none";
  document.getElementById("page-heading").innerText = viewType
    .replace("_", " ")
    .toUpperCase();

  // --- FORMS ---
  searchCont.style.display = "none"; // Hide search by default

  if (viewType === "add_room") {
    area.innerHTML = `
            <div style="padding:20px; max-width:600px;">
                <form onsubmit="postData(event, 'add_room')">
                    <div class="form-group"><label class="form-label">Room No</label><input class="form-input" name="room" type="number" required></div>
                    <div class="form-group"><label class="form-label">Type</label>
                        <select class="form-select" name="type">
                            <option value="Single">Single</option><option value="Double">Double</option><option value="Triple">Triple</option><option value="Suite">Suite</option>
                        </select>
                    </div>
                    <div class="form-group"><label class="form-label">Price (Rs.)</label><input class="form-input" name="price" type="number" required></div>
                    <button class="btn btn-primary" type="submit">Create Room</button>
                </form>
            </div>`;
    return;
  }
  if (viewType === "add_staff") {
    area.innerHTML = `
            <div style="padding:20px; max-width:600px;">
                <form onsubmit="postData(event, 'add_staff')">
                    <div class="form-group"><label class="form-label">Username</label><input class="form-input" name="username" required></div>
                    <div class="form-group"><label class="form-label">Password</label><input class="form-input" name="password" required></div>
                    <div class="form-group"><label class="form-label">Role</label>
                         <select class="form-select" name="role"><option>Worker</option><option>Receptionist</option><option>Manager</option><option>Admin</option></select>
                    </div>
                    <div class="form-group"><label class="form-label">Salary (Rs.)</label><input class="form-input" name="salary" type="number" required></div>
                    <button class="btn btn-primary" type="submit">Register</button>
                </form>
             </div>`;
    return;
  }

  // --- NEW BOOKING: FILTERABLE ROOMS ---
  if (viewType === "newbooking") {
    document.getElementById("page-heading").innerText = "Create Booking";
    area.innerHTML = `
            <div style="padding:20px; display:grid; grid-template-columns: 1fr 1fr; gap:40px;">
                 <div>
                    <h3 class="section-title">1. Select Preferences</h3>
                    <div class="form-group">
                        <label class="form-label">Room Type</label>
                        <select class="form-select" id="bk-type" onchange="fetchAvailableRooms()">
                            <option value="">-- Select Type --</option>
                            <option value="Single">Single</option><option value="Double">Double</option>
                            <option value="Triple">Triple</option><option value="Suite">Suite</option>
                        </select>
                    </div>
                    <div id="avail-room-list" style="margin-top:20px; max-height:300px; overflow-y:auto; border:1px solid var(--border-color); border-radius:10px; padding:10px; display:none;">
                        <!-- List loaded here -->
                    </div>
                 </div>
                 <div>
                    <h3 class="section-title">2. Guest Details</h3>
                    <form onsubmit="postData(event, 'book', 'bookings')">
                        <div class="form-group"><label class="form-label">Guest Name</label><input class="form-input" name="name" required placeholder="Full Name"></div>
                        <div class="form-group"><label class="form-label">Phone</label><input class="form-input" name="phone" required placeholder="0300-1234567"></div>
                        <div class="form-group"><label class="form-label">Selected Room</label><input class="form-input" name="room" id="bk-room-inp" type="number" readonly required placeholder="Select from list ->"></div>
                        <button class="btn btn-primary" type="submit">Confirm Booking</button>
                    </form>
                 </div>
            </div>
        `;
    return;
  }

  if (viewType === "tasks") {
    document.getElementById(
      "content-title"
    ).innerHTML = `TASK MANAGEMENT <button class="btn btn-primary" onclick="openModal('assign_task')" style="float:right; font-size:0.9rem">+ Assign Task</button>`;
  }

  if (viewType === "settings") {
    document.getElementById("page-heading").innerText = "System Settings";
    // Fetch current settings
    const res = await fetch(`${API_BASE}/api/settings`);
    const conf = await res.json();

    area.innerHTML = `
          <div style="max-width:600px; background:white; padding:2rem; border-radius:10px; border:1px solid #e2e8f0;">
              <form onsubmit="updateSettings(event)">
                  <h3 class="section-title">General Configuration</h3>
                  <div class="form-group">
                      <label class="form-label">Hotel Name</label>
                      <input class="form-input" name="name" value="${conf.name}" required>
                      <small style="color:#64748b;">This name will appear on the dashboard and reports.</small>
                  </div>
                   <h3 class="section-title" style="margin-top:20px;">Other Options</h3>
                  <div class="form-group">
                      <label class="form-label">System Mode</label>
                      <select class="form-select" disabled>
                        <option>Production</option>
                        <option>Maintenance</option>
                      </select>
                      <small style="color:#64748b;">Feature coming soon.</small>
                  </div>
                  <button class="btn btn-primary" type="submit">Save Changes</button>
              </form>
          </div>
      `;
    return;
  }

  // --- TABLES (LISTS) ---

  searchCont.style.display = "block"; // Enable search for tables

  // Fetch Data
  let endpoint = `/api/${viewType}`;
  if (viewType === "finance") endpoint = "/api/bookings";

  const res = await fetch(`${API_BASE}${endpoint}`);
  const data = await res.json();

  // Special Render for Finance
  if (viewType === "finance") {
    let total = 0;
    let html = `<table class="data-table" id="data-table"><thead><tr><th>Guest</th><th>Status</th><th>Bill (Rs.)</th></tr></thead><tbody>`;
    data.forEach((r) => {
      if (r.status === "CheckedOut") {
        html += `<tr><td>${r.name}</td><td><span class="status-badge status-checkedout">Paid</span></td><td>Rs. ${r.bill}</td></tr>`;
        total += r.bill;
      }
    });
    html += `</tbody></table><div style="padding:20px; text-align:right"><h2>Total Revenue: Rs. ${total.toLocaleString()}</h2></div>`;
    area.innerHTML = html;
    return;
  }

  // Generic Table Render
  if (data.length > 0) {
    let keys = Object.keys(data[0]);
    let html = `<table class="data-table" id="data-table"><thead><tr>`;
    keys.forEach((k) => (html += `<th>${k.toUpperCase()}</th>`));
    // Add Action Column for Admin/Manager

    // Add Action Column for Admin/Manager
    if (
      ["Admin", "Manager", "Receptionist"].includes(currentRole) &&
      (viewType === "rooms" || viewType === "staff" || viewType === "bookings")
    ) {
      html += `<th>ACTION</th>`;
    }
    html += `</tr></thead><tbody>`;

    data.forEach((row) => {
      html += `<tr>`;
      Object.values(row).forEach((v) => {
        let display = v;
        // Badge logic
        if (typeof v === "string") {
          if (v.toLowerCase() === "active")
            display = `<span class="status-badge status-active">Active</span>`;
          if (v.toLowerCase() === "occupied")
            display = `<span class="status-badge status-occupied">Occupied</span>`;
          if (v.toLowerCase() === "available")
            display = `<span class="status-badge status-available">Available`;
          if (v.toLowerCase() === "present")
            display = `<span class="status-badge status-present">Present</span>`;
        }
        html += `<td>${display}</td>`;
      });
      // Add Action Buttons logic

      // Add Action Buttons logic
      if (["Admin", "Manager", "Receptionist"].includes(currentRole)) {
        let actions = "";
        if (viewType === "rooms" && currentRole !== "Receptionist") {
          actions += `<button class="action-btn edit-btn" onclick="openEdit('room', ${row.id}, '${row.price}')">Edit Price</button> `;
          if (currentRole === "Admin")
            actions += `<button class="action-btn" style="background:#ef4444; color:white; border:none; padding:5px 10px; border-radius:4px; cursor:pointer;" onclick="deleteItem('room', ${row.id})">Del</button> `;
        }
        if (viewType === "staff" && currentRole === "Admin") {
          actions += `<button class="action-btn edit-btn" onclick="openEdit('staff', ${row.id}, '${row.salary}')">Edit Salary</button> `;
          actions += `<button class="action-btn" style="background:#ef4444; color:white; border:none; padding:5px 10px; border-radius:4px; cursor:pointer;" onclick="deleteItem('staff', ${row.id})">Del</button> `;
        }
        if (viewType === "bookings" && row.status === "Active") {
          actions += `<button class="action-btn edit-btn" onclick="openEdit('guest', ${row.id}, '${row.name}')">Edit</button> `;
          actions += `<button class="action-btn" style="background:#ef4444; color:white; border:none; padding:5px 10px; border-radius:4px; cursor:pointer;" onclick="checkoutGuest(${row.id})">Chk Out</button>`;
        }

        if (actions !== "") html += `<td>${actions}</td>`;
        else if (
          document.querySelector("#data-table th:last-child").innerText ===
          "ACTION"
        )
          html += `<td>-</td>`;
      }
      html += `</tr>`;
    });
    html += `</tbody></table>`;

    // --- PRINT BUTTON FOR ATTENDANCE ---
    if (viewType === "attendance" || viewType === "attendance_report") {
      area.innerHTML =
        `<div style="text-align:right; margin-bottom:10px;"><button class="btn btn-outline" onclick="window.print()">🖨 Print Report</button></div>` +
        html;
    } else {
      area.innerHTML = html;
    }
  } else {
    area.innerHTML = '<div style="padding:20px">No records found.</div>';
  }
}

// --- BOOKING LOGIC ---
async function fetchAvailableRooms() {
  const type = document.getElementById("bk-type").value;
  const listArea = document.getElementById("avail-room-list");
  listArea.style.display = "block";
  listArea.innerHTML = "Fetching...";

  const res = await fetch(`${API_BASE}/api/rooms`);
  const allRooms = await res.json();

  const filtered = allRooms.filter(
    (r) => r.type === type && r.status === "Available"
  );

  if (filtered.length === 0) {
    listArea.innerHTML = "<p>No rooms available.</p>";
    return;
  }

  let html = `<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">`;
  filtered.forEach((r) => {
    html += `<div onclick="selectRoom(${r.id})" style="padding:10px; border:1px solid #334155; border-radius:5px; cursor:pointer; text-align:center;" class="room-item">
            <strong>${r.id}</strong><br><small>Rs. ${r.price}</small>
        </div>`;
  });
  html += `</div>`;
  listArea.innerHTML = html;
}

function selectRoom(id) {
  document.getElementById("bk-room-inp").value = id;
  // Highlight effect
  document
    .querySelectorAll(".room-item")
    .forEach((el) => (el.style.background = "transparent"));
  event.currentTarget.style.background = "#4f46e533";
}

// --- EDIT MODAL LOGIC ---
function openEdit(type, id, currentVal) {
  document.getElementById("edit-modal").style.display = "flex";
  document.getElementById("edit-id").value = id;
  document.getElementById("edit-type").value = type;
  document.getElementById("edit-val").value = currentVal;

  if (type === "room")
    document.getElementById(
      "modal-title"
    ).innerText = `Edit Price (Room ${id})`;
  if (type === "staff")
    document.getElementById("modal-title").innerText = `Edit Salary (ID ${id})`;
  if (type === "guest")
    document.getElementById(
      "modal-title"
    ).innerText = `Edit Guest Name (ID ${id})`;
}

function closeModal() {
  document.getElementById("edit-modal").style.display = "none";
}

async function submitEdit(e) {
  e.preventDefault();
  const type = document.getElementById("edit-type").value;
  const id = document.getElementById("edit-id").value;
  const val = document.getElementById("edit-val").value;

  let apiEndpoint =
    type === "add_room"
      ? "add_room"
      : type === "newbooking"
      ? "book"
      : type === "assign_task"
      ? "assign_task"
      : type === "add_staff"
      ? "add_staff"
      : "edit_guest";
  let body = { id: id };
  if (type === "room") body.price = val;
  else if (type === "staff") body.salary = val;
  else body.name = val;

  const res = await fetch(`${API_BASE}/api/${apiEndpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const ret = await res.json();
  alert(ret.message);
  closeModal();
  if (ret.status === "success") {
    if (type === "room") loadView("rooms");
    if (type === "staff") loadView("staff");
    if (type === "guest") loadView("bookings");
    if (type === "add_room") loadView("rooms");
    if (type === "add_staff") loadView("staff");
    if (type === "newbooking") loadView("bookings");
    if (type === "assign_task") loadView("tasks");
  }
}

async function deleteItem(type, id) {
  if (!confirm("Start Delete Sequence? This cannot be undone.")) return;

  let endpoint = type === "room" ? "delete_room" : "delete_staff";
  try {
    const res = await fetch(`${API_BASE}/api/${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: id }),
    });
    const data = await res.json();
    alert(data.message);
    if (data.status === "success") {
      loadView(type === "room" ? "rooms" : "staff");
    }
  } catch (e) {
    alert("Error deleting");
  }
}

async function checkoutGuest(id) {
  if (!confirm("Are you sure you want to Check Out this guest?")) return;

  try {
    const res = await fetch(`${API_BASE}/api/checkout`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: id }),
    });
    const data = await res.json();
    alert(data.message);
    if (data.status === "success") loadView("bookings");
  } catch (e) {
    alert("Action Failed");
  }
}

// --- SEARCH ---

function filterTable() {
  const input = document.getElementById("search-input");
  const filter = input.value.toUpperCase();
  const table = document.getElementById("data-table");
  const tr = table.getElementsByTagName("tr");

  for (let i = 1; i < tr.length; i++) {
    // Start at 1 to skip header
    let visible = false;
    let tds = tr[i].getElementsByTagName("td");
    for (let j = 0; j < tds.length; j++) {
      if (tds[j]) {
        const txtValue = tds[j].textContent || tds[j].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          visible = true;
        }
      }
    }
    tr[i].style.display = visible ? "" : "none";
  }
}

// --- STATS ---
async function loadStats() {
  document.getElementById("page-heading").innerText = "Dashboard";
  document.getElementById("view-area").style.display = "none";
  document.getElementById("stats-area").style.display = "grid"; // Show grid
  document.getElementById("search-container").style.display = "none";

  const res = await fetch(`${API_BASE}/api/stats`);
  const s = await res.json();

  document.getElementById("stats-area").innerHTML = `
        <div class="stat-card">
            <div class="stat-header">
                <div><div class="stat-title">Total Revenue</div><div class="stat-value">Rs. ${s.revenue.toLocaleString()}</div></div>
                <div class="stat-icon"><ion-icon name="wallet-outline"></ion-icon></div>
            </div>
            <div class="stat-trend trend-up"><ion-icon name="trending-up-outline"></ion-icon> +12% from last month</div>
        </div>
        <div class="stat-card">
            <div class="stat-header">
                <div><div class="stat-title">Total Guests</div><div class="stat-value">${
                  s.guests
                }</div></div>
                <div class="stat-icon"><ion-icon name="people-outline"></ion-icon></div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-header">
                 <div><div class="stat-title">Occupancy</div><div class="stat-value">${
                   s.occupied
                 } / ${s.rooms}</div></div>
                 <div class="stat-icon"><ion-icon name="bed-outline"></ion-icon></div>
            </div>
        </div>
         <div class="stat-card">
            <div class="stat-header">
                 <div><div class="stat-title">Active Staff</div><div class="stat-value">${
                   s.staff
                 }</div></div>
                 <div class="stat-icon"><ion-icon name="id-card-outline"></ion-icon></div>
            </div>
        </div>
    `;
}

// --- WORKER ---
async function loadWorkerTasks() {
  document.getElementById("view-area").style.display = "none";
  document.getElementById("worker-area").style.display = "block";

  const res = await fetch(`${API_BASE}/api/my_tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: currentUser }),
  });
  const data = await res.json();

  let html = `<h2 class="section-title">My Assignments</h2><div style="display:grid; gap:15px">`;
  if (data.length === 0) html += "<p>No tasks assigned.</p>";
  else {
    data.forEach((t) => {
      html += `<div class="stat-card" style="display:flex; justify-content:space-between; align-items:center;">
                <div><p style="font-weight:600">${t.desc}</p></div>
                <span class="status-badge status-pending">${t.status}</span>
            </div>`;
    });
  }
  html += `</div>`;
  document.getElementById("worker-area").innerHTML = html;
}

function markAllAttendance() {
  if (confirm("Mark Check-IN for today?"))
    postData(null, "mark_attendance", null, {
      username: currentUser,
      type: "In",
    });
  // Logic simplified for demo
}

async function updateSettings(e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());

  const res = await fetch(`${API_BASE}/api/settings`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  const ret = await res.json();
  alert(ret.message);
  if (ret.status === "success") {
    location.reload(); // Reload to reflect name change
  }
}

// --- GENERAL POST ---

async function postData(e, api, refreshView, manualData) {
  if (e) e.preventDefault();
  let data = manualData;

  if (!data && e) {
    const formData = new FormData(e.target);
    data = Object.fromEntries(formData.entries());
  }

  const res = await fetch(`${API_BASE}/api/${api}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  const ret = await res.json();
  alert(ret.message || ret.status);
  if (ret.status === "success" && refreshView) loadView(refreshView);
}
