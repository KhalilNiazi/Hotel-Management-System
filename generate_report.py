
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

def create_report():
    doc = Document()
    
    # --- STYLE CONFIG ---
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(11)
    
    # --- TITLE ---
    title = doc.add_heading('Luxe Stay – Hotel Management System', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph('Project Report & Documentation', style='Subtitle').alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('Developed by: [Your Name] | UET BBIT 25\'', style='Body Text').alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_page_break()

    # --- 1. INTRODUCTION ---
    doc.add_heading('1. Project Overview', level=1)
    p = doc.add_paragraph(
        "The 'Luxe Stay' Hotel Management System is a comprehensive software solution designed to streamline "
        "the daily operations of a luxury hotel. Built using Python, it offers a versatile multi-platform experience, "
        "allowing users to interact with the system via a Command Line Interface (CLI), a Native Desktop GUI, or a "
        "Modern Web Application."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_paragraph(
        "Key goals of the project included robust data persistence, cloud synchronization, role-based security, "
        "and a premium 'Royal Suite' aesthetic across all graphical interfaces."
    )

    # --- 2. TECHNOLOGY STACK ---
    doc.add_heading('2. Technology Stack', level=1)
    
    table = doc.add_table(rows=1, cols=2)
    table.style = 'Light Shading Accent 1'
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Component'
    hdr_cells[1].text = 'Technologies Used'
    
    data = [
        ("Core Backend", "Python 3.13"),
        ("Data Persistence", "File System (.txt) & Google Sheets (Cloud API)"),
        ("Web Server", "Flask + Waitress (Production WSGI)"),
        ("Web Frontend", "HTML5, CSS3 (Custom 'Royal Suite' Theme), JavaScript (ES6+)"),
        ("Desktop GUI", "CustomTkinter (Modern Dark Mode UI)"),
        ("Networking", "REST API (JSON) + Python Requests")
    ]
    
    for item, tech in data:
        row_cells = table.add_row().cells
        row_cells[0].text = item
        row_cells[1].text = tech

    # --- 3. KEY FEATURES ---
    doc.add_heading('3. Key Features', level=1)
    
    features = [
        ("Role-Based Access Control", "Four distinct roles (Admin, Receptionist, Manager, Worker) with tailored dashboards and permission sets."),
        ("Room Management", "Full CRUD capabilities for rooms, including dynamic pricing and availability tracking."),
        ("Guest Operations", "Streamlined booking process with real-time room checking, guest checking-in, and automated billing upon checkout."),
        ("Cloud Sync", "Optional integration with Google Sheets allows data to be viewed and backed up remotely via a custom App Script."),
        ("Financial Reporting", "Instant generation of revenue reports and billing summaries."),
        ("Staff & Task Management", "Admins can manage staff accounts and assign tasks. Workers can view and complete their assigned duties."),
        ("Attendance System", "Digital clock-in/clock-out functionality with printable reports.")
    ]
    
    for title, desc in features:
        p = doc.add_paragraph()
        runner = p.add_run(f"♦ {title}: ")
        runner.bold = True
        p.add_run(desc)

    doc.add_page_break()

    # --- 4. INTERFACE SHOWCASE ---
    doc.add_heading('4. Interface Showcase', level=1)

    # A. Web Interface
    doc.add_heading('A. Web Interface (index.html)', level=2)
    doc.add_paragraph(
        "The web interface features a 'Royal Suite' dark theme with gold accents, fully responsive layout, "
        "and AJAX-based dynamic content loading."
    )
    
    if os.path.exists("web_screenshot.png"):
        doc.add_picture("web_screenshot.png", width=Inches(6.0))
        doc.add_paragraph("Figure 1: Main Web Landing & Login Page", style='Caption')
    else:
        doc.add_paragraph("[IMAGE MISSING: web_screenshot.png]")

    doc.add_paragraph("\n")

    # B. Desktop GUI
    doc.add_heading('B. Desktop GUI (gui_app.py)', level=2)
    doc.add_paragraph(
        "The Desktop Application provides a native Windows experience using CustomTkinter. "
        "It mirrors the web theme exactly, ensuring brand consistency."
    )
    
    # Placeholder for GUI
    p = doc.add_paragraph()
    run = p.add_run("[USER ACTION REQUIRED: Please paste a screenshot of the running 'gui_app.py' window here]")
    run.font.color.rgb = list(range(3))[0] # Just a hack to access color object, actually simpler:
    from docx.shared import RGBColor
    run.font.color.rgb = RGBColor(255, 0, 0)
    run.bold = True
    
    # C. Console Interface
    doc.add_heading('C. Console Interface (main.py)', level=2)
    doc.add_paragraph(
        "The Command Line Interface provides a robust, fail-safe method for administrators to manage the system "
        "even without a graphical environment."
    )
    
    # Placeholder for Console
    p = doc.add_paragraph()
    run = p.add_run("[USER ACTION REQUIRED: Please paste a screenshot of the running 'main.py' console here]")
    run.font.color.rgb = RGBColor(255, 0, 0)
    run.bold = True

    # --- 5. CONCLUSION ---
    doc.add_heading('5. Conclusion', level=1)
    doc.add_paragraph(
        "The project successfully meets all requirements for a modern Hotel Management System. "
        "By leveraging a decoupled architecture (Backend API + Multiple Frontends), the system remains scalable "
        "and maintainable. The addition of Cloud Sync ensures data safety, while the high-fidelity UI provides "
        "an excellent user experience."
    )

    # Save
    doc.save('Project_Report.docx')
    print("Report generated successfully: Project_Report.docx")

if __name__ == "__main__":
    create_report()
