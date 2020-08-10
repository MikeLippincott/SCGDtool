# Solution Cathode Glow Discharge/ASEQ LR1 Box Spectrometer Data Analysis 

## About

Basic Analysis Script with config file to load user preferecnes. With '.txt' file format as the input to script from output of ASEQ LR1 Box Spectrometer.

### Prerequisites    
 
#### Python:    
pandas
matplotlib
configparser
glob
os
re
os.path
pathlib



```
pip install pandas
```
```
pip install matplotlib
```
```
pip install configparser
```
```
pip install glob
```
```
pip install os
```
```
pip install re
```
```
pip install pathlib
```

# Installation & Usage
## Bash
#### Change Directory to path where SCGDtool will be downloaded
```
cd /path/of/choice
```
```
git clone https://github.com/MikeLippincott/SCGD
```
### Edit Config File for use See 'Config File Changes'

Change Direcotry to SCGDtool folder
```
cd SCGDtool
```
```
python script.py
```

 
## Config File changes
Edit the config.ini file for changed output. This script supports up to 10 different concentrions on one plot.
Change the absolute paths to input and output data in the config. Mute and unmute which concentrations to be graphed and shown in the legend by adding or removing '#' in front of c# in the Colours section of config.


## Authors
Programming: Mike Lippincott    
PI: Thomas Spudich, PhD


## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Acknowledgments
Dr. Spudich for support and testing.
