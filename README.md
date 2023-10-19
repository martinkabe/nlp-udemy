## Install python virtual environment using conda

https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/

conda create -n hface python=3.10 anaconda

## Switch to virtual environment (using conda)

conda activate venv

conda activate hface

## Deactivate virtual environment

conda deactivate

## Delete a no longer needed virtual environment

conda remove -n hface --all

## Install packages

conda install -n venv pandas gensim nltk

<!-- for transformers pipeline - this requires older version of numpy -->

<!-- conda remove -n venv numpy -->

conda install -n venv numpy==1.19.5

conda install -n hface -c huggingface transformers

conda install -n hface -c conda-forge python-dotenv

conda install -n hface -c conda-forge tensorflow

conda install -n venv -c conda-forge transformers

conda install -n venv protobuf

conda install -n venv -c conda-forge accelerate

## Packages snapshot

conda install pip

pip freeze > requirements.txt

## Used datasets

jokes.csv -> https://www.kaggle.com/datasets/jiriroz/qa-jokes/
