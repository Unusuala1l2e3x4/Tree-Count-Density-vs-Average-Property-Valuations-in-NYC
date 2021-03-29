import pandas as pd
import matplotlib.pyplot as plt


def average_property_value(inpath="raw/avroll.csv", outpath="data/property_value_by_zip.csv", drop_less_than = 50):
    df = pd.read_csv(inpath)
    df = df.dropna(subset=['ZIP','FULLVAL'])
    df["ZIP"] = df["ZIP"].astype(int)
    tree_counts = df.groupby('ZIP')['FULLVAL'].agg(['mean','median', 'min', 'max', 'count'])
    tree_counts = tree_counts[tree_counts['count'] >= drop_less_than]
    tree_counts.to_csv(outpath)

    tree_counts[tree_counts['mean'] < 4.9e6]['mean'].hist(bins=30)
    plt.xlabel("Mean Property Value")
    plt.ylabel("Number of Zipcodes")
    plt.title("Mean Property Value Distribution")
    plt.savefig("plots/mean_property_value_distribution.png")

if __name__ == '__main__':
    average_property_value()