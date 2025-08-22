import os
import datetime
import csv
import Recommendations
import graph


def get_name():
    file_exist = os.path.exists('name_txt')
    if file_exist:
        with open('name_txt','r') as name_txt:
            name=name_txt.read()
    else:
        name=input('Enter your name: ')
        with open('name_txt','w') as name_txt:
            name_txt.write(name)
    return name



def get_mood():
    name=get_name()
    print(f'Hi {name},Good to see you!\nHow are you feeling today?\n1-😔 Very Sad\n2-😒 Sad\n3-😐 Neutral\n4-😊 Happy\n5-😃 Very Happy')
    while True:
        try:
            n = int(input('Choose from 1 to 5: '))
            if 1<=n<=5:
               break
            else:
                print('Invalid input!Enter a valid option')
        except ValueError:
            print('Please enter a number between 1 and 5')
    if 1<=n<3:
        q=input(f'Oh,I\'m sorry you are feeling this way {name}.\nWould you like to share what\'s on your mind?\n')
    elif 3<n<=5:
        q=input('Great! What\'s on your mind?\n')
        print("That's great to hear😃.Keep it up!")
    else:
        q=input('Would you like to talk about something? I\'m all ears🙂\n')

    refusals=["no","not now","i don't think so","i'm fine","may be","not sure","nothing"]
    if q.strip().lower() in refusals:
        print("That's okay,you can always talk to me when you're ready 🙂")
    else:
        print("Thank you for sharing that.")
    return n,q
mood,reason=get_mood()


def offer_recommendation():
    print('Would you like to lift your mood with something you enjoy?')
    print('Choose from below:\n1.📚 Read a book\n2.🎧 Listen to music\n3.🍿 Watch a movie\n4.🧘 Try Breathing Exercises')
    print("Let me know and I'll suggest you something good..")
    while True:
        try:
            option=int(input('Enter your choice:'))
            break
        except ValueError:
            print('Please enter a number')

    if option==1:
        Recommendations.reading()
    elif option==2:
        Recommendations.music()
    elif option==3:
        print('What kind of movies would you prefer to watch now?')
        print('1.Malayalam\n2.English\n3.Hindi\n4.Tamil')
        while True:
            try:
                choice=int(input('Enter:'))
                break
            except ValueError:
                print('Please enter a number')

        if choice==1:
            Recommendations.malayalam_movies()
        elif choice==2:
            Recommendations.english_movies()
        elif choice==3:
            Recommendations.hindi_movies()
        else:
            Recommendations.tamil_movies()
    elif option==4:
        Recommendations.breathing_exercises()
    else:
        print("It's ok🙂. Feel free to reach out if you need anything")

print()

date=datetime.datetime.now()
date_str=date.strftime('%Y-%m-%d %H:%M:%S')
rows=[date_str,mood,reason]
file_exists=os.path.exists('mood_info.csv')
with open('mood_info.csv','a',newline='') as mood_info:
    write = csv.writer(mood_info)
    if not file_exists:
        headers=['Date','Mood','Reason']
        write.writerow(headers)
    write.writerow(rows)

print()

if mood>=4:
    print('😃You seem happy today! Keep it up🤗')
    show_avg_mood=input('Do you want to see your average mood so far?(yes/no)').lower()
    if show_avg_mood in ['yes','yeah','sure','ok','of course']:
        with open('mood_info.csv','r') as mood_log:
            moods=[]
            reader=csv.reader(mood_log)
            next(reader)
            for row in reader:
                try:
                    m=int(row[1])
                    moods.append(m)
                except ValueError:
                    continue
            if moods:
                avg_mood=sum(moods)/len(moods)
                print(f'Your average mood so far is {avg_mood:.2f}')
            else:
                print('No data found to calculate')
elif mood==3:
    print('🫤You feel neutral today.Hope the day gets better🫂')
else:
    print('😔Your mood seems very low. No worries..')
    print("I've got your back🙂")
    offer_recommendation()

show_daily_mood=input('Would you like to see a visual graph of mood changes so far?').lower().strip()
if show_daily_mood in ["yes","yeah","sure","of course","absolutely","yup"]:
    graph.visualize()

print()

show_graph=input("Wish to see a visual graph of your mood swings for a specific date?(yes/no) ").lower().strip()
if show_graph in ["yes","absolutely","sure","of course","yup","yeah"]:
    graph.daily_mood_summary()
else:
    name=get_name()
    print(f"Ok,{name}.Stay happy.If you need anything, I'm right here! See you later🙂🫂")












