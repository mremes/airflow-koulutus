import pandas as pd
import requests

HOURLY_DATA_URL = 'https://api.weatherbit.io/v2.0/history/hourly'


def fetch_hourly_data_adapter(api_key, city, templates_dict, **kwargs):
    start_date = templates_dict.get('start_date')
    end_date = templates_dict.get('end_date')
    target = templates_dict.get('target')

    if not start_date:
        raise ValueError("Argument 'start' must be provided.")
    if not end_date:
        raise ValueError("Argument 'end_date' must be provided.")
    if not target:
        raise ValueError("Argument 'target' must be provided.")

    return fetch_hourly_data(api_key, city, start_date, end_date, target)


def fetch_hourly_data(api_key, city, start_date, end_date, target):
    params = dict(city=city,
                  start_date=start_date,
                  end_date=end_date,
                  key=api_key)
    
    res = requests.get(HOURLY_DATA_URL,
                       params=params)

    if res.status_code != 200:
        raise ValueError('API fetch was not successful.')

    data = res.json()['data']

    df = pd.DataFrame.from_records(data)
    df.to_csv(target)
