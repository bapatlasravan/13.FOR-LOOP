"""
for i in range(6): #output will be in vertical 0 1 2 3 4 5 
    print(i)
"""

""""
for i in range(1,50): #output will be in vertical from 1 to 49
    print(i)
"""

"""
for i in range(1,10,2): #output will be in vertical from 1 3 5 7 9
    print(i)
"""
# n no of odd numbers in vertical
"""
for i in range(1,int(input()),2): #H ere we are printing n no of odd numbers in vertical
    print(i)
"""
# n no of odd numbers in horizantal
"""
for i in range(1,int(input()),2): #Here we are printing n no of odd numbers in vertical
    print(i,end=" ")
"""
# printing list using range
"""
n=[0,1,2,3,4,"5"]
for i in n:
    print(i) #if we print i output comes vertically as 0 1 2 3 4 5
"""
"""
n=[0,1,2,3,4,"5",6]
for i in n:
    print(n) # if we print n the output it will repeat  [0,1,2,3,4,"5",6] as seven times(n+1) vertically
"""
# printing set using range
"""
n={"0",1,"2",3,4,"5",6,7,8}
for i in n:
    print(i) #here outcome is in verticall and it is in unordered 
"""
# break
"""
n=["a","b","c","d","e","f","g","h"]
for i in n:
    print(i)
    if i=="d":
        break  #here after d it will not print
"""
# d is also not print by using break
"""
n=["a","b","c","d","e","f","g","h"]
for i in n:
    if i=="d":
        break
    print(i)
"""
# continue in for loop
"""
n=["a","b","c","d","e","f","g","h"]
for i in n:
    if i=="d":
        continue       #Here all stings inside the list printed vertically except "d" 
    print(i)
"""