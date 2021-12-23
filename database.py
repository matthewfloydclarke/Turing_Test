import sqlite3

#The class User saves an individual's id, name and age as identifiers for searching in the database
class User:
    def __init__(self, id, name, age):
        self.id = id                        #Sets id, name and age as attributes of instance
        self.name = name
        self.age = age
        self.sentences = []                 #Creates a list of sentences the user inputted
        self.savedID = False                #Starts with no id, name or age saved in the Users database
        self.savedName = False
        self.savedAge = False
    
    def setID(self, id):                    #Sets user's id
        self.id = id
    
    def setName(self, name):                #Sets user's name
        self.name = name
    
    def setAge(self, age):                  #Sets user's age
        self.age = age

#Creates a database and if there already is one, sends back an error
def createDatabase():
    try:                                                                                            #Tries to...
        con = sqlite3.connect("turing_database.db")                                                 #Connect to the database
        cur = con.cursor()
        cur.execute('CREATE TABLE Users (id INT PRIMARY KEY, name TEXT, age INT)')                  #Create a Users table which includes the user's information
        cur.execute('CREATE TABLE Sentences (id INT, sentence TEXT, PRIMARY KEY (id, sentence))')   #Create a Sentences table which store the sentences inputted by a user
        con.commit()
        con.close() 
    except Exception as e:                                                                          #Otherwise, prints error
        print(e)