from random import gammavariate
from panda3d.core import Vec3


class ENEMY_TYPE (Enum):
    KAMIKAZE = 0
    CHASER = 1


class ENEMY_STATE(Enum):
    IDLE = 0
    CHASE = 1
    ATTACK = 2


class DynamicEnemy:
    dynamic_enemy_name = "DynamicEnemy"

    def __init__(self, world, originalEnemy, pos, ctrav, collisionHandler, type=ENEMY_TYPE.CHASE):
        self.gameObject = originalEnemy.copyTo(world)
        self.gameObject.setPos(world, pos)
        ctrav.addCollider(self.gameObject.find(
            "**collision**"), collisionHandler)

        self.gameObject.setPythonTag("ObjectController", self)
        self.gameObject.setName(DynamicEnemy.dynamic_enemy_name)

        self.type = type
        self.state = ENEMY_STATE.IDLE

    def updateKamikaze(self, world, dt, player):
        diff = player.getPos(world) - self.gameObject.getPos(world)
        distance = diff.length()
        print(distance)

        if(self.state == ENEMY_STATE.IDLE and distance <= 80):
            self.state = ENEMY_STATE.ATTACK
            self.vel = player.getPos(
                world) + world.getRelativeVector(player, Vec3(0, 1, 0))*40 - self.gameObject.getPos(world)
            self.vel.normalize()

        if(self.state == ENEMY_STATE.ATTACK):
            self.activeTimer += dt
            self.gameObject.setPos(
                world, self.gameObject.getPos(world) + self.vel*dt*60)

            if(self.activeTimer >= 5)
                self.gameObject.removeNode()

   def updateChaser(self, world, dt, player):
        diff = player.getPos(world) - self.gameObject.getPos(world)
        distance = diff.length()
        
        if(self.state == ENEMY_STATE.IDLE and distance <= 300 ):
            self.state = ENEMY_STATE.CHASE
            self.vel = player.getPos(world) + world.getRelativeVector(player, Vec3(0,1,0) )*80 - self.gameObject.getPos(world)
            self.vel.normalize()
               
        if( self.state == ENEMY_STATE.CHASE and distance >= 50 ):
            self.gameObject.setPos(world, self.gameObject.getPos(world) + self.vel*dt*30)
            self.activeTimer += dt
            if(self.activeTimer >= 1):
                    self.vel = player.getPos(world) + world.getRelativeVector(player, Vec3(0,1,0) )*80 - self.gameObject.getPos(world)
                    self.vel.normalize()
                    self.activeTimer = 0


    def update(self, world, dt , player):
        self.gameObject.lookAt(player)
        
        if( self.type == ENEMY_TYPE.KAMIKAZE):
            self.updateKamikaze(world,dt,player)
            
        if( self.type == ENEMY_TYPE.CHASER):
            self.updateChaser(world,dt,player)

