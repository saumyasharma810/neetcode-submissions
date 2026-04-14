class MinStack:
    _stack = []
    _min = []

    def __init__(self):
        self._min.append(float('inf'))
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min.append(min(self._min[-1],val))

        

    def pop(self) -> None:
        self._stack.pop()
        self._min.pop()
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min[-1]

        
