

class Bullet:
    def __init__(self, x=0, y=0, move=[0, 0], radius=0.15, speed=0.5, owner_pid=None):
        self.x = x
        self.y = y
        self.move = move
        self.radius = radius
        self.speed = speed
        self.exists = True
        self.owner_pid = owner_pid

    def tick(self, game_board,):
        new_x = self.x + self.move[0] * self.speed
        new_y = self.y + self.move[1] * self.speed

        # Check collision with walls
        if game_board.board[int(new_x)][int(new_y)] != 1:
            self.x = new_x
            self.y = new_y
        else:
            self.exists = False
