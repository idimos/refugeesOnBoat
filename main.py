from models.app import *

class refugeesOnBoat(App):
    """Main App Class"""
    def __init__(self):
        super().__init__()

        App.scene = App.scenes[0]
        print("refugeesOnBoat init")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    refugeesOnBoat().run()
