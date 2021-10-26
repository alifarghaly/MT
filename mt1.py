#Importing the dictionary that has English and Arabic phrases in a python dictionary
from dict import dict
# Importing the REGEX module which is needed for normalizing Arabic texts
import re
# lists of Arabic and English letters to identfy the language of input text
English = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Arabic = ['ش', 'غ', 'ظ', 'ذ', 'خ', 'ث', 'ت', 'س', 'ر', 'ق', 'ض', 'ف', 'ع', 'ص', 'ن', 'م', 'ل', 'ك', 'ي', 'ط', 'ح', 'ز', 'و', 'ه', 'د', 'ج', 'ب', 'ا']

# translate is the main function that gets user's input and figures out if it was
# English or arabic. If the input is English it call transalte_en
# and if the input is Arabic, it call translate_ar

def translate():
    print("Please write the word or phrase you want to translate")
    text = input()
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
# This is the function that gets an English text and outputs the Arabic translation
def translate_en(text):
    text = text.lower()
    if text in dict.keys():
        print(dict[text])
    else:
        print("Sorry, your phrase is not in my data base")
# This is the function that takes an Arabic text and gives the English translation 

def translate_ar(text):
    
    #text= re.sub('أ'|'إ', 'ا', text)
    for key, value in dict.items():
        if text == value:
            print(key)
            if text != value:
                print("Sorry, your phrase is not in my data base")
translate()    
   
