from item_mean_model import ItemMeanModel
import pandas as pd
class ItemMeanModelProvider(ItemMeanModel):
    def __init__(self, ratings):
        self.ratings = ratings
    @property
    def ratings(self):
        return self.__ratings
    @ratings.setter
    def ratings(self, ratings):
        if not isinstance(ratings, pd.DataFrame):
            raise TypeError("unknown data type")
        else:
            self.__ratings = ratings
    def __compute_mean(self):
        df_means = self.ratings.groupby(['userID'])['rating'].mean()
        return df_means.to_dict()
    def get(self):
        return ItemMeanModel(self.__compute_mean())