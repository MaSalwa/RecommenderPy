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
    def compute_mean(self):
        df_means = self.ratings.groupby(['userID'])['rating'].mean()
        return df_means.to_dict()
    def get(self):
        return ItemMeanModel(self.compute_mean())


# if __name__ == "__main__":
#     data = pd.read_csv("/home/salwamaatoug/recommender_material/nonpers-assignment/data/ratings.csv")
#     del data['timestamp']
#     data.columns = ['userID', 'itemID', 'rating']
#     immp = ItemMeanModelProvider(data)
#     print(immp.get().get_mean_rating(2024))
