import time
import behaviour as beh
import os
import random

class Agent:
    def __init__(self, id_, b, x, y):
    	self.id = id_
    	self.b = b
    	self.x = x
    	self.y = y
    
    def get_coordinates(self):
        return self.x, self.y
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def update(self, team_own, team_opp, ball):
        x,y = self.x, self.y
        random.seed(random.random() * self.id)
        rndm = random.randrange(2)
        if self.id > 0:
            if rndm == 0:
                self.b = beh.RuleBased()
            elif rndm == 1:
                self.b = beh.Defensive()
            self.b = beh.UtilityBased()
        self.x, self.y = self.b.next(abs(self.id)-1, team_own, team_opp, ball)

    def run(self, team_own, team_opp, ball):
    	while True:
    		try:
    			x,y = self.x, self.y
	    		self.x, self.y = self.b.next(self.id, team_own, team_opp, ball)
	    		time.sleep(5)
	    	except Exception as e:
	    		print("Killed process for agent", self.id, "due to reason", e)
	    		return
