<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:102D42,50:087E83,100:62D9C1&text=SMART%20HOSPITAL%20QUEUE&fontSize=35&fontColor=FFFFFF&fontAlignY=40&desc=SMART%20PATIENT%20FLOW%20%7C%20DIGITAL%20QUEUE%20MANAGEMENT&descSize=13&descAlignY=60" width="100%" /

Smarter Queues. Reduced Waiting. Better Patient Experience.

<p>
  <img src="https://img.shields.io/badge/Project-Healthcare%20Technology-087E83?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-Streamlit-102D42?style=for-the-badge&logo=streamlit&logoColor=62D9C1" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-087E83?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Development-62D9C1?style=for-the-badge" />
</p><p>
 
</p></div>

## 🩺 ABOUT THE PROJECT

Smart Hospital Queue is a healthcare-focused queue management application developed to simplify patient registration and organize hospital waiting queues.

Traditional hospital queues often involve long waiting periods, manual token management, and inefficient patient flow.

This project provides a digital approach to managing patient queues through token generation, queue tracking, and estimated waiting times.

The project includes two application interfaces:

- Python Application: Developed using Streamlit.
- Web Application: Developed using HTML, CSS, and JavaScript.

The goal is to make hospital queue management more organized, accessible, and efficient.

✨ Key Features

🏥 Patient Management

- Register patients using their names.
- Validate patient name input.
- Add patients to the waiting queue.

🎫 Digital Token Generation

- Automatically generate sequential token numbers.
- Assign unique tokens to registered patients.
- Maintain patient registration order.

👥 Queue Management

- Display patients in waiting order.
- View the current waiting queue.
- Remove individual patients in the web application.
- Clear the waiting queue in the web application.

📢 Patient Calling System

- Call the next patient.
- Automatically remove the called patient from the waiting queue.
- Display the currently serving token.

⏱️ Waiting Time Estimation

- Calculate estimated waiting time using queue position.
- Display individual patient waiting estimates.
- Use a configurable demonstration assumption of 10 minutes per patient ahead.

📊 Dashboard

- Display total waiting patients.
- Show the currently serving token.
- Display the next token number.
- Show estimated waiting time.

💾 Queue State Management

- Python application uses Streamlit session state.
- Web application uses browser Local Storage to retain queue data.

---

## 🛠️ TECHNOLOGY STACK


<p>
  <img src="https://img.shields.io/badge/PYTHON-102D42?style=for-the-badge&logo=python&logoColor=62D9C1" />
  <img src="https://img.shields.io/badge/STREAMLIT-087E83?style=for-the-badge&logo=streamlit&logoColor=white" />
</p><p>
  <img src="https://img.shields.io/badge/HTML5-102D42?style=for-the-badge&logo=html5&logoColor=62D9C1" />
  <img src="https://img.shields.io/badge/CSS3-087E83?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JAVASCRIPT-102D42?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
</p><p>
  <img src="https://img.shields.io/badge/LOCAL%20STORAGE-087E83?style=for-the-badge&logo=googlechrome&logoColor=white" />
</p>

</div>

## 🔄 How The System Works

        PATIENT ARRIVES
               |
               ▼
       PATIENT REGISTRATION
               |
               ▼
        TOKEN GENERATION
               |
               ▼
        JOIN WAITING QUEUE
               |
               ▼
      WAITING TIME ESTIMATION
               |
               ▼
       CALL NEXT PATIENT
               |
               ▼
       PATIENT IS SERVED
               |
               ▼
        QUEUE IS UPDATED




## 📁 Project Structure

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&height=65&color=0:102D42,50:087E83,100:62D9C1&text=PROJECT%20DIRECTORY&fontSize=23&fontColor=FFFFFF" width="100%" />

</div>

<pre>
Smart-Hospital-Queue/
│
├── README.md
│
├── hospital_gui.py
│
├── index.html
│
└── requirements.txt
</pre>

<div align="center">

**SMART HEALTHCARE · SMART MANAGEMENT**


</div>



</div>

## 🚀 INSTALLATION & SETUP

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&height=130&color=0:102D42,50:087E83,100:62D9C1&text=QUICK%20START&fontSize=30&fontColor=FFFFFF&fontAlignY=50" width="100%" />

</div>🧩 STEP 01 — Prerequisites

- Python installed
- Git installed
- VS Code or any code editor
- Modern web browser

📥 STEP 02 — Get the Project

git clone https://github.com/saaqibmohiddin/Smart-Hospital-Queue.git

📦 STEP 03 — Install Requirements

pip install -r requirements.txt

---

🐍 RUN PYTHON APPLICATION

Streamlit Interface

streamlit run hospital_gui.py

🌐 RUN WEB APPLICATION

Browser Interface

Open "index.html" directly in your browser.

Or use VS Code Live Server.

---

<div align="center"><img src="https://img.shields.io/badge/PROJECT-READY%20TO%20RUN-087E83?style=for-the-badge" />

<sub>Smart Technology for Better Patient Flow.</sub>

</div>

---

## 🎯 Project Objectives

- Digitize traditional hospital queue management.
- Simplify patient registration.
- Automate token generation.
- Improve patient queue organization.
- Provide estimated waiting times.
- Make patient flow easier to manage.
- Demonstrate practical applications of Python and web technologies.

---

## 🔮 Future Enhancements

The following features are potential future improvements:

- AI-based waiting-time prediction.
- Real-time queue synchronization.
- Patient appointment scheduling.
- SMS and WhatsApp notifications.
- QR-code-based patient check-in.
- Doctor availability management.
- Emergency priority queue management.
- Patient history and appointment records.
- Hospital administrator dashboard.
- Database integration.
- Mobile-friendly patient application.

---

## ⚠️ Project Scope & Limitations

This project is currently a demonstration application.

- The Python application maintains its queue in Streamlit session state.
- The web application stores queue information in browser Local Storage.
- The two interfaces do not currently share a centralized database.
- Waiting times are based on a fixed demonstration assumption.
- The application is not intended for production clinical use or emergency triage.

A production deployment would require secure authentication, centralized storage, access control, privacy safeguards, and validated queue-management workflows.

---


<div align="center"><img src="https://capsule-render.vercel.app/api?type=rect&height=80&color=0:102D42,50:087E83,100:62D9C1&text=THE%20DEVELOPER&fontColor=FFFFFF&fontSize=22&fontAlignY=60" width="100%" /><br/>MOHAMMED SAAQIB MOHIDDIN

Computer Science & Engineering

Specialization in Artificial Intelligence

<br/><img src="https://img.shields.io/badge/ROLE-AI &%20%E2%80%A2%20PYTHON%20DEVELOPER-087E83?style=for-the-badge&labelColor=102D42" /><br/><br/>

🌐 CONNECT WITH ME

<a href="https://github.com/saaqibmohiddin">
  <img src="https://img.shields.io/badge/VISIT%20MY%20GITHUB-102D42?style=for-the-badge&logo=github&logoColor=62D9C1" />
</a><br/><br/>

<a href="https://github.com/saaqibmohiddin?tab=repositories">View GitHub Repositories →</a>

<br/><br/>

---

DESIGNED WITH PASSION FOR TECHNOLOGY

</div>