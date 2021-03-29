import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

def correlations(inpath="data/zipcodes.csv"):
    df = pd.read_csv(inpath)
    results = smf.ols('np.log(mean_property_value) ~ np.log(number_of_trees)', data=df).fit()
    
    with open('plots/log_bestfit.txt', 'w') as f:
        f.write(str(results.summary()))
        print(results.summary())


    df.plot.scatter('number_of_trees', 'mean_property_value')
    space = np.linspace(df['number_of_trees'].min(),df['number_of_trees'].max())
    predictions = results.predict(exog=dict(number_of_trees=space))
    plt.plot(space, predictions, 'r-', label="Best Fit")
    plt.legend()
    plt.title("Number of Trees vs Property Value by Zip Code")
    plt.ylabel("Mean Property Value")
    plt.xlabel("Number of Trees")
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/log_bestfit.png')

if __name__ == "__main__":
    correlations()