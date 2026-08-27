class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # optimized solution by going backward as we move left, we hold the max already so we know the answer without re-scanning (brute-forcing to check on the right side) -> O(n) time with O(1) complexity

        #syntax: range(start, stop, step) 
        #syntax: max(iterable) 
        # maxE = -1
        # for i in range(len(arr) - 1, -1, -1):
        #     temp = arr[i]
        #     arr[i] = maxE
        #     maxE = max(maxE, temp)
        # return arr

        # brute-force
        maxR = -1
        for i in range(len(arr) -1):
           
            for j in range(i + 1, len(arr)):
                maxR = max(maxR, arr[j])
            arr[i] = maxR
            maxR=-1
        arr[len(arr)-1] = -1 
        return arr
