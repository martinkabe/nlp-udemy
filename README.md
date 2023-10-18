## Install python virtual environment using conda

https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/

conda create -n venv python=3.9 anaconda

## Switch to virtual environment (using conda)

source activate venv

## Deactivate virtual environment

source deactivate

## Delete a no longer needed virtual environment

conda remove -n venv -all

## Install packages

conda install -n venv pandas numpy gensim nltk

## Packages snapshot

conda install pip

pip freeze > requirements.txt

## Used datasets

jokes.csv -> https://www.kaggle.com/datasets/jiriroz/qa-jokes/
