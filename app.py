from flask import Flask, render_template, request, jsonify, redirect, session
from utils import chatbot_reply, save_complaint, get_complaints
import os

app = Flask(__name__)
app.secret_key = "secret123"


# ================= USERS (ROLE-BASED) ================= #
USERS = {
    "admin": {"password": "1234", "role": "admin"},
    "hod": {"password": "1234", "role": "HOD Issue"},
    "mentor": {"password": "1234", "role": "Mentor Issue"},
    "tpo": {"password": "1234", "role": "Placement (TPO) Issue"},
    "accounts": {"password": "1234", "role": "Accounts / Fees Issue"}
}


# ================= HOME ================= #
@app.route("/")
def home():
    return render_template("index.html")


# ================= CHAT ================= #
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    return jsonify({"reply": chatbot_reply(user_input)})


# ================= SUBMIT COMPLAINT ================= #
@app.route("/submit_complaint", methods=["POST"])
def submit_complaint():
    text = request.json["message"]
    category = request.json.get("category", "General Complaint")

    complaint_id = save_complaint(text, category)

    return jsonify({
        "reply": f"✅ Complaint submitted!<br>Your ID: <b>{complaint_id}</b>"
    })


# ================= STUDENT VIEW ================= #
@app.route("/get_complaints")
def get_user_complaints():
    complaints, _ = get_complaints()
    return jsonify(complaints)


# ================= LOGIN ================= #
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username]["password"] == password:
            session["logged_in"] = True
            session["role"] = USERS[username]["role"]
            session["username"] = username
            return redirect("/admin")

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# ================= ADMIN PANEL ================= #
@app.route("/admin")
def admin():
    if not session.get("logged_in"):
        return redirect("/login")

    role = session.get("role")

    complaints, happy_count = get_complaints()

    # 🔥 ROLE-BASED FILTER
    if role != "admin":
        complaints = [c for c in complaints if c["category"] == role]

    return render_template(
        "admin.html",
        complaints=complaints,
        happy=happy_count,
        role=role,
        username=session.get("username")
    )


# ================= UPDATE STATUS ================= #
@app.route("/update_status", methods=["POST"])
def update_status():
    cid = request.json["id"]
    new_status = request.json["status"]

    file_path = os.path.join(os.path.dirname(__file__), "data", "complaints.txt")

    if not os.path.exists(file_path):
        return jsonify({"msg": "No complaints found"})

    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            parts = line.strip().split("|")

            if len(parts) < 5:
                file.write(line)
                continue

            if parts[0] == cid:
                parts[4] = new_status  # status index
                file.write("|".join(parts) + "\n")
            else:
                file.write(line)

    return jsonify({"msg": "Updated successfully"})


# ================= LOGOUT ================= #
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ================= RUN ================= #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)