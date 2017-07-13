"""---------------SPY-CHAT--------------"""




# IMPORTING IS DONE HERE

import details
from spy_details import spy,ChatMessage,Spy,friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
import time


# GLOBALY DECLARED

status_messages=["Do good have good","Busy"]
special=['sos','SOS','HELP','help']



"FRIENDS WILL BE ADDED HERE"
# FUNCTION(FRIEND_LIST)

def add_friend(spy):
    friend = Spy('', '', 0, 0)
    friend.rating = raw_input("Rating b/w 0-10?")
    if friend.rating.isdigit() and len(friend.rating)!=0:
        friend.rating = int(friend.rating)
        if friend.rating<=10 and friend.rating>0:
            friend.name = raw_input("friend_name").title()
            friend.age=raw_input("Age:")
            friend.salutation=raw_input("Mr or Ms or Mrs?").title()
            if((friend.salutation == "Mr") or (friend.salutation == "Mrs") or (friend.salutation == "Ms")):
                    if len(friend.name) > 0 and friend.age >= 12 and friend.rating>=spy.rating \
                         and friend.name.isalpha() and friend.age.isdigit() and len(friend.name)!=0 \
                            and len(friend.age)!=0 :
                       friend.name=str(friend.name)
                       friend.age=int(friend.age)
                       print "%s %s is now your friend , age is %d and rating is %d"%(friend.salutation, friend.name,friend.age,friend.rating)
                       friends.append(friend)
                       return len(friends)
                    else:
                        print "Your details are not valid for being a friend of spy!"
                        return len(friends)
            print "Your details are not valid for being a friend of spy!"
            return len(friends)

        else:
            print "Error:Rating equal or less than 10,So Reenter rating"
            return add_friend(spy)


    else:
        print "Error:Rating equal or less than 10,So Reenter rating"
        return add_friend(spy)


#FUNCTION(SELECT_FRIEND)

def select_friend():
    item_no = 0
    try:
        for friend in friends:
            print '%d. %s %s aged %d with rating %.2f is online' % (item_no + 1, friend.salutation, friend.name,
                                                                    friend.age,
                                                                    friend.rating)
            item_no = item_no + 1
        friend_choice = raw_input("choose friend from list?")
        friend_choice_position = int(friend_choice) - 1
        return friend_choice_position
    except:
        print "ERROR:Choose friend again"
        return select_friend()


"STATUS WILL BE SET HERE"
# FUNCTION(STATUS)

def status(current_status_message):

    update_status_message=None
    try:
        if current_status_message!=None:
            print "your current_status_message is %s\n"%(current_status_message)
        else:
            print "status message is null"
        default=raw_input("Do you want to select from older ones(yes/no)")
        if default.lower()=="no" and len(default)!=0 and default.isalpha(): #here we set condition.
            new_status_message=raw_input("what is your message")
            if len(new_status_message)>0:
                status_messages.append(new_status_message)
                update_status_message=new_status_message
        elif default.lower()=="yes" and len(default)!=0 and default.isalpha():
            item_position=1
            for message in status_messages:
                print "%d  %s"%(item_position,message)
                item_position=item_position+1
            message_selection=int(raw_input("\nchoose from above message"))
            if len(status_messages)>=message_selection:
                update_status_message=status_messages[message_selection-1]
        else:
            print "invalid option"
        if update_status_message:
            print "your update status message is:%s" %(update_status_message)
            return update_status_message
        else:
            print "you didn't update your status message"
            return current_status_message
    except:
        print "ERROR"




"MESSAGE WILL BE ENCODED IN PIC HERE"
# FUNCTION(ENCODE-MESSAGE)

def encode_message():
    friend_choice = select_friend()      # function select_friend() will be called and the output of select_friend will get store in friend_choice
    image = raw_input("image-path?")
    if len(image)!=0:
        output_path = "output.jpg"
        text = raw_input("What do you want to say? ")
        if len(text)>0:
            try:
                Steganography.encode(image, output_path, text)
                new_chat = ChatMessage(text, True)
                friends[friend_choice].chats.append(new_chat)
                print "Your secret message image has hided in the image!"
            except:
                print 'Baad mei try krna'

        else:
            text = "No Message found"
            try:
                Steganography.encode(image, output_path, text)
                new_chat = ChatMessage(text, True)
                friends[friend_choice].chats.append(new_chat)
                print "Default Message is ready"
            except:
                'Try later'


    else:
        print "ERROR:Image path is missing"
        return encode_message()





"MESSAGE SEND BY THE SPY WILL BE DECODED HERE"
# FUNCTION(DECODE-MESSAGE)

def decode_message():
    sender = select_friend()
    output_path = raw_input("image-path?")
    if len(output_path)!=0:
        try:
            secret_text = Steganography.decode(output_path)

            temp = secret_text.split(" ")
            for i in special:
                if i in temp:
                    temp[temp.index(i)] = 'please save me'
            secret_text = str.join(" ", temp)
            new_chat = ChatMessage(secret_text, False)
            if len(secret_text) < 100:
                print "Your secret message has been saved!"
            else:
                del friends[sender]
                print "Friend deleted and message not saved due to access length of message!"

        except :
            print 'error'
    else:
        print "ERROR:Image path cant be empty"
        return decode_message()

"CAN READ THE CHAT WITH SENDING AND READING TIME AND DATE"
#FUNCTION(READ CHAT)

