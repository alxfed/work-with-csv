# -*- coding: utf-8 -*-
"""ingest csv file (even if there are gaps) and format the dates into a unix timestamp like format
"""
import pandas as pd
from numpy import nan


def dateparse(x):
    if x is nan:
        return None
    else:
        return pd.datetime.strptime(x, '%m/%d/%Y')


def main():
    """
    :return: 
    """
    input_file_path = '/home/alxfed/Downloads/Building_Permits.csv'
    output_file_path = '/home/alxfed/Downloads/Transformed_Building_Permits.csv'

    ffile = pd.read_csv(input_file_path,
                        parse_dates=['APPLICATION_START_DATE','ISSUE_DATE', ],
                        date_parser=dateparse,
                        dtype=object)
    ffile.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')