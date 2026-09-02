from datetime import date

print("====================================")
print("       PROJECT HANDOFF GUARDIAN")
print("====================================")

project_name = input("\nProject Name: ")
owner = input("Current Owner: ")
new_owner = input("New Owner: ")
status = input("Project Status (On Track/At Risk/Blocked): ")

handoff_date = date.today()

print("\nEnter completed work:")
completed = input("> ")

print("\nEnter work in progress:")
in_progress = input("> ")

print("\nEnter current blockers:")
blockers = input("> ")

print("\nEnter important decisions:")
decisions = input("> ")

print("\nEnter next actions:")
next_actions = input("> ")

print("\nEnter meeting notes:")
meeting_notes = input("> ")


# -----------------------------
# Project Knowledge
# -----------------------------

knowledge = {
    "project": project_name,
    "owner": owner,
    "new_owner": new_owner,
    "status": status,
    "completed": completed,
    "in_progress": in_progress,
    "blockers": blockers,
    "decisions": decisions,
    "next_actions": next_actions,
    "meeting_notes": meeting_notes
}


# -----------------------------
# Simple AI Assistant
# -----------------------------

print("\n====================================")
print("       🤖 HANDOFF ASSISTANT")
print("====================================")

while True:

    question = input("\nAsk about the project (or type 'done'): ")

    if question.lower() == "done":
        break

    q = question.lower()

    if "owner" in q:
        print("🤖 Current Owner:", owner)
        print("🤖 New Owner:", new_owner)

    elif "status" in q:
        print("🤖 Project Status:", status)

    elif "completed" in q:
        print("🤖 Completed Work:", completed)

    elif "progress" in q or "working" in q:
        print("🤖 Work in Progress:", in_progress)

    elif "blocker" in q or "problem" in q:
        print("🤖 Current Blockers:", blockers)

    elif "decision" in q:
        print("🤖 Important Decisions:", decisions)

    elif "next" in q or "action" in q:
        print("🤖 Next Actions:", next_actions)

    elif "meeting" in q or "notes" in q:
        print("🤖 Meeting Notes:", meeting_notes)

    elif "project" in q:
        print("🤖 Project:", project_name)

    else:
        print("🤖 I don't have information about that yet.")


# -----------------------------
# Create Report
# -----------------------------

report = f"""
====================================
        PROJECT HANDOFF REPORT
====================================

Project: {project_name}
Current Owner: {owner}
New Owner: {new_owner}
Project Status: {status}
Handoff Date: {handoff_date}

====================================
COMPLETED WORK
====================================
{completed if completed else "Not provided"}

====================================
WORK IN PROGRESS
====================================
{in_progress if in_progress else "Not provided"}

====================================
BLOCKERS
====================================
{blockers if blockers else "Not provided"}

====================================
IMPORTANT DECISIONS
====================================
{decisions if decisions else "Not provided"}

====================================
NEXT ACTIONS
====================================
{next_actions if next_actions else "Not provided"}

====================================
MEETING NOTES
====================================
{meeting_notes if meeting_notes else "Not provided"}

====================================
🤖 HANDOFF ASSISTANT
====================================
The project knowledge is available through the interactive assistant.

====================================
📋 HANDOFF CHECKLIST
====================================
☐ Review completed work
☐ Review blockers
☐ Review important decisions
☐ Review next actions
☐ Confirm new owner
☐ Review meeting notes

====================================
     HANDOFF REPORT GENERATED
====================================
"""

print("\n" + report)

with open("handoff_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("✅ Report saved as handoff_report.txt")