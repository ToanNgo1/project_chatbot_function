#list of os_fuction only 3 fuction can be call at a given time that the set limite 3! 
import os
import webbrowser
import subprocess
import keyboard
list_in_use=[]
application_route={"snippingtool":"SnippingTool","notepad":"notepad","vscode":r"E:\Microsoft VS Code\Code.exe","firefox":r"C:\Program Files\Mozilla Firefox\firefox.exe"}
folder_route={}
application_tracker={}      #{vtube studio.exe:"z"}     #contain application name and the process that they currenly occupying, if where to terminate the key will get remove. this act like a live list tracker.  
main_route=r'your desktop path here'               
z,x,c="","",""                                  #process value
def open_a_browser(url:str):
    #note this can not be terminate automaticaly yet 
    #this will open the browser and keep it open even if the strip terminate on if you open the browser first.
    webbrowser.open(url)

def open_application(application:str,application_tracker:dict) -> str|None:         #this take the application route and after it been open it then store that log application in a dict to indicate what being use. 
    global list_in_use,z,x,c
    if "z" not in list_in_use:
        z=subprocess.Popen(application)
        print("process z has been launch") 
        list_in_use.append('z')
        application_name=application.rsplit("\\",1)                 #this is for take the application name only in the route
        application_tracker[application_name[-1].replace(".exe","")]='z'                #this track the name of the application that was open 
    elif "x" not in list_in_use:
        x=subprocess.Popen(application)
        print("process x has been launch")
        list_in_use.append('x')
        application_name=application.rsplit("\\",1)
        application_tracker[application_name[-1].replace(".exe","")]='x'
    elif "c" not in list_in_use:
        c=subprocess.Popen(application)
        print("process c has been launch")
        list_in_use.append('c')
        application_name=application.rsplit("\\",1)
        application_tracker[application_name[-1].replace(".exe","")]='c'
    else:
        return ("sorry all subprocess has been use")
    
def close_application(close_app:str,application_tracker:dict)->str:
    global list_in_use
    global z,x,c
    #close=list_in_use.pop(user_input.strip())          #this remove using the index of the list/array the index
    close=close_app
    if close=='z' and close in list_in_use:
        z.terminate()
        list_in_use.remove(close)                          #remove base on the value that was pass in 
        #z=""
        #record_process_op=
        value=list(key for key in application_tracker if application_tracker[key] == close)             #this should return the key from the value that was input in.
        del application_tracker[value[0]]                                                       #this then remove the key from the dict to show that the process has being terminated.
        print(application_tracker)
        return 'z process has being free of the application , you can now call z'
    
    elif close=='x' and close in list_in_use:
        x.terminate()
        list_in_use.remove(close)
        x=""
        value=list(key for key in application_tracker if application_tracker[key] == close)             #this should return the key from the value that was input in.
        del application_tracker[value[0]]
        return 'x process has being free of the application, you can now call x'
    
    elif close=='c' and close in list_in_use:
        c.terminate()
        list_in_use.remove(close)
        c=""
        value=list(key for key in application_tracker if application_tracker[key] == close)             #this should return the key from the value that was input in.
        del application_tracker[value[0]]
        return 'c process has being free the application, you can now call c'
    else: 
        return" there are no process to terminate"
    
def get_folder(main_route:str,folder_route:dict ):
    search=[directory for directory in os.listdir(main_route) if os.path.isdir(os.path.join(main_route,directory))]       #getting only the directory in a list-> directory name
    for items in search:
        data=r"explorer "+main_route+"\\"+items                          #conver the string into raw first then push it in the dict 
        folder_route[items]=data
    
def drive_set_up():
    global main_route,folder_route
    get_folder(main_route,folder_route)

def driver_url(link:str):
    #voice mode
    if(link.startswith("open a webpage")):
        open_a_browser("https://www.youtube.com/")
    elif (link.startswith("https://www.youtube.com/watch")):
        #youtube link
        open_a_browser(link)
    else:
        #search
        container_url='https://www.youtube.com/results?search_query='
        link=link.split()
        for each_world in link:
            container_url+=each_world + "+"
        open_a_browser(container_url[:-1])

