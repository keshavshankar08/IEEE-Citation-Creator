from tkinter import *
from datetime import date

today = date.today()

#---------------------------Functions---------------------------
def getAuthors(name1,name2,name3,name4,name5,name6):
    numAuthorsInput = 0
    if name1:
        numAuthorsInput+=1
        if name2:
            numAuthorsInput+=1
            if name3:
                numAuthorsInput+=1
                if name4:
                    numAuthorsInput+=1
                    if name5:
                        numAuthorsInput+=1
                        if name6:
                            numAuthorsInput+=1
    if numAuthorsInput == 0:
        return ""
    if numAuthorsInput == 1:
        first1,last1 = authorNameSplitter(name1)
        return first1[0]+". "+last1+". "
    if numAuthorsInput == 2:
        first1,last1 = authorNameSplitter(name1)
        first2,last2 = authorNameSplitter(name2)
        return first1[0]+". "+last1+", "+first2[0]+". "+last2+". "
    if numAuthorsInput == 3:
        first1,last1 = authorNameSplitter(name1)
        first2,last2 = authorNameSplitter(name2)
        first3,last3 = authorNameSplitter(name3)
        return first1[0]+". "+last1+", "+first2[0]+". "+last2+", "+first3[0]+". "+last3+". "
    if numAuthorsInput == 4:
        first1,last1 = authorNameSplitter(name1)
        first2,last2 = authorNameSplitter(name2)
        first3,last3 = authorNameSplitter(name3)
        first4,last4 = authorNameSplitter(name4)
        return first1[0]+". "+last1+", "+first2[0]+". "+last2+", "+first3[0]+". "+last3+", "+first4[0]+". "+last4+". "
    if numAuthorsInput == 5:
        first1,last1 = authorNameSplitter(name1)
        first2,last2 = authorNameSplitter(name2)
        first3,last3 = authorNameSplitter(name3)
        first4,last4 = authorNameSplitter(name4)
        first5,last5 = authorNameSplitter(name5)
        return first1[0]+". "+last1+", "+first2[0]+". "+last2+", "+first3[0]+". "+last3+", "+first4[0]+". "+last4+", "+first5[0]+". "+last5+". "
    if numAuthorsInput == 6:
        first1,last1 = authorNameSplitter(name1)
        first2,last2 = authorNameSplitter(name2)
        first3,last3 = authorNameSplitter(name3)
        first4,last4 = authorNameSplitter(name4)
        first5,last5 = authorNameSplitter(name5)
        first6,last6 = authorNameSplitter(name6)
        return first1[0]+". "+last1+", "+first2[0]+". "+last2+", "+first3[0]+". "+last3+", "+first4[0]+". "+last4+", "+first5[0]+". "+last5+", "+first6[0]+". "+last6+". "

def authorNameSplitter(name):
    first, last = name.split()
    first = first.lower()
    first = first.title()
    last = last.lower()
    last = last.title()
    return first,last

def getTitle(title):
    if title:
        title = title.lower()
        title = title.title()
        title = '"'+title+'."'
        return title
    else:
        return ""

def getPublisher(publisher):
    if publisher:
        publisher += '.'
        return publisher
    else:
        return ""

def formatDate(month,day,year):
    formattedDate = (month+"."+day+"."+year+".")
    return formattedDate

def getPublicationDate(month,day,year):
    if month and day:
        intMonth = int(month)
        intDay = int(day)
        if int(month[0]) > 0 and intMonth<10:
            month = "0"+month
        if int(day[0]) > 0 and intDay<10:
            day = "0"+day
        return formatDate(month,day,year)
    if year:
        return year+"."
    else:
        return ""

def getAccessDate(today):
    date = today.strftime("%m/%d/%Y")
    month,day,year = date.split("/")
    accessDate = formatDate(month,day,year)
    accessDate = "Accessed "+accessDate
    return accessDate

def getLink(link):
    if link:
        return link
    else:
        return ""

def clearBoxes():
    author1Input.delete(0,END)
    author2Input.delete(0,END)
    author3Input.delete(0,END)
    author4Input.delete(0,END)
    author5Input.delete(0,END)
    author6Input.delete(0,END)
    titleInput.delete(0,END)
    publisherInput.delete(0,END)
    publicationMonthInput.delete(0,END)
    publicationDayInput.delete(0,END)
    publicationYearInput.delete(0,END)
    linkInput.delete(0,END)
    Label(formatVis,text="THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER",font=("arial",60),bg="black",fg="black").place(x=30,y=350)

def tempTextAuthor1(event):
    author1Input.delete(0,END)
    author2Input.delete(0,END)
    author3Input.delete(0,END)
    author4Input.delete(0,END)
    author5Input.delete(0,END)
    author6Input.delete(0,END)

def tempTextTitle(event):
    titleInput.delete(0,END)

def tempTextPublisher(event):
    publisherInput.delete(0,END)

def tempTextPubMonth(event):
    publicationMonthInput.delete(0,END)

def tempTextPubDay(event):
    publicationDayInput.delete(0,END)

def tempTextPubYear(event):
    publicationYearInput.delete(0,END)

def tempTextLink(event):
    linkInput.delete(0,END)

def main():
    citation = getAuthors(str(author1.get()),str(author2.get()),str(author3.get()),str(author4.get()),str(author5.get()),str(author6.get()))+getTitle(str(title.get()))+" "+getPublisher(str(publisher.get()))+" "+getPublicationDate(str(pubDateMonth.get()),str(pubDateDay.get()),str(pubDateYear.get()))+" "+getAccessDate(today)+" "+getLink(str(linkPage.get()))
    Label(formatVis,text="THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER THIS IS A FILLER",font=("arial",20),bg="black",fg="black").place(x=30,y=350)
    citationLabel = Label(formatVis,text="Your citation is:     "+citation,font=("arial",20),bg="yellow",fg="black").place(x=30,y=350)
    #copy to clipboard
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(citation)
    clip.destroy()
    copyLabel = Label(formatVis,text="Citation copied to clipboard!",font=("arial",20,"bold"),bg="black",fg="green").place(x=150,y=400)

