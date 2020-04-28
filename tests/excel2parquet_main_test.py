import pandas as pd
import os,unittest
from pandas.util.testing import assert_frame_equal
from main.excel2parquet import *
from main.get_max_temp_rec import *

class TestStart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        raw_file_path = os.path.join(THIS_DIR, './resources/weather.xlsx')
        cls.raw_df = pd.read_excel(raw_file_path, index_col=False)
        parquet_file_path = os.path.join(THIS_DIR, './resources/output.parquet')
        cls.dst_df = pd.read_parquet(parquet_file_path, engine='pyarrow')
        csv_file_path = os.path.join(THIS_DIR, './resources/pd_df.csv')
        cls.pd_df = pd.read_csv(csv_file_path,index_col=0)

    def test_df_load_pd_df(self):
        result = pd_df(self.raw_df)
        expected = self.pd_df
        assert_frame_equal(result,expected)

    def test_get_max_tmp_rec(self):
        result = get_max_temp_rec(self.raw_df)
        self.assertEqual(result.ScreenTemperature.values[0] , float(13.0))
        self.assertEqual(result.Date.values[0], '2016-02-01')
        self.assertEqual(result.Region.values[0], 'Wales')

if __name__ == '__main__':
    unittest.main()