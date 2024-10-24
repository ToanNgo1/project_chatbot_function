#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""auto write text applications"""
__author__="Toan Ngo"
#prototype
import time
import os
import pyautogui
#please pip install the following first before running this auto write to text aplication
# pip time,pyautogui 
# create a file that will be use as text to write 
def write_to_demo(sample_file,sentence_container:list)->None|str:                 #this will be responsible to write to a file and that inturn write to a application that the user selected 
    if(len(sentence_container)>0):
      print(len(sentence_container))
      with open(sample_file+'.txt','w+')as inline:
                  #inline.write("sample datav2")                                                 #pipe feed for text to be put in autotype
                  for i in sentence_container:
                        inline.write(i+"\n")
      inline.close()          #save
    else:
          print("there are nothing in the quere to write.")
          return"null"

def write_to_app(demo_file,flags)->None:
      if(flags!="null"):
            print("you got 10 second to wait for it to auto input to any kinda container that take string")
            time.sleep(10)
            text=open(demo_file+'.txt','r')
            for line in text:
                  pyautogui.typewrite(line)
      else:
            print("there are nothing to write")

def driver_write(world:str, mode:int):
      if mode =="1":      #read from files *world doesnt matter here 
            file_r=input("what are the text file name ?*make sure the file in the same folder as this files:").strip()
            while True:
                  if(file_r in ["stop","terminate","quit","exit"]):
                        break
                  elif(os.path.exists(file_r)):       #check is path is real and exist 
                        break
                  else:
                        print("file is invalid, please put the extention along with the file name")
                        file_r=input("please re enter: ")
                        
            with open(file_r,"r",encoding="utf-8") as inline:
                  content=inline.readlines()
                  inline.close()
            write_to_app('text_container',write_to_demo('text_container',content))

      else: #read from user input  
            write_to_app('text_container',write_to_demo('text_container',[world]))
if __name__== "__main__":
      sentence_test=["this text will be auto write once this program run"]
      #write_to_demo('text_container',sentence_test)    #name of the text file that it will create 
      write_to_app('text_container',write_to_demo('text_container',sentence_test) )
#-testing area----this is a first sample sentencesample
#you coud use this as a read a text files and retype it to text aplications you click on as well  
# 
# #