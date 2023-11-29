import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os #computer operating system

class Mileage():
    
    def __innit__(self, n, n_boot, stat, dat = None):
        self.n = n
        self.n_boot = n_boot
        self.stat = stat
        self.data = dat
        self.boot_stat = []
    
    def load_data(self, dat):
        self.data = dat
        
    def RunSim(self):
        for i in range(self.n_boot):
            boot_sample = self.dat.sample(26, replace = True)
            
            if self.stat == "median":
                eslf.boot_stat.append(float(boot_sample.median()))
            
                
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
         ggplot(boot_df, aes(x='x'))+
         geom_histogram()

            )



os.chdir("C:\\Users\\nsmet\OneDrive\\Documents\\Custom Office Templates")
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]

n = len(dat)

n_boot = 10_000

stat = "mean"

