from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.title = 'Minecraaft Ursina'
window.fullscreen = True
window.fps_counter.enabled = True

txt = Text(text='Shift + Q to exit \nHold left shift to sprint \n\npress T for grass block \nPress z for stone block \nPress u for dirt block',
      scale=1.1, x=-.8, y=.5, color = color.black)

green_cube = color.green
stone_cube = color.gray
dirt_cube = color.brown
block_pick = 1

def update():
    global block_pick

    if held_keys['t']: block_pick = 1
    if held_keys['z']: block_pick = 2
    if held_keys['u']: block_pick = 3

class Voxel(Button):
    def __init__(self, position = (0,0,0), Color = green_cube):
        super().__init__(
        parent = scene,
        position = position,
        model = 'cube',
        origin_y = 0.5,
        texture = 'white_cube',
        color = Color,
        highlight_color = color.blue)

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, Color = green_cube)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, Color = stone_cube)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, Color = dirt_cube)
            if key == 'left mouse down':
                destroy(self)
            if held_keys['shift']:
                player.speed = 5
            else:
                player.speed = 3
class Sky(Entity):
    def __init__(self):
        super().__init__(
        parent = scene,
        model = 'sphere',
        color = color.blue,
        scale = 150,
        double_sided = True)

class Hand(Entity):
    def __init__(self):
        super().__init__(
        parent = camera.ui,
        model = 'cube',
        texture = 'white_cube',
        color = color.orange,
        scale = 0.2,
        scale_y = .5,
        scale_z = .2,
        rotation = Vec3(220, -10, 0),
        position = Vec2(0.4, -0.5))

for z in range(40):
    for x in range(40):
        voxel = Voxel(position = (x,0,z))


player = FirstPersonController()
player.speed = 3
sky = Sky()
hand = Hand()
app.run()
