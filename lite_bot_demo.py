import json
import subprocess
from difflib import get_close_matches 
from list_of_os_fuction import driver_url,open_a_browser,drive_set_up,driver_application,application_tracker
#from util.voice_vox_tts import voicevox_driver_function
from auto_write import driver_write
from files_organizer_prototype import driver_organize
import random
import threading
from QuickSearch import google_sc
import time

from datetime import datetime,date

#from playsound import playsound
tag_ic={}
time_out_space=[]
total_container=[]
tomoe_mode_check=[]
tomoe_respond=[]
thread_voicevox_killswitch=[]
user_name="your name here"
thread_start=False

def Load_Knowlege_Base(file_path: str) -> dict:
    with open(file_path, 'r',encoding="utf-8") as file:
        data:dict = json.load(file)        #utf-8 is add for jp
    return data #this return a dict of json data  load and conver the data to dict

def Save_Knowlege_base(file_path: str, data: dict ):            #this is a case for saving the data in to json file if it doesnt exist 
    with open (file_path, 'w',encoding="utf-8" ) as file:
        json.dump(data,file, indent=2, ensure_ascii=False)         #ascii false is add for jp
    #this take the user input and save it into the json file.

def unpack_multiple_words(total_container: list[str],questions: list[str]) -> None:         #this will populate the question in total container,and it return notthing
    #print("check unpack")
    #print(questions)
    for words in questions:
        for items in words:
            for items2 in items:
                total_container.append(items2)
    #print(total_container)
    return 
 
def Find_Best_Match(user_question: str , questions: list[str] ) -> str | None:          #this take a string value of the user_input and also take a list that contain a string: 
    #global total_container
    #print(questions)               #checker
    matches: list = get_close_matches(user_question, questions, n= 1, cutoff= 0.4)
    return matches[0] if matches else None 
    # this make a case that if matches is found then return the first of the anwsers of the question else return nothing. 

def Get_Answer_For_Question(question: str, knowledge_base: dict)->str | None: 
    #print(knowledge_base)
    for q in knowledge_base["ai_knowlege"]:            #this is the first layer 
        for items in q["question"]:
            
            if items == question:       #if the user input question is in match the question in the json files the return the answer, think of this like the dict with its key,value pair 
                respond=random.choice(q["answer"])
                index_check=q["answer"].index(respond)
                #print(f"{index_check} this is indext check")
                select_jp_version=q["answer_jp"][index_check]
                terminal_com=q["terminal_command"]
                #print(f"please check this: {terminal_com}")
                #print(respond)
                #print(select_jp_version)
                #return q["answer"],q["answer_jp"]
                return respond,select_jp_version,q["tag"],terminal_com
            
def emotion_system(tag:int)->str:
    emotion_chart=int(random.randint(1,100))                    #range from 1-100 mid is 50 
        #emotion_num=emotion_chart                               #level range in turn with the respond tag levl

'''def tag_system(tag: str):                               #this check and remove the tag that already saw in the dict so that it can be use again
    global tag_ic
    global time_out_space
    if tag not in tag_ic:
        tag_ic[tag]=0
    tag_ic[tag]+=1
    for key,value in tag_ic.items:
        if value == 4:
            time_out_tag= tag_ic.pop(key)
            time_out_space.append(time_out_tag)'''

'''def time_out_remove(start:str):
    global time_out_space
    if len(time_out_space) !=0:
        time_out_space.pop(0)'''
#-------------------------------worker function call----------------------------
def curren_time()->str:
    time_filter=time.strftime('%H:%M:%S:%p')
    hour_and_minut=time_filter[:5]+" "+time_filter[-2:]
    return hour_and_minut

def today_date()->str:
    current_date=date.today()
    return current_date

def conver_time(time)->str:
    #print(time)
    time_12=datetime.strptime(time,"%H:%M")
    hour_format_12=time_12.strftime("%I:%M:%p")
    return hour_format_12

def set_notification(hour:int, minute:int)->None:            #thread only a when call it active, when not call, it should be in active. 
    global thread_start
    thread_start=True
    if(minute>60):
        hour+=1
        minute=minute-60

    #print(f"recieve input hour: {hour}, and minute: {minute}")
    set_time=(hour*60+minute)*60
    print(set_time)
    while(set_time>0):
        if(thread_start):
            set_time-=1

            time.sleep(2)
        else:
            break
    #print(f"total sleep time is {set_time} second")
    #time.sleep(set_time)
    for i in range (5):         #you can replace this with sounds notifications
        print("wake up wake up !!!")
        if(thread_start):
            time.sleep(5)
        else:
            break
    thread_start=False              #check if thread still running 
    return

def safety_check(hour,minute,mode):
    if(mode=="T"):
        if(hour.isnumeric()):
            if(minute.isnumeric()):
            
                return True
        else:
            return False
    else:
        if(hour.isnumeric()):
            return True
        else:
            return False


