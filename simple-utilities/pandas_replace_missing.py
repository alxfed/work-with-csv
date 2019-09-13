# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np


def main():
    """
    :return: 
    """
    df = pd.read_csv('FILE_PATH')
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)
    # or
    # ? df.isin([np.inf, -np.inf, np.nan]).any()
    return


if __name__ == '__main__':
    main()
    print('main - done')