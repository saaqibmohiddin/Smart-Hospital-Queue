🏥 SMART HOSPITAL QUEUE

<div align="center"><img src="https://capsule-render.vercel.app/api?type=rect&height=220&color=0:12304A,45:0B8990,100:55C9A5&text=SMART%20HOSPITAL%20QUEUE&fontSize=34&fontColor=FFFFFF&fontAlignY=42&desc=HEALTHCARE%20%7C%20PATIENT%20FLOW%20%7C%20QUEUE%20MANAGEMENT&descSize=13&descAlignY=62" width="100%" />Smarter Patient Flow. Simpler Queue Management.

An organized and user-friendly approach to hospital patient queues.

<br/>"Python" (https://img.shields.io/badge/Python-12304A?style=flat-square&logo=python&logoColor=white)
"Streamlit" (https://img.shields.io/badge/Streamlit-0B8990?style=flat-square&logo=streamlit&logoColor=white)
"HTML5" (https://img.shields.io/badge/HTML5-E66A3C?style=flat-square&logo=html5&logoColor=white)
"CSS3" (https://img.shields.io/badge/CSS3-2878B5?style=flat-square&logo=css3&logoColor=white)
"JavaScript" (https://img.shields.io/badge/JavaScript-C49A27?style=flat-square&logo=javascript&logoColor=white)

</div>---

◈ PROJECT OVERVIEW

Smart Hospital Queue is a Python-based patient queue management project designed to make hospital waiting-line management simple and organized.

It provides two separate interfaces:

- Python Application: Built using Streamlit.
- Web Application: Built using HTML, CSS, and JavaScript.

The system allows users to register patients, generate token numbers, monitor the waiting queue, call the next patient, and estimate waiting time.

---

◈ CORE FEATURES

Feature| Description
Patient Registration| Add patients using their names
Token Generation| Assign a unique token number
Queue Display| View patients currently waiting
Next Patient| Call the next patient in line
Waiting Estimation| Estimate waiting time based on queue position
Patient Removal| Remove a waiting patient in the web interface
Queue Dashboard| View queue statistics in the web interface
Queue Clearing| Clear the waiting queue in the web interface

---

◈ HEALTHCARE DESIGN SYSTEM

The project uses a healthcare-inspired visual direction focused on clarity, trust, accessibility, and simplicity.

Color Palette

Color Name| Hex| Usage
Hospital Blue| "#12304A"| Main identity and headers
Medical Teal| "#0B8990"| Main actions and highlights
Mint Green| "#55C9A5"| Positive status and accents
Clean White| "#F4F8FB"| Background
Soft Mint| "#DCEFEB"| Information sections
Alert Coral| "#E66A65"| Warning and removal actions
Slate Text| "#25364A"| Readable text

UI / UX Direction

- Professional healthcare dashboard appearance.
- Clear patient token visibility.
- Structured queue presentation.
- Simple registration workflow.
- Consistent spacing and typography.
- Responsive web layout.
- Easy-to-understand status indicators.

---

◈ TECHNOLOGY STACK

<div align="center">Technology| Implementation
Python| Core application logic
Streamlit| Python application interface
HTML5| Web interface structure
CSS3| Web interface styling
JavaScript| Queue operations in browser
Local Storage| Browser queue-state persistence

</div>---

◈ PATIENT QUEUE WORKFLOW

       PATIENT ARRIVES
              |
              ▼
      PATIENT REGISTRATION
              |
              ▼
       TOKEN GENERATION
              |
              ▼
       ADD TO WAITING QUEUE
              |
              ▼
      WAITING TIME ESTIMATE
              |
              ▼
       CALL NEXT PATIENT
              |
              ▼
        PATIENT SERVED

---

◈ PROJECT ARCHITECTURE

Smart-Hospital-Queue/
│
├── README.md
│
├── hospital_gui.py
│
├── index.html
│
└── requirements.txt

File Responsibilities

File| Responsibility
"hospital_gui.py"| Streamlit-based patient queue application
"index.html"| HTML/CSS/JavaScript browser interface
"requirements.txt"| Python package requirements
"README.md"| Project documentation

---

◈ GETTING STARTED

Step 01 — Clone Repository

git clone https://github.com/saaqibmohiddin/Smart-Hospital-Queue.git

Step 02 — Navigate to Project

cd Smart-Hospital-Queue

Step 03 — Install Dependencies

pip install -r requirements.txt

Step 04 — Launch Python Application

streamlit run hospital_gui.py

Step 05 — Open Web Application

Open "index.html" in your preferred web browser.

---

◈ WAITING TIME LOGIC

The project uses a simple waiting-time estimation rule:

Estimated Waiting Time = Patients Ahead × 10 Minutes

For example:

Queue Position| Estimated Waiting Time
First patient| 0 minutes
Second patient| 10 minutes
Third patient| 20 minutes
Fourth patient| 30 minutes
Fifth patient| 40 minutes

This is a basic estimate, not a real-time prediction of doctor availability.

---

◈ PROJECT OBJECTIVES

- Organize hospital patient queues.
- Simplify patient registration.
- Reduce manual queue-handling effort.
- Provide token-based patient identification.
- Display estimated waiting times.
- Improve visibility of the waiting queue.

---

◈ FUTURE DEVELOPMENT

Potential improvements for future versions:

- Database integration for persistent patient records.
- Doctor and department-wise queues.
- Appointment scheduling.
- QR-based patient tokens.
- SMS notifications.
- Administrative dashboard.
- Emergency priority handling.
- More accurate waiting-time estimation.

---


<div align="center">SAAQIB MOHIDDIN

Computer Science and Engineering
Artificial Intelligence

""GitHub" (https://img.shields.io/badge/GitHub-Visit%20Profile-12304A?style=for-the-badge&logo=github&logoColor=white)" (https://github.com/saaqibmohiddin)

</div>---

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:55C9A5,50:0B8990,100:12304A&height=110&section=footer" width="100%" />SMART HOSPITAL QUEUE

Organized Queues. Better Patient Flow.

</div>