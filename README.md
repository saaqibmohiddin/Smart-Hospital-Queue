SMART HOSPITAL QUEUE

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=240&color=0:102A43,35:087E8B,70:14B8A6,100:99F6E4&text=SMART%20HOSPITAL%20QUEUE&fontSize=35&fontColor=FFFFFF&fontAlignY=42&desc=PATIENT%20FLOW%20MANAGEMENT%20SYSTEM&descSize=14&descAlignY=64" width="100%" />
</p><p align="center">
  <strong>SIMPLIFYING HOSPITAL QUEUES THROUGH SMART MANAGEMENT</strong>
</p><p align="center">
  Patient Registration &nbsp; • &nbsp; Token Management &nbsp; • &nbsp; Waiting Time
</p><p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/PYTHON-102A43?style=for-the-badge&logo=python&logoColor=5EEAD4" /></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/STREAMLIT-087E8B?style=for-the-badge&logo=streamlit&logoColor=white" /></a>
  <img src="https://img.shields.io/badge/HTML5-E76F51?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-2563EB?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JAVASCRIPT-D6A928?style=for-the-badge&logo=javascript&logoColor=white" />
</p>---

01 / PROJECT INTRODUCTION

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:087E8B,100:102A43&text=HEALTHCARE%20QUEUE%20MANAGEMENT&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>Smart Hospital Queue is a Python-based application designed to organize patient waiting queues and simplify basic hospital queue operations.

The project contains two independent interfaces:

- Python application developed with Streamlit.
- Browser application developed with HTML, CSS, and JavaScript.

The system supports patient registration, automatic token generation, queue display, next-patient calling, and estimated waiting times.

---

02 / APPLICATION FEATURES

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:102A43,100:087E8B&text=PATIENT%20MANAGEMENT&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>01. Patient Registration

Register a patient by entering their name.

02. Token Generation

Automatically generate a sequential token number for every new patient.

03. Waiting Queue

Display the registered patients in their waiting order.

04. Call Next Patient

Call the first patient in the queue and remove them from the waiting list.

05. Waiting Time Estimation

Calculate estimated waiting time based on the number of patients ahead.

06. Queue Dashboard

The browser interface displays:

- Total waiting patients.
- Currently serving token.
- Next token number.
- Estimated total waiting time.

07. Queue Controls

The browser interface supports individual patient removal and clearing the waiting queue.

---

03 / HEALTHCARE DESIGN LANGUAGE

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:0F766E,100:102A43&text=CLINICAL%20VISUAL%20IDENTITY&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>The visual direction is inspired by modern hospital dashboards, patient-care systems, and clinical information interfaces.

Primary Color Palette

<p align="center">
  <img src="https://placehold.co/130x55/102A43/FFFFFF?text=HOSPITAL+BLUE" width="24%" />
  <img src="https://placehold.co/130x55/087E8B/FFFFFF?text=MEDICAL+TEAL" width="24%" />
  <img src="https://placehold.co/130x55/5EEAD4/102A43?text=CLINICAL+MINT" width="24%" />
  <img src="https://placehold.co/130x55/F1F7FA/102A43?text=ICE+WHITE" width="24%" />
</p>Hospital Blue — "#102A43"

Primary identity, headers, and important sections.

Medical Teal — "#087E8B"

Main actions, interactive elements, and highlights.

Clinical Mint — "#5EEAD4"

Positive indicators and secondary accents.

Ice White — "#F1F7FA"

Clean backgrounds and content surfaces.

Soft Aqua — "#E2F5EE"

Information panels and supporting sections.

Alert Coral — "#E76F68"

Warnings and destructive actions.

Visual Design Principles

- Professional healthcare appearance.
- Clean dashboard-inspired presentation.
- Consistent visual hierarchy.
- Clear token and queue information.
- Readable typography.
- Responsive browser layout.
- Meaningful colors for different actions.

---

04 / TECHNOLOGY ARCHITECTURE

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:102A43,100:2563EB&text=TECHNOLOGY%20STACK&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>Python Application

