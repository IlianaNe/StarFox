class InputManager:
    
    arrowUp = 'arrow_up'
    arrowDown = 'arrow_down'
    arrowLeft = 'arrow_left'
    arrowRight = 'arrow_right'
    space = 'space'
    keyA= 'a'
    keyS= 's'
    keyD= 'd'
    keyW= 'w'
    keyV= 'v'
    keyX= 'x'
    
    instance = None
    
    @staticmethod
    def initWith(app, key_list):
        InputManager.instance = InputManager()
        
        for k in key_list:
            InputManager.instance.setInput(k, False)
            app.accept(f'raw-{k}' , InputManager.createInputFunction(k, InputManager.instance, True)  )
            app.accept(f'raw-{k}-up' , InputManager.createInputFunction(k, InputManager.instance, False)  )
            
    @staticmethod
    def createInputFunction(key, inputInstance, down):
        def pressKey():
            inputInstance.setInput(key,down)
        return pressKey
        
    @staticmethod
    def getInput(k):
        return InputManager.instance.get_input(k)    
        
    @staticmethod
    def debug():
        print( InputManager.instance )
        
        
    def __init__(self):
        self.input= { }
    
    def setInput(self, key , state):
        self.input[key] = state
    
    def get_input(self, key):
        return self.input[key]
        
    def __str__(self):
        res = ""
        for k in self.input.items():
            res += f'\n {k[0]} {k[1]}'
        return res