from steganography.steganography import Steganography #imports Steganography class from steganography file indside steganogrsphy module
from datetime import datetime
from spy_details import spy, Spy, ChatMessage, friends #imports spy_detail
from termcolor import *
import colorama




print "SHIELD welcomes you SPY!"
#prints welcome message

STATUS_MESSAGES = ['Coulson is back from the dead', 'Agent Sky has powers', 'Agents of SHIELD ']
#The list made for the statuses

colorama.init()

ques = "Do you wish to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(ques)


def add_status():
#Function defined that adds a status from the user or updates the current  status from the given
#list of status
    updated_status_message = None

    if spy.curr_status_message != None:

        print 'Your current status message is %s \n' % (spy.curr_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the already given status list (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("Enter the status you wish ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above statuses "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You currently don\'t have a status update'

    return updated_status_message


def add_friend():
#Function defined to add spy's friends alongwith the details of them
    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Enter your friend's name Spy: ")
    if set('[~!@#$%^&*()_+{}":;\']+$ " "').intersection(new_friend.name):
        print "Invalid entry. Please Enter a valid name of single word without special characters"
        new_friend.name = raw_input("Enter your friend's name Spy: ")
    else:
        print "Thats a valid friend name"

    new_friend.salutation = raw_input("MR or MS : ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("How old is your mate?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("How amazing are they?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 3.5:


        friends.append(new_friend)
        print 'You have a new Friend <3!'
    else:
        print 'Sorry! This friend isn\'t worth you. We can\'t add spy with the details you gave'

    return len(friends)


def select_a_friend():
    #thid Function lets us select s friend from the list of friends
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Select a SPY mate from the list")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():
    #this function lets you send a message to the friend you selected

    friend_choice = select_a_friend()

    original_image = raw_input("Enter the name of the image you wanna send")
    #enter the name of the image
    ext1=".jpg"
    original_image=original_image+ext1
    output_path = "output.jpg"
    text = raw_input("What do you want to say to your fellow spy? ")
    #enters the message you want to hide in the image

    Steganography.encode(original_image, output_path, text)
    #Hide the message in the image that is being sent

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():
#This function separates the hidden text from the image and displays it

    sender = select_a_friend()

    output_path = raw_input("Enter the file name!!")
    ext='.jpg'
    output_path=output_path+ext

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    #print "Your secret message has been saved!"
    #return secret_text


    if len(secret_text) == 0:
        print "There is nothing in the secret message"
    else:
        if secret_text=='SOS' or secret_text=="Save me" or secret_text=="Help" :
            print "Its an emergencyyyy!!"
            print "Your mate sent -"+secret_text
        else:
            print "You are good to go. Your secret message is given below :"
            print secret_text

def read_chat_history():
    #Function enables you to read the message convos!

    read_for = select_a_friend()

    #print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            cprint(chat.time.strftime("%d %B %Y"),'blue')
            cprint('You said:','red')
            print chat.message
        else:
            cprint(chat.time.strftime("%d %B %Y"),"blue")
            cprint(friends[read_for].name,"red")
            print chat.message


def start_chat(spy):
#Gives you menu choices
    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome to the SHIELD " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you wish to do? \n 1. Add a new status update \n 2. Add a Spy Mate \n 3. Send a secret message to your mate \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                    #print read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of apt age to be a spy'

if existing == "Y" or existing=='y':
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to SHIELD, What is your spy name?: ")
    if set('[~!@#$%^&*()_+{}":;\']+$ " "').intersection(spy.name):
        print "Invalid entry. Please enter a spy name of a single word without special characters"
        spy.name = raw_input("Welcome to SHIELD- Re-Enter a valid spyname: ")
    else:
        print spy.name +"!!  That is a perfect spyname"
        #checks edge case scenarios on the spy name

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
        spy.age = raw_input("What is your age?")
        spy.age=int(spy.age)



        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)


        start_chat(spy)
    else:
        print 'Please add a valid spy name'