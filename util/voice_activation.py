#voice transcrip
import keyboard
import time
import speech_recognition as sr 
recognizer=sr.Recognizer()               #sound file
recognizer.energy_threshold=300
tracer_string=""
switch = False 
#call recording voice and transrip 
'''def voice_record_live():
    while True:
        if keyboard.is_pressed("RIGHT_SHIFT"):
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio=recognizer.listen(source)
                    transcribe=recognizer.recognize_google(audio)
                    converted_value=transcribe.lower()
                    tracer_string=converted_value
                    print(f"this is what you said: {converted_value}")
            except sr.RequestError as e:
             print("could not request results; {0}".format(e))
            except sr.UnknownValueError:
                print("unknown error, can you try again.")
        elif keyboard.is_pressed("RIGHT_CTRL"):
            break'''
def voice_record_live()-> str:
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio=recognizer.listen(source)
                transcribe=recognizer.recognize_google(audio)
                converted_value=transcribe.lower()
                tracer_string=converted_value
                #print(converted_value)
                return converted_value
        except sr.RequestError as e:
            print("could not request results: {0}".format(e))
            print("ie....there are no internet connection to connect to google")
        except sr.UnknownValueError:
            print("unknown error, can you try again.")
            return("unknown error, can you try again.")
    #print("voice has being deactivated!")

def interaction()-> str:
    global switch
    print("press the right_shift for activation and right ctrl for termination !")
    while True:
        if keyboard.is_pressed("RIGHT_SHIFT"):
            print("speak now")
            record=voice_record_live()
            if record in ['stop','terminate','stop aplication']:
                switch=True
            return record 
        elif keyboard.is_pressed("RIGHT_CTRL"):
            return
def driver_interaction()->str:
    print("please press the right shift for activation and right ctrl for termination ! >:)")
    while True:
        if keyboard.is_pressed("RIGHT_SHIFT"):
            print("now listening.....0.<")
            record=voice_record_live()
            if(record=="unknown error, can you try again."):
                print("please press the right shift for activation and right ctrl for termination ! >:d")
                continue
            else:
                return record
        elif keyboard.is_pressed("RIGHT_CTRL"):
            return
if __name__=="__main__":
    #print(f'before {tracer_string}')
    while switch==False:
        print(interaction())
    #print(f'after {tracer_string}')