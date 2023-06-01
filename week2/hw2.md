# Homework week2

## Q1. Install the package
```
$ mlflow --version
```
=> mlflow, version 2.3.2

## Q2. Download and preprocess the data
```
python preprocess_data.py --raw_data_path ./data --dest_path ./output
```
The size of the saved DictVectorizer file?
=> 153660 byte
=> 154 kB

## Q3. Train a model with autolog
```
$ python train.py
```
=> max_depth = 10

## Run MLflow locally
```
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root file:///home/hirobo/works/mlops-zoomcamp-hw/week2/artifact \
    --host 0.0.0.0
```

## Q4. Tune model hyperparameters
The best validation RMSE => 2.45

## Q5. Promote the best model to the model registry
## Q6. Model metadata
