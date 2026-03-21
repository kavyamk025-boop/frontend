# r=5
# k=0
# for i in range(1,r+1):
#     if i%2==0:
#         k=0
#     else:
#         k=1    
#     for j in range(1,i+1):
#         print(k%2,end=" ")
#         k+=1    
#     print()  
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@")      

# r=5
# k=0
# for i in range(1,r+1):
#     if i%2==0:
#         k=1
#     else:
#         k=0
#     for j in range(1,i+1):
#         print(k%2,end=" ")
#         k+=1    
#     print()        

# r=5
# k=0
# for i in range(1,r+1):
#     if i==1 or i==4 or i==5:
#         k=1
#     else:
#         k=0
#     for j in range(1,i+1):
#         print(k%2,end=" ")
#         k+=1    
#     print()     

# for i in range(1,r+1):
#     k=i-1
#     for j in range(1,i+1):
#         print(k%2,end=" ")
#         k+=1
#     print()              


r=5
k=1
for i in range(1,r+1):
    for j in range(1,i+1):
      if k%2==0:
        print(chr(k+96),end=" ")
      else:
         print(chr(k+64),end=" ")
      k+=1
    print()     