def read_chat_history():
    read = select_friend()
    if len(friends[read].chats) != 0:
        for chat in friends[read].chats:
                if chat.sent_by_me:
                        print '[%s] %s: %s' % (colored(chat.time.strftime("%b %d %Y %H:%M:%S"),'blue'), 'encoder said',colored(chat.message,'cyan'))
                        print '[%s] %s read: %s' % (colored(chat.time.strftime("%b %d %Y %H:%M:%S"),'blue'), friends[read].name,colored(chat.message,'cyan'))
    else:
        print 'No chat found'







#FUNCTION(SPYNAME)

def spyname():
    spy_name =raw_input( "What is your name?")
    if spy_name.isalpha() and len(spy_name)!=0:
        spy_name = str(spy_name).title()
        return spy_name
    else:
        print "ERROR:Re-enter your name"
        return spyname()






#FUNCTION(SPY_SALUTATION)

def spysalutation():
    spy_salutation = raw_input("Enter Mr , Mrs or Ms:").title()
    if (spy_salutation == "Mr") or (spy_salutation == "Mrs") or (spy_salutation == "Ms"):
        '''#or is an operator where it applies it tells either one condition or both'''
    else:
        print "ERROR:Wrong Salutation,PLZ Re_Enter Salutation:"
        return spysalutation()
    return spy_salutation








#FUNCTION(SPY_AGE)

def spyage():
    spy_age = raw_input("What is your age?")
    if spy_age.isdigit():
        spy_age=int(spy_age)
        if spy_age > 12 and spy_age< 50:
            spy_age = int(spy_age)
            return spy_age
        else:
            print "Invalid age"
            exit()
    else:
        print "Age must be of int type", "Re-enter your age:"
        return spyage()







#FUNCTION(SPY_RATING)

def spyrating():
      spy_rating = raw_input("Enter your rating:")
      if len(spy_rating) != 0 and spy_rating.isdigit() :
          spy_rating = int(spy_rating)
          if spy_rating >= 0 and spy_rating <= 3:
              print "Your rating is poor"
              return spy_rating
          elif spy_rating > 3 and spy_rating <= 7:
              print "Your rating is good"
              return spy_rating
          elif spy_rating > 7 and spy_rating <= 10:
              print "Your rating is excelent"
              return spy_rating
          else:
              print "Invalid rating,RE-enter the rating:"
              return spyrating()
      else:
             print("ERROR:Re-enter rating:")
             return spyrating()






"MENU IS HERE WE CAN ENTER OUR CHOICE"

#FUNCTION(MENU_FUNCTION)

def start_chat():
    current_status_message = None
    output=raw_input(colored("Do you want to continue yes or no?",'blue'))
    if output.lower()=="yes" and len(output)!=0 and output.isalpha():
            #lower() can convert every string into lower case
            show_menu = True
            while show_menu:
                print "Enter 1 for status update\n","Enter 2 for friend_list\n","Enter 3 for encode a message\n","Enter 4 to decode a message\n","Enter 5 for read chat history\n","Enter 6 for exit\n"
                choose_no = raw_input("What\'s your choice?")

                if len(choose_no)!=0 and choose_no.isdigit() and choose_no!=float(choose_no):
                    choose_no=int(choose_no)
                    if choose_no==1:
                        current_status_message=status(current_status_message)
                    elif choose_no==2:
                        total_friends=add_friend(spy)
                        print 'Total no of friends now you have:',total_friends
                    elif choose_no==3:
                        encode_message()
                    elif choose_no==4:
                        decode_message()
                    elif choose_no==5:
                        read_chat_history()
                    elif choose_no==6:
                        show_menu=False
                        exit()

                else:
                    print "Error:Re_choose your choice"
    elif output.lower()=="no" and len(output)!=0 and output.isalpha():
        exit()

    else:
        start_chat()






" SPY_NAME , SPY_SALUTATION , SPY_AGE , SPY_RATING"

print "let\'s continue"
spy=Spy('','',0,0.0)
spy.name=spyname()
if details.name == spy.name:
    spy.name=details.name
    spy.age = details.age
    spy.rating = details.rating
    spy.salutation=details.salutation
    spy.salutation=spy.salutation.title()
    print "Hello! %s. %s with age %d and rating %d." % (colored(spy.salutation, 'red'),colored(spy.name,'red'),spy.age,spy.rating)
    flag = True
    while(flag):
        try:
            ans=raw_input("Do you want to continue as defalut user(y/n)?")
            if len(ans)!=0 and ans.isalpha():
                if ans.lower() == "y":
                    USER_ID=raw_input("USER_id:")
                    USER_PW=str(raw_input("Password:"))
                    if (USER_ID==details.user_id and USER_PW==details.password):
                        print "WELCOME ADMIN "
                        start_chat()
                    while USER_ID!=details.user_id or USER_PW!=details.password:
                         print "ERROR:re_enter your USER_ID and USER_PW :)"
                         USER_ID = raw_input("USER_id:")
                         USER_PW = str(raw_input("Password:"))
                         if (USER_ID == details.user_id and USER_PW == details.password):
                             print "WELCOME ADMIN "
                             flag = False
                             start_chat()
                if ans.lower() == "n":
                    spy.name=spy.name
                    spy.salutation=spysalutation()
                    spy.age = spyage()
                    spy.rating=spyrating()
                    print "Hello! %s. %s with age %d and rating %d." % (
                    colored(spy.salutation, 'red'), colored(spy.name, 'red'), spy.age, spy.rating)
                    start_chat()
            else:
                 print 'ERROR:Re-enter:'
        except:
            pass

else:
    spy.salutation =spysalutation()
    spy.age = spyage()
    spy.rating = spyrating()
    print "Hello! %s. %s with age %d and rating %d." % (colored(spy.salutation, 'red'),colored(spy.name,'red'),spy.age,spy.rating)
    start_chat()