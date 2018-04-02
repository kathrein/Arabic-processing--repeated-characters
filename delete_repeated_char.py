import re
import argparse
from itertools import groupby

def special_match(char_to_ckh):
    repeated_characters = ['ب','ت','ل','ه','ر','م','ن','ص','ط','د','ف','ي','ه','خ']
    return char_to_ckh in repeated_characters

def modify_str(modified_str,index, repeated_char):
    if index == 0 and repeated_char =='و':
        modified_str = modified_str+'و'+' ''و'
    else :
        if special_match(x):
            modified_str = modified_str+(x*2)
        else:
            modified_str = modified_str+x
    return modified_str


parser = argparse.ArgumentParser()                                               

parser.add_argument("--input_file", "-f", type=str, help='the input text file.', required=True)

parser.add_argument("--output_file", "-o", type=str, help='the output text file.', required=True)

rx = re.compile(r'(.)\1{1,}') # check if there is repeated consecutive characters more than once


if __name__ == '__main__':
    args = parser.parse_args()
    with open("/Users/xabuka/Desktop/"+args.input_file, mode = 'r', encoding = 'utf-8')  as text_file: 
        lines = text_file.readlines()
            
    
    modified_str =""
    
    
    for line in lines: # for each line in the file
        words = line.split(' ')
        for word in words: # for each word in line
            groups = groupby(word) 
            result = [(label, sum(1 for _ in group)) for label, group in groups] # compute number of consecutive characters
            rxx = rx.search(word)
            if rxx: # if it contains sequential characters
                index = 0 # to locate the repeated character
                modified_str = modified_str+ ' '
                for x,y in result:
    
                    if y > 1:
                        modified_str = modify_str(modified_str,index, x)
                    else:
                        modified_str = modified_str+ x # if the character has one apperance 
                    index = index +y
            else: # if there is no repeated characters in the word 
                modified_str = modified_str +' '+ word
    
    
    fout = open('/Users/xabuka/Desktop/'+args.output_file, 'w', encoding = 'utf-8')
    fout.write(modified_str)
          
    #print( modified_str)