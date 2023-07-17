import pandas as pd
from datetime import datetime


def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)


def prepare_data(df, categorical):
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    return df


def test_prepare_data():
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),     
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    categorical = ['PULocationID', 'DOLocationID']

    expected_result = [
        {'PULocationID': '-1', 'DOLocationID': '-1', 'tpep_pickup_datetime': dt(1, 2), 'tpep_dropoff_datetime': dt(1, 10), 'duration': 8.0},
        {'PULocationID': '1', 'DOLocationID': '-1', 'tpep_pickup_datetime': dt(1, 2), 'tpep_dropoff_datetime': dt(1, 10), 'duration': 8.0},
        {'PULocationID': '1', 'DOLocationID': '2', 'tpep_pickup_datetime': dt(2, 2), 'tpep_dropoff_datetime': dt(2, 3), 'duration': 1.0}]

    df = prepare_data(df, categorical)
    result = df.to_dict(orient='records')
    
    assert result == expected_result


if __name__ == "__main__":
    test_prepare_data()
