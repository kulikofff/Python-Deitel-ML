#pip install transformers
#pip install diffusers
#pip uninstall torch
#pip cache purge
#pip install pytorch torchvision cudatoolkit
#pip install torch
#pip install -U sacremoses

#pip uninstall telebot
#pip uninstall PyTelegramBotAPI
#pip install pyTelegramBotAPI
#pip install --upgrade pyTelegramBotAPI

import telebot #pip install pyTelegramBotAPI
import torch
import os

from diffusers import StableDiffusionPipeline

'''
#For developing translate from RU to EN
from transformers import FSMTForConditionalGeneration, FSMTTokenizer
mname = "facebook/wmt19-ru-en"
tokenizer = FSMTTokenizer.from_pretrained(mname)
model = FSMTForConditionalGeneration.from_pretrained(mname)
'''

token = '5789547990:AAHOqaE4mqkGrtqenxUvlWHgBLWAw9QLwD4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Imagine any picture in English text and wait for 10-15 minutes, it is on CPU:(((')

@bot.message_handler(content_types=['text'])
def send_text(message):
    action_function(message)

def action_function(message):
    if message.text.lower():
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True)
        #Use huggingface-cli login for enterging use_auth_token value        
        pipe.to("cpu")
        prompt = message.text
        image = pipe(prompt)["sample"][0]
        image.save(f"test.png")
        filename = "test.png"
        with open(filename, "rb") as f:
           data = f.read()
        bot.send_document(message.chat.id, data)

import time

if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue