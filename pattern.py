n = 5

# for i in range(n):
#     print("*" * (n-i))

# n = int(input())

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n,0,-1):
#     print(i)

#Square patterns

#nxn

n=4

# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#Right angled triangle

# for i in range(1,n+1): #raw
#     for j in range(i): #column
#         print("*",end=" ")
#     print()

'''  *
    * *
   * * *
  * * * *'''

# for i in range(1,n+1): # raw
#     for j in range(n-i): #mange space
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ") # column
#     print()


# * * * * 
#  * * * * 
#   * * *  
#    * *   
#     *    

for i in range(n,0,-1): # raw
    for j in range(n-i): #mange space
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ") # column
    print()