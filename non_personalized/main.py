from mean_item_based_recommender import MeanItemBasedRecommender
import pandas as pd

def main():
    data = pd.read_csv("/home/salwamaatoug/recommender_material/nonpers-assignment/data/ratings.csv")
    del data['timestamp']
    data.columns = ['userID', 'itemID', 'rating']
    num_item = 10
    mean_recom = MeanItemBasedRecommender(num_item, data)
    print(mean_recom.n_highest())

if __name__ == "__main__":
    main()
