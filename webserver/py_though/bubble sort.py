#Bubble Sort

sampleList = [6,5,4,3,2,1]

def bubbleSort(sourceBubbleSortList):
  #how long the list
  listLength = len(sourceBubbleSortList)
  i = 0
  # the i here to count how many value not in
  while i < listLength-1:
    j = listLength - 1
    # here to compare two value
    while j > i:
      print(" sourceBubbleSortList = " + str(sourceBubbleSortList))
      #compare two value, replace it if here are diffrent big, and continute to compare until finish all of it
      if sourceBubbleSortList[j] < sourceBubbleSortList[j-1]:
        tempNum = sourceBubbleSortList[j]
        sourceBubbleSortList[j] = sourceBubbleSortList[j-1]
        sourceBubbleSortList[j-1] = tempNum
      
      j = j - 1
    i = i + 1

return sourceBubbleSortList
