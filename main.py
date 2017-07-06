"""---------------SPY-CHAT--------------"""




# IMPORTING IS DONE HERE

import details
from spy_details import spy,ChatMessage,Spy,friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored,cprint
import time



status_messages=["Do good have good","Busy"]
special=['sos','SOS','HELP','help']

# FUNCTION(FRIEND_LIST)
def friend_list():
    friend=Spy('','',0,0)
    friend.name = raw_input("friend_name")
    friend.rating =int(raw_input("Rating?"))
    friend.age=int(raw_input("Age:"))
    friend.salutation=str(raw_input("MR. or MS.?"))
    if len(friend.name) > 0 and friend.age >= 12 and friend.rating<=10:
        print "%s %s is now your friend and your\'s friends age is %d and rating is %d"%(friend.salutation, friend.name,friend.age,friend.rating)
        friends.append(friend)
    else:
        print "Your details are not valid for being a friend of spy!"







 #FUNCTION(SELECT_FRIEND)
def select_friend():
    for friend in friends:
        print friend.name
    choose_friend = raw_input("Choose friend from friend list? :")
    friend_choice_position = int(choose_friend) - 1
    return friend_choice_position




# FUNCTION(STATUS)
def status(current_status_message):
    updated_status_message=None
    if current_status_message!=None:
        print "your current_status_message is %s\n"%(current_status_message)
    else:
        print "status messages is null"
    default=raw_input("Do you want to select from older ones(y/n)?")
    if default=="n":
        new_status_message=raw_input("What message do you want to set?")
        if len(new_status_message)>0:
            status_messages.append(new_status_message)
            updated_status_message=new_status_message
    elif default=="y":
        item_position=1
        for message in status_messages:
            print "%d  %s"%(item_position,message)
            item_position=item_position+1
        message_selection=int(raw_input("\nchoose from above messages"))
        if len(status_messages)>=message_selection:
            updated_status_message=status_messages[message_selection-1]
        else:
            print "invalid option"


    if updated_status_message:
        print "your updated status message is:%s" % (updated_status_message)
    else:
        print "you did\'t update your status message"
        print updated_status_message
    return updated_status_message



# FUNCTION(ENCODE-MESSAGE)

def encode_message():
    friend_choice = select_friend()
    image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(image, output_path, text)
    new_chat = ChatMessage(text, True)
    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image has hided in the image!"


# FUNCTION(DECODE-MESSAGE)

def decode_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    temp = secret_text.split(" ")
    for i in special:
        if i in temp:
            temp[temp.index(i)]='please save me'
    secret_text = str.join(" ",temp)
    new_chat = ChatMessage(secret_text, False)
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"



#FUNCTION(READ CHAT)
def read_chat_history():
    read = select_friend()
    for chat in friends[read].chats:
        if chat.sent_by_me:
                print '[%s] %s: %s' % (colored(chat.time.strftime("%b %d %Y %H:%M:%S"),'blue'), 'You said',colored(chat.message,'cyan'))
        else:
                print '[%s] %s read: %s' % (colored(chat.time.strftime("%b %d %Y %H:%M:%S"),'blue'), friends[read].name,colored(chat.message,'cyan'))


#FUNCTION(MENU_FUNCTION)
def start_chat():
    current_status_message = None
    output=raw_input(colored("Do you want to continue yes or no?",'blue'))
    if output.lower()=="yes":
        show_menu = True
        while show_menu:
            print "Enter 1 for status update\n","Enter 2 for friend_list\n","Enter 3 for encode a message\n","Enter 4 to decode a message\n","Enter 5 for read chat history\n","Enter 7 for exit\n"
            choose_no=int(raw_input("What\'s your choice?"))
            if choose_no==1:
                current_status_message=status(current_status_message)
            elif choose_no==2:
                friend_list()
            elif choose_no==3:
                encode_message()
            elif choose_no==4:
                decode_message()
            elif choose_no==5:
                show_menu = read_chat_history()
            elif show_menu==6:
                show_menu=False
    if output=="no" or output=="N0" or output=="No":
        exit()


# spy name age will be given here
print "let\'s continue"
spy=Spy('','',0,0.0)
spy.name =raw_input("Enter your name?")
if details.name == spy.name:
    spy.age = details.age
    spy.rating = details.rating
    spy.salutation=details.salutation
    print "Hello! %s %s. your age is %d and your rating is %d" %(colored(spy.salutation,'red'),colored(spy.name,'red'),spy.age,spy.rating)
else:
    length = len(spy.name)
    # print type(spy.name)
    spy.age = int(raw_input("Enter your age?"))
    if length > 0 and spy.name.isalpha():
        spy.salutation = raw_input("Mr. or Miss?")
        print "Hello!" + " " +colored(spy.salutation,'red') +" "+colored(spy.name,'red')+"."+"Your age is %d"%(spy.age)
    spy.rating = int(raw_input("Enter your rating?"))
    if spy.rating > 8 and spy.rating < 10:
        print "Exellent rating"
    elif spy.rating > 5 and spy.rating < 8:
        print "Great rating"
    elif spy.rating > 0 and spy.rating <= 5:
        print "Poor rating"
    else:
        print "Wrong input"
    if length>100:
        del spy

start_chat()