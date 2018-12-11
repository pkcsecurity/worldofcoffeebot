import utils
from bullet import Bullet


class Player:
    def __init__(self, x=0, y=0, speed=0.25, pid=None, life=10, character=0, radius=1):
        self.pid = pid
        self.x = x
        self.y = y
        self.speed = speed
        self.face = [0, 0]
        self.move = [0, 0]
        self.attacking = False
        self.radius = radius
        self.life = life
        self.character = 0
        self.bullet_cooldown = 0

    def tick(self, game_board, bullets):
        new_x = self.x + self.move[0] * self.speed
        new_y = self.y + self.move[1] * self.speed

        # Check collision with walls
        if game_board.board[int(new_x)][int(new_y)] != 1:
            self.x = new_x
            self.y = new_y

        # Check collision with bullets
        for b in bullets:
            if b.owner_pid != self.pid:
                bullet_distance = utils.distance([self.x, self.y], [b.x, b.y])
                if bullet_distance < (self.radius + b.radius) and b.exists:
                    print("Ouch! PID {} got hit!".format(self.pid))
                    self.life -= 1
                    b.exists = False

        if self.attacking and self.bullet_cooldown <= 0:
            new_bullet = Bullet(x=self.x, y=self.y, move=self.face, owner_pid=self.pid)
            bullets.append(new_bullet)
            self.bullet_cooldown = 20
        else:
            self.bullet_cooldown -= 1

    def update(self, move, face, attacking):
        self.move = move
        self.face = face
        self.attacking = attacking

    def __str__(self,):
        return 'Player {}: pos [{}, {}]'.format(self.pid, self.x, self.y)