def tomoe_mode():       #change tomoe speaking mode M for morning N for night                   #this is a thread
    global tomoe_mode_check,thread_voicevox_killswitch
    half_day=12
    tomoe_mode_check.append(str(curren_time()[-2:]))      #starting mode

    while True: 
        if(thread_voicevox_killswitch):
            break
        get_hour=conver_time(str(curren_time().split()[0]))[:2]
        get_mint=conver_time(str(curren_time().split()[0]))[3:5]
        sleep_time=abs(int(get_hour)-half_day)*60+get_mint*60             #get second from hour
        #count down
        while(sleep_time>0):
                if(thread_voicevox_killswitch):
                    break
                else:
                    sleep_time-=1
                    time.sleep(1)                   #clock tick down one second at a time and costance checking the kill switch 
        if tomoe_mode_check:        #not empty 
            tomoe_mode_check.pop()
            get_AM_PM=tomoe_mode_check.append(str(curren_time()[-2:]))
        #time.sleep(sleep_time)                                      #sleep until time to change mode
        

'''def voice_vox(data_bank)->None:                              #deamon thread that access the data respond bank for data.
    global thread_voicevox_killswitch,tomoe_mode_check
    #voice vox start on main first
    #print(f"starting {data_bank}")
    while True:
        if(thread_voicevox_killswitch):
            break
        if(data_bank):
            #print(data_bank)
            text=data_bank.pop(0)
            voicevox_driver_function(text,tomoe_mode_check[0])              #sleep for 5 second and then activate voice 
            time.sleep(2)
        else:
            time.sleep(2)'''
    

def webcall():
    check=input("youtube y/n :?").lower().strip()
    if check=="y":
        mode=input("search youtube ? y/n: ").lower().strip()
        if(mode=="y"):
            user_input=input("what are you searching ?: ")
            driver_url(user_input)
        else:
            driver_url("open a webpage")    #open youtube only
            #user_input=input("open youtube? y/n: ")
            #if(user_input=="n"):
            #    driver_url("open a webpage")    #open youtube only
            #else:
            #    user_input=input("enter your url: ")
            #    open_a_browser(user_input)
            #    print("open webprocess")
        #else:
            #user_input=input("what are you searching ?: ")
            #driver_url(user_input)
    else:           #open normal web page
                user_input=input("URL->(or exit to leave): ")
                if(user_input.strip().lower() in ["exit", "teminate","quit","stop"]):
                    return
                exten="https://"+(user_input.replace("https://",""))
                open_a_browser(exten)

#def show_text_on_sceen(text:str):
    #return
