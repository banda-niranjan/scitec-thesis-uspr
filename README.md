# Master Thesis Files

**Here consists non-confidential codes and files related to my Master's Thesis.**

The below command is to be run only once. Since, currently a virtual environment named ust has been already created, DO NOT run this command.

```sh
% To create a virtual environment
python3 -m env nameoftheenvironment

% To activate the virtual environment enter the following
source ust/bin/activate

% To install a package such as pyvisa in the terminal below

pip3 install pyvisa

% To run the current script, open terminal and enter the following command

python3 ./scpi_rigol.py

```

condaenvultra.yaml contains all the necessary libraries to be installed for automating Oscilloscope, function generator, voltage generator and the prototype for signal acquisition and signal processing.
