
class Subscriber:
    def __init__(self):
        pass
    
    def Get_Notitification(self, **kwargs):
        pass


class Notifier:
    def __init__(self):
        self.subsribers = []
        
    def Notify(self):
        pass
    
    def Subscribe(self, subscriber):
        # TODO : Needs type check
        self.subsribers.append(subscriber)
    
    def Unsubscribe(self, subscriber):
        if subscriber in self.subsribers:
            self.subsribers.remove(subscriber)
    
    
    
    
    
    
    