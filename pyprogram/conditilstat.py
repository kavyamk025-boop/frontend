# # per=90
# # # if per>=85:
# # #     print("distinction")
# # # elif per>=60:
# # #     print("first class")
# # # else:
# # #     print("sec")        
# # #     per=77
# # if per>=85:
# #         print("dist")
# # if per>=70:
# #         print("first")
# # if per>=40:
# #         print("second")
# # if per>=35:
# #         print("just pass")
# # if per<35:
# #         print("better luck next time")    
# day=1
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday") 
#     case 3:
#         print("wednesday") 
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")

# l=["dsd","ds","hgh","hgj","gfdg"]
# s=["fg","g","dsd","fds"]
# for i in l:
#     print("hi",i)
# for i in range(5,5,-10):
#     print("huyyyyyyy....")  




# row=int(input("enter rows"))
# for i in range(row):
#   for j in range(row):
#         print(i+1,end="-")  
#   print()      

# row=4
# for i in range(1,row+1):
#     for j in range(1,row+1):
#         print(" ",end="*")
#     print()
# rows=5   
# # for i in range(1,rows+1):
# #     for j in range(1,i-1):
# #         print("*",end=" ")
# #     print()
# for i in range(1,rows+1):
#     for j in range(rows,rows-i,-1):
#        print(j,end=" ")
#     print()

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#        print(j,end=" ")
#     print()

# for i in range(1,rows+1):
#     for j in range(5,rows-i,-1):
#        print(j,end=" ")
#     print()

# for i in range(1,rows+1):
#     for j in range(rows+1-i,rows+1):
#        print(j,end=" ")
#     print()

# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#        print(j,end=" ")
#     print()
# r=5
# for i in range(1,r+1):
#     for j in range(1,r+1-i):
#        print("*",end=" ")
# #     print()
# r=5
# for i in range(1,r+1):
#     for j in range(i,r):
#         print(" ",end=" ")
#     for j in range(r-i+1,r+1):
#         print("*",end=" ")   
#     print()       
    
r=5
# for i in range(1,r+1):
#     for j in range(i,r):
#         print(" ",end=" ")
#     for j in range(r-i+1,r+1):
#         print("*",end=" ")
#     for j in range(r+i,r+r+1):
#         print("+",end=" ")
        
        
#     print()       

# for i in range(1,r+1):
    
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("+",end=" ")    
#     print()


# r=5
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for k in range(i,r+1):
#         print("+",end=" ")   
#     print()

# r=5
# for i in range(1,r+1):
#     for k in range(1,r-i+1):
#         print(" ",end=" ") 
#     for j in range(r+i,r+1,-1):
#         print("*",end=" ")
#     for j in range(r-i+1,r+1):
#         print("*",end=" ")      
#     print()  
#     #   * 
#       * * *   
#     * * * * * 
#   * * * * * * *
# * * * * * * * * *  

# r=5
# for i in range(1,r+1):
  
#     for j in range(1,r-i+1):
#         print(" ",end=" ")       
#     for k in range(1,i+1):
#         print("*",end=" ") 
    
   
#     print()  

# r=5
# for i in range(1,r+1):
#     for j in range(i,0,-1):
#         print(chr(j+64),end=" ")
#     print()   
# A 
# B A 
# C B A
# D C B A
# E D C B A     

# r=5
# for i in range(1,r+1):
#     for j in range(r,r-i,-1):
#         print(chr(64+j),end=" ")
#     print()   
# E 
# E D 
# E D C
# E D C B
# E D C B A
# r=5
# for i in range(1,r+1):
#     for j in range(r-i+1,r+1):
#         print(chr(64+j),end=" ")
#     print()    
# E 
# D E 
# C D E
# B C D E
# A B C D E    
# for i in range(r):
#     for j in range(r):
#       if i==0 or i==r-1 or j==0 or j==r-1:
#           print("*",end=" ")
#       else:    
# #         print(" ",end=" ")    
# #     print()    
# # * * * * * 
# # *       * 
# # *       *
# # *       *
# # * * * * *    
# # r=5
# # for i in range(1,r+1):
# #     print(" "*(r-i),end=" ")
# #     print("*"*i)


# def strStr(haystack, needle):
#         i=0
#         j=0
#         while i<len(haystack):
#             while j<len(needle):
#                 if haystack[i]==needle[j]:
#                     i+=1
#                     j+=1
#                     if j==len(needle):
#                       return i-len(needle) 
#                 else:
#                     j+=1
#         return -1  
# print(strStr("leetcode","code"))

