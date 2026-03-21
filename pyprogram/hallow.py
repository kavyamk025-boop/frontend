# r=5
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         if i==1 or i==r or i==j or i+j==r+1 or j==1 or j==r:
#            print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    
# * * * * * 
# * *   * * 
# *   *   *
# * *   * *
# * * * * *           
    
# r=13
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         if i==1 or (r+1)//2==i or(r+1)//2==j or i==r or i==j or i+j==r+1 or j==1 or j==r:
#            print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()     
# * * * * * * * * * * * * *
# * *         *         * *
# *   *       *       *   *
# *     *     *     *     *
# *       *   *   *       *
# *         * * *         *
# * * * * * * * * * * * * *
# *         * * *         *
# *       *   *   *       *
# *     *     *     *     *
# *   *       *       *   *
# * *         *         * *
# * * * * * * * * * * * * *          



# r=9
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         if i==1 or (r+1)//2==i or(r+1)//2==j or i==r or i==j or i+j==r+1 or j==1 or j==r:
#            print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()   
# 1 2 3 4 5 6 7 8 9
# 1 2     5     8 9
# 1   3   5   7   9
# 1     4 5 6     9
# 1 2 3 4 5 6 7 8 9
# 1     4 5 6     9
# 1   3   5   7   9
# 1 2     5     8 9
# 1 2 3 4 5 6 7 8 9



# r=5
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         if i==1 or j==r or i==j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")    
#     print()        
# 1 2 3 4 5 
#   2     5 
#     3   5
#       4 5
#         5



# r=5
# for i in range(0,r+1):
#     for j in range(0,r+2):
#         if (i==1 and j%3==0) or (i-2==j) or(i+j==8) or (i==0 and j%3!=0) :
#             print("*",end=" ")
#         elif(i==2 and j==2) or (i==2 and j==3) or (i==2 and j==4):
#             print("@",end=" ")    
#         else:
#             print(" ",end=" ")    
#     print()        
# for i in range(4,-1,-1):
#     for j in range(0,r+2):
#         if (i==1 and j%3==0) or (i-2==j) or(i+j==8) or (i==0 and j%3!=0) :
#             print("*",end=" ")
#         elif(i==2 and j==2) or (i==2 and j==3) or (i==2 and j==4):
#             print("@",end=" ")    
#         else:
#             print(" ",end=" ")    
#     print() 
#   * *   * *   
# *     *     * 
# *   @ @ @   *
#   *       *
#     *   *
#       *
#     *   *
#   *       *
# *   @ @ @   *
# *     *     *
#   * *   * *
for i in range(1,5+1):
    for j in range(1,3+1):
        if i==1 or j==3 or i==5 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print(" ",end=" ")
    
    for j in range(1,3+1):
        if (j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")            

    for j in range(1,3+1):
        if i%2==1 or (j==3 and i<=3) or (j==1 and i>=3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    
    for j in range(1,3+1):
        if i%2==1 or j==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    
    for j in range(1,3+1):
        if   j==3 or (i==1 and j==1) or (i==2 and j==1 ) or(i==2 and j==3 ) or(i==3 and j==1)or(i==3 and j==2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    
    for j in range(1,3+1):
        if    i%2==1 or (i==2 and j==1) or  (i==4 and j==3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    for j in range(1,3+1):
        if    i%2==1 or(i==4 and j==1) or (i==2 and j==1) or  (i==4 and j==3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")

    for j in range(1,3+1):
        if    i==1 or j==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    for j in range(1,3+1):
        if i==1 or j==3 or i==5 or j==1 or(i==3 and j==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print(" ",end=" ")    

    for j in range(1,3+1):
        if    i%2==1 or (i==2 and j==1) or  (i==4 and j==3) or(i==2 and j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")  


    for j in range(1,3+1):
        if (j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")            
    for j in range(1,3+1):
        if i==1 or j==3 or i==5 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print(" ",end=" ")
    
    print()            

print("__________________________________________________________________________________________________________-")    
for i in range(1,6):
    for j in range(1,4):
        if j==1  or (i==2 and j==2) or(i==4 and j==2) or(i==1 and j==3) or(i==5 and j==3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    for j in range(1,4):
        if i==1 or i==3 or j==1 or j==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")  

    for j in range(1,4):
        if (j==1 and i<=3) or(j==3 and i<=3) or (i==5 and j==2) or(i==4 and j==1) or(i==4 and j==3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")  
          
    for j in range(1,4):
        if (j==1 and i<=3) or(j==3 and i<=3) or (i==5 and j==2) or(i==4 and j==2)  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")      


    for j in range(1,4):
        if i==1 or i==3 or j==1 or j==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")  

    print()            
