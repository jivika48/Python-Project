#simple chatbot
import random

flag=True
print("Chatbot: My name is jivika. Let's have a conversation! Also,"
" if you want to exit any time, just type bye")

GREET_INPUTS = ["hello", "hi", "greeting", "sup", "hey"]
GREET_CARE = ["what's up", "how are you", "all good"]
GREET_RESPONSES = ["hi", "hey", "nods", "hi there", "hello", "I am glad! you are talking to me"]
CARE_RESPONSES = ["I am fine, thanks for asking!", "I am good, what about you", "pretty good, how's it going for you"  ]
def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)
         
        elif  sentence in GREET_CARE:
            return random.choice(CARE_RESPONSES)
        
while (flag==True):
    user_response = input("YOU: ").lower()

    if 'bye' not in user_response:
        if 'thanks' in user_response or 'thank you' in user_response:
            flag=False
            print("chatbot: you are welcome..")
        else:
            if greet(user_response)!= None:
                print("chatbot: ", greet(user_response))  
    elif 'bye' in user_response:
        flag=False
        print("chatbot: Goodbye! Have a good day.\ntake care..")

    
