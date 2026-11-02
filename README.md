🏥 Smart Hospital Queue

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=190&color=0:102B3F,50:087E83,100:66DEC5&text=SMART%20HOSPITAL%20QUEUE&fontSize=32&fontColor=FFFFFF&fontAlignY=42&desc=PATIENT%20QUEUE%20MANAGEMENT%20SYSTEM&descSize=13&descAlignY=62" width="100%" />
</p><p align="center">
  <strong>BETTER ORGANIZATION. SIMPLER PATIENT FLOW.</strong>
</p><p align="center">
  A Python-based hospital queue management project with a Streamlit application and a separate web interface.
</p><p align="center">
  <img src="https://skillicons.dev/icons?i=python,html,css,js" height="42" />
  <img src="https://img.shields.io/badge/Streamlit-087E83?style=flat-square&logo=streamlit&logoColor=white" height="24" />
</p>---

01. Project Overview

Smart Hospital Queue is designed to simplify patient registration and organize hospital waiting queues.

The project provides two independent applications:

Python Application

- Developed using Python and Streamlit.
- Provides patient registration and queue management.

Web Application

- Developed using HTML, CSS, and JavaScript.
- Provides a browser-based queue management interface.

The system supports token generation, queue monitoring, next-patient calling, and waiting-time estimation.

---

02. Features

Patient Registration

Register patients by entering their names.

Token Generation

Automatically assign sequential token numbers.

Queue Management

Display patients in their waiting order.

Next Patient

Call the next patient and update the waiting queue.

Waiting Time Estimation

Estimate waiting time according to the patient's position.

Web Dashboard

The browser interface displays queue statistics, including waiting patients, serving token, next token, and estimated waiting time.

Additional Web Controls

- Remove individual waiting patients.
- Clear the waiting queue.
- Retain queue state through browser local storage.

---

03. Technologies Used

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,html,css,js" />
</p><p align="center">
  <img src="https://img.shields.io/badge/STREAMLIT-Application-087E83?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>- Python — Application logic
- Streamlit — Python application interface
- HTML5 — Web structure
- CSS3 — Web styling
- JavaScript — Browser functionality

---

04. Patient Queue Workflow

flowchart TD
    A([Patient Arrives]) --> B[Patient Registration]
    B --> C[Generate Token]
    C --> D[Join Waiting Queue]
    D --> E[Estimate Waiting Time]
    E --> F[Call Next Patient]
    F --> G([Patient Served])

    style A fill:#087E83,color:#fff
    style G fill:#087E83,color:#fff
    style B fill:#DDF5EF,color:#12304A
    style C fill:#DDF5EF,color:#12304A
    style D fill:#DDF5EF,color:#12304A
    style E fill:#DDF5EF,color:#12304A
    style F fill:#DDF5EF,color:#12304A

Waiting Time Calculation

Estimated Waiting Time = Patients Ahead × 10 Minutes

Example:

- Position 1 — 0 minutes
- Position 2 — 10 minutes
- Position 3 — 20 minutes
- Position 4 — 30 minutes
- Position 5 — 40 minutes

This is a basic fixed estimate, not a real-time prediction of doctor availability.

---

05. Project Structure

Smart-Hospital-Queue/
│
├── README.md
├── hospital_gui.py
├── index.html
└── requirements.txt

---

06. Installation and Execution

Step 1 — Clone the Repository

git clone https://github.com/saaqibmohiddin/Smart-Hospital-Queue.git

Step 2 — Open the Project Folder

cd Smart-Hospital-Queue

Step 3 — Install Required Packages

pip install -r requirements.txt

Step 4 — Run the Python Application

streamlit run hospital_gui.py

Step 5 — Open the Web Application

Open the "index.html" file in your web browser.

---

07. Developer

<p align="center">
  <strong>SAAQIB MOHIDDIN</strong>
  <br/>
  Computer Science and Engineering
  <br/>
  Artificial Intelligence
</p><p align="center">
  <a href="https://github.com/saaqibmohiddin">
    <img src="https://img.shields.io/badge/VISIT%20MY%20GITHUB%20PROFILE-102B3F?style=for-the-badge&logo=github&logoColor=66DEC5" />
  </a>
</p><p align="center">
  <a href="https://github.com/saaqibmohiddin/Smart-Hospital-Queue">
    View Smart Hospital Queue Repository
  </a>
</p>---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:66DEC5,50:087E83,100:102B3F&section=footer" width="100%" />
  <strong>SMART HOSPITAL QUEUE</strong>
  <br/>
  <sub>Organized Queues. Better Patient Flow.</sub>
</p>