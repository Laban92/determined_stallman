- To Install :

Download Files:
https://www.dropbox.com/sh/bipyn15zq9h0jap/AADMfGTZr4b61F7BJmjRtWOEa?dl=0

First install Anaconda:
```
https://docs.anaconda.com/anaconda/install/
```
Then download my environment file (environment.yml) and install it by typing in the terminal:

```
conda env create -f environment.yml
```
 

- To Reproduce Results :

First run data_wrangling.py to process the datasets and make one big filtered dataset.

Then, run train_model.py to train the model on the processed dataset. (trained model weights are included)

Finally run Initiate.py to evaluate a sample dataset and calculate some metrics.
