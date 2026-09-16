class Solution(object):
    def reorderList(self, head):
        arr = []
        
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        leng=len(arr)
        mid=(leng+1)//2
        arr1=arr[:mid]
        arr2=arr[mid:][::-1]
        arrf=[]
        for i in range(len(arr2)):
            arrf.append(arr1[i])
            arrf.append(arr2[i])
        if len(arr1) > len(arr2):
            arrf.append(arr1[-1])
        
        print(arrf)
        curr = head
        for value in arrf:
            curr.val = value
            curr = curr.next