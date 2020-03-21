import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind


class Model:
    def __init__(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2
        self.avg_total = 190768.7115

    def ttest1(self):
        df = pd.DataFrame(pd.read_csv(self.filename1)).iloc[1:31, 1]
        stat, p = ttest_1samp(df, 190768.7)
        return round(p, 5)

    def ttest2(self):
        df1 = pd.DataFrame(pd.read_csv(self.filename1)).iloc[1:31, 1]
        df2 = pd.DataFrame(pd.read_csv(self.filename2)).iloc[1:31, 1]
        stat, p = ttest_ind(df1, df2, equal_var=False)
        return round(p, 5)
