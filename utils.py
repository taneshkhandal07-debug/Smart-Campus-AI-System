import datetime
import random
import os

# ====== 🔗 UPDATE THESE LINKS ======
SYLLABUS_LINK = "https://jecrcuniversity.edu.in/admission/b-tech-computer-science-and-engineering/"
TIMETABLE_LINK = "https://drive.google.com/drive/folders/1r5uJ5ZiQaETAEqDjh9h6jAIZGUnXWxyy?usp=drive_link"


# ================= CHATBOT ================= #

def chatbot_reply(user_input):
    text = user_input.lower()

    # ---------- GREETINGS ----------
    if any(word in text for word in ["hi", "hello", "hey"]):
        return random.choice([
            "👋 Hey! How can I help you today?",
            "Hello! Ask me anything related to campus 😊",
            "Hi there! Need help with fees, exams or anything?"
        ])

    # ---------- SYLLABUS (WITH BUTTON) ----------
    elif any(word in text for word in ["syllabus", "subject", "course", "curriculum", "modules"]):
        return f'''
📚 You can access the syllabus here:<br><br>
<a href="{SYLLABUS_LINK}" target="_blank">
<button class="chat-btn">📚 Open Syllabus</button>
</a>
'''

    # ---------- TIMETABLE (WITH BUTTON) ----------
    elif any(word in text for word in ["timetable", "time table", "schedule", "routine", "class timing"]):
        return f'''
📅 You can access the timetable here:<br><br>
<a href="{TIMETABLE_LINK}" target="_blank">
<button class="chat-btn">📅 Open Timetable</button>
</a>
'''

    # ---------- NAVIGATION ----------
    elif any(word in text for word in ["library", "lab", "canteen", "admin", "location"]):
        return random.choice([
            "📍 It's located near the main academic block.",
            "📍 You’ll find it in the central campus area.",
            "📍 Check signboards."
        ])

    # ---------- EXAMS ----------
    elif any(word in text for word in ["exam", "test", "midterm", "endterm"]):
        return random.choice([
            "📅 You can check exam schedule on ERP → Exams section.",
            "📅 Exam details are available on ERP and notice board.",
            "📅 Login to ERP to view your exam timetable."
        ])

    # ---------- FEES ----------
    elif any(word in text for word in ["fee", "payment", "fees", "pay"]):
        return random.choice([
            "💰 Pay fees through ERP → Fees section.",
            "💰 You can pay online via ERP portal.",
            "💰 For issues, contact accounts@jecrcu.edu.in"
        ])

    # ---------- COMPLAINT ----------
    elif any(word in text for word in ["wifi", "issue", "problem", "not working", "complaint", "error"]):
        return random.choice([
            "🛠 You can submit this issue in the Complaints section.",
            "🛠 Please use the complaint panel to report this.",
            "🛠 I suggest raising a complaint for quick resolution."
        ])

    # ---------- ATTENDANCE ----------
    elif any(word in text for word in ["attendance", "present", "absent"]):
        return random.choice([
            "📊 Check attendance via ERP dashboard.",
            "📊 Login to ERP → Attendance section.",
            "📊 Attendance details are available on ERP."
        ])

    # ---------- CONTACT ----------
    elif any(word in text for word in ["contact", "email", "support"]):
        return "📞 Check the FAQs & Contact section for all details."

    # ---------- TIMINGS ----------
    elif any(word in text for word in ["timing", "college time"]):
        return "⏰ College usually runs from 9 AM to 5 PM."

    # ---------- EMERGENCY ----------
    elif any(word in text for word in ["urgent", "emergency"]):
        return "🚨 Call 1800-120-5616 or visit Admin Block (NYB)."

    # ---------- HELP ----------
    elif "help" in text:
        return (
            "🤖 I can help you with:<br>"
            "• Fees 💰<br>"
            "• Exams 📅<br>"
            "• Complaints 🛠<br>"
            "• Attendance 📊<br>"
            "• Syllabus 📚<br>"
            "• Timetable 📅<br><br>"
            "Try asking something like 'Show timetable'"
        )

    # ---------- DEFAULT ----------
    else:
        return random.choice([
            "🤖 Try asking about syllabus, timetable, fees, or exams.",
            "🤖 I can help with campus-related queries. Type 'help' to see options.",
            "🤖 Not sure about that, but I can guide you on student services."
        ])


# ================= COMPLAINT SYSTEM ================= #

def save_complaint(text, category):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    complaint_id = "C" + str(random.randint(1000, 9999))
    time = datetime.datetime.now().isoformat()

    file_path = os.path.join(data_dir, "complaints.txt")

    with open(file_path, "a") as file:
        file.write(f"{complaint_id}|{time}|{category}|{text}|Pending\n")

    return complaint_id


def get_complaints():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "complaints.txt")

    complaints = []
    happy_count = 0

    if not os.path.exists(file_path):
        return complaints, happy_count

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split("|")

            if len(parts) < 5:
                continue

            cid, time_str, category, text, status = parts

            created_time = datetime.datetime.fromisoformat(time_str)
            now = datetime.datetime.now()

            # ---------- DELAY LOGIC ----------
            if status == "Pending" and (now - created_time).total_seconds() > 86400:
                status_display = "Delayed"
            else:
                status_display = status

            # ---------- HAPPY STUDENTS ----------
            if status == "Resolved" and (now - created_time).total_seconds() <= 86400:
                happy_count += 1

            complaints.append({
                "id": cid,
                "time": time_str,
                "category": category,
                "text": text,
                "status": status_display
            })

    return complaints, happy_count