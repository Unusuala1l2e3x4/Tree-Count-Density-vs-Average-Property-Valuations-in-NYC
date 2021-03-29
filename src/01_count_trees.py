import pandas as pd

def count_trees(inpath="raw/trees.csv", outpath="data/trees_by_zip.csv"):
    df = pd.read_csv(inpath)
    tree_counts = df.groupby('zipcode')['tree_id'].count()
    tree_counts.to_frame(name="number_of_trees").to_csv(outpath)

if __name__ == '__main__':
    count_trees()