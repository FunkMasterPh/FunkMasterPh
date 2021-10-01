from __future__ import annotations
from misc import Door
from monster_class import Monster
from goblin_class import *

#template for creating a room object
class Room:

    def __init__(self, roomDesc, objects: list):

        self._roomDesc = roomDesc
        self._objects = objects
        self._westExit = None
        self._eastExit = None
        self._northExit = None
        self._southExit = None
        self._dark = False
    
    #returns dark status on room
    def getDark(self):
        return self._dark
    
    #returns a description of the room
    def getRoomDesc(self):
        return self._roomDesc

    #if there are objects in the room it returns them
    def getObjects(self):
        if self._objects:
            return self._objects
    
    #returns west exit of a room
    def getExitWest(self):
        return self._westExit

    #returns north exit of a room
    def getExitNorth(self):
       return self._northExit
    
    #returns south exit of a room
    def getExitSouth(self):  
        return self._southExit

    #returns east exit of a room
    def getExitEast(self):
        return self._eastExit
    
    #sets room to dark
    def setDark(self, lightStatus):
        self._dark = lightStatus
    
    #sets west exit of a room
    def setExitWest(self, room: Room):
        self._westExit = room
    
    #sets north exit of a room
    def setExitNorth(self, room: Room):
        self._northExit = room

    #sets east exit of a room
    def setExitEast(self, room: Room):
        self._eastExit = room
    
    #sets south exit of a room
    def setExitSouth(self, room: Room):
        self._southExit = room


    #def summonObjects(self):
        #return self._objects

    #def getNextRoom(self, current_room):
        #return None
