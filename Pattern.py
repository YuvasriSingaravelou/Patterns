###problem 1
##n=6
##for i in range(n):
##   print("*" * n)

    
##Problem 2    
for i in range(1,6):
   for j in range(1,7):
       if j%2!=0:
           print((j//2+1),end=" ")
       else:
           print(i,end=" ")
   print()
    
###Problem 3
##for i in range(1,6):
##   for j in range(1,4):
##       print(i,j,end=" ")
##   print()

###Problem 4

##for i in range(1,6):
## for j in range(0,5):
##     print(i+j*5,end=" ")
## print()

###Problem 5
##for i in range(1,6):
## for j in range(0,5):
##   if j==3:
##     print(((22-i)-1),end=" ")
##   elif j%2!=0:
##     print(((12-i)-1),end=" ")
##   else:
##     print(i+j*5,end=" ")
## print()

#Problem 6
##for i in range(1,6):
## for j in range(1,i+1):
##   print(j,end=" ")
## print()

###Problem 7
##
##a=input("Enter a String:")
##for i in a:
##if " "==i:
##   print(end="")
## else:
##   print(i,end=" ")
##    
##
###problem 20
##for i in range(5):
##    for j in range(5):
##        if i%2==0:
##            print((j+1)%2,end=" ")
##        else:
##            print(0,end=" ")
##    print()
##
###problem 19
##for i in range(5):
## for j in range(5):
##   if i%2==0:
##     print((j+1)%2,end=" ")
##   else:
##     print(1,end=" ")
## print()
##
###Problem 18
##for i in range(1,6):
##    for j in range(0,5):
##        if (i+j)%2==0:
##            print(0,end=" ")
##        else:
##            print(1,end=" ")
##    print()
##


##Problem 1
##n = 5
##for i in range(n):
##   for j in range(n):
##      if i == 0 or i == n - 1 or j == 0 or j == n - 1:
##         print("*", end=" ")
##      else:
##            print(" ", end=" ")
##   print()
##

##Problem 2
##n = 5 
##for i in range(n):
##   for j in range(n):
##      if i == 0 or i == n - 1 or j == 0 or j == n - 1:
##         print("*", end=" ")
##      else:
##            print(" ", end=" ")
##   print()


##n = 5 
##for i in range(n):
##   for j in range(n):
##      if i == 0 or i == n - 1 or j == 0 or j == n - 1:
##         print("*", end=" ")
##      else:
##            print(" ", end=" ")
##
##print()


##n=7
##for i in range(n):
##   for j in range(n):
##      if i==3:
##         print("*",end=" ")
##      elif i==0 and j==3:
##         print("*",end=" ")
##      elif i==1 and j==4:
##         print("*",end=" ")
##      elif i==2 and j==5:
##         print("*",end=" ")
##      elif i==4 and j==5:
##         print("*",end=" ")
##      elif i==5 and j==4:
##         print("*",end=" ")
##      elif i==6 and j==3:
##         print("*",end=" ")
##      else:
##         print(" ",end=" ")
##   print()
      
         
         

##n = 5 
##for i in range(n):
##   for j in range(n):
##      if i == 0 or i == n-1 or j == 0 :
##         print("*", end=" ")
##      else:
##            print(" ", end=" ")
##
##   print()
##
##
##n = 9
##for i in range(n):
##   for j in range(n):
##      if i == 0 or i == n - 1 or j == 0 or j == n - 1:
##         print("*", end=" ")
##      elif i==1 and j==2 or i==1 and j==6 or i==7 and j==2 or i==7 and j==6 or i==2 and j==1 or i==2 and j==7 or i==6 and j==1 or i==6 and j==7:
##          print(" ",end=" ")
##      elif i==2 or j==2 or j==8 or i==6 or j==2 or j==6 or  i==4 and j==4:
##          print("*",end=" ")
##      else:
##          print(" ",end=" ")
##      
##   print()


n =7
for i in range(n):
   for j in range(n):
       if i==1 and j==0 or i==1 and j==6 or i==2 and j==0 or i==2 and j==1 or i==2 and j==5 or i==2 and j==6 or i==5 and j==6 or i==4 and j==0 or i==4 and j==1 and i==3 or j==1 and i==3 or j==2 and i==3 or j==4 and i==3 or j==5 and i==3 or j==6 and i==3 or j==0:
          print(" ",end=" ")
       elif i==3 and j==3 or i==0 and j==5:
          print("*",end=" ")
         
       else:
        print("*",end=" ")
      
    
    
   print()


##def myfunc(a):
##   print(a)
##   map(myfunc,l)
## 
##    






