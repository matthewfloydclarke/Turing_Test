import sqlite3

#The class User saves an individual's id, name and age as identifiers for searching in the database
class User:
    def __init__(self, id, name, age):
        self.id = id                        #Sets id, name and age as attributes of instance
        self.name = name
        self.age = age
        self.sentences = []                 #Creates a list of sentences the user inputted
        self.savedid = False                #Starts with no id, name or age saved in the Users database
        self.savedName = False
        self.savedAge = False
    
    #Sets user's id
    def setid(self, id):
        self.id = id
    
    #Sets user's name
    def setName(self, name):
        self.name = name
    
    #Sets user's age
    def setAge(self, age):
        self.age = age

    #Saves the id of the user into the Users database. If there are no ids in the table,
    #the id will be set as 0, otherwise it'll be 1 above current largest id
    def saveid(self):
        con = sqlite3.connect('turing_database.db')         #Connects to the database
        cur = con.cursor()
        try:                                                #Tries to...
            cur.execute('SELECT id FROM Users')             #Select all ids from the Users table
            ids = cur.fetchall()
            max_id = max(ids)                               #Find the largest id
            id = max_id[0]+1                                #Set the user's id to 1 above current largest id
            self.id = id                                    
        except Exception as e:                              #If there are no ids in the table
            print("saveid",e)                               #Then print error and set id as 0
            self.id = 0
        try:                                                                            #Tries to...
            cur.execute('INSERT INTO Users VALUES (?, ?, ?)',(self.id, None, None,))    #Insert the user's id into the table
            con.commit()
        except Exception as e:                                                          #If the id already exists in the table
            print("saveid",e)                                                           #Then print error and pass
        con.close()

    #Gets the id of the user from the Users database using their name or name and age
    def getid(self):
        if self.name != None:                                                                                   #If there is a value for user's name then
            try:                                                                                                #Try to...
                con = sqlite3.connect('turing_database.db')                                                     #Connect to the database
                cur = con.cursor()
                try:                                                                                            #And try to...
                    cur.execute('SELECT id, name FROM Users WHERE name = ?',(self.name,))                       #Select all the ids and names where name equals user's name
                    ids = cur.fetchall()
                    if len(ids) <= 1:                                                                           #If there are other people sharing the user's name
                        self.id = ids[0][0]                                                                     #Then set as the first
                    else:                                                                                       #If there are other people sharing the user's name
                        cur.execute('SELECT * FROM Users WHERE name = ? AND age = ?',(self.name,self.age,))     #Then select one user with matching name and age
                        ids = cur.fetchone()
                        self.id = ids[0]                                                                        #Sets id as user's id from the table
                except Exception as e:                                                                          #If there isn't a name that matches, no age given or no name and age matches
                    print("getid",e)                                                                            #Then print error
                con.close()
            except Exception as e:                                                                              #If the database doesn't exist
                print("----",e,"----")                                                                          #Then print error

    #Gets all the information of the user
    def getUser(self):
        if self.id != None:                                                 #If there is a value for id then
            try:                                                            #Tries to...
                con = sqlite3.connect("turing_database.db")                 #Connect to the database
                cur = con.cursor()
                cur.execute('SELECT * FROM Users WHERE id = ?',(self.id,))  #Selects all the information about the user
                data= cur.fetchall()
                con.close()
                return data                                                 #Returns it to the user
            except Exception as e:                                          #If there is an error
                print(e)                                                    #Then print the error

    #Saves the name of the user with their corresponding id
    def saveName(self):
        if self.id != None and self.name != None:                                               #If there is a value for user id and name then
            try:                                                                                #Try to...
                con = sqlite3.connect('turing_database.db')                                     #Connect to the database
                cur = con.cursor()
                cur.execute('UPDATE Users SET name = ? WHERE id = ?',(self.name, self.id,))   #Insert the user's id and name into the table
                con.commit()
                con.close()
            except Exception as e:                                                              #If it can't
                print("saveName",e)                                                             #Then print error
    
    #Saves the age of the user with their corresponding id
    def saveAge(self):
        if self.id != None and self.age != None:                                                #If there is a value for user id and age then
            try:                                                                                #Try to...
                con = sqlite3.connect('turing_database.db')                                     #Connect to the database
                cur = con.cursor()
                cur.execute('UPDATE Users SET age = ? WHERE id = ?',(self.age, self.id,))    #Insert the user's id and age into the table
                con.commit()
                con.close()
            except Exception as e:                                                              #If it can't
                print("saveAge",e)                                                              #Then print error

    #Saves the name and age of the user with their corresponding id
    def saveUser(self):
        if self.id != None and self.name != None and self.age != None:                          #If there is a value for user id, name and age then
            try:                                                                                #Try to...
                con = sqlite3.connect('turing_database.db')                                     #Connect to the database
                cur = con.cursor()
                cur.execute('UPDATE Users SET name = ?, age = ? WHERE id = ?',(self.name, self.age, self.id,))   #Insert the user's id, name and age into the table
                con.commit()
                con.close()
            except Exception as e:                                                              #If it can't
                print("saveAll",e)                                                              #Then print error

    #Saves the sentences inputted by the user into the Sentences table
    def saveSentence(self, sentence):
        if self.id != None:                                                                     #If there is a value for id then
            try:                                                                                #Tries to...
                con = sqlite3.connect('turing_database.db')                                     #Connect to the database
                cur = con.cursor()
                if len(self.sentences) > 0:                                                     #If there are any values in the sentences list
                    for i in self.sentences:                                                    #Loop through each item in the list
                        cur.execute('INSERT INTO Sentences VALUES (?, ?)',(self.id, i,))        #And add it into the table with the user's id
                        con.commit()
                    self.sentences.clear()                                                      #Clear the list
                else:
                    cur.execute('INSERT INTO Sentences VALUES (?, ?)',(self.id, sentence,))     #If there is nothing in the list, add it straight into the table
                    con.commit()
                    con.close()
            except Exception as e:                                                              #If there is an error
                print("saveSentence",e)                                                         #Then print the error
        else:
            self.sentences.append(sentence)                                                     #If there is no id, add inputs into sentences list


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