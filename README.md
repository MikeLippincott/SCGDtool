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
### Bash
```
cd #/path/of/choice
```
```
git clone github.com/MikeLippincott/SCGD
```
```
cd SCGD
```
```
python script.py
```

 
## Running the tests
Edit the config.ini file for changed output. This script supports up to 10 different concentrions on one plot.
Change the absolute paths to input and output data in the config. Mute and unmute which concentrations to be graphed and shown in the legend by adding or removing '#' in front of c# in the Colours section of config.


## Authors
Programming: Mike Lippincott    
PI: Thomas Spudich, PhD


## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Acknowledgments
Dr. Spudich for support and testing.
