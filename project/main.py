from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from Settings import world_settings as world_settings

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.white,
            highlight_color = color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)

app = Ursina()
window.title = "Mincecraft KSS"
skybox_image = load_texture("./assets/Textures/Sky/sky2.jpg")
Sky(texture=skybox_image)

for z in range(128):
    for x in range(128):
        voxel = Voxel(position=(x,0,z))
        
player = FirstPersonController()
camera.clip_plane_far = 48

app.run()