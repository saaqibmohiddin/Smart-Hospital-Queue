🏥 SMART HOSPITAL QUEUE

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:102D42,45:087E83,100:65D9C0&text=SMART%20HOSPITAL%20QUEUE&fontSize=34&fontColor=FFFFFF&fontAlignY=40&desc=PATIENT%20FLOW%20MANAGEMENT%20SYSTEM&descSize=14&descAlignY=60" width="100%" />
</p><p align="center">
  <strong>ORGANIZED QUEUES. EFFICIENT PATIENT FLOW.</strong>
</p><p align="center">
  A simple and user-friendly solution for hospital patient queue management.
</p>---

🩺 ABOUT THE PROJECT

Smart Hospital Queue is a Python-based project designed to simplify patient registration and hospital waiting-line management.

It provides two separate interfaces:

- Streamlit Application — A Python-based graphical interface.
- Web Application — A browser-based interface developed using HTML, CSS, and JavaScript.

The system helps manage patient tokens, organize waiting queues, call the next patient, and estimate waiting time.

---

✦ SYSTEM FEATURES

01 — Patient Registration

Register patients by entering their names.

02 — Token Generation

Automatically assign a unique token number to each registered patient.

03 — Queue Management

Display patients in their waiting order.

04 — Next Patient

Call the next patient and update the queue.

05 — Waiting Time Estimation

Estimate waiting time using the patient's position in the queue.

06 — Queue Dashboard

The browser interface displays:

- Total patients waiting
- Currently serving token
- Next token number
- Estimated total waiting time

07 — Queue Controls

The browser interface also supports removing individual patients and clearing the waiting queue.

---

🎨 DESIGN SYSTEM

The README and project presentation follow a modern healthcare dashboard design.

Visual Identity

Color| Hex Code| Application
Deep Hospital Blue| "#102D42"| Main identity
Medical Teal| "#087E83"| Actions and highlights
Clinical Mint| "#65D9C0"| Positive accents
Ice White| "#F4F8FA"| Background
Soft Aqua| "#E8F4F3"| Information sections
Slate| "#263B4A"| Typography
Alert Coral| "#E76F68"| Warnings and removal

Design Principles

- Minimal and professional layout
- Healthcare-inspired color palette
- Clear visual hierarchy
- Easy-to-read patient information
- Consistent spacing and typography
- Mobile-friendly web interface

---

⚙️ TECHNOLOGY STACK

Technology| Role
Python| Application logic
Streamlit| Python graphical interface
HTML5| Web page structure
CSS3| Styling and responsive layout
JavaScript| Browser queue operations
Local Storage| Browser queue-state storage

---

🔄 HOW THE SYSTEM WORKS

       PATIENT ARRIVES
              |
              ▼
      REGISTER PATIENT
              |
              ▼
       GENERATE TOKEN
              |
              ▼
        JOIN QUEUE
              |
              ▼
      ESTIMATE WAIT TIME
              |
              ▼
      CALL NEXT PATIENT
              |
              ▼
        PATIENT SERVED

---

⏱️ WAITING TIME CALCULATION

The project uses a basic waiting-time estimation method.

Estimated Waiting Time = Number of Patients Ahead × 10 Minutes

Example:

Patient Position| Estimated Wait
1| 0 minutes
2| 10 minutes
3| 20 minutes
4| 30 minutes
5| 40 minutes

This is a fixed estimate for demonstration purposes, not a real-time prediction of doctor availability.

---

📁 PROJECT STRUCTURE

Smart-Hospital-Queue/
│
├── README.md
├── hospital_gui.py
├── index.html
└── requirements.txt

File Description

File| Purpose
"hospital_gui.py"| Streamlit-based queue management
"index.html"| Browser-based queue application
"requirements.txt"| Python dependencies
"README.md"| Project documentation

---

🚀 INSTALLATION & EXECUTION

Step 1 — Clone the Repository

git clone https://github.com/saaqibmohiddin/Smart-Hospital-Queue.git

Step 2 — Open the Project Directory

cd Smart-Hospital-Queue

Step 3 — Install Dependencies

pip install -r requirements.txt

Step 4 — Run the Python Application

streamlit run hospital_gui.py

Step 5 — Run the Web Application

Open "index.html" directly in your web browser.

---

🎯 PROJECT OBJECTIVES

- Simplify patient registration.
- Organize hospital waiting queues.
- Generate unique patient tokens.
- Display queue information clearly.
- Estimate patient waiting times.
- Reduce manual queue-management effort.

---

🔮 FUTURE ENHANCEMENTS

- Database integration for patient records
- Doctor-wise and department-wise queues
- Appointment scheduling
- QR-based token generation
- Patient notification system
- Administrative dashboard
- Emergency patient priority management
- Improved waiting-time estimation

---

👨‍💻 DEVELOPER

Saaqib Mohiddin

Computer Science and Engineering

Artificial Intelligence

"GitHub Profile" (https://github.com/saaqibmohiddin)

"Project Repository" (https://github.com/saaqibmohiddin/Smart-Hospital-Queue)

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:65D9C0,50:087E83,100:102D42&section=footer" width="100%" />
</p><p align="center">
  <strong>SMART HOSPITAL QUEUE</strong>
  <br/>
  <sub>Better Organization. Simpler Patient Flow.</sub>
</p>