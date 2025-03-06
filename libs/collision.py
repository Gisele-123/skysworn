from networkx import center
from libs.vector import Vec3


class Rect:

    def __init__(self, player, x=0, y=0, w=1, h=1):
        self.center = [x, y]
        self.width = w
        self.height = h
        self.player = player

    def checkCollWithPlayer(self, playerPos, playerWidth):
        return self.center[0] + 1.5 + playerWidth > playerPos.x > self.center[0] - 1.5 - playerWidth and \
                self.center[2] + 1.5 + playerWidth > playerPos.z > self.center[2] - 1.5 - playerWidth

def handleCollisionWithPlayer(self, player):
    temp = Vec3(self.center[0], 0, self.center[1])
    norm = self.player.camera.cam_pos - temp

    if abs(norm.x) > abs(norm.z):
        norm = Vec3(1, 0, 0) if norm.x > 0 else Vec3(-1, 0, 0)
    else:
        norm = Vec3(0, 0, 1) if norm.z > 0 else Vec3(0, 0, -1)

    dir = norm  # Ensure `dir` is properly defined
    temp = norm ** dir
    self.player.camera.cam_pos -= dir * self.player.currentSpeed
    self.player.camera.cam_pos += (temp ** norm).normalize() * self.player.currentSpeed

    playerWidth = player.width  # Assuming `player` has a `width` attribute
    if self.player.left and not self.player.right:
        if self.center[0] + 1.5 + playerWidth > player.x > self.center[0] - 1.5 - playerWidth and \
           self.center[1] + 1.5 + playerWidth > player.z > self.center[1] - 1.5 - playerWidth:
            self.player.camera.cam_pos += (norm + ((temp ** norm) - dir)).normalize() * self.player.currentSpeed

    elif not self.player.left and self.player.right:
        if self.center[0] + 1.5 + playerWidth > player.x > self.center[0] - 1.5 - playerWidth and \
           self.center[1] + 1.5 + playerWidth > player.z > self.center[1] - 1.5 - playerWidth:
            self.player.camera.cam_pos += (norm + ((temp ** norm) - dir)).normalize() * self.player.currentSpeed
