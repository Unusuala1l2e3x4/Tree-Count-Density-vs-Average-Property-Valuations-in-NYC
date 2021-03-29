import pandas as pd
import matplotlib.pyplot as plt

def join_zips(trees_path="data/trees_by_zip.csv", property_path="data/property_value_by_zip.csv", species_path = 'data/species_by_zip.csv', outpath="data/zipcodes.csv"):
    trees = pd.read_csv(trees_path)
    properties = pd.read_csv(property_path)
    species = pd.read_csv(species_path)
    
    merged = trees.merge(properties, left_on='zipcode', right_on='ZIP')
    merged = merged.merge(species, left_on='zipcode', right_on='zipcode')
    merged = merged[['zipcode', 'number_of_trees', 'mean'] + list(species.columns)]
    merged = merged.rename(columns = {'mean':'mean_property_value'})

    print(merged.head())
    merged.to_csv(outpath)

    merged.plot('number_of_trees', 'mean_property_value', kind='scatter')
    plt.xscale('log')
    plt.yscale('log')
    plt.title("NYC Tree Density vs Value by Zip Code")
    plt.ylabel("Mean Property Value")
    plt.xlabel("Number of Trees")
    plt.savefig("plots/value_vs_trees.png")

if __name__ == '__main__':
    join_zips()