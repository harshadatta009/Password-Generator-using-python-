import random as rd
import string as st

#input the length of password
length= int(input("Enter the length of password: "))

# define data
lower = st.ascii_lowercase
upper = st.ascii_uppercase
numbers = st.digits
symbols = st.punctuation

# combine the data 
all = lower + upper + numbers + symbols

#use randome 
tmp = rd.sample(all,length)

#create a password 
password ="".join(tmp)

#print the password
print(password)
