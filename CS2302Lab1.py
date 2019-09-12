# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#function to turn word into a list
def split_word(word):
  return list(word)

#function to find anagrams
def find_anagrams(word, i):
  list_of_anagrams=[]
  if (i==len(word)-1):
    separator = ', '
    anagram=separator.join(word)
    list_of_anagrams.append(anagram)
  else:
    j=i
    for j in range(len(word)):
      temp=word[i]
      word[i]=word[j]
      word[j]=temp
      find_anagrams(word, i+1)
      temp=word[i]
      word[i]=word[j]
      word[j]=temp
  return list_of_anagrams
      

#creates a list from file of words
file = open('words_alpha.txt', 'r')
words_list = file.readlines()

#asks for word, calls function to split word into letters, and initiates an index
word = input('Enter a word or empty String to finish: ')
list_of_letters=split_word(word)
letter_index=0

#call function to find anagrams
list_of_anagrams=find_anagrams(list_of_letters, letter_index)
list_of_anagrams.sort()

length_of_anag_list=len(list_of_anagrams)
length_of_words_list=len(words_list)

for i in range(length_of_anag_list):
  for j in words_list:
    if(words_list[j]==list_of_anagrams[i]):
      print(list_of_anagrams[i])