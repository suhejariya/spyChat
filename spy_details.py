from datetime import datetime
from termcolor import colored

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

friend_1 = Spy('Ishu', 'Mr.', 20, 7)
friend_2 = Spy('Neha', 'Ms.', 19, 2)
friend_3 = Spy('Shikha', 'Ms.',20, 3)
friend_4=Spy('Kirti','Ms.',20,8)


friends = [friend_1, friend_2, friend_3,friend_4]