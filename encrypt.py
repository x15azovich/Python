# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:27:36 2015

@author: Anthony
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  30 17:57:58 2015

@author: Anthony
"""
'''from itertools import groupby
'''
#Delete all of the puncuation in the
#Excerpt text file
def deletePuncuation(puncuatedWord):   #The for loop in the main method passes   
    realList=[]                        #in each individual word in the list of 
    realWord=""                        #individual words
    for letter in puncuatedWord:       #if the individual letter in the word is
        if letter.isalpha():           #in fact a letter then create a new word
            realWord+=letter           #consisting of only alpha characters
    realList.insert(0, realWord)       #Then create a list and turn it into 
                                       #nothing but lower case since the count
    noPuncuation=' '.join(realList)    # of the word does not matter when 
    noPuncuation=noPuncuation.lower()  #it comes to case and then return the
    return noPuncuation                # lowercase list created of 
    #only real lettered strings
    
    #Caesar cypher algorithm
def BruteForceCaesar(letter):
    x=""
    solution=""
    alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
              "y", "z"]
    for i in range(len(alphabet)):
        if letter== alphabet[i] and i <=20:
            x=alphabet[i+5]
            solution += x
        if letter==alphabet[i] and i> 20:
            x=alphabet[i-21]
            solution += x
            
    return solution
#if the letter is located below or equal to the 20th index in the alphabet
    #then add 5 to the index, creating the cypher
#if the letter is located above the 20th index then subtract 21 from it to 
    #get the same affect as looping back around the array. 

              


#Main Method


#Open the text file and split it by the spaces
#into a list
with open("excerpt.txt") as f:
   puncuatedList=f.read().split()
   
#Variables   
   longString=""
   cypherString=""
  
   
   
#separte the list that has the puncuation in it
#into individual strings   
   for wordPunc in puncuatedList:
       longString+=deletePuncuation(wordPunc)
#create a long string of nothing but letters     
   
   #create the ceasar cypher
   for letter in longString:
       cypherString+=BruteForceCaesar(letter)
   print(longString)
   print(cypherString)
   # print the string to the text file
   noFormat= open("stripped-file.txt", "w")   
   noFormat.write("%s" % longString)
   #Print the ceasar cypher to the text file
   cyber= open("cypher.txt", "w")   
   cyber.write("%s" % cypherString)
   
   
   
