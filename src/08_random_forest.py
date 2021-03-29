from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt

def species_random_forest(inpath='data/zipcodes.csv'):
    print("Hello!")
    df = pd.read_csv(inpath)
    count_columns = [column for column in df.columns if '_count' in column]

    X = df[count_columns]
    y = df['mean_property_value']
    print(X)
    print(y)

    clf = RandomForestRegressor(random_state=0)
    clf.fit(X,y)
    print("World!")


    importances = pd.DataFrame(dict(name=count_columns, importance=clf.feature_importances_)).sort_values('importance', ascending=False).head(10)
    print(importances)
    plt.bar(importances['name'], importances['importance'])
    plt.xticks(rotation=10)
    plt.xlabel("Species")
    plt.ylabel("Gini Importance")
    plt.show()




if __name__ == '__main__':
    species_random_forest()