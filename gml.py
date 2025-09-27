from pathlib import Path
import pandas as pd
import yaml

def get_yaml_files():
    """ 
    Get a list of the yaml files from the gddb data directory.
    """

    current_directory = Path().cwd()/'..'/'gdshowsdb'/'data'/'gdshowsdb'
    yaml_files = [item for item in current_directory.glob('*.yaml')]

    return yaml_files


def create_yaml_file_df(yaml_file):
    dict_list = []

    # Extract the year from the filename
    year = yaml_file.name.split('.')[0]

    with open(yaml_file, "r", encoding="utf-8") as f: 
        data = yaml.safe_load(f)

    for date in data.keys():
        uuid = data[date][':uuid']
        venue = data[date][':venue']
        city = data[date][':city']
        state = data[date][':state']
        country = data[date][':country']

        for set in data[date][':sets']:
            set_uuid = set[':uuid'] 
            for item in set[':songs']:
                song_uuid = item[':uuid']
                name = item[':name']
                segued = item[':segued']
                dict_list.append({'date': date, 
                                'year': year,
                                'uuid': uuid,
                                'venue': venue,
                                'city': city,
                                'state': state,
                                'country': country,
                                'set_uuid': set_uuid,
                                'song_uuid': song_uuid,
                                'name': name,
                                'segued': segued
                                })

    df = pd.DataFrame(dict_list)

    return df, data