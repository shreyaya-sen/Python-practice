student ={
    "name" : "shreya",
    "subject" : {
        "maths" : 100,
        "english" : 100,
        "iks" : 100
    }
}
print(student["subject"]["iks"])
print(list(student.keys()))
print(student.keys()) 
print(len(student))#length of key ie student and subject
print(len(list(student.keys())))
print(student.values()) 
print(list(student.values()))
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
student.update({"CITY" : "DELHI"})
print(student)