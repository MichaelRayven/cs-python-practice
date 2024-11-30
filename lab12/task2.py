messages_count = int(input("Enter the number of messages: "))
message_queue = []
messages = ""

if not messages_count:
    print("No messages found.")
    exit()
else:
    messages = input("Enter message order: ")[:messages_count]

# This works assuming the messages consist only of "Q" and "A"
for message in messages:
    if message == "Q":
        message_queue.append("Q")
    elif len(message_queue) > 0:
        message_queue.pop(0)
    else:
        print("-")
        break
else:       
    if len(message_queue) > 0:
        print("-")
    else:
        print("+")