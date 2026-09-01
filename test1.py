"""i=0  
while i<=:
    print(i) 
   i+=1 """
    
    
"""number=[1,2,3,4,5,6,7,8,9]
for num in number :
    print(num-1)"""




"""grades= [75,66,33,98,77,45,66]
new_grades =[]
for gre in grades:
    bouns = gre+5
    new_grades.append(bouns)

print("original grages" ,grades)
print("grade after bouns" ,new_grades)"""



#help("keywords ")الكلمات المحجوزه 









#lambda type punctin

#hello = lambda name,age: F"hello: {name} your age is: {age}"
#print (hello("ahmed",20))








#file handling

#"""import pandas as pd

# Main Current Working Directory


#df =pd.read_excel (r"C:\Users\phers\Desktop\shet1 ecxel.xlsx")


# le = open("D:\Python\Files\osama.txt")


#print(df)












#import pandas as pd
#myfi le = open (r"D:\python\files \fun.txt","w")

#myfile.write ("elzero web school\n" * 100) 







#print(round(159.599))
#print(list(range(0)))


"""while the_tries > 0:

  try:  # Try To Open The File

    print("Enter The File Name With Absolute Path To Open")

    print(f"You Have {the_tries} Tries Left")

    print(r"Example: D:\Python\Files\yourfile.extension")

    file_name_and_path = input("File Name => : ").strip()

    the_file = open(file_name_and_path, 'r')

    print(the_file.read())

    break

  except FileNotFoundError:

    print("File Not Found Please Be Sure The Name is Valid")

    the_tries -= 1

  except:

    print("Error Happen")

  finally:

    if the_file is not None:

      the_file.close()

      print("File Closed.")

else:

  print("All Tries Is Done")
"""
  













#print("hello data engineer world!")


"""
file_name = "info.txt"


with open(file_name, "w") as file:
    file.write("Ahmed\n")

with open(file_name, "r") as file:
    content = file.read()

with open(file_name, "a") as file:
    file.write("Age: 20\n")
"""











"""
def addittion (num1,num2):

    if type (num1) != int or  type (num2) != int:

        
      print("no int")


    else:

    
      print(num1+num2)

addittion(100,100) 
"""













"""
def cleanword(word):
    
    if len (word) == 1:
        
        return word 
    
    print (f"print start function{word}")

    if word[0] ==word[1]:
        
        print(f"print Before condition {word}")

        return cleanword(word[1:])

    print (f"print Before return{word}")

    return word[0] + cleanword(word[1:])

print (cleanword ("www0000rrrldd"))
"""










"""
# إنشاء ملف جديد وإضافة نص فيه
with open("data.txt", "r", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("هذا سطر جديد.")
"""



"""
# فتح الملف للقراءة
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()  # قراءة كل النص الموجود في الملف
    print( content)


# فتح الملف في وضع الإضافة (Append)
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nmy name is ahmed ")



    # إنشاء ملف جديد باسم file2.txt
with open("file2.txt", "w", encoding="utf-8") as file:
    file.write("my name is ahmed mohamed   iam from cairo")

print("my name is ahmed mohamed\niam from cairo") 
"""










"""
with open("file2.txt", "r", encoding="utf-8") as file2:
    for line in file2:
        print(line)
        if line.startswith("3"):
            break
"""      





"""
import os

path = r"c:\Python\Files"
os.makedirs(path, exist_ok=True)

with open(rf"{path}\ahmed.txt", "w") as myFile:
    myFile.write("Hello From Python File With Love")
"""











"""
myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open(r"c:\Python\Files\ahmed.txt", "w")
myFile.writelines(myList)
"""


#############################################################################################################
################################################################################################################
###############################################################################################################
###############################################################################################################
################################################################################################################
################################################################################################################
###############################################################################################################








