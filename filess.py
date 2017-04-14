#!/usr/bin/python

import os
def messages_with_id(message_id):
    filenames = []
    try:
        files_path = os.path.expanduser("~/Desktop/RESTApi/files/")
        all_filenames = os.listdir(files_path)
        for fileidx in range (len(all_filenames)):
            name = all_filenames[fileidx]
        
            if name[:len(message_id)] == message_id:
                filenames.append(files_path+all_filenames[fileidx])

    except Exception:
        filenames = []
        print("No files found")

    return filenames
