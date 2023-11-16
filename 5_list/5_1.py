student = ["Marius Nyhagen", "Magnus Fløgum,", "Dennis Yeboha", "Ada Kristine Moen", "Hibak Mohamud Yusuf"]

student.append(student[2])
student[2] = "Ole"
student[2] += " Nordmann"
student.insert(4, "Monty Python")

print(len(student))
student.remove("Ole Nordmann")
print(len(student))
print(student.index("Monty Python"))

print(student[0:3])

reverse_student = student[::-1]
even_student = student[0::2]

print(student)
print(even_student)
print(reverse_student)