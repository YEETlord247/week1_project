import numpy as np
# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        name = input("What is your name? ")
        age = input("What is your age? ")
        print("Creating ...")
        p1 = Person(name, age)
        self.list_of_people.append(p1)
        pass

    def login(self):
        for i in range(len(self.list_of_people)):
            print((i + 1), self.list_of_people[i].name)
        choice = int(input("Enter the number next to the user you would like to log into as: "))
        return self.list_of_people[choice - 1]
    
    
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friendlist = []
        self.messages = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(person_object)
        pass
    
    def print_friends(self):
        print("\n" + self.name + "'s Friends List: ")
        for i in range(len(self.friendlist)):
            print((i + 1), self.friendlist[i].name, "")
        pass

    def edit_Details(self):
        new_Age = eval(input("Enter new Age: "))
        self.age = new_Age
        new_Name = input("Enter your new Name: ")
        self.name = new_Name
    
    def send_message(self, msg):
        #implement sending message to friend here
        return "From: " + self.name + "\n" + msg

    def add_Message(self, message):
        self.messages.append(message)
    
    def view_Messages(self):
        for i in self.messages:
            print(self.messages[i])
    
    def return_Friend(self, index):
        return self.friendlist[index]
