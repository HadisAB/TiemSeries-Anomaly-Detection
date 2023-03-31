# TiemSeries-Anomaly-Detection
In this project we are going to find the anomalies in time series radio KPIs (Telecom industry) .

## ADTK Python Library
In this project we have detected anomalies in the behaviour of two time series radio KPIs.<br />
Two below methods have been applied on two different KPIs through 'adtk' library.<br />
you can find the details [here](https://github.com/HadisAB/TiemSeries-Anomaly-Detection/blob/main/AnomalyDetectionGit.py) .

### SeasonalAD
In this method the algorithm will find a periodic behaviour in the time series and find abnormal behaviour.<br />
Firstly, it is better to make your data compatible with the method by applying 'validate_series' on it. Then it is time to fit the model.

<img src=https://github.com/HadisAB/TiemSeries-Anomaly-Detection/blob/main/PayloadAnomaly.png/>

### ThresholdAD
This model needs you to define some thresholds based on your knowledge on the time series behaviour.<br />
It is better to make your data compatible with the method by applying 'validate_series' on it before fitting the model.

<img src=https://github.com/HadisAB/TiemSeries-Anomaly-Detection/blob/main/Thresholdmethod.png/>
