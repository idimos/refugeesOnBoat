from models.app import *

class refugeesOnBoat(App):
    def __init__(self):
        super().__init__()

        Scene()
        # Scene(bg=(255,255,0))

        App.scene = App.scenes[0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    refugeesOnBoat().run()
