w=['Strawberry','Greetings','Umbrella','Teacher','Lollipop']
with open('words_list','a+') as words:
    for word in w:
        words.write(word.lower())
        words.write('\n')
words.close()




