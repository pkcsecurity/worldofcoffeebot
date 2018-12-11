class Player:
    def __init__(self, x=0, y=0, speed=0.25, pid=None, life=10):
        self.pid = pid
        self.x = x
        self.y = y
        self.speed = speed
        self.face = [0, 0]
        self.move = [0, 0]
        self.attacking = False
        self.radius = 1
        self.life = life

    def tick(self, game_board):
        new_x = self.x + self.move[0] * self.speed
        new_y = self.y + self.move[1] * self.speed

        # Check collision with walls
        if game_board.board[int(new_x)][int(new_y)] != 1:
            self.x = new_x
            self.y = new_y

    def __str__(self,):
        return 'Player {}: pos [{}, {}]'.format(self.pid, self.x, self.y)
