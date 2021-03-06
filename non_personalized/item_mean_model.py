class ItemMeanModel:
    """Item Mean Model defines the mean ratings data structure
    It turns the mean ratings dictionary to a frozenset
    
    Raises:
        TypeError -- invalid type, should be a dictionary
    
    Returns:
        dictionary -- mean ratings {itemID : mean_rating}
    """

    def __init__(self, means):
        self.means = means
        self.__item_means = frozenset(means.items())
    @property
    def means(self):
        return self.__means
    @means.setter
    def means(self, means):
        if not isinstance(means, dict):
            raise TypeError("invalid type, should be a dictionary")
        else:
            self.__means = means

    def get_known_items(self):
        return dict(self.__item_means).keys()

    def has_item(self, item_id):
        return item_id in self.get_known_items()

    def get_mean_rating(self, item_id):
        if self.has_item(item_id):
            return dict(self.__item_means)[item_id]
        else:
            raise ValueError("unknow item ID")