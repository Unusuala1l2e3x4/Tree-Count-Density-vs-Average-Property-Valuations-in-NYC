import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

def correlations(inpath="data/zipcodes.csv"):
    df = pd.read_csv(inpath)
    count_columns = [column for column in df.columns if '_count' in column]
    results = smf.ols('mean_property_value ~ ' + " + ".join(count_columns), data=df).fit()

    with open('plots/species_linear.txt', 'w') as f:
        f.write(str(results.summary()))
        print(results.summary())
        


if __name__ == "__main__":
    correlations()