


class Map():
    def __init__(self,x_max,y_max, goal_x, goal_y):
        self.x_max = x_max
        self.y_max = y_max
        self.goal_x = goal_x
        self.goal_y = goal_y
        

class Player():
    def __init__(self, name, map):
        self.name = name
        self.x = 0
        self.y = 0
        self.map = map
    
    def move_up(self):
        if self.y < slef.map.y_max:
            self.y += 1

    def move_down(self):
        if self.y > 0:
            self.y -= 1

    def move_right(self):
        if self.x < self.map.x_max:
            self.x += 1

    def move_left(self):
        if self.x > 0 :
            self.x -= 1


    def pick_tressure(self):

        if self.x == self.map.goal_x and self.y == self.map.goal_y:
            print(self.name, "hittade skatten")

        else:
            print(self.name "kunde inte hitta skatten")        
        

map_object = Map(5,4,2,1)
player_1 = Player('isak', map_object)
player_2 = Player('marisa', map_object)


player_1.move_up()
player_2.move_up()
