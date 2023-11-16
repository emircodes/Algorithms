def quickSort(self):
    quickSortRec(self,0,self.length)
    return self
        
def quickSortRec(A, lo, hi):
    # sorts A[lo:hi]
   if hi-lo <= 1:
        return 
            
    iPivot = partition(A,lo,hi)
    
    quickSortRec(A,lo,iPivot)
    quickSortRec(A,iPivot+1,hi)
    
def partition(self, lo, hi):
    pivot = lo.data
    smaller = LinkedList()
    other = LinkedList()
    B = [0 for i in range(lo,hi)]
    loB = 0
    hiB = len(B)-1
    for i in range(lo+1,hi):
        if A[i] < pivot:
            B[loB] = A[i]
            loB += 1 
        else:
            B[hiB] = A[i]
            hiB -= 1
    B[loB] = pivot
        
    for i in range(len(B)):
        A[lo+i] = B[i]
    return lo+loB