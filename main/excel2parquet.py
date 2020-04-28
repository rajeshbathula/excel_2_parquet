import pandas as pd
import glob
import sys
import uuid
import argparse, os
import xlrd

def read_excel_folder(excel_folder):
    try:
        src_excel_files = glob.glob("{}/*".format(excel_folder))
        if len(src_excel_files) > 0:
            return pd.concat(pd.read_excel(f, index_col=False) for f in src_excel_files)
        else:
            print('No Excel files in input folder, kindly upload and rerun from project folder!')
            sys.exit()
    except xlrd.biffh.XLRDError as e:
        print("kindly place EXCEL files in input folder and try again!")
        sys.exit()

def pd_df(df):
    df['ObservationDate'] = pd.to_datetime(df['ObservationDate']).dt.strftime('%Y-%m-%d %H:%M:%S')
    return df

def to_parquet(input,output):
    df = read_excel_folder(input)
    pq_df = pd_df(df)
    file_name = str(uuid.uuid1())
    os.makedirs(output, exist_ok=True)
    output_file = f'{output}{file_name}.parquet'
    pq_df.to_parquet(output_file,engine='pyarrow', compression= 'snappy')
    print('success!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--input_location', required=False, default="./input/")
    parser.add_argument('--output_location', required=False, default="./output/")
    args = vars(parser.parse_args())
    to_parquet(args['input_location'],args['output_location'])