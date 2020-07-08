import sqlite3

def createTable():
    dbConnection = sqlite3.connect("testDB.db")
    cursor = dbConnection.cursor()
    cursor.execute("""CREATE TABLE JOBS(
        company_name text,
        company_location text,
        job_title text,
        company_url text,
        job_skills
        )""")
    dbConnection.commit()
    dbConnection.close()
    

def insert(companyName, jobTitle, companyLocation, url, skills):
    dbConnection = sqlite3.connect("testDB.db")
    cursor = dbConnection.cursor()
    cursor.execute("Insert into jobs values (:company_name, :company_location,:job_title, :company_url, :job_skills)",
            {
               'company_name': companyName,
               'company_location': companyLocation,
               'job_title': jobTitle,
               'company_url': url,
               'job_skills': skills,
            })               
    dbConnection.commit()
    dbConnection.close()

def getAllJobs():
    dbConnection = sqlite3.connect("testDB.db")
    cursor = dbConnection.cursor()

    cursor.execute("Select *, oid from jobs")
    allRecords = cursor.fetchall()
    dbConnection.close()
    
    return allRecords
    