# ----------------------------
# -- Numpy => Create Arrays --
# ----------------------------
"""
import numpy as np

# print(dir(np))

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" * 50)

# Type

print(type(my_list))
print(type(my_array))

print("#" * 50)

# Accessing Elements

print(my_list[0])
print(my_array[0])

print("#" * 50)

a = np.array(10)
b = np.array([10, 20])
c = np.array( [ [1, 2], [3, 4] ] )
d = np.array( [ [ [5, 6], [7, 9] ], [ [1, 3], [4, 8] ] ] )

print(d[1][1][-1])
print(d[1, 1, 1])
print(d[1, 1, -1])

print("#" * 50)

# Number Of Dimensions

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#" * 50)

# Custom Dimensions

my_custom_array = np.array([1, 2, 3], ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim)

print(my_custom_array[0, 0, 0])
"""


#################################################################################################################




# ---------------------------------------------
# -- Numpy => Compare Data Location And Type --
# ---------------------------------------------
"""
import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_list[0])
print(my_list[1])

print(my_array[0])
print(my_array[1])

print("#" * 50)

print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

print("#" * 50)

my_list_of_data = [1, 2, "A", "B", True, 10.50]
my_array_of_data = np.array([1, 2, "A", "B", True, 10.50])

print(my_list_of_data)
print(my_array_of_data)

print("#" * 50)

print(my_list_of_data[0])
print(my_array_of_data[0])

print(type(my_list_of_data[0]))
print(type(my_array_of_data[0]))

print("#" * 50)

my_list_of_data_two = [1, 2, "A", "B", True, 10.50]
my_array_of_data_two = np.array([1, 2, "A"])

print(my_list_of_data_two)
print(my_array_of_data_two)

print("#" * 50)

print(my_list_of_data_two[0])
print(my_array_of_data_two[0])

print(type(my_list_of_data_two[0]))
print(type(my_array_of_data_two[0]))
ملاحظات الدرس
"""


 #####################################################################################################################



 # -------------------------------------------------
# -- Numpy => Compare Performance And Memory Use --
# -------------------------------------------------
# - Performance
# - Memory Use
# -------------------------------------------------
"""
import numpy as np
import time
import sys

elements = 150000

my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"List Time: {time.time() - list_start}")

array_start = time.time()
array_result = my_array1 + my_array2
print(f"Array Time: {time.time() - array_start}")

# for n1, n2 in zip(my_list1, my_list2):

# 	print(n1 + n2)

print(list_result)
print(array_result)

my_array = np.arange(100)

print(my_array)
print(my_array.itemsize)
print(my_array.size)
print(f"All Bytes: {my_array.itemsize * my_array.size}")

print("#" * 50)

my_list = range(100)
print(sys.getsizeof(1))
print(len(my_list))
print(f"All Bytes: {sys.getsizeof(1) * len(my_list)}")
"""


######################################################################################################################




# ----------------------------
# -- Numpy => Array Slicing --
# ----------------------------
"""
import numpy as np

# Slicing => [Start:End:Steps] Not Including End

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim)
print(a[1])
print(a[1:4])
print(a[:4])
print(a[2:])

print("#" * 50)

b = np.array([["A", "B", "X"], ["C", "D", "Y"], ["E", "F", "Z"], ["M", "N", "O"]])

print(b.ndim)
print(b[1])

print("#" * 50)

print(b[2:, :2])
print(b[2:, :2:2])
ملاحظات الدرس
"""



#########################################################################################################################



