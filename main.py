import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import random
import os
import subprocess
r=sr.Recognizer()

genre=["1:pop",'2:rock','3:metal','4:dance','5:workout','6:jazz','7:Bollywood','8:Sandalwood','9:Tollywood','10:Kollywood']
joke=["i ate a clock yesterday.....it was very time consuming","a perfectionist walked into a bar.....apparently,the bar wasnt set high enough","sleep is a weak substitute for coffee",'what kind of a shoe does a frog wear?  open toad']
game = ['1:2048','2:flappy bird','3;Krunker','4: tictactoe']

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 225)
def speak(text):
    engine.say(text)
    engine.runAndWait()


def online():
    print('starting all system applications')
    speak('starting all system applications')
    print('installing all drivers')
    speak('installing all drivers')
    print('every driver is installed')
    speak('every driver is installed')
    print('all systems have been started')
    speak('all systems have been started')
    print('now i am online ')
    speak('now i am online ')
    print('Thank you for using assistant, i was made by tarun and mayur of grade 11')
    speak('Thank you for using assistant, i was made by tarun and mayur of grade 11')

    
def wishme():
    hour=int(datetime.datetime.now().hour)
    #date=int(datetime.datetime.now().day)
    #year=int(datetime.datetime.now().year)
    #print(hour)
    #print(date)
    #print(year)
    if hour>=0 and hour<12:
        print('Good Morning ')
        speak('Good morning ')
    elif hour>=12 and hour<18:
        print('Good Afternoon')
        speak('Good afternoon')
    else:
        print('Good Evening')
        speak('Good evening')
    print('i am assistant,how may i assist you,ask me for help if you dont know how to use')
    speak('i am assistant,how may i assist you,ask me for help if you dont know how to use')
    

if __name__ == '__main__':
    online()
    wishme()
    engine.runAndWait()


    
#defining math operations
def add(num1, num2): 
	return num1 + num2 

def subtract(num1, num2): 
	return num1 - num2 


def multiply(num1, num2): 
	return num1 * num2 

 
def divide(num1, num2): 
	return num1 / num2





