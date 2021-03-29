import pandas as pd

def count_trees(inpath="../raw/trees.csv", inpath2 = "../raw/avroll.csv", outpath="../data/properties.csv"):
	#trees_dataframe = pd.read_csv(inpath)
	properties_dataframe = pd.read_csv(inpath2)
	properties_dataframe["STADDR"] = properties_dataframe["STADDR"].astype(str)
	properties_dataframe["Street"] = [" ".join(street_num.split(" ")[-2:]) for street_num in properties_dataframe["STADDR"].to_list()]
	properties_groupby_street = properties_dataframe.groupby("Street")['FULLVAL'].mean()
	properties_groupby_street.to_csv(outpath)
	print(properties_groupby_street)
	#print(properties_dataframe["Street"])
if __name__ == '__main__':
	count_trees()