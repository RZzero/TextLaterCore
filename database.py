#!/usr/bin/python
#

import MySQLdb
from message import Message


'''
        #  This method given a platform (Gmail, Telegram, Hotmail) return
        a list of messages with status NS (Not Send) from our database.
'''

def to_be_send_messages(ptform):

    _messages_ = []  #  List that the method returns

    db = MySQLdb.connect("","","","")
                        #  server, user, password, database
    cursor = db.cursor()

    query = "SELECT idMessage, platform, sender, ToM,subject, content, timeToSend, messageStatus FROM Message WHERE messageStatus = {0} AND platform = '{1}'".format("'NS'", ptform)

    cursor.execute(query)

    messages = cursor.fetchall()
    for m in messages:
        id_message = m[0]
        platform = m[1]
        sender = m[2]
        to_m = m[3].split(", ")
        subject = m[4]
        content = m[5]
        time_to_send = m[6]
        message_status = m[7]

        message_ = Message(id_message, platform, sender, to_m, subject, content,
                           time_to_send, message_status)
        _messages_.append(message_)

    db.close()

    return _messages_