#---------------------------Display Window---------------------------
#Tab setup
formatVis = Tk()
formatVis.title("IEEE Formatter 2.0")
formatVis.geometry("800x500")
formatVis.configure(bg="black")

#Tab Headings
heading1 = Label(formatVis, text="IEEE Citation Creator", font=("arial",40,"bold"),bg="black",fg="steelblue").pack(pady=5)
heading2 = Label(formatVis,text="© 2022 - Keshav Shankar", font=("arial",20,"bold"),bg="black",fg="steelblue").pack(pady=5)

#Author Inputs
#author 1
author1Label = Label(formatVis,text="Author 1: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=30,y=120)
author1 = StringVar()
author1Input = Entry(formatVis,textvariable=author1,width=25,bg="lightgray")
author1Input.place(x=130,y=120)
author1Input.insert(0,"Firstname Lastname")
author1Input.bind("<FocusIn>",tempTextAuthor1)
#author 2
author2Label = Label(formatVis,text="Author 2: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=30,y=150)
author2 = StringVar()
author2Input = Entry(formatVis,textvariable=author2,width=25,bg="lightgray")
author2Input.place(x=130,y=150)
author2Input.insert(0,"Firstname Lastname")
#author 3
author3Label = Label(formatVis,text="Author 3: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=30,y=180)
author3 = StringVar()
author3Input = Entry(formatVis,textvariable=author3,width=25,bg="lightgray")
author3Input.place(x=130,y=180)
author3Input.insert(0,"Firstname Lastname")
#author 4
author4Label = Label(formatVis,text="Author 4: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=30,y=210)
author4 = StringVar()
author4Input = Entry(formatVis,textvariable=author4,width=25,bg="lightgray")
author4Input.place(x=130,y=210)
author4Input.insert(0,"Firstname Lastname")
#author 5
author5Label = Label(formatVis,text="Author 5: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=30,y=240)
author5 = StringVar()
author5Input = Entry(formatVis,textvariable=author5,width=25,bg="lightgray")
author5Input.place(x=130,y=240)
author5Input.insert(0,"Firstname Lastname")
#author 6
author6Label = Label(formatVis,text="Author 6: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=30,y=270)
author6 = StringVar()
author6Input = Entry(formatVis,textvariable=author6,width=25,bg="lightgray")
author6Input.place(x=130,y=270)
author6Input.insert(0,"Firstname Lastname")

#Title
titleLabel = Label(formatVis,text="Title: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=400,y=120)
title = StringVar()
titleInput = Entry(formatVis,textvariable=title,width=30,bg="lightgray")
titleInput.place(x=460,y=120)
titleInput.insert(0,"ex: Signal Processing")
titleInput.bind("<FocusIn>",tempTextTitle)

#Publisher
publisherLabel = Label(formatVis,text="Publisher: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=400,y=150)
publisher = StringVar()
publisherInput = Entry(formatVis,textvariable=publisher,width=25,bg="lightgray")
publisherInput.place(x=506,y=150)
publisherInput.insert(0,"ex: NCBI")
publisherInput.bind("<FocusIn>",tempTextPublisher)

#Publication Date
publicationDateLabel = Label(formatVis,text="Publication Date: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=400,y=180)
pubDateMonth = StringVar()
pubDateDay = StringVar()
pubDateYear = StringVar()
publicationMonthInput = Entry(formatVis,textvariable=pubDateMonth,width=4,bg="lightgray")
publicationMonthInput.place(x=570,y=180)
publicationMonthInput.insert(0,"Month")
publicationMonthInput.bind("<FocusIn>",tempTextPubMonth)
publicationDayInput = Entry(formatVis,textvariable=pubDateDay,width=4,bg="lightgray")
publicationDayInput.place(x=633,y=180)
publicationDayInput.insert(0,"Day")
publicationDayInput.bind("<FocusIn>",tempTextPubDay)
publicationYearInput = Entry(formatVis,textvariable=pubDateYear,width=4,bg="lightgray")
publicationYearInput.place(x=694,y=180)
publicationYearInput.insert(0,"Year")
publicationYearInput.bind("<FocusIn>",tempTextPubYear)
Label(formatVis,text="/",font=("arial",18),bg="black",fg="white").place(x=615,y=180)
Label(formatVis,text="/",font=("arial",18),bg="black",fg="white").place(x=680,y=180)

#link
linkLabel = Label(formatVis,text="Link: ",font=("arial",20,"bold"),bg="black",fg="white").place(x=400,y=210)
linkPage = StringVar()
linkInput = Entry(formatVis,textvariable=linkPage,width=30,bg="lightgray")
linkInput.place(x=460,y=210)
linkInput.insert(0,"ex: ncbi.nlm.nih.gov")
linkInput.bind("<FocusIn>",tempTextLink)

#run button
runBut = Button(formatVis, text="Click to Cite",width=20,height=2,fg="darkgreen",bg="lightgreen",font=("arial",15,"bold"),command=main)
runBut.place(x=460,y=250)

#clear button
clearBut = Button(formatVis,text="Click to Clear",width=20,height=2,fg="red",font=("arial",15,"bold"),command=clearBoxes)
clearBut.place(x=460,y=300)

#Run tab
formatVis.mainloop()