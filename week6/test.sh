export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export S3_ENDPOINT_URL=http://localhost:4566
export INPUT_FILE_PATTERN=s3://nyc-duration/in/yellow/{year:04d}-{month:02d}.parquet
export OUTPUT_FILE_PATTERN=s3://nyc-duration/out/yellow/{year:04d}-{month:02d}.parquet

pytest tests

python integration_test.py
