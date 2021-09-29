from __future__ import annotations
from monster_class import Monster
from goblin_class import *
#import room_test

class Room:

    def __init__(self, roomDesc, objects: list):

        self._roomDesc = roomDesc
        self._objects = objects
        self._westExit = None
        self._eastExit = None
        self._northExit = None
        self._southExit = None
    

    def getRoomDesc(self):
        
        return self._roomDesc

    def getObjects(self):
        if self._objects:
            return self._objects
            
    def summonObjects(self):
        # To-Do
        return self._objects
    
    def getNextRoom(self, current_room):

        return None

    def setExitWest(self, room: Room):
        self._westExit = room
    
    def setExitNorth(self, room: Room):
        self._northExit = room

    def setExitEast(self, room: Room):
        self._eastExit = room
    
    def setExitSouth(self, room: Room):
        self._southExit = room

    def getExitWest(self):
        return self._westExit

    def getExitNorth(self):
        return self._northExit
    
    def getExitSouth(self):
        return self._southExit

    def getExitEast(self):
        return self._eastExit

