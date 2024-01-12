import pygame as pg
import random

class game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        res = (600,600)
        self.screen = pg.display.set_mode(res)
        self.background=pg.image.load('/home/aaditya/system/vs/py/pygame/flappy/1.png')
        self.background=pg.transform.scale(self.background,(600,600))
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(60)/1000
        self.list_for_pipe_direction=[0,600]
        self.pipe_dir=1
        self.rect_present_or_not=0
        self.pipe_y=0
        self.flag=0
        self.pipe_height=0
        self.score=0
        self.font=pg.font.SysFont(None,30)
        self.new_game()
        
        

    def new_game(self):
        self.points=0
        self.x=100
        self.count=45
        self.y=self.screen.get_width()//2
        self.pipe_x=600
        self.b_pos=pg.Vector2(self.x,self.y)
        self.pipe_pos=pg.Vector2(self.pipe_x,self.pipe_y)


        
        
    def random_pipe(self):
        self.pipe_y=random.choice(self.list_for_pipe_direction)
        self.pipe_height=random.randint(150,200)
        if self.pipe_y == 0:
            self.pipe_pos.y=self.pipe_y
            self.pipe_dir=1
        else:
            self.pipe_pos.y=600-self.pipe_height
            self.pipe_dir=-1
        self.pipe_pos.x=self.pipe_x
        return 1

    def update_pipe(self):
        self.pipe_pos.x-=self.count*self.dt
        pg.draw.rect(self.screen,'green',(self.pipe_pos.x,self.pipe_pos.y,150,self.pipe_height))
        if self.pipe_pos.x<0:
            self.count+=2
            self.score+=1
            return 0
        else:
            return 1
    def collision_checker(self):
        if self.b_pos.x<self.pipe_pos.x+150 and self.b_pos.x>self.pipe_pos.x:
            if self.pipe_dir == -1 and int(self.b_pos.y)+40>=self.pipe_pos.y:
                return 1
            if self.pipe_dir == 1 and int(self.b_pos.y)-40<=self.pipe_height:
                return 1
        return 0
 
    def apply_gravity(self):
    	self.b_pos.y+=0.8

    def draw(self):
        sctxt=self.font.render("Score:"+str(self.score),True,"red")
        self.screen.blit(self.background,(0,0))
        self.screen.blit(sctxt,[20,20])
        if self.flag==0:
            self.flag=self.random_pipe()
        else:
            self.flag=self.update_pipe()
        pg.draw.circle(self.screen,'red',self.b_pos,40)
        self.apply_gravity()

    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.b_pos.y-=250*self.dt
        self.draw()

        pg.display.flip()
        
    def runner(self):
        run=True
        while run:
            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                    run=False
                    break
            if int(self.b_pos.y)>550:
                print('game over !!')
                run=False
                break

            if self.collision_checker():
                print('game over !!')
                run=False
                break                
            self.update()
        pg.quit()

if __name__ == '__main__':
    obj = game()
    obj.runner()
