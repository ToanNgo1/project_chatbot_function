#offline voice 
from vosk import Model,KaldiRecognizer
import pyaudio
import keyboard
#load the model for the language #note this one work not that great, try to get the open ai offline version a try 
model=Model(r"C:\Users\Toan\Desktop\project speech\main method\util\vosk-model-small-en-us-0.15")
recognizer=KaldiRecognizer(model,16000)     #(model,frequency)
mic= pyaudio.PyAudio()
stream=mic.open(format=pyaudio.paInt16,channels= 1, rate=16000, input=True, frames_per_buffer=8192 )
stream.start_stream()
#create a stop and start button

def interaction():
    while True:
            data=stream.read(4096,exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                text= recognizer.Result()
                
                re_shape=text[14:-3]
                return(re_shape)
            #if re_shape=="stop":
             #       break
if __name__=="__main__":
    #word="ah2222"
     stop=False
     while stop==False:
        if keyboard.is_pressed('RIGHT_SHIFT'):
            print("speak")
            print(f"result: {interaction()}")
            print("right shift to speak and right ctrl to end")
        elif keyboard.is_pressed('RIGHT_CTRL'):
                stop=True
