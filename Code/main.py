import ai, nlt, database, conversation      #Imports all other python files

#If statement allows only the user to run the code
if __name__ == "__main__":
    print("Hello World!")
    database.createDatabase()                       #Creates the database in database.py

    user = database.User(None, None, None)          #Initiates an instance of User from database.py
    user.saveid()                                   #Saves the id into the Users table
    print("User's id is",user.id)

    user_reply = conversation.initialMessage()      #Gets the reply from the initial chatbot message

    name = input("What's your name? ")              #Asks for the user's name
    user.setName(name)                              #Sets the input as user's name
    user.saveName()                                 #Saves name into the table

    age = int(input("How old are you? "))           #Asks for the user's age
    user.setAge(age)                                #Sets the input as user's age
    user.saveAge()                                  #Saves age into the table

    inputs = [10, 3, 4]                             #AI test inputs
    mlp = ai.Structure(inputs, 3, 2, 2)             #Test instance
    print(mlp.aiNum)                                #Print AI number