<img src="https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/STREAMLIT-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />The Streamlit application handles patient registration, token generation, queue display, and next-patient calling using session state.

Browser Application

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/JAVASCRIPT-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />The browser application provides a separate queue interface with local storage for retaining its queue state.

---

05 / QUEUE PROCESS

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:087E8B,100:102A43&text=PATIENT%20FLOW&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>        PATIENT ARRIVAL
               |
               v
       PATIENT REGISTRATION
               |
               v
         TOKEN GENERATION
               |
               v
        WAITING QUEUE
               |
               v
       WAITING TIME ESTIMATE
               |
               v
       CALL NEXT PATIENT
               |
               v
         PATIENT SERVED

---

06 / WAITING TIME CALCULATION

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:102A43,100:0F766E&text=WAITING%20TIME%20LOGIC&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>The application uses a simple fixed waiting-time estimation rule.

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Arial&weight=bold&size=18&duration=3000&pause=1000&color=087E8B&center=true&vCenter=true&width=500&lines=Waiting+Time+%3D+Patients+Ahead+%C3%97+10+Minutes" />
</p>Example:

- First patient: 0 minutes.
- Second patient: 10 minutes.
- Third patient: 20 minutes.
- Fourth patient: 30 minutes.
- Fifth patient: 40 minutes.

This is a basic demonstration estimate and does not represent actual doctor availability.

---

07 / PROJECT STRUCTURE

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:102A43,100:087E8B&text=APPLICATION%20FILES&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>Smart-Hospital-Queue/
│
├── README.md
├── hospital_gui.py
├── index.html
└── requirements.txt

hospital_gui.py

Python Streamlit application.

index.html

Browser-based HTML, CSS, and JavaScript application.

requirements.txt

Python dependency list.

README.md

Project documentation.

---

08 / INSTALLATION & EXECUTION

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:087E8B,100:102A43&text=GET%20STARTED&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>STEP 01 — Clone Repository

git clone https://github.com/saaqibmohiddin/Smart-Hospital-Queue.git

STEP 02 — Open Project Folder

cd Smart-Hospital-Queue

STEP 03 — Install Dependencies

pip install -r requirements.txt

STEP 04 — Start Python Application

streamlit run hospital_gui.py

STEP 05 — Start Browser Application

Open "index.html" in your browser.

---

09 / PROJECT OBJECTIVES

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:102A43,100:087E8B&text=PROJECT%20GOALS&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>- Simplify patient registration.
- Organize hospital waiting queues.
- Generate unique patient tokens.
- Make queue status easier to understand.
- Provide basic waiting-time estimates.
- Reduce manual queue-management effort.

---

10 / FUTURE DEVELOPMENT

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:087E8B,100:0F766E&text=FUTURE%20ROADMAP&fontSize=20&fontColor=FFFFFF" width="100%" />
</p>Planned Improvement| Purpose
Database Integration| Persistent patient records
Doctor Management| Doctor-wise queue handling
Department Management| Separate department queues
Appointment Scheduling| Manage patient appointments
QR Token Generation| Simplify token access
SMS Notifications| Notify patients
Admin Dashboard| Centralized queue monitoring
Emergency Priority| Prioritize emergency patients

---

11 / DEVELOPER

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=150&color=0:102A43,50:087E8B,100:5EEAD4&text=SAAQIB%20MOHIDDIN&fontSize=30&fontColor=FFFFFF&fontAlignY=40&desc=COMPUTER%20SCIENCE%20%26%20ENGINEERING%20%7C%20AI&descSize=12&descAlignY=65" width="100%" />
</p><p align="center">
  <a href="https://github.com/saaqibmohiddin">
    <img src="https://img.shields.io/badge/VISIT%20GITHUB-102A43?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=130&color=0:5EEAD4,50:087E8B,100:102A43&section=footer" width="100%" />
</p><p align="center">
  <strong>SMART HOSPITAL QUEUE</strong>
  <br/>
  <sub>ORGANIZED QUEUES. BETTER PATIENT FLOW.</sub>
</p>