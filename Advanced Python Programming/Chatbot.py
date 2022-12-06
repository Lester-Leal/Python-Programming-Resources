# IMPORTANT: pip install nltk
# A simple Python chatbot that uses natural language processing libraries to respond to user input
# This chatbot uses a simple list of pairs, where each pair consists of a regular
# expression that matches user input, and a list of responses that the chatbot can choose
# from to respond to the user. When the chatbot receives input from the user,
# it checks each regular expression in the pairs list and selects the first one
# that matches the user's input. It then responds with one of the responses from the list.

# Author: Jorn Blaedel Garbosa


from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla)', ['hello there', 'hi there', 'hey there']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*) weather (.*)', ['The weather in %1 is %2']],
    ['(.*) (tired|sleepy)',
     ['I\'m sorry to hear that you\'re % 2. You should try to get some rest.']],
    ['(.*) (favorite|best) (.*)', ['My favorite %3 is %2']],
    ['(.*) (joke|funny)', ['Why was the math book sad? Because it had too many problems.']],
    ['(.*) (love|like) (.*)', ['I\'m glad you % 2 % 3.']],
    ['(.*) (good|great|excellent) (.*)', ['I\'m glad you think % 3 is %2.']],
    ['(.*) (bad|terrible|horrible) (.*)',
     ['I\'m sorry to hear that you think % 3 is %2.']],
    ['(.*) (hungry|starving)',
     ['You should eat something. Do you want me to find a nearby restaurant?']],
    ['(.*) (interested|excited) (.*)', ['That\'s great! I\'m glad you\'re %2 about %3.']],]

chatbot = Chat(pairs, reflections)

print('type \'exit\' to stop conversing')

while True:
    user_input = input('User: ')
    if user_input == 'exit':
        print('Good bye!')
        break
    else:
        response = chatbot.respond(user_input)
        print('Chatbot:', response)
