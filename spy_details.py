from datetime import datetime

class Spy:
#class created to intake the details of the spy

    def __init__(self, name, salutation, age, rating):
        #constructor created
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    #class created to save the details of the messages of chat history

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Phil Coulson', 'Mr.', 30, 4.7)

friend_one = Spy('Nick Fury', 'Mr.', 35, 5.0)




friends = [friend_one]