import numpy as np

def m_sum(a):
    sum=np.sum(a)
    print("Sum=",sum)
    print()

def m_mean(a):
    mean=np.mean(a)
    print("Mean=",mean)
    print()

def m_median(a):
    median=np.median(a)
    print("Median=",median)
    print()

def min_n_max(a):
        min=np.min(a)
        min_idx=np.argmin(a)
        max=np.max(a)
        max_idx=np.argmax(a)  
        print("Minimum and index: ",min,min_idx)           
        print("Maximum and index: ",max,max_idx)  
        print()   

def m_var(a):
    variance=np.var(a)
    print("Variance=",variance)
    print()

def m_std(a):
    stnd=np.std(a)
    print("Standard deviation=",stnd)
    print()

def m_reshape(a):
  try:
        print("Original shape:", a.shape)
        new_shape = tuple(map(int, input("Enter new shape (e.g., 2 3): ").split()))

        # Check if total number of elements is same
        if np.prod(new_shape) != a.size:
            print(f"Error: Cannot reshape array of size {a.size} into shape {new_shape}")
        else:
            a = a.reshape(new_shape)
            print("Reshaped successfully. New shape:", a.shape)
            print(a)
  except ValueError:
        print("Invalid input. Please enter valid integers for shape.")
  except Exception as e:
        print("Unexpected error:", e)
  return a
  print()   

def percen(a):
    p=float(input("Enter the percentile number(1-100):"))
    per=np.percentile(a,p)
    print("Percentile=",per)
    print()  
def m_transpose(a):
    t=a.T
    print("Transpose= ",t)
    print()
def m_flatten(a):
    print("Flattened matrix: ",a.flatten())
    print()
def m_exdim(a):
    print("Dimension expanded matrix: ",np.expand_dims(a))   
    print() 
def m_sort(a):
    print("Sorted matrix: ",np.sort(a))
    print()   
def m_det(a):
    print("Determinant= ",np.linalg.det(a))
    print()     
#heading
print("NUMBER CHRUNCHER TOOLKIT")
print("------------------------")

print("Array information: ")
print()
dim=int(input("Enter the dimension(1-3):"))
print()
if(dim==1):
    row=int(input("Enter the number of elements: "))
    print()
    a=[] 
    for i in range(1):
        rows=list(map(float,input(f"Enter the {row} row elements: ").split()))
        while len(rows)!=row:
            print(f"Invalid input. Please enter {row} row elements: ")
            rows=list(map(float,input(f"Enter the {row} row elements: ").split()))
        a.append(rows)
    print()    
    a=np.array(a) 
    a=np.squeeze(a)                                                      
    print("Entered matrix: ")
    print(a)        
      
elif(dim==2):
   row=int(input("Enter the number of rows: "))
   col=int(input("Enter the number of cols: "))
   a=[]                                                                     #a_raw[]
   for i in range(row):                                                     #for i in range(row):   
      rows=list(map(float,input(f"Col{i+1}: ").split()))                        #rows=input(f"row{i+1}:").split()
      while len(rows) != col:                                                  #a_raw.append(rows)
         print("Invalid input. Please enter exactly", col, "values.")         #while len(rows)!=col:
         rows = list(map(float, input(f"Col {i+1}: ").split()))               #print("Invalid input. Please enter exactly", col, "values.")  
                                                                             #rows=input(f"row{i+1}:").split()
      a.append(rows)                                                           #a_raw.append(rows)
   print()                                                                   # a = np.array(a_raw, dtype=int)
   a=np.array(a)                                                          
   print("Entered matrix:")
   print(a) 

elif(dim==3):
   a=[]
   block=int(input("Enter the number of blocks: "))    
   row=int(input("Enter the number of rows in a block: "))
   col=int(input("Enter the number of cols in a block: "))
   for i in range(block):
       for j in range(row):
               rows=list(map(float,input(f"Enter the {i+1} block's {j+1} row:").split()))  
               while len(rows)!=col:
                   print("Invalid input. Please enter exactly", col, "values.")   
                   rows=list(map(float,input(f"Enter the {i+1} block's {j+1} row:").split()))
               
               a.append(rows)
   a=np.array(a).reshape(block,row,col)
   print(a)                                                               


