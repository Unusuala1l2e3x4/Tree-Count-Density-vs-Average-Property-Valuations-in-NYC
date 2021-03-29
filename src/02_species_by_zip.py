import pandas as pd

def species_by_zip(inpath="raw/trees.csv", outpath="data/species_by_zip.csv"):
    df = pd.read_csv(inpath)
    table = pd.pivot_table(df, values='tree_id', index='zipcode', columns='spc_common', aggfunc='count').fillna(0)
    table.columns = [name.lower().replace(' ', '_').replace('\'', '').replace('-','_') + '_count' for name in table.columns]
    table.to_csv(outpath)

if __name__ == '__main__':
    species_by_zip()