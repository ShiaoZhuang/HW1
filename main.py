# Author: Shiao Zhuang sqz5328@psu.edu
A = 4.0
Am = 3.67
Bp = 3.33
B = 3.0
Bm = 2.67
Cp = 2.33
C = 2.0
D = 1.0
F = 0.0
############################################
oneG = input("Enter your course 1 letter grade: ")
oneC = input("Enter your course 1 credit: ")
if oneG == 'A': 
  print(f"Grade point for course 1 is: {A}")
  oneG = 4.0
elif oneG == 'A-': 
  print(f"Grade point for course 1 is: {Am}")
  oneG = 3.67
elif oneG == 'B+': 
  print(f"Grade point for course 1 is: {Bp}")
  oneG = 3.33
elif oneG == 'B': 
  print(f"Grade point for course 1 is: {B}")
  oneG = 3.0
elif oneG == 'B-': 
  print(f"Grade point for course 1 is: {Bm}")
  oneG = 2.67
elif oneG == 'C+': 
  print(f"Grade point for course 1 is: {Cp}")
  oneG = 2.33
elif oneG == 'C': 
  print(f"Grade point for course 1 is: {C}")
  oneG = 2.0
elif oneG == 'D': 
  print(f"Grade point for course 1 is: {D}")
  oneG = 1.0
else : 
  print(f"Grade point for course 1 is: {F}")
  oneG = 0.0
############################################
twoG = input("Enter your course 2 letter grade: ")
twoC = input("Enter your course 2 credit: ")
if twoG == 'A': 
  print(f"Grade point for course 2 is: {A}")
  twoG = 4.0
elif twoG == 'A-': 
  print(f"Grade point for course 2 is: {Am}")
  twoG = 3.67
elif twoG == 'B+': 
  print(f"Grade point for course 2 is: {Bp}")
  twoG = 3.33
elif twoG == 'B': 
  print(f"Grade point for course 2 is: {B}")
  twoG = 3.0
elif twoG == 'B-': 
  print(f"Grade point for course 2 is: {Bm}")
  twoG = 2.67
elif twoG == 'C+': 
  print(f"Grade point for course 2 is: {Cp}")
  twoG = 2.33
elif twoG == 'C': 
  print(f"Grade point for course 2 is: {C}")
  twoG = 2.0
elif twoG == 'D': 
  print(f"Grade point for course 2 is: {D}")
  twoG = 1.0
else : 
  print(f"Grade point for course 2 is: {F}")
  twoG = 0.0
############################################
threeG = input("Enter your course 3 letter grade: ")
threeC = input("Enter your course 3 credit: ")
if threeG == 'A': 
  print(f"Grade point for course 3 is: {A}")
  threeG = 4.0
elif threeG == 'A-': 
  print(f"Grade point for course 3 is: {Am}")
  threeG = 3.67
elif threeG == 'B+': 
  print(f"Grade point for course 3 is: {Bp}")
  threeG = 3.33
elif threeG == 'B':
  print(f"Grade point for course 3 is: {B}")
  threeG = 3.0
elif threeG == 'B-': 
  print(f"Grade point for course 3 is: {Bm}")
  threeG = 2.67
elif threeG == 'C+': 
  print(f"Grade point for course 3 is: {Cp}")
  threeG = 2.33
elif threeG == 'C': 
  print(f"Grade point for course 3 is: {C}")
  threeG = 2.0
elif threeG == 'D': 
  print(f"Grade point for course 3 is: {D}")
  threeG = 1.0
else : 
  print(f"Grade point for course 3 is: {F}")
  threeG = 0.0
############################################
print(f"Your GPA is: {(float(oneC)*oneG + float(twoC)*twoG + float(threeC)*threeG)/(float(oneC)+float(twoC)+float(threeC))}")

