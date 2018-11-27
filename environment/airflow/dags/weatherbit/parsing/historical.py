import pandas as pd
import ast
import sys


def parse_weather(templates_dict, **kwargs):
    source = templates_dict.get('source')
    target = templates_dict.get('target')

    df = pd.read_csv(source)
    parsed_records = [ast.literal_eval(x) for x in df.weather]
    # Update records with timestamp
    for i, record in enumerate(parsed_records):
        record['timestamp'] = df.timestamp_utc[i]
    df = pd.DataFrame.from_records(parsed_records)
    df.to_csv(target, index=False)


def parse_temperature(templates_dict, **kwargs):
    source = templates_dict.get('source')
    target = templates_dict.get('target')

    df = pd.read_csv(source)[['temp', 'timestamp_utc']]
    df.to_csv(target, index=False)