#-----------------------------------------end worker------------------------------------------------
#----------------------------------------start bot respond------------------------------------------
def chat_bot(user_name):
    #open the file
    global thread_start
    knowledge_base: dict =Load_Knowlege_Base('ai_learn_lite.json')
    #print(knowledge_base)
    print(f"welcome back {user_name}!!!!! (0.<) ")
    unpack_multiple_words(total_container,[[q["question"] for q in knowledge_base["ai_knowlege"]]])
    #print(unpack)
    while True: 
        #time.sleep(3)
        user_input=input("please enter something: ")
        if user_input.lower() in ["quit","exit","terminate","done"]:
            if(thread_start==True):
                if(td.is_alive()):
                    thread_start=False
            break
        #print(total_container)
        best_match: str| None = Find_Best_Match(user_input, total_container)            #this either wil toss a none of a answer if it in the json files. 
        #this code above will take the value name "question" in the json file and pack them in to a list, then it will be pass to find_best_match as a list.
        #print(best_match)  
        
        if best_match:
            answer: str = Get_Answer_For_Question(best_match, knowledge_base)
            answer_en=answer[0]
            #answer_jp=answer[1]
            if(answer[3] =="who im i"):
                answer_en=answer_en.replace(":",f"{user_name}")
            print(f' bot en: {answer_en}')
            #print(f' bot jp: {answer_jp}')
            #tomoe_respond.append(answer_jp)
            #time.sleep(3)
            #print(f'com {answer[3]}')
           #winCommand('close ', alias)
            #playsound(r'D:\stream event\text pop.wav',)
            #winsound.Playsound(None, winsound. SND_PURGE)
            #playsound()
            '''
            #display on sceen 
            show_text_on_sceen(answer[0])
            #call jp voiceover 
            voicevox_driver_function(answer[1],'N')
            '''
            #return answer
            #this is where i call the voice vox and call oparation function/voice tts vox take only jp language
            '''
            if (answer[0] in ["yesh......what do you want","sure what would its be ?","nya~!"],):
                task: list=input(what do you want to do?:)
                if task[0]=="open:"
                    if len(list_in_use)!=3
                        if len(application_tracker)
            '''
            if(answer[3] =="time check"):
                #time.sleep(300)
                current_t=curren_time()
                print(f'here the time {current_t} and {today_date()}')
                print(f"change time to 12hous {conver_time(current_t.split()[0])}")
                #tomoe_respond.append(conver_time(current_t.split()[0]))

            if(answer[3]=="set notification"):
                user_input_H=input("what are the Hour in (00): ")
                user_input_M=input("what are the Minute in (00) format: ")
                if((user_input_H  in ["exit","terminate","leave","quit","shutdown"]) or (user_input_M in ["exit","terminate","leave","quit","shutdown"])):
                    print("a.....ok quitting set timer")
                elif(safety_check(user_input_H,user_input_M,"T")):                    #perform safety check of the user input 
                    print(f"i will remind you in {user_input_H} hour and {user_input_M} minute")
                    td=threading.Thread(target=set_notification,args=(int(user_input_H),int(user_input_M)))
                    td.start()                    #it will start and sit in the background 
                    
                    #set_notification(user_input_H,user_input_M)
                else:
                    print("the format are not correct, please only input number only >:l ")

            if(answer[3] =="initiating application"):
                print("application")
                #currently under development
                user_input=input("please enter the mode you want [(open/close):(app/folder)] or check current process:").strip().lower().split(":")
                if(len(user_input)==2):
                    driver_application(user_input[0],user_input[1])
                elif(user_input==["check current process"]):
                    print(f"this is the current process: {application_tracker} ")
                else:   #error handle
                    print("there are no command for that......")


                #tomoe_respond.append("このプロセスは現在開発中だ.")

            if(answer[3] == "initiating webprocess"):
                webcall()

            if(answer[3] == "initiating search"):
                ## 
                user_input=input("what do you want to search ?: ")
                respond=google_sc(user_input)
                print(respond)
                user_input=input("do you want visit these website ? y/n: " ).strip().lower()
                if(user_input=="y"):
                    user_choose=input(f"please select for the available link\n{respond} \nin the format of 0-{len(respond)}: ")
                    if(safety_check(user_choose,"","")):
                        if(int(user_choose)<=len(respond)):
                            get_url=respond[int(user_choose)]
                            open_a_browser(get_url)
                    else:
                        print("the selection you pick does not exist")



                #tomoe_respond.append("これが検索結果である")
                #print("open web search")

            if(answer[3] == "initiating organize"):
               driver_organize()
               #print("organize")

            if(answer[3]=="initiating autowrite"):
                user_input=input("but first what mode do you want 1 or other *1 is for reading the file, other for is user input: ")
                if(user_input.strip()=="1"):
                    driver_write("none",user_input)
                else:
                    user_input=input("now please enter your sentence.....or copy and paste: ")
                    driver_write(user_input,0)
              

        else: 
            print(f"bot: i dont know what the {user_input} sorry (;-;)")
            #teaching bot area
            #print("bot: i dont know the anwser. can you teach me ?")
            ''''user_choice=input("y/n").strip().lower()

            
            #new_answer_jp: str=input('japanese version please!: ')

            if (user_choice.lower() == "y"):
                new_answer: str = input('type the answer: ').strip()
                new_answer_jp: str=input('japanese version please!: ')
                terminal_com=input("terminal com: ")
                knowledge_base['ai_knowlege'].append({"tag": "N","question": [user_input], "answer": [new_answer], 'answer_jp': [new_answer_jp],'terminal_command':[]})
                Save_Knowlege_base('ai_learn_lite.json',knowledge_base)
                print("you input have being log !")'''

if __name__ =='__main__':
    #starting voice vox 
    # p=subprocess.Popen(r"d:\AI project\voicevox\VOICEVOX\run.exe")
    # th=threading.Thread(target=tomoe_mode,name="mode changer")
    # time.sleep(12)
    # #prep
    #starting voice vox 
    #load up program 
    print("loading..........^.^")
    #tomoe_mode_check.append("M")
    #p=subprocess.Popen(r"d:\AI project\voicevox\VOICEVOX\run.exe")
    #x=threading.Thread(target=tomoe_mode,name="tomoe mode")
    #T=threading.Thread(target=voice_vox, args=(tomoe_respond,))
    #T.start()
    drive_set_up()      #set up folder
    #time.sleep(7)
    print("welcome to the tomoe interactive system >:3")
    #tomoe_respond.append("ホイ～、私の名前はトモエデス～,そして、巴インタラクティブシステムへようこそ.")
    #time.sleep(4)
    chat_bot(user_name)
    #thread_voicevox_killswitch.append("end")
    #time.sleep(2)
    #print(T.is_alive())
    #get_folder()
    print("bai bai ")
    #p.terminate()
