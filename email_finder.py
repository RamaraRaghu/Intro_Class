#Rakshith Raghu(rr5de) and Christian May

import urllib.request


__author__ = 'chris_000'

import urllib.request


def url_to_list(url):
    url = ("https://cs1110.cs.virginia.edu/emails.html")
    opening = urllib.request.urlopen(url)#opens the web page

    raw_list = []
    for line in opening:
       decoded = line.decode("UTF-8")
       decoded = decoded.strip()
       decoded = str(decoded)
       print("decoded is",decoded)
       decoded = pluckTheFeathers(decoded)
       print("After plucking",decoded)
       raw_list.append(decoded)
    return(raw_list)




def standard_email_case(line_string, char_index):
   up_to_at = 0          #define variables
   top = 0
   mason = ["0","1","2","3","4","5","6","7","8","9"] #WHAT ARE THE NUMBERS MASON!!!
   period = ""

   for i in range(len(line_string)):       #finds the position of the @ character
       if (line_string[i] == "@"):
           up_to_at = i
           break

   after_at = len(line_string) - up_to_at
   final_string = line_string

   for i in range(after_at, len(line_string), 1):
       if (final_string[i] == " " or final_string[i] == ">" or final_string[i] == ':'):
           for z in range(i,up_to_at, -1):
               if final_string[z] == ".":
                   period = z
           if "." not in final_string[up_to_at:i] or mason in final_string[period:i]:
               final_string = -1
               return final_string
               break

           for z in range(i,period, -1):
               if "." in final_string[up_to_at:i]:
                   final_string = -1
                   break
           final_string[up_to_at:i] = final_string[period:i].lower()
           final_string = final_string[0:i]
           top = i
           break
   for i in range(len(final_string), 0,-1):
       if(final_string[i] == " " or final_string[i] == ">" or final_string[i] == ":"):
           final_string = final_string[i:top]
           break

   top = len(final_string)
   if(final_string[top] == "." or final_string[top] == ","):
       top = top -1
       final_string = final_string[0:top]

   return final_string


######################################################33

#opens website, opens blank list, reads and strips lines while there are lines to be read and stripped, then finally returns the list
#outputs a list of lines of the website

def list_of_lines_string_reader(decoded_website, string, list_index, character_index): #searches for string within the list decoded_website, starting at the line designated by line_index, and at the character designated by char_index, returns the position of the first character where the phrase is found, after the given list and char index. It returns -1 when it can't find anything else.
    #list_index = 0
    #char_index = 0
    list_length = len(decoded_website) #calculate length of input list
    for i in range(list_index, list_length): #iterate through with i, starting at the input row, through to the end of the list

        line_length = len(decoded_website[list_index]) #
        string_length = len(string)
        iterations = line_length - string_length + 1 - character_index + 1
        for char_index in range(character_index, iterations):
            stringFromFile = ""
            for chars in range (string_length):
                stringFromFile = stringFromFile + str(decoded_website[list_index][char_index + chars-1])
            if stringFromFile == string:
                return (list_index, char_index)
                break
            else:
                potato = 0 #junk variable
    return(-1)

def rstripPeriod(email_string):
    if email_string.endswith("."):
        email_string.rstrip(".")

def pluckTheFeathers(email_string):
    email_string = email_string.lower()
    if "nospam" in email_string:
        email_string = email_string.replace("nospam","")
    if " (at) " in email_string:
        email_string = email_string.replace(" (at) ","@")
    if " (at)" in email_string:
        email_string = email_string.replace(" (at)","@")
    if "(at) " in email_string:
        email_string = email_string.replace("(at) ","@")
    if "(at)" in email_string:
        email_string = email_string.replace("(at)","@")
    if " (dot) " in email_string:
        email_string = email_string.replace(" (dot) ",".")
    if " (dot)" in email_string:
        email_string = email_string.replace(" (dot)",".")
    if "(dot) " in email_string:
        email_string = email_string.replace("(dot) ",".")
    if "(dot)" in email_string:
        email_string = email_string.replace("(dot)",".")
    if ">" in email_string:
        email_string = email_string.replace(">"," ")
    if "<" in email_string:
        email_string = email_string.replace("<"," ")
    if ":" in email_string:
        email_string = email_string.replace(":"," ")
    if ";" in email_string:
        email_string = email_string.replace(";"," ")
    return email_string

def underscores(email):
    alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    split_list = email.split("@")
    if "_" in split_list[1]:
        for char in alphabetList:
            test_site = split_list[1].replace("_",char)
            file_variable = "https://"+test_site
            import urllib.request
            try:
                req = urllib.request.Request(file_variable)
                with urllib.request.urlopen(req) as response:
                    the_page = response.read()
                email = email.replace("_",char)
                return(email)
            except:
                0 == 0
    return(email)

    new_email = split_list[0]

def reverse(email):
    split_email = email.split("@")
    if "." in split_email[0] and "." not in split_email[1]:
        email = email[::-1]

def find_emails_in_website(url):
   master_list = url_to_list(url) #split web page by line
   master_email_list = []
   row = 0
   for iterations in range(len(master_list)):               #starts loop
       position_of_at = list_of_lines_string_reader(master_list[iterations], "@", 0, row) #finds position of first @_at)
       if position_of_at == -1:
           "potato"
           4
           "fuck?"
           "where are the errors mason?"
       else:
           row_number = position_of_at[0] #finds row of first @
           line = master_list[row_number] #line on which we're checking
           listSplitByAts = line.split("@") #splits line by @
           NumOfAts = len(listSplitByAts) - 1 #counts num of @
           for i in range(NumOfAts): #starts for loop
               listSplitByAts[i] = listSplitByAts[i].split(" ")#splits each entry in the list by spaces
           for i in range(NumOfAts): #starts for loop
               possible_email = reverse(underscores(rstripPeriod(listSplitByAts[i][len(listSplitByAts[i])] + "@" + listSplitByAts[i+1][0]))) #adds last of list + first of next list to get
               if possible_email not in master_email_list:
                   master_email_list.append(possible_email)
           row = position_of_at[1]
   for i in range(len(master_email_list)):
       works = True
       while works:
           email = master_email_list[i]

           #Test 1 below here
           split_email = email.split("@")
           if "." not in split_email[1]:
               works = False

            #Test 2 below
           list_split_by_ats_then_periods = split_email[1].split(".") - 1
           if len(split_email[1][list_split_by_ats_then_periods]) < 2:
               works = False

          #Test 3 below: tests if there's a num after the period
           numList = ["1","2","3","4","5","6","7","8","9","0"]
           for num in numList:
                if num in list_split_by_ats_then_periods[1][len(split_email[1][list_split_by_ats_then_periods])]:
                    works = False

       if works == False:
           master_email_list[i] = "potato"
       else:

        master_email_list = master_email_list.remove("potato")
   return master_email_list

def main():
    print("Successfully reached main")
    print(find_emails_in_website("https://cs1110.cs.virginia.edu/emails.html"))
    print("Now Back in main")
main()