class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        self.upheap(arr, n, i)
        self.downheap(arr, n, i)
    
    # compare i with its parent
    def upheap(self, arr, n, i):
        p = self.parent(i)
        if i>0 and arr[p] > arr[i]:
            arr[i], arr[p] = arr[p], arr[i]
            self.upheap(arr, n, p)
         
    #  compare i with its children
    def downheap(self, arr, n, i):
        if self.leftChild(i)<n:
            if (self.rightChild(i)<n) and (arr[self.leftChild(i)] > arr[self.rightChild(i)]):
                minChildPos = self.rightChild(i)  
            else: 
                minChildPos = self.leftChild(i)
            if arr[i] > arr[minChildPos]:
                arr[i], arr[minChildPos] = arr[minChildPos], arr[i]
                self.downheap(arr, n, minChildPos)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n):
            self.upheap(arr, n, i)
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        while n > 0:
            self.remove(arr, n, 0)
            n-=1
        
        arr.reverse()
        
    # insert new node
    def insert(self, arr, elt):
        arr.append(elt)
        self.upheap(arr, len(arr), len(arr)-1)
    
    # remove node
    def remove(self, arr,n, i):
        arr[n-1],arr[i] = arr[i],arr[n-1]
        self.heapify(arr, n-1, i)
    
    # update node
    def update(self, arr, i, elt):
        arr[i] = elt
        self.heapify(arr, len(arr), i)
        
    # get minimun node
    def getMin(self, arr):
        return arr[0]
        
    # get left child
    def leftChild(self, i):
        return 2*i + 1
    
    # get right child
    def rightChild(self, i):
        return 2*i + 2
    
    # get parent
    def parent(self, i):
        return (i-1)//2