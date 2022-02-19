class Mode:
    def __init__(self):
        self.mode = 'n'
    
    def getMode(self):
        return self.mode

    def change(self, md):
        assert isinstance(md, str)
        self.mode = md

MODE = Mode()