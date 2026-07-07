class CountSquares:

    def __init__(self):
        self.x_axis_list = defaultdict(set)
        self.points = defaultdict(int)

        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.x_axis_list[point[0]].add(point[1])
        

    def count(self, point: List[int]) -> int:
        x,y = point[0], point[1]
        total = 0
        for y_coord in self.x_axis_list[x]:
            if y_coord == y:
                continue
            # square left
            # p1 = x,y p2 = x, y_cord
            # p3 = x - abs(y-y_coord), y p4 = x - abs(y-y_coord), y_coord
            if (x - abs(y-y_coord), y) in self.points and (x - abs(y-y_coord), y_coord) in self.points:
                total += self.points[(x,y_coord)] * self.points[(x - abs(y-y_coord), y)] * self.points[(x - abs(y-y_coord), y_coord)]
        
            # square right
            # p1 = x,y p2 = x, y_cord
            # p3 = x + abs(y-y_coord), y p4 = x + abs(y-y_coord), y_coord
            if (x + abs(y-y_coord), y) in self.points and (x + abs(y-y_coord), y_coord) in self.points:
                total += self.points[(x,y_coord)] * self.points[(x + abs(y-y_coord), y)] * self.points[(x + abs(y-y_coord), y_coord)]
            
        return total

        
