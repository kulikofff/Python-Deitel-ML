import os
import uuid
import telebot, json, requests, librosa, librosa.display

import torch
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
from datasets import load_dataset
import soundfile as sf

token = 'FILL IT'
bot = telebot.TeleBot(token)

model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-small-mustc-en-ru-st")
processor = Speech2TextProcessor.from_pretrained("facebook/s2t-small-mustc-en-ru-st")


def query(filename):
    API_TOKEN = 'FILL IT'
    API_URL = "https://api-inference.huggingface.co/models/facebook/s2t-small-mustc-en-ru-st"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Скажите текст на английском')

@bot.message_handler(content_types=['voice'])
def send_text(message):
    action_function(message)
    
    
def action_function(message):    
    filename = str(uuid.uuid4())
    file_name_full="./voice/"+filename+".ogg"
    file_name_full_converted="./ready/"+filename+".wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)
    os.system("ffmpeg -i "+file_name_full+"  "+file_name_full_converted)
    output = query(file_name_full_converted)
    i = list(output.values())       
    print(i) 
    bot.reply_to(message, i)
    os.remove(file_name_full)
    os.remove(file_name_full_converted) 


import time
if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
