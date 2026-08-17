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


# Check missing information
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


# Create report
report = f"""
====================================
        PROJECT HANDOFF REPORT
====================================

Project: {project_name}
Current Owner: {owner}
New Owner: {new_owner}
Project Status: {status}
Handoff Date: {handoff_date}

COMPLETED WORK
{completed if completed else "Not provided"}

WORK IN PROGRESS
{in_progress if in_progress else "Not provided"}

BLOCKERS
{blockers if blockers else "Not provided"}

IMPORTANT DECISIONS
{decisions if decisions else "Not provided"}

NEXT ACTIONS
{next_actions if next_actions else "Not provided"}

HANDOFF CHECKLIST
☐ Review completed work
☐ Review blockers
☐ Review important decisions
☐ Review next actions
☐ Confirm new owner
"""


# Add missing information warning
if missing:
    report += "\n⚠️ MISSING INFORMATION\n"

    for item in missing:
        report += f"- {item}\n"

    report += "\nRecommendation: Complete the missing information before handoff.\n"

else:
    report += "\n✅ HANDOFF CHECK\n"
    report += "All important information has been provided.\n"


report += """
====================================
     HANDOFF REPORT GENERATED
====================================
"""


# Show report
print(report)


# Save report
with open("handoff_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("✅ Report saved as handoff_report.txt")