#!/usr/bin/python

class Message:
    id_message = ""
    platform = ""
    subject = ""
    sender = ""
    to_m = []
    content = ""
    time_to_send = ""
    message_status = ""

    def __init__(self, id_message, platform, sender, to_m, subject,  content, time_to_send, message_status):
        self.id_message = id_message
        self.platform = platform
        self.subject = subject
        self.sender = sender
        self.to_m = to_m
        self.content = content
        self.time_to_send = time_to_send
        self.message_status = message_status

    def to_string(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(self.id_message, self.platform, self.subject, self.sender, self.to_m, self.content, self.time_to_send, self.message_status)
