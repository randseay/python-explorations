def word_count(some_string):
    composition_dict = {}
    word_list = some_string.split()

    for word in word_list:
        if word.lower() in composition_dict:
            composition_dict[word.lower()] += 1
        else:
            composition_dict[word.lower()] = 1

    return composition_dict

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(list_of_dicts, string):
    list_of_strings = []
    for each_dict in list_of_dicts:
        list_of_strings.append(string.format(**each_dict))

    return list_of_strings

treehouse_teachers = {
    'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
    'Kenneth Love': ['Python Basics', 'Python Collections']
}

def most_classes(teachers_dict):
    max_count = 0
    busiest_teacher = ""

    for teacher in teachers_dict:
        if len(teachers_dict[teacher]) > max_count:
            busiest_teacher = teacher
            max_count = len(teachers_dict[teacher])

    return busiest_teacher

def num_teachers(teachers_dict):
    return len(teachers_dict)

def stats(teachers_dict):
    list_of_teachers = []

    for teacher in teachers_dict:
        list_of_teachers.append([teacher, len(teachers_dict[teacher])])

    return list_of_teachers

def courses(teachers_dict):
    all_courses = []

    for course in teachers_dict.values():
        all_courses.extend(course)

    return all_courses


def main():
    print(word_count("This is a big test this IS A BIG Test"))
    print(string_factory(dicts, string))
    print("The busiest teacher at Treehouse is {}.".format(most_classes(treehouse_teachers)))
    print("The number of teachers is {}.".format(num_teachers(treehouse_teachers)))
    print("Here is a list of each teacher with the number of classes they teach:\n{}.".format(stats(treehouse_teachers)))
    print("Here is a list of all courses:\n{}".format(courses(treehouse_teachers)))

main()
