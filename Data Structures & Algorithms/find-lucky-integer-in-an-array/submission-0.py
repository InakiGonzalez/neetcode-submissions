from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_count = Counter(arr)
        res = -1
        print(arr_count)
        for k,v in arr_count.items():
            print("k: ",k)
            print("v: ",v)
            if int(k) == v:
                res = max(res,v)
        return res