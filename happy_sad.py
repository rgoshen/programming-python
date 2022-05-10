happy_emoticons = [':)', ':-)']
sad_emoticons = [':(', ':-(']

string = input()

happy_count = sum(string.count(emoticon) for emoticon in happy_emoticons)
sad_count = sum(string.count(emoticon) for emoticon in sad_emoticons)

if(happy_count == 0 and sad_count == 0):
    print('none')
elif(happy_count > sad_count):
    print('happy')
elif(happy_count < sad_count):
    print('sad')
else:
    print('unsure')
