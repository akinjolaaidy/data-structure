classmates = ["Charles" , "Mohammad" , "Ali" , "Ahmed" , "Hassan" , "Hussain" , "Fatima"]
print("Class list:", classmates)


print("total number of classmates:", len(classmates))
print("First classmate:", classmates[0])
print("Last classmate:", classmates[-1])
print("First three classmates:", classmates[0:3])


classmates.append("Aisha")
print("\nAfter adding a new classmate:", classmates)
classmates.remove("Ali")
print("After removing a classmate:", classmates)
classmates.sort()
print("sorted classmates:", classmates)
classmates.reverse()
print("reversed classmates:", classmates)


teacher = {"name": "John", "age": 30, "subject": "Math" , "experience": 5}
print("\nTeacher information:" ,teacher)


print("subject taught by the teacher:", teacher["subject"])
print("teacher's age:", teacher["age"])
print("teacher's experience:", teacher.get("experience" , "Not available"))
teacher["experience"] = 6
teacher["email"] = "john@example.com"
teacher.pop("experience")
print("Updated teacher information:", teacher)

roll_numbbers = [1 , 2 ,3 , 4 , 5 , 6 , 7 ]
names = ["Charles" , "Mohammad" , "Ali" , "Ahmed" , "Hassan" , "Hussain" , "Fatima"]
student_directory = dict(zip(roll_numbbers , names))
print("\nStudent directory:", student_directory)
print("Student at Roll 3:", student_directory[3])

