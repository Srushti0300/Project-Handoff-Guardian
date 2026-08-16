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


print("\n====================================")
print("        PROJECT HANDOFF REPORT")
print("====================================")

print("New Owner:", new_owner)
print("Project Status:", status)
print("Handoff Date:", handoff_date)
print("\nProject:", project_name)
print("Current Owner:", owner)

print("\n✅ COMPLETED WORK")
print(completed)

print("\n🔄 WORK IN PROGRESS")
print(in_progress)

print("\n⚠️ BLOCKERS")
print(blockers)

print("\n🧠 IMPORTANT DECISIONS")
print(decisions)

print("\n📌 NEXT ACTIONS")
print(next_actions)

print("\n====================================")
print("     HANDOFF REPORT GENERATED")
print("====================================")