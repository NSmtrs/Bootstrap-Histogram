import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os #computer operating system



os.chdir("C:\\Users\\nsmet\OneDrive\\Documents\\Custom Office Templates")
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]

n = len(variable)

n_boot = 10_000

stat = "mean"

boot_stat = []

for i in range(n_boot):
    boot_sample = dat.sample(26, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    
        
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
        
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
    else:
        raise TypeError("Wrong statistic name")

boot_df = pd.DataFrame({'x': boot_stat})

(
 ggplot(boot_df, aes(x='x'))+
 geom_histogram()

    )
