"""
Functions to load specific datasets.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

from tsdb.data_loading_funcs.beijing_multisite_air_quality import load_beijing_air_quality
from tsdb.data_loading_funcs.electricity_load_diagrams import load_electricity
from tsdb.data_loading_funcs.physionet_2012 import load_physionet2012
from tsdb.data_loading_funcs.physionet_2019 import load_physionet2019
from tsdb.data_loading_funcs.ucr_uea_datasets import load_ucr_uea_dataset
from tsdb.data_loading_funcs.vessel_ais import load_ais
