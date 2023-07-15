# Homework week5

## Q1. Refactoring
```
if __name__ == "__main__":
```

## Q2. Installing pytest
=> Both of the above options are correct

## Q3. Writing first unit test
=> 4

## Q4. Mocking S3 with Localstack
=> endpoint-url

```
aws configure --profile localstack
```
```
aws --endpoint-url=http://localhost:4566 s3 mb s3://nyc-duration --profile localstack
```
```
aws --endpoint-url=http://localhost:4566 s3 ls --profile localstack
2023-07-16 01:00:54 nyc-duration
```

## Q5. Creating test data
```
python integration_test.py
```

```
aws s3 ls --endpoint-url=http://localhost:4566 s3://nyc-duration/in/yellow/2
022-01.parquet --profile localstack
```
=> 3667

## Q6. Finish the integration test
predicted sum duration: 31.507450372727607
=> 31.51

