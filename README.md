# How Powerful are Graph Neural Networks?

This repository is the replication of PyTorch implementation of the experiments in the following paper: 

Keyulu Xu*, Weihua Hu*, Jure Leskovec, Stefanie Jegelka. How Powerful are Graph Neural Networks? ICLR 2019. 

[arXiv](https://arxiv.org/abs/1810.00826) [OpenReview](https://openreview.net/forum?id=ryGs6iA5Km) 



## Installation
Install PyTorch following the instuctions on the [official website] (https://pytorch.org/). The code has been tested over PyTorch 0.4.1 and 1.0.0 versions.

The experiment is tested under Linux Environment

Create a conda virtual environment first

```
conda create --name GNN python=3.7
```

install the Pytorch 1.0.0 version

```
conda install pytorch==1.0.0 torchvision==0.2.1 cuda100 -c pytorch
```


Then install the other dependencies.

```
pip install -r requirements.txt
```

## Test run
Unzip the dataset file
```
unzip dataset.zip
```

and run

```
python main.py
```

The default parameters are not the best performing-hyper-parameters used to reproduce our results in the paper. Hyper-parameters need to be specified through the commandline arguments. Please refer to our paper for the details of how we set the hyper-parameters. For instance, for the COLLAB and IMDB datasets, you need to add `--degree_as_tag` so that the node degrees are used for input node features.

To learn hyper-parameters to be specified, please type
```
python main.py --help
```

### Generate Experiment Plot

first run experiments and store the results in "file A".

Use graph.py to generate the plot.

See graph.py for more detailed explaination.



## Cross-validation strategy in the paper
The cross-validation in our paper only uses training and validation sets (no test set) due to small dataset size. Specifically, after obtaining 10 validation curves corresponding to 10 folds, we first took average of validation curves across the 10 folds (thus, we obtain an averaged validation curve), and then selected a single epoch that achieved the maximum averaged validation accuracy. Finally, the standard devision over the 10 folds was computed at the selected epoch. 

