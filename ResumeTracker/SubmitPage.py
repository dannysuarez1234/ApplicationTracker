from tkinter import *
from Queries import *
from ViewPage import *

def submitPage():
    root = Tk()
    companyName = Label(root, text = "Company Name:")
    companyEntry = Entry(root, width = 50)  
    jobTitle = Label(root, text = "Job Title:")
    titleEntry = Entry(root, width = 50)
    companyLocation = Label(root, text = "Location:")
    locationEntry = Entry(root, width = 50)
    companyURL = Label(root, text = "Website:")
    URLEntry = Entry(root, width = 50) 
    companySkills = Label(root, text = "Desired Skills")
    skillsEntry = Entry(root, width = 50)

    companyName.grid(row = 0, column=0)
    companyEntry.grid(row = 0, column = 1) 
    jobTitle.grid(row = 1, column = 0)
    titleEntry.grid(row = 1, column = 1)
    companyLocation.grid(row = 2, column = 0)
    locationEntry.grid(row = 2, column = 1)
    companyURL.grid(row = 3, column = 0)
    URLEntry.grid(row = 3, column = 1)
    companySkills.grid(row = 4, column = 0)
    skillsEntry.grid(row = 4, column = 1)
    

    def submitEntry():
        insert(companyEntry.get(),titleEntry.get(),locationEntry.get(),
               URLEntry.get(),skillsEntry.get())
        companyEntry.delete(0, END)
        titleEntry.delete(0, END)
        locationEntry.delete(0, END)
        URLEntry.delete(0, END)
        skillsEntry.delete(0, END)
        
    submitButton = Button(root, text = "Submit",command = submitEntry)
    submitButton.grid(row = 5, column = 0)

    def viewJobs():
        root.destroy()
        viewPage()
        
        
        
        
    viewButton = Button(root, text = "View Jobs",command = viewJobs)
    viewButton.grid(row = 5, column = 1)


    
    

    root.mainloop()



    

