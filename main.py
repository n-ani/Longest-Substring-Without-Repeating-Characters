'''Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring without repeating characters.'''

#store the string value.
sub=str(input("Enter your string value: "))
#take an empty string variable for store the non repeating characters.
sub1=''
#for loop to execution
for i in sub:
  #check if element from sub is already appear in sub1 or not.
  if i not in sub1:
    #store the character in the sub1.
    sub1=sub1+i
  
print("\nThe answer is {}, with the length of {}".format(sub1,len(sub1)))
