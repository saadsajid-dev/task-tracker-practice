#Program: Task Tracker - User Input and Data Types
#Author: Saad
#Description: This program collects user input and demonstrates data types logic

task_id = input("Enter Task ID: ")
estimated_hours = input("Enter Estimated Hours: ")

#convert task_id to an integer
task_id = int(task_id)
# Convert estimated_hours to a float
estimated_hours = float(estimated_hours)

print ()
print ("Task ID:", task_id)
print (type(task_id))
print ()
print ("Estimated Hours:", estimated_hours)
print (type(estimated_hours))
print ()