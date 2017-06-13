# -*- coding: utf-8 -*- 
from cutkum2 import segment_text
import re

input =  open("input.txt","r",encoding='utf-8')

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9ก-๙(),!?\'\`]]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    #string = string.replace(u'\ufeff', '')
    return string.strip().lower()


result=[]
for line in input:
  words = clean_str(line)
  word = segment_text(words)
  result.append(word)
  print(word)

outputFile = open('output.txt', 'w',encoding='utf-8')
for item in result:
  outputFile.write("%s\n" % item)

print(result)

