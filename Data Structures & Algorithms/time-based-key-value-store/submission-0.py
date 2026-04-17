class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.mapping[key]
        if len(lst) == 0:
            return ""
        l,r = 0, len(lst)-1

        while l<r:
            print(l,r)
            mid = (l+r)//2
            if lst[mid][0] < timestamp:
                l = mid+1
            elif lst[mid][0] > timestamp:
                r = mid-1
            else:
                return lst[mid][1]
        if lst[l][0] <= timestamp:
            return lst[l][1]
        if l > 0:
            return lst[l-1][1]
        return ""

        
