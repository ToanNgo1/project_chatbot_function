#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""files organizer"""
__author__=""
#prototype 
import os
import shutil
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
black_list=["files_organizer_prototype"]       #files name for black list 
#stop_command=[]     #un-use for now
#                       work function
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
def moving_file(dst_path,main_directory,file_type):
    undo_key=[main_directory,dst_path,file_type]
    try:
        os.chdir(main_directory)        #point to the main where you will be moving the file
    except:
        return ("the directory where the fill will be taking from doesnt exist")
    list_of_file=os.listdir()
    for file in list_of_file:
        #print(os.path.splitext(file)[0])
        if os.path.splitext(file)[0] in black_list:
             continue
        if file.endswith(file_type):
            packet=os.path.join(main_directory,file)
            count=0
            if  not os.path.exists(os.path.join(dst_path,file)):
                print(f"moving file {file} to {dst_path} now")
                #
                shutil.move(packet,dst_path)
            else:
                print(F"this file {file} already exist in the destination of the directory(unmove)")
            ''' extrac_start,extrac_end=os.path.splitext(file)
            count+=1
            oldname=packet
            newname=os.path.join(main_directory,f"{extrac_start}_{count}{extrac_end}")'''
    return undo_key

             
def rever_move(list_path:list):
    file_type=list_path.pop()
    main_directory=list_path.pop()
    dst_path=list_path.pop()
    container=[main_directory,dst_path,file_type]
    return container    #(1.2.3)

def check_sub(dst_path,mode:str|None)->list:   #target folder mode
    #needed_sub=['document','code','video','image','web']
    container=[]
    packet_return=[]
    for files in os.listdir(dst_path):
          path_check=os.path.join(dst_path,files)
          #print(path_check)
          if os.path.isfile(path_check):            #scan the files to get their extenstion 
            extenstion_cut_beginning,extenstion_cut_end=os.path.splitext(files)
            #print(f"beginning of file {extenstion_cut_beginning}")
            #print(f"end of the file{extenstion_cut_end}")
            container.append(extenstion_cut_end)
    #now all the files have theirs extenstion cutoff
   # print(f"before {container}")
    container=list(set(container))
  #  print(container)
    for items in container:     #only return the extenstion of what folder are needed
        # print(f"items {items}")
         category_packet=category(items)
         #print(category_packet)
         packet_return.append(category_packet)
    if(mode=='[1]'):            #create the folder
        for folder in packet_return:
            if(folder==None):               #skip files type that the program not understand yet: you can change this by modifind the category section.
                 packet_return.remove(folder)
                 continue
            absolute_path=os.path.join(dst_path,folder)#the route of the folders 
           # print(absolute_path)
            if not os.path.exists(absolute_path):
                os.makedirs(absolute_path)
            else:
                print(f"this folders already exist {folder}" )
       # print(os.listdir(dst_path))
    else:
        return packet_return

