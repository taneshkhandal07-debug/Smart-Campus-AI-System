# 🎓 Smart Campus AI System

**🚀 [Live Demo](https://smart-campus-ai-system.onrender.com)** &nbsp;|&nbsp; **[Login](https://smart-campus-ai-system.onrender.com/login)**

Students at most colleges deal with slow, opaque complaint handling — questions go unanswered for days, complaints get submitted on paper or over email and then disappear into a black box, and there's no way to check status without chasing someone down. Administrative staff, meanwhile, are juggling complaints across departments with no shared system, which means duplicated effort and no visibility into what's actually getting resolved.

Smart Campus AI System centralizes this: a chatbot handles common student questions instantly, complaints are submitted and tracked digitally with a unique ID, and each administrative department only sees the complaints relevant to them — solo-built end to end, including the multi-role permission model.

---

## Who this is for

**Students** who need quick answers to routine questions and a way to submit and track complaints without chasing staff for updates.

**Administrative staff** (Admin, HOD, Mentor, TPO, Accounts) who need department-specific visibility into complaints instead of a single shared, unsorted inbox.

**College management**, who need aggregate analytics on complaint volume and resolution speed rather than relying on anecdotal reporting from each department.

---

## ⚡ Key Features

### 🤖 AI Chatbot
Handles common student queries instantly across four categories — fees, exams, timetable, and attendance — so students get answers without needing to contact staff directly. *(Rule-based in v1; see Product Decisions below.)*

![AI Chatbot](./Screenshot%20(19).png)

### 🛠️ Complaint Management System
Students submit complaints through a digital form and receive a unique Complaint ID for tracking. Status moves through four states:
- 🟠 Pending &nbsp; 🔵 Seen &nbsp; 🟢 Resolved &nbsp; 🟣 Delayed *(auto-detected when a complaint exceeds its resolution timeline)*

![Complaint Tracking](./Screenshot%20(21).png)

### 👨‍💼 Role-Based Admin Dashboard
Five distinct access levels, each scoped to relevant complaints only:
- **Admin** — full access, all complaints
- **HOD** — department-related complaints
- **Mentor** — student welfare complaints
- **TPO** — placement-related complaints
- **Accounts** — fee-related complaints

![Role-Based Dashboard](./Screenshot%20(20).png)

### 📊 Analytics Dashboard
Real-time view of total, pending, seen, and resolved complaints — built so management can monitor resolution efficiency without pulling manual reports.

![Analytics Dashboard](./Screenshot%20(40).png)

### 🎨 Modern UI/UX
Responsive layout, dark mode, and smooth transitions across the dashboard.

![UI Dark Mode](./Screenshot%20(35).png)

---

## Product Decisions

A few calls made deliberately when scoping v1, rather than just "what I had time to build":

**Rule-based chatbot over generative AI, for v1.** The chatbot resolves a fixed set of common query categories (fees, exams, timetable, attendance) using rule-based logic rather than an LLM. This kept response behavior predictable and easy to validate for a first release — generative AI chatbot capability is explicitly scoped for Phase 3, once there's more usage data to ground it in.

**Five roles, not one shared inbox.** Modeling Admin, HOD, Mentor, TPO, and Accounts as separate access levels — each seeing only their relevant complaints — was a deliberate design choice over a simpler single-queue system, because a shared inbox doesn't reflect how complaint ownership actually works across departments. This was the most complex piece of the product to reason through solo, since it meant mapping which complaint categories belong to which real-world department.

**Delayed-complaint detection was automated, not manual.** Rather than relying on staff to notice an overdue complaint, the system automatically flags anything that exceeds its expected resolution timeline — directly targeting the "lack of complaint transparency" problem identified as a core pain point.

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

## 🛠️ Tech Stack

**Backend:** Python (Flask) &nbsp;|&nbsp; **Frontend:** HTML, CSS, JavaScript &nbsp;|&nbsp; **Database:** SQLite &nbsp;|&nbsp; **Deployment:** Render &nbsp;|&nbsp; **Version Control:** Git & GitHub

---

## 👨‍💻 Author

**Tanesh Khandal**
🎓 JECRC University — Cybersecurity & Tech Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a star and sharing it!

