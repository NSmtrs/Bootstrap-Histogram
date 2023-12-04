import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os  # computer operating system
import numpy as np

class Mileage():
    
    def __init__(self, n, n_boot, stat, dat=None):
        self.n = n
        self.n_boot = n_boot
        self.stat = stat
        self.data = dat
        self.boot_stat = []
    
    def load_data(self, dat):
        self.data = dat
        
    def RunSim(self):
        for _ in range(self.n):
            boot_sample = self.data.sample(26, replace=True)
            
            if self.stat == "median":
                self.boot_stat.append(float(boot_sample.median()))
            
            elif self.stat == "mean":
                self.boot_stat.append(float(boot_sample.mean()))
                
            elif self.stat == "std dev":
                self.boot_stat.append(float(boot_sample.std()))
                
            else:
                raise TypeError("Wrong statistic name")
        
        return self.boot_stat        
        
    def ClearSim(self):
        self.boot_stat = []
    
    def Plot_Data(self):
        boot_df = pd.DataFrame({'x': self.boot_stat})
        (
         ggplot(boot_df, aes(x='x')) +
         geom_histogram(binwidth=1)  # Adjust binwidth as needed
        )
    
    def Conf_Int(self, level=95):
        lb = (100 - level) / 2
        ub = (100 - lb)
        if len(self.boot_stat) > 0:
            return np.percentile(self.boot_stat, [lb, ub])
        else:
            print("Not enough data for a valid answer")

# Example usage:
os.chdir("C:\\Users\\nsmet\\OneDrive\\Documents\\Custom Office Templates")
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat = dat["Combined Mileage (mpg)"]

n = len(dat)
n_boot = 10_000
stat = "mean"

mileage_simulator = Mileage(n, n_boot, stat, dat)
mileage_simulator.RunSim()
mileage_simulator.Plot_Data()
confidence_interval = mileage_simulator.Conf_Int()
print("Confidence Interval:", confidence_interval)