def driver_application(states:str,mode:str):
    #check if the application are full ?
    global application_tracker,application_route,list_in_use

    if (states=="open" and mode=="app"):
        if (len(list_in_use) !=3):
            print(f"list of function:{application_route.keys()}")
            user_input=input("please select one application from the list: ").strip().lower()

            print()
            open_application(application_route[user_input],application_tracker)
            print(f"application has been register as active: {application_tracker}")
    #close aplication 
        else:
            print("please close one of the application first")
            driver_close(application_tracker,list_in_use)

    elif (states=="open" and mode =="folder"):
        if(len(list_in_use)!=3):
            print(f"here the list of folder: {folder_route.keys()}")
            user_input=input("please enter the selective folder from the list (case-sensetive): ").strip().lower()
            if(user_input not in folder_route.keys()):
                print ("there are no such folder") 
                return
            open_application(folder_route[user_input],application_tracker)
            print(f"application has been register as active: {application_tracker}")
    #close aplication 
        else:
            print("please close one of the application first")
            driver_close(application_tracker,list_in_use)
    elif(states=="close"):       #close the app/folder
        driver_close(application_tracker,list_in_use)
    else:
        print("thare are no such command!!!")


def driver_close(application_tracker:dict, list_use:list):
    if application_tracker:
        print(f"these are the current application that is currently register as active: {application_tracker}")
        user_input=input("please enter the process to be close: ").lower()
        while True:
            if(user_input in list_use):
                break
            else:
                print("there are no such application:")
                user_input=input(f"please enter the process to be close again {application_tracker}: ").lower()
        close_application(user_input,application_tracker)
    else:
        print("there are no application to close ")

if __name__ =='__main__':
    #url_sample='https://www.youtube.com/watch?v=U5qtF20HFP8&list=RDU5qtF20HFP8&start_radio=1'
    #url_search='https://www.youtube.com/results?search_query=' #this is for searching
    #search='mediocre- sohbana'.split()
    #for each_world in search:
    #    url_search +=each_world + "+"
    #webbrowser.open(url_search[:-1])
    #root_pattern=r
    #user_input="D:\SteamLibrary\steamapps\common\VTube Studio\VTube Studio.exe"
   
    '''print(f"list of function that available {application_route.keys()}")
    get_folder(main_route,folder_route)
    print(f"here the list of folder {folder_route.keys()}") 
    user_input=folder_route['Code_files']'''
    #if(os.path.exists(user_input.rsplit(" ",1)[1])): #path checker
    #    print("the path exist!!!!!")
    #print(os.path.exists(user_input.rsplit(" ",1)[1]))
    '''user_input2=folder_route['Document_files']'''
    #print(user_input)
    #user_input=r"".join("explorer C:\Users\Toan\Desktop\Code_files")
    #user_input=application_route["vscode"]
    #combine_route=root_
    #if("https://www.youtube.com/watch" in url_sample):

    #    open_a_browser(url_sample)
    '''open_application(user_input,application_tracker)
    open_application(user_input2,application_tracker)
    print(application_tracker)
    print(list_in_use)
    print("please press right ctrl button")
    keyboard.wait('RIGHT_CTRL')
    while(application_tracker): #check is dict is empty if so then it false by defaul
        #print("in")
        user_input=input("enter the process to be close:")
        close_application(user_input,application_tracker)             #this will be base in the user input of what to close by the mapping of dict
    print(f" check application tracker: {application_tracker}")
    print('done')'''
    '''testing'''
    drive_set_up()
    print(f"the folder are now set up {folder_route}")
    print(f"here a re a list of application {application_route.keys()}\n and the folder route{folder_route.keys()}")
    user_input=input("what do you wan do (open/close):(app/folder)?").split(":")
    if(len(user_input)==2):   
        driver_application(user_input[0],user_input[1])
        while(application_tracker):
            #user_input=input(f"enter the process to close {list_in_use}:")
            driver_application("close","")

    print("done")