# choices  
print()
while True:
    print("1.Sum of the matrix elements.")
    print("2.Mean of matrix elements.")
    print("3.Meadian of matrix.")
    print("4.Minimum and maximum.")
    print("5.Variance.")
    print("6.Standard deviation.")
    print("7.Reshape matrix.")
    print("8.Percentile")
    print("9.Transpose the matrix.")
    print("10.Flatten the matrix.")
    print("11.Expand the dimension of the matrix.")
    print("12.Sort the matrix.")
    print("13.Calculate determinant.")
    print("14.Perform mathemetical operations with another matrix.")
    print("15.Other operations.")
    print("16.Other attributes.")
    print("17.Exit")
    choice=int(input("Enter the option: "))
    print()
    #operations
    if(choice==1):
       m_sum(a)
    elif(choice==2):
       m_mean(a)
    elif(choice==3):
        m_median(a)
    elif(choice==4):
        min_n_max(a)
    elif(choice==5):
        m_var(a)
    elif(choice==6):
        m_std(a)
    elif(choice==7):
        m_reshape(a)
    elif(choice==8):
        percen(a)          
    elif(choice==9):
        m_transpose(a)
    elif(choice==10):
        m_flatten(a)   
    elif(choice==11):
        m_exdim(a)     
    elif(choice==12):
        m_sort(a)
    elif(choice==13):
        if row!=col or dim!=2:
            print("Calculation of deteminant is not possible for shape ",a.shape)
        else:
            m_det(a)   
    elif(choice==14):
     try:  
        dim_2=int(input("Enter the dimension of second matrix: "))
        print()
        if(dim_2==1):
          row2=int(input("Enter the number of elements: "))
          print()
          b=np.full((row2),None)
          proceed=0
          try:
                np.broadcast_shapes(a.shape, b.shape)
                proceed=1
          except ValueError:
                print(" Matrices are not compatible for mathematical operations.")
                proceed=0 
          if(proceed==1):
            a2=[]
            for i in range(1):

              row2s=list(map(float,input(f"Enter the {row2} row elements: ").split()))
              while len(row2s)!=row2:
                   print(f"Invalid input. Please enter {row2} row elements: ")
                   row2s=list(map(float,input(f"Enter the {row2} row elements: ").split()))
                
              a2.append(row2s)
            print()    
            a2=np.array(a2) 
            a2=np.squeeze(a2)                                                      
            print("Entered matrix: ")
            print(a2)        
      
        elif(dim_2==2):
            row2=int(input("Enter the number of rows: "))
            col2=int(input("Enter the number of cols: "))
            b=np.full((row2,col2),None)
            proceed=0
            try:
                np.broadcast_shapes(a.shape, b.shape)
                proceed=1
            except ValueError:
                print(" Matrices are not compatible for mathematical operations.")
                proceed=0 
            if(proceed==1):  
             a2=[]                                                 
             for i in range(row2):                                                    
               rows2s=list(map(float,input(f"Col{i+1}: ").split()))

               while (len(rows2s) != col2):       
                                              
                       print("Invalid input. Please enter exactly", col2, "values.")         
                       rows2s = list(map(float, input(f"Col {i+1}: ").split()))               
                                                                         
               a2.append(rows2s)                                                          
             print()                                                                   
             a2=np.array(a2)                                                          
             print("Entered matrix:")
             print(a2) 

        elif(dim_2==3):
        
           block2=int(input("Enter the number of blocks: "))    
           row2=int(input("Enter the number of rows in a block: "))
           col2=int(input("Enter the number of cols in a block: "))
           b=np.full((block2,row2,col2),None)
           proceed=0
           try:
                np.broadcast_shapes(a.shape, b.shape)
                proceed=1
           except ValueError:
                print(" Matrices are not compatible for mathematical operations.")
                proceed=0 
           if(proceed==1):
            a2=[]
            for i in range(block2):
              for j in range(row2):
                 rows2s=list(map(float,input(f"Enter the {i+1} block's {j+1} row:").split()))  
                 while (len(rows2s)!=col2) :
                 
                     print("Invalid input. Please enter exactly", col2, "values.")   
                     rows2s=list(map(float,input(f"Enter th1e {i+1} block's {j+1} row:").split()))

                 a2.append(rows2s)
            a2=np.array(a2).reshape(block2,row2,col2)
            print(a2) 
  

     except ValueError:
         print("Unexpected error occured.")
     if(proceed==1):
         print("Operations:") 
         print()
         print("1.Addition.")  
         print("2.Subtraction.") 
         print("3.Multiplication(*).")
         print("4.Division.")
         print("5.Power.")
         print("6.Modulo.")
         print("7.Floor division.")
         print("8.Dot product(@).")
         print("9.Concatenate.")
         print("10.Stack.")
         print("11.Hstack.")
         print("12.Vstack.")
         print("13.Exit")
         print()
         
         while True:
          ch=int(input("Choose the operation."))
          if ch>13 :
              print("Invalid choice, please enter again.")
          else:
              break   
               
         print()
         if(ch==1):
             print("Matrix after addition: ",a+a2)
             print()
         elif(ch==2):
             print("Matrix after subtraction: ",a-a2)    
             print()
         elif(ch==3):
             print("Matrix after multiplication: ",a*a2)  
             print()  
         elif(ch==4):
             print("Matrix after division: ",a/a2)
             print()
         elif(ch==5):
             print("Matrix after power operation: ",a**a2)  
             print() 
         elif(ch==6):
             print("Matrix after modulo operation: ",a%a2)  
             print()
         elif(ch==7):
             print("Matrix after floor divisiom: ",a//a2)  
             print()
         elif(ch==8):
             print("Dot product: ", np.dot(a,a2))
         elif(ch==9):
          if dim==dim_2:
            if dim==1:
              print("After concatenation: ",np.concatenate((a,a2)))
            elif dim==2:
              while True:  
                axiss=int(input("Enter the axis(0-1)")) 
                if(axiss>2):
                    print("Invalid axis,please enter valid one.")
                else:
                    break              
              print(f"Concatenation along axis {axiss}: ", np.concatenate((a,a2),axis=axiss))
            elif dim==3:
              while True:  
                axiss=int(input("Enter the axis(0-1)")) 
                if(axiss>3):
                    print("Invalid axis,please enter valid one.")
                else:
                    break              
              print(f"Concatenation along axis {axiss}: ", np.concatenate((a,a2),axis=axiss)) 
          else:
               print("Incompatible dimension.")   
         elif(ch==10):
          if dim==dim_2:
            if dim==1:
              print("After concatenation: ",np.stack((a,a2)))
            elif dim==2:
              while True:  
                axiss=int(input("Enter the axis(0-1)")) 
                if(axiss>1):
                    print("Invalid axis,please enter valid one.")
                else:
                    break              
              print(f"Concatenation along axis {axiss}: ", np.stack((a,a2),axis=axiss))
            elif dim==3:
              while True:  
                axiss=int(input("Enter the axis(0-2)")) 
                if(axiss>2):
                    print("Invalid axis,please enter valid one.")
                else:
                    break              
              print(f"Concatenation along axis {axiss}: ", np.stack((a,a2),axis=axiss)) 
          else:
               print("Incompatible dimension.")  
         elif(ch==11):
             try:
               if a.shape[0] == a2.shape[0]:  # Check rows match
                 print("After hstack:\n", np.hstack((a, a2)))
               else:
                 print("Cannot hstack: row count does not match.")    
             except Exception as e:
                 print("Error during hstack:", e)
   
         elif(ch==12):
             try:
                if a.shape[1] == a2.shape[1]:  # Check columns match
                   print("After vstack:\n", np.vstack((a, a2)))
                else:
                   print("Cannot vstack: column count does not match.")
             except Exception as e:
                   print("Error during vstack:", e)
                                      
         elif(ch==13):
             print("Returning to main menu.") 
             print()   

    elif(choice==15):
        
         print("Operations:") 
         print()
         print("1.Inverse of the matrix.")  
         print("2.Round up matrix.") 
         print("3.Round up to higher value.")
         print("4.Round upto lower value.")
         print("5.Split.")
         print("6.Hsplit.")
         print("7.Vsplit.")
         print("8.Shuffle.")
         print("9.Random choice.")
         print("10.Exit")
         print()
        
         while True:
          ch=int(input("Choose the operation."))
          if ch>10 :
              print("Invalid choice, please enter again.")
          else:
              break        
         print()
         if(ch==1):
           try:
              print("Inverse: ", np.linalg.inv(a))
           except np.linalg.LinAlgError:
              print("Matrix is not invertible.")
           print()
         elif(ch==2):
             print("Round up matrix: ",np.round(a))    
             print()
         elif(ch==3):
             print("Matrix after rounding up to higher value: ",np.ceil(a))  
             print()  
         elif(ch==4):
             print("Matrix after rounding up to lower value: ",np.floor(a))
             print()
         elif(ch==5):
             parts=int(input(f"Enter the parts(1-{a.size}):"))
             print("Matrix after splitting: ",np.split(a,parts))  
             print() 
         elif(ch==6):
            if dim==1 :
             parts=int(input(f"Enter the parts(1-{a.size}):"))
             print("Matrix after hsplit: ",np.hsplit(a,parts))  
            elif dim==2: 
             parts=int(input(f"Enter the parts(1-{a[0].size}):"))
             print("Matrix after hsplit: ",np.hsplit(a,parts))
            elif dim==3:
             parts=int(input(f"Enter the parts(1-{a[1].size}):"))
             print("Matrix after hsplit: ",np.hsplit(a,parts))
            print()
         elif(ch==7):
            if dim==1 :
             parts=int(input(f"Enter the parts(1-{a.size}):"))
             print("Matrix after vsplit: ",np.vsplit(a,parts))  
            elif dim==2: 
             parts=int(input(f"Enter the parts(1-{a[1].size}):"))
             print("Matrix after vsplit: ",np.vsplit(a,parts))
            elif dim==3:
             parts=int(input(f"Enter the parts(1-{a[2].size}):"))
             print("Matrix after vsplit: ",np.vsplit(a,parts))
            print()
         elif(ch==8):
             print("Matrix after shuffling: ",np.random.shuffle(a)) 
         elif(ch==9):
             if dim==1:
                 print("Random choice: ",np.random.choice(a)) 
             else:
                 af=np.flatten(a)
                 print("Random choice: ",np.random.choice(af))    
         elif(ch==10):   
             print("Returning to main menu.") 
             print()               

    elif(choice==16):
        print("Atrributes: ")
        print()
        print("1.Dimension of matrix.")
        print("2.Size of matrix.")
        print("3.Datatype of the matrix.")
        print("4.Shape of matrix.")
        print("5.Itemsize of matrix.")
        print("6.Exit")
        print()
        while True:
          ch=int(input("Choose the operation."))
          if ch>6 :
              print("Invalid choice, please enter again.")
          else:
              break   
               
        print()
        if(ch==1):
             print("Dimension of the matrix: ",a.ndim)
             print()
        elif(ch==2):
             print("Size of the matrix: ",a.size)    
             print()
        elif(ch==3):
             print("Datatype of the matrix: ",a.dtype)  
             print()  
        elif(ch==4):
             print("Shape of the matrix: ",a.shape)
             print()
        elif(ch==5):
             print("Itemsize of the matrix: ",a.itemsize)  
             print() 
        elif(ch==6):
             print("Exiting to main menu.")  
             print()
    elif(choice==17):   
     print("Exiting menu.")
     break
    ##FINALLY DONE 😊😊