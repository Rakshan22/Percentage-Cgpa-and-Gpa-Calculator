marks_of_first_subject = (int(input("Enter your marks in the first subject: ")))
marks_of_second_subject = (int(input("Enter your marks of the second subject: ")))
marks_of_third_subject = (int(input("Enter your marks of the third subject: ")))
marks_of_fourth_subject = (int(input("Enter your marks of the fourth subject: ")))
marks_of_fifth_subject = (int(input("Enter your marks of the fifth subject: ")))
total_marks_of_one_subject = (int(input("Enter the total marks in the test of one subject: ")))
total_marks = marks_of_first_subject + marks_of_second_subject + marks_of_third_subject + marks_of_fourth_subject + marks_of_fifth_subject
total_marks_of_all_subjects = total_marks_of_one_subject*5
percentage = total_marks/total_marks_of_all_subjects*100
cgpa = percentage/9.5
gpa = percentage/100*4
print(str(percentage) + "%")
print(str(cgpa) + " cgpa")
print(str(gpa) + " gpa")


