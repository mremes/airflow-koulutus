import pandas as pd
import ast
import sys


def parse_weather_adapter(templates_dict, **kwargs):
    source = templates_dict.get('source')
    target = templates_dict.get('target')
    return parse_weather(source, target)


def parse_weather(source, target):
    df = pd.read_csv(source)
    parsed_records = [ast.literal_eval(x) for x in df.weather]
    # Update records with timestamp
    for i, record in enumerate(parsed_records):
        record['timestamp'] = df.timestamp_utc[i]
    df = pd.DataFrame.from_records(parsed_records)
    df.to_csv(target, index=False)


def parse_temperature_adapter(templates_dict, **kwargs):
    source = templates_dict.get('source')
    target = templates_dict.get('target')
    return parse_temperature(source, target)


def parse_temperature(source, target):
    df = pd.read_csv(source)[['temp', 'timestamp_utc']]
    df.to_csv(target, index=False)
