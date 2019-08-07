#Rakshith Raghu (rr5de)

from urllib import request

lou_url = 'http://stardock.cs.virginia.edu/louslist/Courses/view/CS'

Debt_ID = 0
Course_Number = 1
Section = 2
Course_Title = 3
Instructor = 4
Type_of_Class = 5
Hours = 6
Monday = 7
Tuesday = 8
Wednesday = 9
Thursday = 10
Friday = 11
Start_Time = 12
End_Time = 13
Location = 14
Enrollment = 15
Allowable_Enrollment = 16
Latitude = 17
Longitude = 18

def url_to_file (url):
    opening = request.urlopen(url)
    data = str(opening.read())
    lines = data.split(";")
    dest_file = r'lou.csv'
    fx = open(dest_file, "w")
    for line in lines:
        fx.write(line + '\n')
    fx.close()
    return fx

def file_to_list(file):
    opening = open(file, "w")
    raw_list = []
    mega_list = []
    small_list = []

    for line in opening:
        line = line.strip()
        raw_list.append(line)

    for i in range(0,len(raw_list), 18):
        for z in range(0,18):
            small_list.append(raw_list[i+z])
        mega_list.append(small_list)

    return mega_list

def instructors(department):
    file = url_to_file("http://stardock.cs.virginia.edu/louslist/Courses/view/CS")
    total_list = file_to_list(file)
    teachers = []

    for i in range(len(total_list)):
        if(department in total_list[i] and total_list[i][4] not in teachers):
            teachers.append(total_list[i][4])
    return teachers



def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    file = url_to_file("http://stardock.cs.virginia.edu/louslist/Courses/view/CS")
    total_list = file_to_list(file)
    criteria = [dept_name, has_seats_available, level, not_before, not_after]
    add = False
    final_list = []

    if(not_before != None):
        criteria[3] = int(not_before)
        before = criteria[3]
    if(not_after != None):
        criteria[4] = int(not_after)
        after = criteria[4]
    if(level != None):
        lower = (int(level)//1000)*1000
        higher = lower + 1000

    for i in range(len(total_list)):
        for z in range(1,len(criteria)):
           if(criteria[z] != None):
               if(criteria[z] ==  has_seats_available):
                   if(has_seats_available == True):
                       seats = int(total_list[i][16])-int(total_list[i][15])
                       if(seats > 0):
                           add = True
                       else:
                           add = False
                           break
                   else:
                       add = True
               if(criteria[z] == level):
                   if(int(total_list[i][1]) >= lower and int(total_list[i][1])< higher):
                       add = True
                   else:
                       add = False
                       break
               if(criteria[z] == before):
                   if(total_list[i][12] >= before or total_list[i][12] == -1):
                       add = True
                   else:
                       add = False
                       break
               if(criteria[z] == after):
                   if(total_list[i][12] <= after or total_list[i][12] == -1):
                       add = True
                   else:
                       add = False
                       break
           else:
               add = True
        if(criteria[0] == total_list[i][0] and add == True):
            final_list.append(total_list[i])

    return final_list














