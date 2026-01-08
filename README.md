<div align="center">

# 🏨 HOTEL MANAGEMENT SYSTEM

<br>

### _Transform Hospitality Management with Seamless Excellence_

<br>

![Last Commit](https://img.shields.io/github/last-commit/KhalilNiazi/Hotel-Management-System?style=for-the-badge)
![Top Language](https://img.shields.io/github/languages/top/KhalilNiazi/Hotel-Management-System?style=for-the-badge)
![Language Count](https://img.shields.io/github/languages/count/KhalilNiazi/Hotel-Management-System?style=for-the-badge)
![License](https://img.shields.io/github/license/KhalilNiazi/Hotel-Management-System?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/KhalilNiazi/Hotel-Management-System?style=for-the-badge)

<br>

### _Built with the tools and technologies:_

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![Tkinter](https://img.shields.io/badge/tkinter-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [System Interfaces](#-system-interfaces)
- [User Roles](#-user-roles)
- [Core Features](#-core-features)
- [Technology Stack](#-technology-stack)
- [Installation & Setup](#-installation--setup)
- [System Architecture](#-system-architecture)
- [Screenshots](#-screenshots)
- [Python Concepts](#-python-concepts-used)
- [Future Enhancements](#-future-enhancements)
- [Project Team](#-project-team)
- [License](#-license)

---

## 🎯 Project Overview

The **Hotel Management System** is a flexible, multi-interface application designed to transform hotel operations through digital automation. This cutting-edge system guarantees optimal accessibility and flexibility with **THREE** unique user interfaces:

- 🖥️ **Console Interface** - Quick CLI for terminal operations
- 🎨 **Desktop GUI** - Modern CustomTkinter interface with dark mode
- 🌐 **Web Application** - Browser-based responsive design

### Project Objectives

- ✅ Streamline hotel operations and reduce human error
- ✅ Provide multiple access points for different user preferences
- ✅ Enable real-time data synchronization across all interfaces
- ✅ Implement robust role-based access control
- ✅ Automate billing and financial reporting
- ✅ Track staff performance and attendance

This project is developed for academic learning and practical understanding of core Python concepts, web development, and GUI programming.

---

## 🌟 Key Features

### 🏢 **Multi-Interface Support**

- Console-based terminal interface for quick operations
- Professional Desktop GUI with modern aesthetics
- Responsive web portal accessible from any browser
- Seamless data synchronization across all platforms

### 🔐 **Role-Based Access Control**

Four distinct user roles with precisely defined permissions:

- **Administrator** - Full system control
- **Receptionist** - Guest management and bookings
- **Manager** - Oversight and analytics
- **Worker/Staff** - Task and attendance management

### 💰 **Dynamic Billing System**

- Automatic fee calculation based on stay duration
- Room rate integration with real-time pricing
- Additional service charges (food, amenities)
- Professional invoice generation with hotel branding

### 📊 **Comprehensive Reporting**

- Financial reports and revenue tracking
- Booking analytics and occupancy rates
- Staff attendance monitoring
- Task completion statistics

---

## 🖥️ System Interfaces

### 1. 🖤 Console Interface (CLI)

**Libraries:** `os`, `sys`, `time`

The Command Line Interface provides a quick and efficient way to interact with the system. Features include:

- Color-coded menus for enhanced readability
- Fast data entry without navigation overhead
- Lightweight operation directly in terminal
- Perfect for users who prefer keyboard-driven workflows

```bash
python main.py
```

### 2. 🎨 Desktop GUI Application

**Libraries:** `CustomTkinter`, `Tkinter`

A professional graphical interface with modern design:

- Clean dark mode aesthetic
- Rounded corners and smooth animations
- Responsive scaling for all screen sizes
- Intuitive navigation and form inputs
- Professional appearance for desktop operations

### 3. 🌐 Web Application

**Libraries:** `Flask`, `HTML5`, `CSS3`, `JavaScript`

Browser-based interface for universal access:

- Responsive design adapts to any device
- No installation required - works in any browser
- Real-time updates and dynamic content
- Modern UI with smooth interactions
- Deployed on Vercel for easy access

```bash
python app.py
```

---

## 👥 User Roles

### 🛡️ ADMINISTRATOR

**Login Credentials:**

- Username: `admin`
- Password: `admin123`

**Responsibilities:**

- ➕ Adding new rooms to inventory
- 📝 Managing complete room details
- 👤 Creating and managing staff accounts
- 🎯 Assigning worker duties and tasks
- 📋 Viewing all bookings and guest information
- 💵 Accessing financial and billing reports
- 📊 Monitoring staff attendance
- 💳 Processing guest checkouts and bills
- ⚙️ Configuring system settings (hotel name)
- 📈 Viewing system statistics and analytics

---

### 🎫 RECEPTIONIST

**Login Credentials:**

- Username: `recept1` (assigned by admin)
- Password: `123` (assigned by admin)

**Responsibilities:**

- 🏨 Viewing available rooms
- ✅ Registering new guests (bookings)
- 🚪 Processing guest check-ins and checkouts
- 🧾 Generating bills and invoices
- 📖 Viewing all booking records
- 📝 Updating guest information
- 💼 Managing daily front desk operations

---

### 📊 MANAGER

**Login Credentials:**

- Username: `manager1` (assigned by admin)
- Password: `123` (assigned by admin)

**Responsibilities:**

- 🏢 Monitoring room inventory status
- 📈 Reviewing booking analytics
- 💰 Analyzing financial reports and revenue
- 👥 Overseeing staff attendance
- 📊 Viewing system statistics and metrics
- 📋 Monitoring worker duties and task completion
- 🎯 Strategic oversight of hotel operations

---

### 👷 WORKER/STAFF

**Login Credentials:**

- Username: Assigned by admin
- Password: Assigned by admin

**Responsibilities:**

- ⏰ Check-in for duty (attendance clock-in)
- 🏁 Check-out after duty (attendance clock-out)
- 📋 View assigned tasks and responsibilities
- ✅ Mark tasks as completed
- 📊 View personal task status
- 💵 View salary information

---

## 🔧 Core Features

### 🏨 Room Management

- Add, edit, and delete rooms
- Room type classification (Single, Double, Twin, Suite)
- Real-time availability tracking
- Automatic conflict prevention
- Price management per room type

**Room Types:**

- **Single [S]** - 1 Bed, Max 1 Person
- **Double [D]** - 1 Bed, Max 2 Persons
- **Twin [T]** - 2 Beds, Max 2 Persons
- **Suite [ST]** - Luxury, Max 4 Persons

### 👤 Guest Booking System

- Complete booking lifecycle management
- Automatic room availability validation
- Guest information storage
- Check-in and checkout processing
- Booking history and records

### 💳 Dynamic Billing

- Automatic bill calculation based on:
  - Stay duration (nights)
  - Room rates
  - Additional services (food, amenities)
- Professional invoice generation
- Hotel branding on all invoices
- Payment tracking and records

### 👥 Staff Management

- User account creation with role assignment
- Salary tracking and management
- Staff directory with complete information
- Secure authentication for all roles
- Permission-based access control

### 📝 Task Assignment

- Assign tasks to specific workers
- Track task status (Pending/Completed)
- View personal task lists
- Monitor task completion rates
- Performance analytics

### ⏰ Attendance Tracking

- Check-in/check-out timestamps
- Date-wise attendance logs
- Staff attendance reports
- Automated time tracking
- Historical attendance data

### 💰 Financial Reporting

- Total revenue calculation
- Guest-wise billing records
- Revenue tracking across all transactions
- Financial summaries and analytics
- Exportable reports

### ⚙️ System Configuration

- Customizable hotel name
- Settings reflected across all interfaces
- Persistent configuration storage
- System preferences management

---

## 🛠️ Technology Stack

### Programming Languages

- **Python 3.x** - Core backend logic
- **JavaScript** - Web interface interactivity
- **HTML5** - Web structure
- **CSS3** - Web styling

### Frameworks & Libraries

#### Console Interface

```
os, sys, time
```

- Terminal operations and system interactions
- Color-coded output for better UX

#### Desktop GUI

```
CustomTkinter, Tkinter
```

- Modern UI components with dark mode
- Professional widgets and layouts
- Cross-platform desktop application

#### Web Application

```
Flask, HTML/CSS/JavaScript
```

- Backend API with Flask
- Responsive frontend design
- RESTful architecture

### Data Storage

- **File-based persistence** - JSON/Text files
- Real-time data synchronization
- Cross-platform compatibility
- No complex database setup required

### Development Tools

- **GitHub** - Version control and collaboration
- **Vercel** - Web application deployment
- **VS Code** - Development environment

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning repository)

### Step 1: Clone Repository

```bash
git clone https://github.com/KhalilNiazi/Hotel-Management-System.git
cd Hotel-Management-System
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Console Interface

```bash
python main.py
```

### Step 4: Run Desktop GUI

```bash
python gui_main.py
```

### Step 5: Run Web Application

```bash
python app.py
```

Then open your browser and navigate to:

```
http://localhost:5000
```

### Default Admin Credentials

```
Username: admin
Password: admin123
```

---

## 🏗️ System Architecture

### System Workflow

```
1. User Login
   ↓
2. Credential Validation
   ↓
3. Role Identification
   ↓
4. Role-Based Menu Display
   ↓
5. User Operations
   ↓
6. Data Persistence (Files)
   ↓
7. Logout/Exit
```

### Data Flow

- All interfaces share the same data layer
- File-based storage ensures data persistence
- Real-time synchronization across platforms
- Atomic operations prevent data corruption

### Security Features

- Encrypted password storage
- Role-based access control (RBAC)
- Input validation and sanitization
- Session management
- Secure authentication

---

## 📸 Screenshots

### Console Interface

![Console Interface](docs/images/console_interface.png)
_Color-coded terminal interface with menu-driven navigation_

### Desktop GUI

![Desktop GUI](docs/images/desktop_gui.png)
_Modern CustomTkinter interface with dark mode_

### Web Portal

![Web Portal](docs/images/web_portal.png)
_Responsive web design accessible from any browser_

### Admin Dashboard

![Admin Dashboard](docs/images/admin_dashboard.png)
_Comprehensive admin control panel_

### Booking Management

![Booking System](docs/images/booking_system.png)
_Guest booking and check-in interface_

---

## 🐍 Python Concepts Used

This project demonstrates proficiency in:

- ✅ **Functions** - Modular code organization
- ✅ **Loops** - Iterative operations (for, while)
- ✅ **Conditional Statements** - Decision making (if/elif/else)
- ✅ **File Handling** - Data persistence (read/write operations)
- ✅ **Exception Handling** - Error management (try/except)
- ✅ **Data Structures** - Lists, dictionaries, tuples
- ✅ **Object-Oriented Programming** - Classes and objects
- ✅ **Modular Programming** - Code reusability
- ✅ **String Manipulation** - Text processing
- ✅ **Date/Time Operations** - Timestamp management
- ✅ **Input/Output Operations** - User interaction
- ✅ **Role-Based Access Control** - Security implementation

---

## 🚀 Future Enhancements

### Completed ✅

- [x] Console-based interface
- [x] Graphical user interface (GUI)
- [x] Web application interface
- [x] Role-based access control
- [x] Dynamic billing system

### Planned 📋

- [ ] Database integration (MySQL/PostgreSQL)
- [ ] Online booking portal for customers
- [ ] Email notifications for bookings
- [ ] SMS alerts and reminders
- [ ] Payment gateway integration
- [ ] Advanced analytics dashboard
- [ ] Mobile application (iOS/Android)
- [ ] Cloud deployment (AWS/Azure)
- [ ] Multi-language support
- [ ] API for third-party integrations
- [ ] Backup and restore functionality
- [ ] Advanced reporting with charts/graphs

---

## 👨‍💻 Project Team

This project was developed as part of the **Introduction to Programming (Semester 2)** course at the **University of Engineering and Technology (UET)**, Institute of Business & Management (BBIT).

### Team Members

| Name                           | Roll Number     |
| ------------------------------ | --------------- | 
| **Mohammad Bin Ali**           | 2025(S) BBIT 50 |
| **Muhammad Khalil Akbar Khan** | 2025(S) BBIT 57 |
| **Syeda Hifsa Rizwan**         | 2025(S) BBIT 59 |

### Supervisor

**Sir M. Sarfraz**  
Course Instructor - Introduction to Programming

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/KhalilNiazi/Hotel-Management-System/issues).

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Contact & Support

For questions, suggestions, or support:

- 📧 Email: khalilniazi@uet.edu.pk
- 🐙 GitHub: [@KhalilNiazi](https://github.com/KhalilNiazi)
- 🌐 Project Link: [Hotel Management System](https://github.com/KhalilNiazi/Hotel-Management-System)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

## 🙏 Acknowledgments

- University of Engineering and Technology (UET) for providing the opportunity
- Sir M. Sarfraz for guidance and mentorship
- CustomTkinter library for modern GUI components
- Flask framework for web development
- Open-source community for inspiration and resources

---

<div align="center">

**Made with ❤️ by UET BBIT Students**

_Transforming hospitality management, one line of code at a time_

</div>