# class Solution(object):
#     def strStr(self, haystack, needle):
#         i=0
#         j=0
#         while i<len(haystack):
#             while j<len(needle):
#                 if haystack[i]==needle[j]:
#                     i+=1
#                     j+=1
#                     if j==len(needle):
#                       return i-len(needle) 
#                 else:
#                     j+=1
#         return -1
# r=5
# for i in range(1,r+1):
#     print("+"*i,end=" ")
#     print("*"*(r-i+1))


# r=5
# for i in range(1,r+1):
#     for j in range(r-i+1,r+1):
#         print(j,end=" ")
#     print()   
# r=10
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")    
#     for j in range(1,i):
#         print("*",end=" ")
#     print()
#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * * 
# r=5
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(r-i+1,r+1):
#         print(j,end=" ")    
#     for j in range(r-1,r-i,-1):
#         print(j,end=" ")
#     print()    
# for i in range(r-1,0,-1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(r-i+1,r+1):
#         print(j,end=" ")    
#     for j in range(r-1,r-i,-1):
#         print(j,end=" ")
#     print()  
#         5 
#       4 5 4 
#     3 4 5 4 3
#   2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2 1
#   2 3 4 5 4 3 2
#     3 4 5 4 3
#       4 5 4
#         5            
#         5
#       4 5 4
#     3 4 5 4 3
#   2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2 1
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")    
#     for j in range(2,i+1):
#         print(j,end=" ")
    # print()     
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# # 5 4 3 2 1 2 3 4 5             
# r=5
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(r,r-i,-1):
#         print(j,end=" ")
#     for j in range(r+2-i,r+1):
#         print(j,end=" ")
#     print() 
# #       5
#       5 4 5
#     5 4 3 4 5
#   5 4 3 2 3 4 5
# 5 4 3 2 1 2 3 4 5           

# r=5
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print() 
#         1 
#       1 2 1 
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1 
# r=5  
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for j in range(i,r+1):
#         print(r+1-i,end=" ")   
#     for j in range(1,r-i+1):
#         print(r+1-i,end=" ")     
#     print()                    
# r=5
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(r,r-i,-1):
#         print(j,end=" ")
#     for j in range(r+2-i,r+1):
#         print(j,end=" ")    
#     print()    
# for i in range(r-1,0,-1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(r,r-i,-1):
#         print(j,end=" ")
#     for j in range(r+2-i,r+1):
#         print(j,end=" ")    
#     print()     
#         5 
#       5 4 5 
#     5 4 3 4 5
#   5 4 3 2 3 4 5
# 5 4 3 2 1 2 3 4 5
#   5 4 3 2 3 4 5
#     5 4 3 4 5
#       5 4 5
#         5     
# r=5
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")    
#     print()    
# for i in range(r-1,0,-1):
#     for j in range(1,r-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")    
#     print()  
# r=5
# for i in range(1,r+1):
#     for j in range(1,i+1):
#       print("*",end=" ")
#     print()

# r=5
# for i in range(1,r+1):
#     k=1
#     for j in range(1,i+1):
#       print(k,end=" ")
#       k+=1
#     print()
# r=5
# for i in range(1,r+1):
#     k=5
#     for j in range(1,i+1):
#       print(k,end=" ")
#       k-=1
#     print()    
# r=5
# k=1
# for i in range(1,r+1):
#     for j in range(1,i+1):
#       print(k,end=" ")
#       k+=1
#     print()    
# r=5
# for i in range(1,r+1):
#     k=i
#     for j in range(1,i+1):
#       print(k,end=" ")
#       k-=1
#     print()        
# r=5
# for i in range(1,r+1):
#     k=5
#     for j in range(1,i+1):
#       print(k,end=" ")
#       k+=1
#     print()    

# r=5
# for i in range(1,r+1):
#     k=r-i+1
#     for j in range(1,i+1):
#       print(k,end=" ")
#       k+=1
#     print()        
# r=5
# for i in range(1,r+1):
#     k=i
#     for j in range(1,i+1):
#       print(k,end=" ")
#       k+=1
#     print()    
# r=5
# k=65
# for i in range(1,r+1):
#     for j in range(1,i+1):
#       print(chr(k),end=" ")
#       k+=1
#     print()  
# r=5
# k=0
# for i in range(1,r+1):
#     for j in range(1,i+1):
#      if k>4:
#         k=0
#      print(k,end=" ")
#      k+=1
#     print()  
# k=0
# for i in range(1,r+1):
#     for j in range(1,i+1):
#      print(k%5,end=" ")
#      k+=1
#     print()
# 0
# 1 2
# 3 4 0
# 1 2 3 4
# 0 1 2 3 4

for i in range(1,r+1):
    for j in range(1,r-i+1):
        print(" ",end=" ") 
    for j in range(1,i+1):
        print(i,end=" ")
        
    print()    