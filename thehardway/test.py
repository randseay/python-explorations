lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

class_list = [lloyd, alice, tyler]

# Add your function below!
def average(lst):
    return float(sum(lst)) / len(lst)
    
def get_average(student_dict):
    return average(student_dict["homework"]) * 0.1 + average(student_dict["quizzes"]) * 0.3 + average(student_dict["tests"]) * 0.6

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(a_class_list):
    class_total = 0
    for each_student in a_class_list:
        class_total += get_average(each_student)
    class_average = float(class_total) / len(a_class_list)
    return class_average

print "The class average is %f" % get_class_average(class_list)

print "That is a(n) %s!" % get_letter_grade(get_class_average(class_list))
