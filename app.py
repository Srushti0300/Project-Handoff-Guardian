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


# Create the report
report = f"""
====================================
        PROJECT HANDOFF REPORT
====================================

Project: {project_name}
Current Owner: {owner}
New Owner: {new_owner}
Project Status: {status}
Handoff Date: {handoff_date}

✅ COMPLETED WORK
{completed}

🔄 WORK IN PROGRESS
{in_progress}

⚠️ BLOCKERS
{blockers}

🧠 IMPORTANT DECISIONS
{decisions}

📌 NEXT ACTIONS
{next_actions}

📋 HANDOFF CHECKLIST
☐ Review completed work
☐ Review blockers
☐ Review important decisions
☐ Review next actions
☐ Confirm new owner

====================================
     HANDOFF REPORT GENERATED
====================================
"""


# Show report in terminal
print(report)


# Save report to file
with open("handoff_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("✅ Report saved as handoff_report.txt")