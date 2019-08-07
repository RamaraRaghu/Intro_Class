#Rakshith Raghu(rr5de)

GENDER = 0
AGE = 1
YEAR = 2
MAJOR = 3
STATE = 4
ICE_CREAM = 5
DORM = 6
OS = 7
BIRTH_DATE = 8

def read_data_file(filename):
    raw_data = []
    student_data = []
    data = []
    file = open(filename, "r")

    for line in file:
        line = line.strip()
        raw_data.append(line)

    for i in range(len(raw_data)):
        data = raw_data[i].split(",")
        student_data.append(data)

    return student_data

def get_average_list(student_list):
    age = []
    ages = []
    for i in range(len(student_list)):
        age.append(student_list[i][1])
    for i in range(len(age)):
        ages.append(age[i])

    average = float(sum(ages)/ len(ages))

    return average

def count_by_group(student_list, item_to_count=GENDER, group_by=None, group_by_value=None):
    count = item_to_count
    dictionary = {}
    top = []
    single_part = []
    if (group_by == None):
        for i in range(len(student_list)):
           top.append(student_list[i][count])
    if (group_by != None):
        for i in range(len(student_list)):
            if(student_list[i][group_by] == group_by_value):
                top.append(student_list[i][count])
    for i in range(len(top)):
        if(top[i] not in single_part):
            single_part.append(top[i])
    for i in range(len(single_part)):
        number = top.count(single_part[i])
        dictionary[single_part[i]] = number
    return dictionary

def most_common(student_list, item_to_count=GENDER, group_by=None, group_by_value=None):
    counting = count_by_group(student_list, item_to_count, group_by, group_by_value)
    largest = max(counting.values())
    type = []
    mods = []
    for key in counting:
        mods.append(key)
    for i in range(len(mods)):
        if counting.get(mods[i]== largest):
            type.append(mods[i])
    mods.sort()
    final = (mods, largest)
    return final







