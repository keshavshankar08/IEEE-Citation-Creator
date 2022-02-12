#This program takes a variety of input for a publication and creates an IEEE style citation
#Created by Keshav Shankar
from datetime import date
import time

today = date.today()

def getAuthors():
    authorsFirstName = []
    authorsLastName = []
    name = input("Enter the author in (Firstname Lastname) format. (CTRL+C to kill):    ")
    if name:
        first, last = name.split()
        first = first.lower()
        first = first.title()
        last = last.lower()
        last = last.title()
        authorsFirstName.append(first)
        authorsLastName.append(last)    
    while name:
        name = input("Enter another author in (Firstname Lastname) format. BLANK TO STOP:   ")
        if name:
            first, last = name.split()
            first = first.lower()
            first = first.title()
            last = last.lower()
            last = last.title()
            authorsFirstName.append(first)
            authorsLastName.append(last)  
    numAuthors = len(authorsFirstName)
    authorsFormatted = ""

    if numAuthors == 1:
        authorsFormatted = authorsFirstName[0][0] + ". " + authorsLastName[0]+"."
    else:
        for i in range(numAuthors):
            authorsFormatted = authorsFormatted+" "+authorsFirstName[i][0] + ". " + authorsLastName[i]+","
        authorsFormatted = authorsFormatted[:-1] +"."
    return authorsFormatted

def getTitle():
    title = input("Enter the title:     ")
    title = title.lower()
    title = title.title()
    title = '"'+title+'."'
    return title

def getPublisher():
    publisher = input("Enter the publisher:     ")
    publisher = publisher.lower()
    publisher = publisher.title()
    publisher += '.'
    return publisher

def formatDate(month,day,year):
    formattedDate = (month+"."+day+"."+year+".")
    return formattedDate

def getPublicationDate():
    date = input("Enter the publication date (month day year) or (12 8 2004) format:    ")
    month,day,year = date.split()
    intMonth = int(month)
    intDay = int(day)
    if intMonth<10:
        month = "0"+month
    if intDay<10:
        day = "0"+day
    return formatDate(month,day,year) 

def getAccessDate(today):
    date = today.strftime("%m/%d/%Y")
    month,day,year = date.split("/")
    accessDate = formatDate(month,day,year)
    accessDate = "Accessed "+accessDate
    return accessDate

def getLink():
    link = input("Enter the source link:    ")
    return link

def main():
    citation = getAuthors()+" "+getTitle()+" "+getPublisher()+" "+getPublicationDate()+" "+getAccessDate(today)
    print("")
    print("YOUR CITATION IS:    "+citation)
    print("")

while True:
    main()
    print("---------------- Restarting Program ... ----------------")
    print("")
    time.sleep(2)
