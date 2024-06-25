
from maths_handler import *
from star_class import *

class Flag:
    def __init__(self, width: int, height: int, option: str) -> None:
        """
        Constructor that initializes flag's attributes
        :param width: flag width value
        :param height: flag height value
        :param option: flag option ordinary or TZion 
        """
        self.width = width
        self.height = height
        if option == "o" or option == "O" or option == "z" or option == "Z":
            self.option = option
        else:
            raise ValueError("enter O or Z only for option")
    
    def get_flag_size(self) -> int:
        """
        Method calculates and returns flag's size
        :return: flag's size value
        """
        return self.height * self.width
    
    def display_flag_dimensions(self) -> None:
        """
        Method displays flag dimensions
        :return: No return value
        """
        print(f"flag width is:{self.width} cm, flag height is:{self.height} cm")
        
    def draw_horizontal_stripe(self):
        """
        Method displays flag horizontal stripe
        :return: return a line of stripe
        """
        return ('*' * self.width)
    
    def draw_paddings(self):
        """
        Method displays flag empty padding
        :return: return a empty space 
        """
        return(' ' * self.width)
    
    def create_star_of_david(self, star_size: int, option: str):
        """
        Method create star of david flag object
        :return: return a star of david object
        """
        return Star(star_size,option) 
        
    
    # GETTERS
    @property
    def width(self):
        """
        Setter returns the flag width
        :return: flag width
        """
        return self.__width

    @property
    def height(self):
        """
        Setter returns the flag height
        :return: flag height
        """
        return self.__height
    
    @property
    def option(self):
        """
        Setter returns the flag kind option
        :return: flag option
        """
        return self.__option
    
# SETTERS
    @width.setter
    def width(self, width: int):
        """
        Setter sets flag width
        :param width: A value to set the width
        :return: None
        """
        
        self.__width = width

    @height.setter
    def height(self, height: int):
        """
        Setter sets flag height
        :param height: A value to set the height
        :return: None
        """

        self.__height = height
        
    @option.setter
    def option(self, option: str):
        """
        Setter sets flag kind option
        :param option: A value to set the option
        :return: None
        """

        self.__option = option
        
    def __str__(self):
            """
            Method print a string that displays the flag in the specific format
            :return: No return value
            """
            # Draw the top stripe
            for _ in range(STRIPE_ROW):
                print(self.draw_horizontal_stripe())

            # Draw the top padding
            for _ in range(padding(self.width,self.height)):
                print(self.draw_paddings()) 

            # create and print the Star of David
            for line in self.create_star_of_david(star_size(self.width,self.height),self.option).star_matrix:
                print("".join(line).center(self.width))

            # Draw the bottom padding
            for _ in range(padding(self.width,self.height)):
                print(self.draw_paddings())
                
            # Draw the bottom stripe
            for _ in range(STRIPE_ROW):
                print(self.draw_horizontal_stripe())
            
            # check the matrix size fit for TZION star and printing a message 
            if self.create_star_of_david(star_size(self.width,self.height),self.option).rows < 5 and (self.option == "z" or self.option =="Z"):
                print(" small dimensions, can't print a TZion(צ,z) flag ")
                
            return ""