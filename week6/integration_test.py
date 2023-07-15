import subprocess
import pandas as pd
from tests.test_batch import dt


def get_storage_options():
    return {
        'client_kwargs': {'endpoint_url': 'http://localhost:4566'}
    }


def get_input_path(year, month):
    return f"s3://nyc-duration/in/yellow/{year:04d}-{month:02d}.parquet"


def get_output_path(year, month):
    return f"s3://nyc-duration/out/yellow/{year:04d}-{month:02d}.parquet"


def prepare_test_data():
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]

    columns = ['PULocationID', 'DOLocationID',
               'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df_input = pd.DataFrame(data, columns=columns)

    input_file = get_input_path(2022, 1)

    df_input.to_parquet(
        input_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=get_storage_options()
    )


def main():

    completed_process = subprocess.run(['python', 'batch.py', '2022', '1'],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       text=True)

    if completed_process.stdout:
        print(f'stdout: {completed_process.stdout}')

    if completed_process.stderr:
        print(f'stderr: {completed_process.stderr}')

    result_file = get_output_path(2022, 1)

    df = pd.read_parquet(result_file, storage_options=get_storage_options())

    assert round(df['predicted_duration'].sum(), 2) == 31.51


if __name__ == "__main__":
    main()
