import requests
import subprocess
import numpy as np 
import json
import sounddevice as sd
import keyboard
import time
from rich import print
host='127.0.0.1'
port='50021'
speaker_day=20
speaker_night=66
#mod_table={"speedScale":1.0,"pitchScale":0.0,"intonationScale":1.5,"prePhonemeLength":0.5,"postPhonemeLength":0.6,"outputSamplingRate":24500}
#only thing that you should modify is the pitchScale 
def post_audio_query(tranlated:str, day_time:str)->dict:
    if day_time=="M":
        #pick day speaker
        params= {"text" : tranlated, "speaker": speaker_day}
    elif day_time=="N":
        #pick night speaker
        params={"text" : tranlated, "speaker": speaker_night}
    res = requests.post(f'http://{host}:{port}/audio_query',params=params,)
    query_data=res.json()
    query_data["intonationScale"] = 1.5                    #default 1.0
    query_data["volumeScale"] =1.2                         #default is 1.0
    query_data["prePhonemeLength"] = 0.5                   #default is 0.1 
    query_data["postPhonemeLength"] = 0.6
    query_data["outputSamplingRate"] = 24500
    return query_data
def post_synthesis(query_data: dict, day_time:str)-> bytes:
    if day_time=="M":
        params={"speaker":speaker_day}
    elif day_time=="N":
        params={"speaker": speaker_night}
    headers={"content_type":"application/json"}

    res = requests.post(
        f'http://{host}:{port}/synthesis',
        data=json.dumps(query_data),
        params=params,
        headers=headers,
    )
    return res.content

def play_wavfile(wav_data: bytes):
    sample_rate=24500
    wav_array = np.frombuffer(wav_data, dtype=np.int16)
    sd.play(wav_array,sample_rate,blocking=True)
#when call it will take a daytime system to switch voice type
 
def text_to_voice(text: str,day_of_time : str):
    dayx=day_of_time.upper()
    res =post_audio_query(text,dayx)
    wav=post_synthesis(res,dayx)
    play_wavfile(wav)

def voicevox_driver_function(text:str,day_mode:str):
    #this will requier the user to turn on voice vox first in the other aplication 
    time.sleep(5)
    text_to_voice(text,day_mode)
#def driver_function_on(mode:str):
#    if mode=='on':
#        driver_function()

if __name__=="__main__":
    #day mode M and N
    #driver_function_on("on")
    #what you need to do is to run the exe file in the main method as a subprocess popen then it will start and wait for a string, then it will start doing it task
    p=subprocess.Popen(r"d:\AI project\voicevox\VOICEVOX\run.exe")
    print("please press right ctrl")
    keyboard.wait("RIGHT_CTRL")
    
    time.sleep(20)
    text_to_voice('ホイ～、私の名前はトモエデス～,そして、巴インタラクティブシステムへようこそ.','m')
    p.terminate()
    #driver_function_on("off")