#importing required modules 
import os
import socket
import string

#setting path variables 
base_dir = '/home/data'
output_dir ='/home/output'

#accessing all files in the given directory 
files = os.listdir(base_dir)

#extracting text files 
txt_files = []
for file in (files):
    if file.endswith('.txt'):
        txt_files.append(file)


#locating target files 
if_file_path = os.path.join(base_dir, 'IF.txt')
limerick_file_path = os.path.join(base_dir, 'Limerick-1.txt')
res_file_path = os.path.join(output_dir,'result.txt')

#calculating no words in IF.txt
wc_if = 0
with open(if_file_path) as file_if:
    for row in file_if:
        wc_if+=len(row.split())


#calculating no of words in Limerick-1.txt
wc_lim = 0
with open(limerick_file_path) as file_lim:
    for row in file_lim:
        wc_lim+=len(row.split())  

#computing top 3 frequent words in the IF.txt
words = {}
with open(if_file_path) as file_if:
    for stat in file_if:
        for word in stat.split():
            word = word.translate(str.maketrans('', '', string.punctuation))
            word = word.capitalize()
            if word in words:
                words[word]+=1
            else:
                words[word]=1

#using lambda function
sort_words = sorted(words.items(), key=lambda x: x[1], reverse=True)[:3]

#getting the host machine's IP address
hostname = socket.gethostname()
IP_address = socket.gethostbyname(hostname)

#writing output to the result.txt
with open(res_file_path,'w') as res_file:
    res_file.write(f"List of all the text files in the directory\n")
    for file in txt_files:
        res_file.write(f"{file}\n")
    res_file.write(f"No of words in Limerick.txt:{wc_lim}\n")
    res_file.write(f"No of words in IF.txt:{wc_if}\n")
    res_file.write(f"Total of words : {wc_if+wc_lim}\n")
    res_file.write(f"Top 3 words with their counts in IF.txt\n")
    for wd,wc in sort_words:
        res_file.write(f"{wd} -> count: {wc}\n")    
    res_file.write(f"IP address of the machine: {IP_address}\n")

#displaying output from result.txt file
with open(res_file_path) as res_file:
    for line in res_file:
        print(line)















    