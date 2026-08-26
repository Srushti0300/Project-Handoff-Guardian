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
# Automatic Action Extraction
# -----------------------------

actions = []

sentences = meeting_notes.replace("!", ".").replace("?", ".").split(".")

for sentence in sentences:
    sentence = sentence.strip()

    if not sentence:
        continue

    words = sentence.lower()

    action_words = [
        "need to",
        "should",
        "must",
        "will",
        "complete",
        "finish",
        "create",
        "update",
        "fix",
        "review",
        "test",
        "prepare"
    ]

    if any(word in words for word in action_words):
        actions.append(sentence)


# -----------------------------
# Automatic Decision Extraction
# -----------------------------

detected_decisions = []

for sentence in sentences:
    sentence = sentence.strip()

    if not sentence:
        continue

    words = sentence.lower()

    decision_words = [
        "decided",
        "decision",
        "agreed",
        "selected",
        "chosen",
        "approved"
    ]

    if any(word in words for word in decision_words):
        detected_decisions.append(sentence)


# -----------------------------
# Missing Information Check
# -----------------------------

missing = []

if not completed.strip():
    missing.append("Completed work")

if not in_progress.strip():
    missing.append("Work in progress")

if not blockers.strip():
    missing.append("Blockers")

if not decisions.strip():
    missing.append("Important decisions")

if not next_actions.strip():
    missing.append("Next actions")

if not meeting_notes.strip():
    missing.append("Meeting notes")


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
🤖 DETECTED ACTION ITEMS
====================================
"""

if actions:
    for number, action in enumerate(actions, start=1):
        report += f"{number}. {action}\n"
else:
    report += "No action items detected.\n"


report += """
====================================
🧠 DETECTED DECISIONS
====================================
"""

if detected_decisions:
    for number, decision in enumerate(detected_decisions, start=1):
        report += f"{number}. {decision}\n"
else:
    report += "No decisions detected.\n"


report += """
====================================
HANDOFF CHECKLIST
====================================
☐ Review completed work
☐ Review blockers
☐ Review important decisions
☐ Review next actions
☐ Confirm new owner
☐ Review meeting notes
"""


if missing:
    report += """
====================================
⚠️ MISSING INFORMATION
====================================
"""

    for item in missing:
        report += f"- {item}\n"

    report += "\nRecommendation: Complete the missing information before handoff.\n"

else:
    report += """
====================================
✅ HANDOFF CHECK
====================================
All important information has been provided.
"""


report += """
====================================
     HANDOFF REPORT GENERATED
====================================
"""


# Display report
print(report)


# Save report
with open("handoff_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("✅ Report saved as handoff_report.txt")