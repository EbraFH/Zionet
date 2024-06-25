from maths_handler import *

class Star:
    def __init__(self, size: int, option:str):
        """
        Constructor that initializes star's attributes
        :param base: star base value
        :param column: star column value
        :param rows:  rows value
        :param size : size value 
        :param star_matrix : flag matrix container
        """
        self.size = size
        self.base = base_of_star(size)
        self.column = column_of_star(size)
        self.rows = rows_of_star(size)
        self.star_matrix = self.create_star()
        if option == "z" or option == "Z":
            self.star_matrix = self.create_tzion_star()

    def create_star(self):
        """
        Method create and returns star's of david
        :return: matrix of david star  
        """
        star = [] # star list
        row = [] # helper row list
        
        # the hed of the star()
        for i in range(self.rows//4):
            for j in range(self.column):
                if j==((self.column//2)-i) or j==((self.column//2)+i):
                    row.append("*")
                else:
                    row.append(" ")
            star.append(row)
            row=[]
        
        # Create the the first horizontal row in the star
        for i in range(self.column):
            row.append("*")
        star.append(row)
        row=[]
        
        # Create the small middle two triangles for the above half
        for i in range(self.rows//4):
            for j in range(self.column):
                if  j==1+i or j==((self.column//3)-1-i) or j==(2*(self.column//3)+1+i) or j==self.column-i-2 :
                    row.append("*")
                else:
                    row.append(" ")
            star.append(row)
            row=[]
        
        # copping the first half as a mirrored column
        if self.base >= 3:
            for i in range(self.rows//2-1,-1,-1):
                for j in range(len(star[i])):
                    row.append(star[i][j])
                star.append(row)
                row=[]

        return star

    def create_tzion_star(self):
        """
        Method create and returns tzion star's of david
        :return: matrix of tzion david star  
        """
        starZ = [] # helper list
        # to create the TZION star the base have to be more than 5 if not returning ordinary david star
        if len(self.star_matrix) >= 5:
            # create the lest to make the changes on it
            for row in self.star_matrix:
                starZ.append(row)
            
            # replacing the asterisks ("*") with later ("O") to make צ and z in david star
            for i in range(len(starZ)//4,(len(starZ)//4)*3+1):
                for j in range(len(starZ[i])):
                    if (i-j==len(starZ)//4) or (j >= len(starZ[i])//3*2 and i==len(starZ)//4) or (i == (len(starZ)//4)*3 and (j <= len(starZ[i])//3 or j >= len(starZ[i])//3*2)) or (j==len(starZ[i])-i+len(starZ[i])//3//2-1) or (j==len(starZ[i])//3-i+len(starZ[i])//3//2 and i<=len(starZ)//4*2):
                        starZ[i][j] = "O"
            return starZ
        else:
            return self.star_matrix

    def get_star_size(self) -> int:
        """
        Method calculates and returns star's size
        :return: star's size value
        """
        return self.rows * self.column
    
    def display_star_dimensions(self) -> None:
        """
        Method displays star dimensions
        :return: No return value
        """
        print(f"star column is:{self.column} cm, star rows is:{self.rows} cm")
        
    # GETTERS
    @property
    def column(self):
        """
        Setter returns the star column
        :return: star column
        """
        return self.__column

    @property
    def rows(self):
        """
        Setter returns the star rows
        :return: star rows
        """
        return self.__rows
    
    @property
    def base(self):
        """
        Setter returns the star base
        :return: star base
        """
        return self.__base
    
    @property
    def star_matrix(self):
        """
        Setter returns the star matrix
        :return: star matrix
        """
        return self.__star_matrix
    
# SETTERS
    @column.setter
    def column(self, column: int):
        """
        Setter sets star column
        :param column: A value to set the column to
        :return: None
        """
        
        self.__column = column

    @rows.setter
    def rows(self, rows: int):
        """
        Setter sets star rows
        :param rows: A value to set the rows to
        :return: None
        """
        
        self.__rows = rows
        
    @base.setter
    def base(self, base: str):
        """
        Setter sets small star base
        :param base: A value to set the base
        :return: None
        """
        
        self.__base = base
        
    @star_matrix.setter
    def star_matrix(self, star_matrix: list):
        """
        Setter sets small star base
        :param base: A value to set the base
        :return: None
        """

        self.__star_matrix = star_matrix
        
    def __str__(self):
            """
            Method print a string that displays the star in the specific format
            :return: No return value
            """
            # print the Star of David centered
            for line in self.star_matrix:
                print("".join(line).center(self.size))
            return ""