engine.setProperty('rate', 200)
def takeCommand():
    with sr.Microphone() as source:
        print('what can i do for you')
        speak('what can i do for you')
        audio=r.listen(source)
        try:
            query = (r.recognize_google (audio, language="en-IN"));
            #r.energy_threshold = 50
            r.pause_threshold=0.5
            #r.operation_timeout = 'none'
        
            print('User said:',query)
            query=query.lower()


            if "help" in query:
                print('''                 WIKIPEDIA - metal wikipedia
                 GOOGLE - open google
                 YOUTUBE - open youtube
                 STACKOVERFLOW - open stackoverflow
                 GITHUB - open github
                 JOKE -  tell me a joke
                 MUSIC - play music
                 PYTHON - open IDLE or open python
                 OFFICE FOLDER - open office
                 WORD - open word
                 POWERPOINT - open powerpoint
                 EXCEL - open excel
                 CALCULATOR - use calculator
                 CHATBOT - speak!
                 MAIL - send gmail
                 GAMES - play game
                 CLOSE AI- close
                 CODE RED - opens a video to JEE preps 
                 SHUTDOWN PC- shutdown''')
                 
            elif "wikipedia" in query:
                query=query.replace("wikipedia","")
                text=(wikipedia.summary(query, sentences=2))
                speak('According to wikipedia')
                print(text)
                speak(text)

            elif "google" in query:
                webbrowser.open('google.com')

            elif "youtube" in query:
                webbrowser.open('youtube.com')

            elif "stack overflow" in query:
                webbrowser.open('stackoverflow.com')

            elif "github" in query:
                webbrowser.open('github.com')

            elif "gmail" in query:
                webbrowser.open('gmail.com')

            elif "joke" in query:
                x=random.randint(0,4)
                print(joke[x])
                speak(joke[x])


            elif "music" in query:
                print(genre)
                speak(genre)
                speak('Enter code of the genre you want to listen')
                select=input(('Enter code of the genre you want to listen'))
            
                if select == '1':
                    webbrowser.open('www.youtube.com/watch?v=Neu8kbCop48')
                elif select == '2':
                    webbrowser.open('www.youtube.com/watch?v=sA1f0LBdTQQ')
                elif select == '3':
                    webbrowser.open('www.youtube.com/watch?v=PI1oVXHTPUI')
                elif select == '4':
                    webbrowser.open('www.youtube.com/watch?v=UX1cdPqW5M8')
                elif select == '5':
                    webbrowser.open('www.youtube.com/watch?v=a1CwygQ13VI')
                elif select == '6':
                    webbrowser.open('www.youtube.com/watch?v=qj9NFFvJ7o4')
                elif select == '7':
                    webbrowser.open('www.youtube.com/watch?v=JJyOiuX0e1M')
                elif select == '8':
                    webbrowser.open('www.youtube.com/watch?v=ebz20FHrT44&list=RDQM565GLzPLoBE&start_radio=1')
                elif select == '9':
                    webbrowser.open('www.youtube.com/watch?v=7o11CfS6uBI')
                elif select == '10':
                    webbrowser.open('www.youtube.com/watch?v=L25VCKhvGB0')
                
            elif 'shutdown' in query:
                speak('understood ')
                speak('connecting to command prompt')
                speak('shutting down your computer')
                cmdCommand = "shutdown -s"
                process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                
            elif "open idle" in query or "open python" in query:
                idlepath = "C:\\Python368\\Lib\\idlelib\\idle.pyw"
                os.startfile(idlepath)

               
            elif "open office" in query:
                officepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013"
                os.startfile(officepath)

            elif "open excel" in query:
                excelpath = "C:\\Program Files\\Microsoft Office\\Office15\\EXCEL.EXE"
                os.startfile(excelpath)

            elif "open powerpoint" in query:
                ppp= 'C:\\Program Files\\Microsoft Office\\Office15\\POWERPNT.EXE'
                os.startfile(ppp)

            elif "open word" in query:
                wpath= 'C:\\Program Files\\Microsoft Office\\Office15\\WINWORD.EXE'
                os.startfile(wpath)

            elif 'hi' in query or 'hey' in query or 'hello' in query or 'sup' in query:
                print('hello,hope you have a nice day')
                speak('hello,hope you have a nice day')

            elif 'good morning' in query:
                hour=int(datetime.datetime.now().hour)
                if hour>0 and hour<12:
                    print('Good Morning')
                    speak('Good morning')
                elif hour>12 and hour<18:
                    print('Good Afternoon')
                    speak('Good afternoon')
                else:
                    print('Good Evening')
                    speak('Good evening')

            
            elif 'good afternoon' in query:
                hour=int(datetime.datetime.now().hour)
                if hour>0 and hour<12:
                    print('Good Morning')
                    speak('Good morning')
                elif hour>12 and hour<18:
                    print('Good Afternoon')
                    speak('Good afternoon')
                else:
                    print('Good Evening')
                    speak('Good evening')

            elif 'good night' in query:
                print('good night,dont let the bed bugs bite')
                speak('good night,dont let the bed bugs bite')


            elif 'calculator' in query:
                print('''Please select operation 
	         1. Add
		 2. Subtract 
	         3. Multiply
        	 4. Divide''') 
                speak('''Please select operation 
		1. Add
		2. Subtract 
		3. Multiply
		4. Divide''') 
                select = input("Select operations form 1, 2, 3, 4 :") 
 
                number1 = int(input("Enter first number: ")) 
                number2 = int(input("Enter second number: "))

                print(number1, number2)

                if select == '1':
                    print(add(number1,number2)) 

                elif select == '2':
                    print(subtract(number1,number2))
					 

                elif select == '3':
                    print(multiply(number1,number2))
					 

                elif select == '4':
                    print(divide(number1,number2)) 
					
                else:
                     print("Invalid input")

            elif 'game' in query or 'games' in query:
                print(game)
                speak(game)
                game_input=input('Enter  game code you want to play')
                speak('Enter game code you want to play')
                if game_input == '1':
                    p2048='C:\\games\\2048\\graphics_2048.py'
                    os.startfile(p2048)

                elif game_input == '2':
                    webbrowser.open('flappybird.io/')

                elif game_input == '3':
                    webbrowser.open('krunker.io/?game=SIN:cqm1b')

                elif game_input == '4':
                    pttt='C:\\games\\tic\\line.py'
                    os.startfile(pttt)
                else:
                    print('No game found!')
                    speak('No game found!')


            elif 'code red' in query:
                webbrowser.open('www.youtube.com/watch?v=Od6faPWrJ1s')
                        
                    
            elif 'close' in query:
                print("okay sir")
                speak("okay sir")
                exit()
                sys.exit()
                

            else:
                print('I didnt understand what you said, please try again')
                speak('I didnt understand what you said, please try again')

        except:
            print('I didnt understand what you said, please try again')
            speak('I didnt understand what you said, please try again')
            
            return "none"
        return query



        
if __name__=='__main__':
    while True:
        takeCommand()



engine.runAndWait()
