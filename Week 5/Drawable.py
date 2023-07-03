#File Name:   Drawable.py
#Author:      Noel Aniyankunju(na932) and Jackie Cheng(jc4653)
#Purpose:     Abstract class that allows us to create drawable objects
#             with different shapes, at a given location (x, y)
#Last update: 2/2/21 - A. Medlock

import pygame
from abc import ABC, abstractmethod

class Drawable(ABC):
    def __init__(self, x = 0, y = 0):
        '''
        Constructor:
        __init__
        Purpose: This constructors would be used to create a Drawable object
        Parameters
        x: x-value of the drawn object
        y: y-value of the drawn object
        No Return
        Usage: object1 = Drawable()
        '''
        self.__x = x
        self.__y = y
        
    def getLoc(self):
        '''
        Getter
        getLoc()
        Purposes: Method to get the x and y values of an object
        Parameters:
        self: refers to this instance of the object
        Return: a tuple of the x and y values of this instance of the objects
        Usage: drawable.getLoc()
        '''
        return (self.__x, self.__y)
        
    def setLoc(self, p):
        '''
        Setter
        setLoc()
        Purpose: assigns the x and y values with the x and y values of the lsit
        Parameters:
        self: refers to this instance of the object
        p: a list of values for the x and y values
        '''
        self.__x = p[0]
        self.__y = p[1]
    
    @abstractmethod
    def draw(self, surface):
        '''
        Abstract Method
        draw()
        Parameters:
        self: refers to this instance of the object
        surface: designated display/surface that the graphics are drawn on
        No return
        '''
        pass

class Rectangle(Drawable):
    def __init__(self, color, width, height, xValue = 0, yValue = 0):
        '''
        Constructor:
        __init__
        Purpose: This constructors would be used to create a Rectangle object
        Parameters
        color: defines the color of the rectangle using RGB integer ranges
        width: int value for the width of the rectangle
        height: int value for the height of the rectangle
        xValue: x-value of the drawn object
        yValue: y-value of the drawn object
        No Return
        groundPlane = Rectangle(greenColor, 0, 200, 500, 300)
        '''
        super().__init__(xValue, yValue)
        self.__width = width
        self.__height = height
        self.__color = color
        
    def draw(self, surface):
        '''
        Abstract Method
        draw()
        Parameters:
        self: refers to this instance of the object
        surface: designated display/surface that the graphics are drawn on
        Usage: Rectangle.draw(surface)
        '''
        location = self.getLoc()
        pygame.draw.rect(surface, self.__color, (self.__width, self.__height, location[0], location[1]))
        

class Snowflake(Drawable):
    def __init__(self, color, xValue = 0, yValue = 0, maxY = 300):
        '''
        Constructor:
        __init__
        Purpose: This constructors would be used to create a Snowflake object
        Parameters
        color: defines the color of the rectangle using RGB integer ranges
        xValue: x-value of the drawn object
        yValue: y-value of the drawn object
        No Return
        snowflakeGeneration = Snowflake(whiteColor, randomXSnowflake, 0)
        '''
        super().__init__(xValue, yValue)
        self.__color = color
        
    def draw(self, surface):
        '''
        Abstract Method
        draw()
        Parameters:
        self: refers to this instance of the object
        surface: designated display/surface that the graphics are drawn on
        Usage: Snowflake.draw(surface)
        '''
        location = self.getLoc()
        pygame.draw.line(surface, (255, 255, 255), (location[0] - 5, location[1]), (location[0] + 5, location[1]))
        pygame.draw.line(surface, (255, 255, 255), (location[0], location[1] - 5), (location[0], location[1] + 5))
        pygame.draw.line(surface, (255, 255, 255), (location[0] - 5, location[1] - 5), (location[0] + 5, location[1] + 5))
        pygame.draw.line(surface, (255, 255, 255), (location[0] - 5, location[1] + 5), (location[0] + 5, location[1] - 5))
        
        
    def getY(self):
        '''
        Getter Method
        getY()
        Parameters:
        self: refers to this instance of the object
        Usage: Snowflake.getY()
        '''
        return self.__yValue
    
    def setY(self,value):
        '''
        Setter Method
        setY()
        Parameters:
        self: refers to this instance of the object
        value: used to hold the value in which yValue will be updated with 
        Usage: Snowflake.setY()
        '''
        self.__yValue = value
        
    
    