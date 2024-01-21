import numpy as np
import pandas as pd


def cal_topsis_score(df, w, i, out_file):
    df = df.select_dtypes(np.number)
    df.to_csv(out_file, index=False)
