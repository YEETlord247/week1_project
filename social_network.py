#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()
    current_User = Person("", 0)
    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "5":
                    break
                elif (inner_menu_choice == "1"):
                    current_User.name = input("Enter your new name: ")
                    current_User.age = int(input("Enter your new Age: "))
                    break
                elif (inner_menu_choice == "2"):
                    friend_Name = input("What is the name of the friend you would like to add: ")
                    i = 0
                    while (i < len(ai_social_network.list_of_people)):
                        if (ai_social_network.list_of_people[i].name == friend_Name):
                            current_User.add_friend(ai_social_network.list_of_people[i])
                            print(friend_Name, "has been added to your friends list")
                            break
                        else:
                            i += 1
                        print("User could not be found.")
                    break   
                elif (inner_menu_choice == "3"):
                    current_User.print_friends()    
                    break                 
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                
        elif choice == "3":
            current_User = ai_social_network.login()
            print("Welcome,", current_User.name,"\n########################################################")
                

        elif choice == "4":
            print("Thank you for visiting. Goodbye")
            ai_social_network.list_of_people.clear()
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()