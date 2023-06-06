# Homework week3

## Q1. Human-readable name
=> @task(retries=3, retry_delay_seconds=2, name="Read taxi data")

## Q2. Cron
=> 0 9 3 * *

## Q3. RMSE
(Assume that the pool `mlops-zoomcamp-process` with type `process` is created and deployment.yaml is ready.)

Push the code to GitHub and run this from the project root directory:
```
prefect deploy --all
```
=> Deployment `main-flow/week3-q3-q4` created with pool `mlops-zoomcamp-process`

Start the worker:
```
prefect worker start --pool 'mlops-zoomcamp-process'
```

Run the flow with custom parameters
```
{
  "train_path": "week3/data/green_tripdata_2023-01.parquet",
  "val_path": "week3/data/green_tripdata_2023-02.parquet"
}
```
=> 5.19331

## Q4. RMSE (Markdown Artifact)
Same as the Q4, run the flow with custom parameters
```
{
  "train_path": "week3/data/green_tripdata_2023-02.parquet",
  "val_path": "week3/data/green_tripdata_2023-03.parquet"
}
```

And run the flow and check the artifact:
=> 5.37

## Q5. Emails
=> email_send_message

## Q6. Prefect Cloud
=> Actions


