# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:07:59 2023

@author: hadis.ab
"""

import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from datetime import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf, pacf
import numpy as np
import warnings
warnings.filterwarnings("ignore")


data_add=r"D:\Reports_Projects\DS_ML_Tavanafarin_Training\proj02\Input.xlsx"
data=pd.read_excel(data_add, thousands=',' ,header=1)
data=data[data['SITE']=='T4602X']
#data=data[data['SITE']=='T6849X']
del data['SITE']

#kpi='2G_DCR_IR(%)'
kpi='4G_Payload_PDCP_DL_Mbyte_IR(MB)'
#kpi_avail='2G_TCH_AVAILABILITY_IR(%)'
data=data[['Time', kpi]]
data=data[data['Time']>='2022-12-01']
data.isna().sum()
data=data.ffill(axis = 0)
data.isna().sum()


data['Time']=pd.to_datetime(data['Time'])

import datetime
#data['Day'] = pd.date_range("2022-01-01", periods=len(data['Time']), freq="D")
#data=data.rename(columns={'Time':'Day'})
from adtk.data import validate_series
data=data.set_index('Time')

#data=data[kpi]
data = validate_series(data)
print(data)
data.describe()

from adtk.visualization import plot
plot(data)
plt.show()

#Anomaly detection
#from adtk.data import resample
from adtk.detector import SeasonalAD
seasonal_vol = SeasonalAD()
anomalies = seasonal_vol.fit_detect(data[kpi])
anomalies.value_counts()
plot(data[kpi], anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
plt.savefig(r'D:\Reports_Projects\DS_ML_Tavanafarin_Training\proj02\PayloadAnomaly.png')
plt.show()
## Exception: Could not find significant seasonality.

#---------------Threshold method
from adtk.detector import ThresholdAD
threshold_val = ThresholdAD(high=4, low=-1)
anomalies_thresh = threshold_val.detect(data[kpi])
anomalies_thresh.value_counts()
from adtk.visualization import plot
plot(data[kpi], anomaly=anomalies_thresh, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='black')

plt.savefig(r'D:\Reports_Projects\DS_ML_Tavanafarin_Training\proj02\Thresholdmethod.png')
plt.show()
#-----------

