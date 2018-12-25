class ItemMeanModelProvider:
    def __init__(self, num_top_rated):
        self.num_top_rated = num_top_rated  
    @property
    def num_top_rated(self):
        return self.__num_top_rated
    
    @num_top_rated.setter
    def num_top_rated(self, num_top_rated):
        if not isinstance(num_top_rated, int):
            raise TypeError("non valid type, should be a positive integer")
        elif num_top_rated <= 0:
            raise ValueError("invalid number of top rated items, should be a positive integer")
        else:
            self.__num_top_rated = num_top_rated