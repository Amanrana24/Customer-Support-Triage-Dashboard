from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = [
    {"id": 1, "customer": "John Smith", "body": "I was charged twice for my January invoice. Please fix this urgently.", "timestamp": "2026-02-10"},
    {"id": 2, "customer": "Emma Wilson", "body": "The app crashes every time I try to upload a PDF file.", "timestamp": "2026-02-11"},
    {"id": 3, "customer": "Michael Brown", "body": "Can you add dark mode support in the next update?", "timestamp": "2026-02-11"},
    {"id": 4, "customer": "Sophia Davis", "body": "I haven’t received my refund yet. It has been 10 days.", "timestamp": "2026-02-12"},
    {"id": 5, "customer": "Liam Johnson", "body": "Login is not working on mobile.", "timestamp": "2026-02-12"},
    {"id": 6, "customer": "Olivia Martinez", "body": "It would be great to export reports as CSV files.", "timestamp": "2026-02-13"},
    {"id": 7, "customer": "Noah Anderson", "body": "Where can I change my password?", "timestamp": "2026-02-13"},
    {"id": 8, "customer": "Ava Taylor", "body": "Payment failed but money was deducted from my account.", "timestamp": "2026-02-14"},
    {"id": 9, "customer": "William Thomas", "body": "The dashboard is loading very slowly.", "timestamp": "2026-02-14"},
    {"id": 10, "customer": "Isabella Moore", "body": "Can you add two-factor authentication for better security?", "timestamp": "2026-02-15"},
    {"id": 11, "customer": "James Jackson", "body": "The app freezes when I try to generate a report.", "timestamp": "2026-02-15"},
    {"id": 12, "customer": "Mia White", "body": "How do I update my billing details?", "timestamp": "2026-02-16"},
    {"id": 13, "customer": "Benjamin Harris", "body": "I am getting an unknown server error message.", "timestamp": "2026-02-16"},
    {"id": 14, "customer": "Charlotte Martin", "body": "Please add integration with Slack notifications.", "timestamp": "2026-02-17"},
    {"id": 15, "customer": "Lucas Thompson", "body": "My subscription was cancelled without notice.", "timestamp": "2026-02-17"},
    {"id": 16, "customer": "Amelia Garcia", "body": "The file upload feature is not working properly.", "timestamp": "2026-02-18"},
    {"id": 17, "customer": "Henry Clark", "body": "Can I get a copy of my last three invoices?", "timestamp": "2026-02-18"},
    {"id": 18, "customer": "Evelyn Rodriguez", "body": "The system logged me out automatically multiple times.", "timestamp": "2026-02-18"},
    {"id": 19, "customer": "Alexander Lewis", "body": "Feature request: add customizable dashboard widgets.", "timestamp": "2026-02-19"},
    {"id": 20, "customer": "Harper Lee", "body": "Urgent: I cannot access my account after the latest update.", "timestamp": "2026-02-19"},
]

def classify_message(message):
    text = message["body"].lower()

    if any(word in text for word in ["crash", "error", "not working", "freezes", "failed", "cannot access", "slow"]):
        category = "Bug"
    elif any(word in text for word in ["invoice", "refund", "charged", "payment", "billing", "subscription"]):
        category = "Billing"
    elif any(word in text for word in ["add", "feature", "support", "integration", "export"]):
        category = "Feature Request"
    else:
        category = "General"

    if "urgent" in text or "charged twice" in text or "cannot access" in text:
        priority = "High"
    elif category == "Bug":
        priority = "Medium"
    else:
        priority = "Low"

    message["category"] = category
    message["priority"] = priority
    message["resolved"] = False

for msg in messages:
    classify_message(msg)

def get_summary():
    category_count = {}
    priority_count = {}

    for msg in messages:
        category_count[msg["category"]] = category_count.get(msg["category"], 0) + 1
        priority_count[msg["priority"]] = priority_count.get(msg["priority"], 0) + 1

    return category_count, priority_count

@app.route("/")
def dashboard():
    category_filter = request.args.get("category")
    priority_filter = request.args.get("priority")

    filtered = messages

    if category_filter:
        filtered = [m for m in filtered if m["category"] == category_filter]

    if priority_filter:
        filtered = [m for m in filtered if m["priority"] == priority_filter]

    category_count, priority_count = get_summary()

    return render_template(
        "index.html",
        messages=filtered,
        category_count=category_count,
        priority_count=priority_count
    )

@app.route("/resolve/<int:id>")
def resolve(id):
    for msg in messages:
        if msg["id"] == id:
            msg["resolved"] = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
