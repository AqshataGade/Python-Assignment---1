#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Q1
## Store a message in a variable, and then print that message.

Basic_msg = "This is just to show how to store value in variable and print the same."
Basic_msg


# In[2]:


## Q2
## Store a message in a variable andprint that message. Then change the value of your variable to a new message andprint the new message.

Change_msg = "This is the original message."
print(Change_msg)
Change_msg = "This is updated message."
print(Change_msg)


# In[6]:


## Q3
## Store a person’s name in a variable andprint a message to that person.

User_name = input("Please Enter your name: ")
User_msg = print("Hello, ",User_name,"Python is easy language. Would you like to learn more about python today?")


# In[7]:


## Q4
## Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print('Dhiman once said, "If they say it is impossible...It is impossible for them and not for you"')


# In[8]:


## Q5
## Repeat Above Exercise, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message.Print your message.6.

famous_person = "Dhiman"
message = "once said, If they say it is impossible.....It is impossible for them and not for you"
print(famous_person,message)


# In[10]:


## Q6
## Write addition, subtraction, multiplication, and division operations that each result in the number 8.
## Your output should simply be four lines with the number 8 appearing once on each line.

print(4+4)
print(16-8)
print(4*2)
print(int(16/2))


# In[11]:


## Q7
## Store your favouritenumber in a variable.Then, using that variable, create a message that reveals your favour itenumber.
## Print that message. 

fav_no = 40
print('My favourite number is ',fav_no)


# In[12]:


## Q8
## Choose two of the programs you’ve written and add at least one comment to each.
## If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file.
## Then write one sentence describing what the program does.

#This code is to show the calculations
print(4+4)
print(16-8)
print(4*2)
print(int(16/2))

# Below code is to display inspiring quote
print('Dhiman once said, "If they say it is impossible...It is impossible for them and not for you"')


# In[13]:


## Q9
## Store the names of a few of your friends in a list called names.
## Print each person’s name by accessing each element in the list, one at a time.

names = ['Pannu','Kruti','baba']
print(names[0])
print(names[1])
print(names[2])


# In[14]:


## Q10
## Start with the list you used in Exercise 9, but instead of just printing each person’s name, print a message to them. 
## The text of each message should be the same, but each message should be personalized with the person’sname.

names = ['Pannu','Kruti','baba']
print(names[0],', you are awesome friend of mine.')
print(names[1],', you are awesome friend of mine.')
print(names[2],', you are awesome friend of mine.')


# In[16]:


## Q11
## Think of your favouritemode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
## Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

transportation_mode = ['Local train','Express','AC Local']
for element in transportation_mode: print('I would like to travel by ' + element + ' major missing due to lockdown')


# In[ ]:




