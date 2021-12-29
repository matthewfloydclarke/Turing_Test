import ai, nlt, database, conversation      #Imports all other python files

#If statement allows only the user to run the code
if __name__ == "__main__":
    print("Hello World!")
    database.createDatabase()

    user = database.User(None, None, None)
    user.saveid()
    print("user's id is",user.id)