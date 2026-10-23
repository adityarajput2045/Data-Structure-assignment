# Rotate the array d number of time
""" 
arr =  [10,45,0,12,0,56]  d = 4
first rotation = [56,10,45,0,12,0]
Second rotation = [0,56,10,45,0,12]
Third rotation = [12,0,56,10,45,0]
first rotation = [0,12,0,56,10,45]
"""

def rotateArrayDNumbersTime(arr,d):
  n = len(arr)
  arr = arr[n-d:] + arr[:n-d]
  return arr
  
result = rotateArrayDNumbersTime([10,45,0,12,0,56],4)
print(result)