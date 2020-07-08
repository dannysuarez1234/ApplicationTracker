from tkinter import *
from Queries import *

def viewPage():
    root = Tk()
    companyLabel = Label(root, text = "Company Name")
    companyLabel.grid(row = 0,column = 0)

    allRecords = getAllJobs()
    currentRow = 1
    
    for record in allRecords:
        cLabel = Label(root, text = record[0])
        cLabel.grid(row = currentRow, column = 0)
        currentRow = currentRow + 1
        

    root.mainloop()

    


