# -*- coding: utf-8 -*-
"""
Created on Mon Nov  30 17:57:58 2015

@author: Anthony
"""
'''from itertools import groupby
'''
#Delete all of the puncuation in the
#Excerpt text file
def deletePuncuation(puncuatedWord):   #The foor loop in the main method passes   
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
    
    
#Delete all of the Duplicated words
#in any list
def deleteDuplicates(clist):            #add every item to an empty list and 
    tempList=[]                         #do not add it to the list if it has 
    for i in clist:                     #been previously added. Then return the
        if i not in tempList:           #uniquly created list
            tempList.append(i)
    return tempList
            
    
    
#Count the number of times an
#individual item occurs in the list
def countEmUp(sortedList):
    x=""                                 #use the count function found on stack
    for i in range (len(sortedList)):    #overflow to count how many times the 
          x+= str(sortedList.count(sortedList[i])) +  " "
    return x                             #item appears in the list



#combine the sorted list with the conted values
#used in the first text file without the formattting
def combineLists(sortedList, countedStrings):
    x=""
    for i in range(len(sortedList)):
            x+= sortedList[i] + " " + countedStrings[i]+ "\n"
    return x


#get only the digits from the combined list
#since the combined list without duplicates
#has the correct mapping of each word to number
def formatList(numbers):            #cycle through the indiviual strings
    x=""                            #separtate the digits with the is digit 
    for i in range (len(numbers)):  #method
        if numbers[i].isdigit():
            x+=numbers[i]
    return x







#Main Method


#Open the text file and split it by the spaces
#into a list
with open("excerpt.txt") as f:
   puncuatedList=f.read().split()
   
#Variables   
   longString=""
   countedNums=""
   combinedNums=""
   formattedNums=""
   sortedList=[]
   
   
   
#separte the list that has the puncuation in it
#into individual strings   
   for wordPunc in puncuatedList:
       longString+=deletePuncuation(wordPunc) + " "
#create a list for counted and a list for sorting       
   clist=longString.split()
   sortedList=longString.split()
#sort the sorting list in alphebetical order with
#the sort method found on stack overflow
   sortedList.sort()
#create a string to store the counted values

                                             
#split the string into a list                
                                            #use the sorted list so that each
   countedStrings=countEmUp(sortedList)     #word and number will map to each 
   allCount=countedStrings.split()          #other
#Combine the strings and the numbers with a method
#You cannot delete the duplicated of the allCount
#because a lot of words will only show up and then
#the mapping would be off when you try to print it
#in the file, Therefore, The combine method is needed
   combinedNums= combineLists(sortedList, allCount) 
   countedNumsAndStrings=combinedNums.split("\n")
#Delete the duplicates of the mapped strings and numbers
   noDuplicates=deleteDuplicates(countedNumsAndStrings)
#After all the numbers are combined take out the numbers 
#that are mapped to each word in order to create a new format
#then repeat this with the words
   
#separated list of numbers
   for i in range (len(noDuplicates)):
       formattedNums+=formatList(noDuplicates[i])+ " "
   numberList= formattedNums.split()
#separated list of words
   stringList=deleteDuplicates(sortedList)
   print(stringList)



   
   # print the combined words and numbers
   noFormat= open("sorted-word-count.txt", "a")   
   for item in noDuplicates:
       noFormat.write("%s\n" % item)
   # create a new format with the words and numbers
   #being in separate columns equally spaced (the reason
   # for separated the combined numbers and words)
   Format=open("formatted-word-count.txt", "a")
   for i in range(len(noDuplicates)-1):
      Format.write("\n" + stringList[i] + " " 
      + numberList[i].rjust(20-len(stringList[i])))
       
   
