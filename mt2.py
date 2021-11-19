# Importing the required module for text  to speech conversion and speech to text

import re
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from dict import dict
import tkinter as tk
from tkinter import *

English = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Arabic = ['ش', 'غ', 'ظ', 'ذ', 'خ', 'ث', 'ت', 'س', 'ر', 'ق', 'ض', 'ف', 'ع', 'ص', 'ن', 'م', 'ل', 'ك', 'ي', 'ط', 'ح', 'ز', 'و', 'ه', 'د', 'ج', 'ب', 'ا']

root = Tk()
root.geometry("300x300")
root.title(" NLP  ")
  
def Take_input():
    text = inputtxt.get("1.0", "end-1c")
    _text = text.replace(' ', '')
# four variables to store count of English and/or Arabic letters
    engcount = 0
    aracount = 0
    ar = 0
    en = 0
# Language identification based on the language of the majority of letters in a text
    for letter in _text:
        if letter in English:
            engcount = engcount  + 1
            en = engcount / len(_text)
    
        if letter in Arabic:
            aracount = aracount + 1
            ar = aracount / len(_text)
    if en >= .5:
        translate_en(text)
    if ar >= .5:
        translate_ar(text)
def translate_en(text):
    text = text.lower()
    if text in dict.keys():
# converting text into acoustic signal (speech)
        myobj = gTTS(text=(dict[text]), lang='ar', slow=False)
        myobj.save('sound1.mp3')
# playing the acoustic signal of the English translation 
        playsound('sound1.mp3') 
        Output.insert(END, dict[text])
        os.remove('sound1.mp3')
        
import pyttsx3
def translate_ar(text):
    
    #text= re.sub('أ'|'إ', 'ا', text)
    for key, value in dict.items():
        if text == value:
# converting text into acoustic signal (speech)
            engine = pyttsx3.init()
# playing the acoustic signal of the English translation
            engine.say(key)
            engine.runAndWait()
            Output.insert(END, key)    
      
l = Label(text = "Please the word or phrase you would like to translate ")
inputtxt = Text(root, height = 10,
                width = 40,
                bg = "light yellow")
  
Output = Text(root, height = 10, 
              width = 40, 
              bg = "light blue")
  
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Translate",
                 command = lambda:Take_input())
  
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
  
mainloop()





#Importing the dictionary that has English and Arabic phrases in a python dictionary

# Importing the REGEX module which is needed for normalizing Arabic texts

 

# lists of Arabic and English letters to identfy the language of input text


# translate is the main function that gets user's input and figures out if it was
# English or arabic. If the input is English it call transalte_en
# and if the input is Arabic, it call translate_ar

#def translate():
#print("Please write the word or phrase you want to translate")

# This is the function that gets an English text and outputs the Arabic translation spoken and written

    
# This is the function that takes an Arabic text and gives the English translation 

            
