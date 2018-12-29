"""
The mean_based_recommender will provide non personnalized 
recommendations based on the items mean ratings
"""
class ItemMeanModelProvider:
    """
    ItemMeanModel Provider class provides the top N highest rated items
    First, it sets the number of top rated items.
    The number of top rated items can be entered by the user and should be a positive integer.
    
    Raises:
        TypeError -- non valid type, should be a positive integer
        ValueError -- invalid number of top rated items, should be a positive integer
    
    Returns:
        integer -- TBD
    """

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