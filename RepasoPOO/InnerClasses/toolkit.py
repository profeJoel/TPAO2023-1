class Toolkit:
    
    def __init__(self, id):
        self.id = id
        self.hammer = self.Hammer(1)
        self.handsaw = self.Handsaw(1)
        self.drill = self.Drill(1)
        
    class Hammer:
        def __init__(self, id):
            self.id = id
            
    class Handsaw:
        def __init__(self, id):
            self.id = id
    
    class Drill:
        def __init__(self, id):
            self.id = id