# SPEIS-analysis
Jupyter notebook leveraging impedance.py to simplify the batch analysis of staircase potential electrochemical impedance spectroscopy (SPEIS) data. Using the first cell, the filename of the mpt file located in the same directory as the notebook can be specified. Further parameters can be set using the input prompts in the notebook. After completion of the fitting, a subdirectory with the same filename as the MPT file will be created. The fitting result and current state of the notebook get saved as .xlsx and .html files, respectively.

## Dependencies
The notebook has been developed using the following Jupyter notebook environment:
* Python (3.8.8)
* impedance.py (1.2.2)
* NumPy (1.19.2)
* Matplotlib (3.3.4)
* Pandas (1.2.4)
* IPython (7.22.0)
