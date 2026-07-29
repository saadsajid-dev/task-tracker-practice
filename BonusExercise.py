#Program: Task Tracker - Bonus Exercise - Student Task Tracker
#Author: Saad
#Description: This program collects student task registration details from the user
#and displays them in a formatted manner

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
course_name = input("Enter Course Name: ")
assignment_name = input("Enter Assignment Name: ")
assignment_deadline = input("Enter Assignment Deadline (DD-MM-YYYY): ")
estimated_hours = input("Enter Estimated Hours to Complete Assignment: ")
submission_status = input("Enter Submission Status (Leave Blank for False): ")

#Conversions
#convert student_id to an integer
student_id = int(student_id)
# Convert estimated_hours to a float
estimated_hours = float(estimated_hours)
# Convert submission_status to a boolean
submission_status = bool(submission_status)

# Display the collected information in a formatted manner
print ()
print ("=" * 30)
print ("Student Task Tracker")
print ("=" * 30)
print ("Student ID:", student_id)
print ("Student Name:", student_name)
print ("Course Name:", course_name)
print ("Assignment Name:", assignment_name)
print ("Assignment Deadline:", assignment_deadline)
print ("Estimated Hours:", estimated_hours)
print ("Submission Status:", submission_status)
print ("=" * 30)
print ()

# Display the data types of the collected information
print ("Data Types of Collected Information:")
print ("Student ID:", type(student_id))
print ("Student Name:", type(student_name))
print ("Course Name:", type(course_name))
print ("Assignment Name:", type(assignment_name))
print ("Assignment Deadline:", type(assignment_deadline))
print ("Estimated Hours:", type(estimated_hours))
print ("Submission Status:", type(submission_status))
print ()