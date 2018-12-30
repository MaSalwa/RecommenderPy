from item_mean_model_provider import ItemMeanModelProvider
import pandas as pd

class MeanItemBasedRecommender(ItemMeanModelProvider):
    """
    ItemMeanModel Provider class provides the top N highest rated items
    First, it sets the number of top rated items.
    The number of top rated items can be entered by the user and should be a positive integer.
    
    Raises:
        TypeError -- non valid type, should be a positive integer
        ValueError -- invalid number of top rated items, should be a positive integer
    
    Returns:
        data frame -- top rated item ids with their corresponding ratings
    """

    def __init__(self, num_top_rated, ratings):
        self.num_top_rated = num_top_rated  
        self.ratings = ratings
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
    def n_highest(self):
        means = self.get().means
        df_means = pd.DataFrame.from_dict(means, orient = "index")
        df_means.columns = ['rating']
        return df_means.nlargest(self.num_top_rated, ['rating'])