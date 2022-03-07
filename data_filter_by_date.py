import pandas as pd

def date_filter(date):
    features = pd.read_csv('Data/large_twitch_features.csv')
    edges = pd.read_csv('Data/large_twitch_edges.csv')
    valid_features = features[features["updated_at"] >= date]
    valid_features = valid_features[valid_features["created_at"] <= date]
    valid_edges = edges[edges["numeric_id_1"].isin(list(valid_features["numeric_id"]))]
    valid_edges = valid_edges[valid_edges["numeric_id_2"].isin(list(valid_features["numeric_id"]))]
    return valid_edges, valid_features

date = '2017-11-21'
filtered_edges, filtered_features = date_filter(date)