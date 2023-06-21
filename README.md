# SMEFTsimFeyn
Draw Feynman diagrams for SMEFTsim models 

```
git clone --recursive git@github.com:GiacomoBoldrini/SMEFTsimFeyn.git
```

Usage:

```
usage: run.py [-h] -m MODEL -o OUTPUT -op OPERATORS [OPERATORS ...]
              [-np NPROC]

Command line parser to plot feynman diagrams from SMEFTsim models

optional arguments:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        The SMEFTsim relative/absolute path to the UFO folder
                        you want to use
  -o OUTPUT, --output OUTPUT
                        The output folder where you want to save plots
  -op OPERATORS [OPERATORS ...], --operators OPERATORS [OPERATORS ...]
                        The operators you want to plot
  -np NPROC, --nproc NPROC
                        Number of process for multiprocessing
```


An example:

```
python run.py -m SMEFTsim/UFO_models/SMEFTsim_topU3l_MwScheme_UFO -op cW cHW cHWB -o plot_folder --nproc 8
```
