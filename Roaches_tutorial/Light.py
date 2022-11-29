import Notification

class LightState:
    ON = 1
    OFF = 0

class Light(Notification.Notifier):
    def __init__(self):
        super().__init__()
        self.state = LightState.OFF
        self._light_color = {
            LightState.ON:(200,200,200), 
            LightState.OFF:(0,0,0)
            }
        
    def Flip_Switch(self):
        if self.state == LightState.OFF:
            self.state = LightState.ON
        else:
            self.state = LightState.OFF
        self.Notify()
    
    def Notify(self):
        for s in self.subsribers:
            s.Get_Notification(state=self.state)
    
    def Get_Light_Color(self):
        return self._light_color[self.state]
    
    
    
    
    
    
    