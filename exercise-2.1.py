#Ask for the name and age of your classmates

def get_the_data_of_the_classmates(classmates_cuantity):
    classmates = []
    for i in range(classmates_cuantity):
        name = input("Introduce the name of the classmate: ")
        age = int(input("Introduce the age of the classmate: "))
        classmate = (name,age)
        classmates.append(classmate)
    classmates.sort(key=lambda x:x[1])
    assistent = classmates[0][0]
    teacher = classmates[-1][0]
    return assistent,teacher

assistent,teacher = get_the_data_of_the_classmates(5)

print(f"The teacher is : {teacher} and the assistent is {assistent}")