def category(files_extent):
    image_extension=['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    video_extension=['.mp4', '.avi', '.mkv', '.mov']
    document_extension=[ '.txt','.docx', '.pdf', '.xlsx']
    code_extension=['.py','.ipynb','.java','.js','.class'] #update if you want to add more extenstion to the container folders  
    web_extension=['.htm','.css']
    web_aplication=['.url',]
    #sample_injeck=['.txt']
    #print(f'files_extent {files_extent}')
    if files_extent in image_extension:
                return "Image_files"                #this is the name of the folder that it will create
    elif files_extent in video_extension:
                return "Video_files"
    elif files_extent in document_extension:
                #print(f"exten {exten}")
                return "Document_files"
    elif files_extent in code_extension:
                return "Code_files"
    elif files_extent in web_extension:
                return "webDevelopment_files"
    elif files_extent in web_aplication:
                return"webApps"
    #elif files_extent in sample_inject:
    #            return "sample folder name"
    else:
             pass
     
def arrange_files (dst_path):                   #this responsible for making folder to contains files
    #sub_folder=["document","code","java","video","image","web"]
    global black_list
    sub_folder=check_sub(dst_path,None)         #return the extenstion of the files only 
    print(sub_folder)
    for folder in sub_folder:
        if(folder==None):                       #if the program not knowinng the files type it will skips it 
             sub_folder.remove(folder)
             #print(sub_folder)
             continue
        absolute_path=os.path.join(dst_path,folder)#the route of the file
        if not os.path.exists(absolute_path):
            os.makedirs(absolute_path)
        else:
            print(f"this folders already exist {folder}" )

    #os.chdir(dst_path)
   # print(os.listdir(dst_path))
    for files in os.listdir(dst_path):
        file_path_check=os.path.join(dst_path,files)
        #print(f"{file_path_check} test")
        if os.path.isfile(file_path_check):
            category_check=os.path.splitext(files)[1]
            blackList_check=os.path.splitext(files)[0]
            if(blackList_check in black_list ):
                 continue
            extention_check=category(category_check)
           # print(f"ext {extention_check}")
            if extention_check in sub_folder:
                #print(files)                   #black list
                new_file_name=os.path.join(dst_path,files)   
                locate=os.path.join(dst_path,extention_check)#location os the folder you can put file to
                #print(os.path.exists(os.path.join(locate,files)))
                #print(locate)
                #print(os.path.join(locate,files))
                count=1
                if os.path.exists(os.path.join(locate,files)):
                    while True:
                        exten=os.path.splitext(files)[1]
                        main=os.path.splitext(files)[0].rsplit("_",1)[0]
                        print(main)
                        print(f"exten {exten}")
                        old_name=new_file_name
                        new_file_name=os.path.join(dst_path,f"{main}_{count}{exten}")
                       # print(old_name)
                        #print(new_file_name)
                        os.rename(old_name,new_file_name)
                       # print(os.path.exists(os.path.join(locate,f"{main}_{count}{exten}")))
                        
                        if(os.path.exists(os.path.join(locate,f"{main}_{count}{exten}"))):
                            count+=1
                            #print(os.path.join(locate,new_file_name))
                            #print("stop")
                            continue
                        else:
                             break
                #print("now movving file")
                #print(new_file)
                #print(locate)
                
                shutil.move(new_file_name,locate)

def search_folder(target_directory:str,extenstion:str,file_name:str)->list|str:
    #return_packet=[]
    #return_packet_alt=[]
    return_packet_alt_dict={}
    search_condition=False
    key="go"
     #move pointer to the destination 
    #print("check")
    try:
        os.chdir(target_directory)              #change directory
    except:
        print("this directory doesnt exist")
        return
    print('successful changing directory')
    list_file=os.listdir(target_directory)
          
    for files in list_file:
        #print(files)
        check=os.path.join(target_directory,files)
        if os.path.isfile(check):
            if(extenstion=="none"):
                file_name_extract=os.path.splitext(files)[0]
                if(file_name in file_name_extract):
                    #print("yes")
                    #return_packet_alt.append(files)
                    return_packet_alt_dict[files]=check
                    key="stop"
            elif(file_name=="none"):
                extenstion_extract=os.path.splitext(files)[1]
                if(extenstion_extract==extenstion):
                    if key=="go":
                        key="stop"
                    #return_packet_alt.append(files)
                    return_packet_alt_dict[files]=check         #contain files name and route
            else:    
                return_packet_alt_dict[files]=check
                #print("int")
                #print(return_packet_alt_dict)
        #if(extenstion==None):
    if (key=="go") and  (len(return_packet_alt_dict)>0):      
        file_name_com=file_name+extenstion      #if both name and type are know 
        if file_name_com in return_packet_alt_dict:
            '''items_index=return_packet.index(file_name_com)
            extract=str(return_packet.pop(items_index))
            route=os.path.join(target_directory,extract)'''
            route=return_packet_alt_dict[file_name_com]
            search_condition=True
    elif key=="stop":
         print("here all the files that similar to the requested files ")
         #print(return_packet_alt_dict)
         for item,value in return_packet_alt_dict.items():
              print(f'{item}:\t {value}')
    if search_condition:
        print(f'{file_name_com}:\t{route}')
        #print(return_packet_alt_dict)
    else:
        if not return_packet_alt_dict:
             print("there are no files with that name and extenstion ")
       # else:
        #    print(return_packet)
        else:
             print("there are no files in the target directory")

def check_directory(main_directory:str)->list:          #return what directory in the current destination
     route=main_directory
     container_directory=[directory for directory in os.listdir(route) if os.path.isdir(os.path.join(route,directory))]
     return container_directory
#-------------------------------------------------------------------------------------------------------------------------
#                                                user input handle
#-------------------------------------------------------------------------------------------------------------------------
#funtion_dict={"move file":moving_file,"arrange all file":arrange_files,}
def case_check(x):
    match x:
        case "move":
            return "move file"
        case "arrange":
            return "arrange all"
        case "search":
            return "search"
        case "create_folders":
            return "create folders"
        case "check directory":
            return "check directory"

def case_check_search(x_name:str,y_type:str)->bool:
    #print(x_name)
    #print(y_type)
    if (x_name.lower().strip()=="none") and (y_type.lower().strip() != "none"):
        return(False,True)
    elif (y_type.lower().strip()=="none") and (x_name.lower().strip() !="none"):
        return(True,False)
    else:
        return ("can not start a search if two elements are unknow")
    
def number_check(x):
    instr_table=["arrange all","move file","search","create folders","check directory"]
    #print(f'start {x}')
    #print(type(x))
    match x:
        case "1":
            return instr_table.pop(0)
        case "2":
            return instr_table.pop(1)
        case "3":
            return instr_table.pop(2)
        case "4":
            return instr_table.pop(3)
        case "5":
            return instr_table.pop(4)
         
def input_func():
    user_input=input("please enter what you want to do: arrange all file[arrange],move file[move], search files[search], create a folders[create_folders],check directory [check directory] for all files type or[1-5] \nor type !help for more information \nor type exit to close: ")
    #switch=False
    while True:     #mode selection 
       
        #filter 
        user_process=user_input.strip()
        if(user_process=="exit"): #terminate 
            print("terminating") 
            #sys.exit()
            return "exit"
        #send
        if(user_process.isdigit()):
            #print("test")
            number_short=number_check(user_process)
            #print(number_short)
            #print( not number_short)
            if number_short:
                print(f'current selected mode: {number_short}')
                activation(number_short)
                return number_short
        elif(user_process.isalpha()):
            print("text")
            packet=case_check(user_process.lower())
            if packet:    
                print(f'current selected mode: {packet}')
                activation(packet)
               #user_input=input("there are no function for that !!!!\n sellect on of these [move file,arrange all,search files,create folders] or select from 1-4")
                #print("sample")
                #print(stop_command)
                return packet
        user_input=input("there are no function for that !!!!\n sellect on of these [move,arrange,search,create_folders] or select from 1-5: ")

def activation(mode:str)->None:
    #one directory mode
    #check_point=["","none"]
   # bot=False
    check=input("you want to use local files [execution] or [change directory]: ").strip().lower()
    check_re=True
    while True:
        if check in ["quit","terminate","stop","exit"]:
             return
        if check in["execution local","lex"]:
            break
        elif check in ["change directory","cd"]:
            user_currentDT=input("please enter the current directory: ")
            if os.path.exists(user_currentDT):
                break
            else:
                 print("path doesnt exits !")
        else:
            check=input("please enter execution local or change directory: ").strip().lower()

    if mode in ["arrange all","search","create folders","check directory"]:       #all these only need one directory
        if check_re==False:
            user_currentDT=os.getcwd()                          #local execution mode
            #user_currentDT=input("please enter the current directory: ")
            if mode =="arrange all":
                #sort all files in the folder
                #user_choice=input("would you like to run this where the this file current located ? y/n: ").strip().lower()
                #if(user_choice in["n","no"]):
                #    print("path")
                #    arrange_files(user_currentDT)

                #else:
                #    print("current")
                #    arrange_files(os.getcwd())

                print("function call arrange")
                arrange_files(user_currentDT)

            elif mode=="check directory":
                print(check_directory(user_currentDT))

            elif mode =="search":
                #search the folder 
                #extra function 
                print("note:\n this search funtion can only run if you know what files name you looking for or the extention of the files")
                files_extent=input("please enter the files extention if you know (or leave it empty): ")
                file_name=input("please enter the files name of the search aplication( or leave it empty): ")
                #check point()
                files_extent=files_extent.lower().strip()
                file_name=file_name.lower().strip()
                if files_extent == "" or file_name == "":
                    print("function call search: ")
                    if(files_extent == ""):
                        files_extent="none"
                    if(file_name == ""):
                        file_name="none"
                    search_folder(user_currentDT,files_extent,file_name)

                else:   #normal search 
                    print("function call search: ")
                    search_folder(user_currentDT,files_extent,file_name)
            else:
                #create a folder for each files type
                    print("function creating a folders")

                    check_sub(user_currentDT,'[1]')
            return user_currentDT
                    
        else:                   #change of directory mode also only mode run by tomoe
             #user_currentDT=input("please enter the current directory: ")
            if mode =="arrange all":
                #sort all files in the folder
                #user_choice=input("would you like to run this where the this file current located ? y/n: ").strip().lower()
                #if(user_choice in["n","no"]):
                #    print("path")
                #    arrange_files(user_currentDT)

                #else:
                #    print("current")
                #    arrange_files(os.getcwd())

                print("function call arrange")
                arrange_files(user_currentDT)

            elif mode =="search":
                #search the folder 
                #extra function 
                print("note:\n this search funtion can only run if you know what files name you looking for or the extention of the files")
                files_extent=input("please enter the files extention if you know (or leave it empty): ")
                file_name=input("please enter the files name of the search aplication( or leave it empty): ")
                #check point()
                files_extent=files_extent.lower().strip()
                file_name=file_name.lower().strip()
                if files_extent == "" or file_name == "":
                    print("function call search ")
                    if(files_extent == ""):
                        files_extent="none"
                    if(file_name == ""):
                        file_name="none"
                    search_folder(user_currentDT,files_extent,file_name)

                else:   #normal search 
                    print("function call search")
                    search_folder(user_currentDT,files_extent,file_name)

            elif mode=="check directory":
                print(check_directory(user_currentDT))

            else:
                #create a folder for each files type
                    print("function creating a folders")

                    check_sub(user_currentDT,'[1]')
            return user_currentDT
                
    else:#move file from one diractory to another:
        #move file
        user_destinationDT=input("please enter the folder that you want to move files into: ")
        if(os.path.exists(user_currentDT)):
            file_type=input("enter the file type you want move")
            if(file_type.strip()==""):
                print("there are no file type move")
            else:
                print("move function")
                moving_file(user_destinationDT,user_currentDT,file_type)
        else:
             print("path do not exist !")
        
#write to file for memo
def write_to_memo(DT:str)->str:
    content=["last destination directory are"]
    with open("last_DT.txt","w+",encoding="utf-8")as inline:
               for i in content:
                   inline.write()
                
#---------------------------------------------------------------------------------------------------------------------
#                                           driver
def driver_organize():
    while True:
        user_receive=input_func()
        print(user_receive)
        if user_receive=="exit":
            break
        #do stuff here
        #activation(user_receive)
        #----------------------------------------------
        more=input("do you want to do something else?")
        if(more.lower() in["no","exit","done"] ):
            break
    print("terminating")
    
#--------------------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    black_list.append("notev3")
    #t=threading.Thread(thread1,"loading")
    while True:
        user_receive=input_func()
        print(user_receive)
        if user_receive=="exit":
            break
        #do stuff here
        #activation(user_receive)
        #----------------------------------------------
        more=input("do you want to do something else?: ")
        if(more.lower() in["no","exit","done"] ):
            break
    print("terminating")
