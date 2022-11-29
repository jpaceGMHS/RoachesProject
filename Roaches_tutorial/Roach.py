import pygame as py
from Notification import Subscriber
import math
import random as rand


class Behaviors:
    FLEE = 0
    WANDER = 1


class Roach(Subscriber):
    def __init__(self, surface, x=0, y=0):
        super().__init__()
        self._behaviors = {Behaviors.FLEE:self.Run_Away, Behaviors.WANDER:self.Wander}
        self.surface = surface
        self.location = (x, y)
        self.velocity = 1
        self.angle = 0
        self.state = Behaviors.WANDER
        self.target = None
        self.target_proximity = 20
        
    # Private Methods
    
    def _get_random_target(self,start_x, stop_x, start_y, stop_y):
        x = rand.randint(start_x, stop_x)
        y = rand.randint(start_y, stop_y)
        return (x, y)
    
    def _get_target_angle(self):
        if not self.target:
            return None
        angle = math.atan2((self.target[1] - self.location[1]), self.target[0] - self.location[0])
        return math.degrees(angle)  
    
    def _get_next_location(self):
        x = math.cos(self.angle) * self.velocity + self.location[0]
        y = math.sin(self.angle) * self.velocity + self.location[1]
        return (x, y)
    
    def _get_offscreen_target(self):
        # TODO : In Progress
        return (-50, 200)
    
    def _is_onScreen(self):
        if self.location[0] < 0 or self.location[0] > self.surface.get_width():
            return False
        if self.location[1] < 0 or self.location[1] > self.surface.get_height():
            return False
        return True
    
    
    def _target_reached(self):
        return math.dist((self.location[0], self.location[1]), (self.target[0], self.target[1])) <= self.target_proximity
    
    def _move_to_target(self):
        if self._target_reached():
            if self.state == Behaviors.WANDER:
                self.target = self._get_random_target(0, self.surface.get_width(), 0, self.surface.get_height())
        self.angle = self._get_target_angle()
        self.location = self._get_next_location()
        
    
    def _set_state(self, state):
        self.state = state
        self.target = None
    
    # Public API
    
    def Run_Away(self):
        #TODO : in progress
        if self._is_onScreen() and self.target == None:
            self.target = self._get_offscreen_target()
        self._move_to_target()
    
    def Wander(self):
        if self.target == None:
            self.target = self._get_random_target(0, self.surface.get_width(), 0, self.surface.get_height())
        self._move_to_target()
        
    def Run_Current_Behavior(self):
        self._behaviors[self.state]()
    
    def Get_Notification(self, **kwargs):
        print("notified")
        if 'state' in kwargs.keys():
            if kwargs['state'] == 0:
                self._set_state(Behaviors.WANDER)
            elif kwargs['state'] == 1:
                self._set_state(Behaviors.FLEE)
    
    def Draw(self):
        py.draw.ellipse(self.surface, (255, 255, 255), py.rect.Rect(self.location[0], self.location[1], 20, 20))

        if self.target:
            py.draw.ellipse(self.surface, (255, 255, 0), py.rect.Rect(self.target[0], self.target[1], 5, 5))