# -------------------------------------------
# -- Numpy => Data Types And Control Array --
# -------------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
# -------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex-floating point
# 'm' timedelta
# 'M' datetime
# 'O' (Python) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
# ------------------------------------------------
"""
import numpy as np

# Show Array Data Type

my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.5, 20.15, 3.601])
my_array3 = np.array(["Osama_Elzero", "B", "Ahmed"])

print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)

print("#" * 50)

# Create Array With Specific Data Type

my_array4 = np.array([1, 2, 3], dtype=float) # float Or 'float' Or 'f'
my_array5 = np.array([1.5, 20.15, 3.601], dtype=int) # int Or 'int' Or 'i'
# my_array6 = np.array(["Osama_Elzero", "B", "Ahmed"], dtype=int) # Value Error

print(my_array4.dtype)
print(my_array5.dtype)
# print(my_array6.dtype)

print("#" * 50)

# Change Data Type Of Existing Array

my_array7 = np.array([0, 1, 2, 3, 0, 4])
print(my_array7.dtype)
print(my_array7)

print("#" * 50)

my_array7 = my_array7.astype('float')
print(my_array7.dtype)
print(my_array7)

print("#" * 50)

my_array7 = my_array7.astype('bool')
print(my_array7.dtype)
print(my_array7)

print("#" * 50)

# Test Capacity

my_array8 = np.array([100, 200, 300, 400], dtype='f')
print(my_array8.dtype)
print(my_array8[0].itemsize) # 4 Bytes

my_array8 = my_array8.astype('float') # Change To Float64
print(my_array8.dtype)
print(my_array8[0].itemsize) # 8 Bytes
"""



###############################################################################################################################



# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Dividation
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------------------------------------
"""
import numpy as np

# Arithmetic Operations

my_array1 = np.array([10, 20, 30])
my_array2 = np.array([5, 2, 4])

print(my_array1 + my_array2) # result [15, 22, 34]
print(my_array1 - my_array2) # result [5, 18, 26]
print(my_array1 * my_array2) # result [50, 40, 120]
print(my_array1 / my_array2) # result [2, 10, 7.5]

print('#' * 50)

my_array3 = np.array([[1, 4], [5, 9]])
my_array4 = np.array([[2, 7], [10, 5]])

print(my_array3 + my_array4) # result [ [3, 11], [15, 14] ]
print(my_array3 - my_array4) # result [ [-1, -3], [-5, 4] ]
print(my_array3 * my_array4) # result [ [2, 28], [50, 45] ]
print(my_array3 / my_array4) # result [ [0.5, 0.57142857], [0.5, 1.8] ]

print('#' * 50)

# Min, Max, Sum

my_array5 = np.array([10, 20, 30])
print(my_array5.min())
print(my_array5.max())
print(my_array5.sum())

print('#' * 50)

my_array6 = np.array([[6, 4], [3, 9]])
print(my_array6.min())
print(my_array6.max())
print(my_array6.sum())

print('#' * 50)

# Ravel

my_array7 = np.array([[6, 4], [3, 9]])
print(my_array7.ravel())

my_array8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(my_array8.ndim)
print(my_array8.ravel())
x = my_array8.ravel()
print(x.ndim)
ملاحظات الدرس
"""



##########################################################################################################3




# ------------------------------------
# -- Numpy => Array Shape & ReShape --
# ------------------------------------
# Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
# ----------------------------------------------
"""
import numpy as np

my_array1 = np.array([1, 2, 3, 4])
print(my_array1.ndim)
print(my_array1.shape)

print("#" * 50)

my_array2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(my_array2.ndim)
print(my_array2.shape)

print("#" * 50)

my_array3 = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])
print(my_array3.ndim)
print(my_array3.shape)

print("#" * 50)

my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_array4.ndim)
print(my_array4.shape)

reshaped_array4 = my_array4.reshape(3, 4)
print(reshaped_array4.ndim)
print(reshaped_array4.shape)
print(reshaped_array4)

print("#" * 50)

my_array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(my_array5.ndim)
print(my_array5.shape)

print("#" * 50)

# reshaped_array5 = my_array5.reshape(-1)
# reshaped_array5 = my_array5.reshape(4, 5)
reshaped_array5 = my_array5.reshape(2, 5, 2)
print(reshaped_array5.ndim)
print(reshaped_array5.shape)
print(reshaped_array5)
"""





#############################################################################################################
################################################################################################################
###############################################################################################################
###############################################################################################################
################################################################################################################
################################################################################################################
###############################################################################################################






import pandas as pd

students = ({'std_id':[1001,1002,1003,1004,1005],
           'std_name':["ahmed","hazam","omar","hamada","khaled"],
           'marks':[480,420,510,570,450],
           'avarage':[5,85,95,40,77]})

df=pd.DataFrame(students)
print(df)