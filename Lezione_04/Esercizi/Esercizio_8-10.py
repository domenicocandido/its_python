list1 = ("Ciao!", "Come stai?", "Bel cane!")
sent_messages = ()

def send_messages(list1):
    for i in list1:
        print (i)
        sent_messages.append(i)
        list1.pop(i)

send_messages(list1)