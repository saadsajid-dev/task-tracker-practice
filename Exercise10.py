#Program: Task Tracker - Mini Task Tracker Registration
#Author: Saad
#Description: This program collects task registration details from the user
#and displays them in a formatted manner

task_id = input("Enter Task ID: ")
task_name = input("Enter Task Name: ")
employee_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
priority = input("Enter Priority (High/Medium/Low): ")
estimated_hours = input("Enter Estimated Hours: ")
completion_status = input("Enter Completion Status (Leave Blank for False): ")

#Conversions
#convert task_id to an integer
task_id = int(task_id)
# Convert estimated_hours to a float
estimated_hours = float(estimated_hours)
# Convert completion_status to a boolean
completion_status = bool(completion_status)

print ()
print ("=" * 30)
print ("Task Tracker Report")
print ("=" * 30)
print ("Task ID:", task_id)
print ("Task Name:", task_name)
print ("Employee Name:", employee_name)
print ("Department:", department)
print ("Priority:", priority)
print ("Estimated Hours:", estimated_hours)
print ("Completion Status:", completion_status)
print ("=" * 30)
print ()