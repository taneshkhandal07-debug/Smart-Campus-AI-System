# 🎓 Smart Campus AI System

🚀 **Live Demo Link:** https://smart-campus-ai-system.onrender.com  

  **Live Demo login link:** https://smart-campus-ai-system.onrender.com/login

Students at most colleges deal with slow, opaque complaint handling — questions go unanswered for days, complaints submitted on paper or over email disappear into a black box, and there's no way to check status without chasing someone down. Administrative staff juggle complaints across departments with no shared system, leading to duplicated effort and no visibility into what's actually getting resolved.
Smart Campus AI System centralizes this: a chatbot handles common student questions instantly, complaints are submitted and tracked digitally with a unique ID, and each administrative department only sees the complaints relevant to them — solo-built end to end, including the multi-role permission model.

---
## Who this is for

**Students** who need quick answers to routine questions and a way to submit and track complaints without chasing staff for updates.

**Administrative staff** (Admin, HOD, Mentor, TPO, Accounts) who need department-specific visibility into complaints instead of a single shared, unsorted inbox.

**College management**, who need aggregate analytics on complaint volume and resolution speed rather than relying on anecdotal reporting from each department.

---

## 📌 Overview

The **Smart Campus AI System** is a web-based solution that simplifies student support services by integrating:

- 🤖 Intelligent chatbot for instant query resolution  
- 🛠 Complaint management system with tracking  
- 👨‍💼 Role-based admin dashboard  
- 📊 Real-time analytics for issue monitoring  
- 🎨 Modern UI with dark mode & smooth interactions  

This system reduces manual effort and improves communication between students and administration.

---

## ✨ Features

### 🤖 AI Chatbot
- Handles queries related to:
  - Fees 💰
  - Exams 📅
  - Timetable 📚
  - Attendance 📊
- Provides instant responses
- Simulates real-time typing experience
<img width="1920" height="1080" alt="Screenshot 2026-04-14 110117" src="https://github.com/user-attachments/assets/a5aa1c58-5e2f-4f12-9d7a-820aab7f5418" />
*(Rule-based in v1 — see Product Decisions below for why.)*
---

### 🛠 Complaint Management System
- Submit complaints easily
- Unique Complaint ID generation
- Track complaint status:
  - Pending 🟠  
  - Seen 🔵  
  - Resolved 🟢  
  - Delayed 🟣 (auto-detected)
<img width="1920" height="1080" alt="Screenshot (21)" src="https://github.com/user-attachments/assets/b4212702-c683-46b7-bcbf-cbb4ce733eb6" />

---

### 👨‍💼 Role-Based Admin Dashboard
- Different access levels:
  - Admin (Full access)
  - HOD
  - Mentor
  - TPO (Placement)
  - Accounts
- Each role views only relevant complaints
- Status update system with dropdown UI
<img width="1920" height="1080" alt="Screenshot 2026-04-14 110411" src="https://github.com/user-attachments/assets/f9aa0c3d-38d1-495f-8e18-e2fca438b13b" />

---

### 📊 Analytics Dashboard
- Total complaints
- Pending, Seen, Resolved counts
- Helps in monitoring resolution efficiency
<img width="1920" height="1080" alt="Screenshot (40)" src="https://github.com/user-attachments/assets/97a576a6-8e81-4b5b-9f16-4436b75cc985" />
<img width="1920" height="1080" alt="Screenshot (34)" src="https://github.com/user-attachments/assets/34481461-a4e4-49e2-ad38-49a2025b31f7" />


---

### 🎨 Modern UI/UX
- Clean dashboard layout
- Dark mode support 🌙
- Smooth animations & transitions
- Interactive components
<img width="1920" height="1080" alt="Screenshot (35)" src="https://github.com/user-attachments/assets/c42ac94e-278a-420b-b6ce-6374417a7580" />
<img width="1920" height="1080" alt="Screenshot (36)" src="https://github.com/user-attachments/assets/fcaf0557-8630-457c-8ba7-a7caaac96e5e" />


---
## Product Decisions

A few calls made deliberately when scoping v1, rather than just "what I had time to build":

**Rule-based chatbot over generative AI, for v1.** The chatbot resolves a fixed set of common query categories (fees, exams, timetable, attendance) using rule-based logic rather than an LLM. This kept response behavior predictable and easy to validate for a first release — generative AI chatbot capability is explicitly scoped for Phase 3, once there's more usage data to ground it in.

**Five roles, not one shared inbox.** Modeling Admin, HOD, Mentor, TPO, and Accounts as separate access levels — each seeing only their relevant complaints — was a deliberate design choice over a simpler single-queue system, because a shared inbox doesn't reflect how complaint ownership actually works across departments. This was the most complex piece of the product to reason through solo, since it meant mapping which complaint categories belong to which real-world department.

**Delayed-complaint detection was automated, not manual.** Rather than relying on staff to notice an overdue complaint, the system automatically flags anything that exceeds its expected resolution timeline — directly targeting the lack of complaint transparency identified as a core pain point.

**No mobile app or external integrations (WhatsApp, SMS) in v1.** Scoped out deliberately to ship a working web platform first; both are on the Phase 2/3 roadmap rather than cut entirely.

**Deliberately out of scope for v1:** email/SMS notifications, automated complaint routing, voice-enabled chatbot, mobile app, WhatsApp integration, sentiment analysis — all roadmapped for later phases.

---

## How Success Was Defined

Rather than just "does it run," the project was scoped against:
- Complaint submission rate and chatbot usage frequency
- Average resolution time and resolution rate
- Delayed-complaint percentage
- Reduction in administrative workload (qualitative)

---

## 🛠 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
Smart-Campus-AI-System/

│
├── data/
│   └── complaints.txt          # flat-file storage for submitted complaints
│
├── static/
│   └── (CSS, JS, and other front-end assets)
│
├── templates/
│   ├── index.html              # student-facing chatbot + complaint UI
│   ├── login.html              # admin/staff login
│   └── admin.html              # role-filtered complaint dashboard
│
├── app.py                      # Flask routes, auth, role-based filtering
├── utils.py                    # chatbot logic, complaint save/retrieve helpers
├── requirements.txt
└── README.md
```
