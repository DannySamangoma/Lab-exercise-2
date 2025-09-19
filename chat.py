name = input('enter your name: ')
print('hello ' + name + '! nice to meet you')
feeling = input('how are you feeling today? ')
if feeling.lower() == 'good':
    print('thats great to hear, ' + name + '!')
elif feeling.lower() == 'bad':
    print('im sorry to hear that, ' + name + '. i hope your day gets better!')
print('it was nice chatting with you, ' + name + '! have a great day!')