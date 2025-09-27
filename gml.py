from pathlib import Path
import pandas as pd
import yaml




current_directory = Path().cwd()/'..'/'gdshowsdb'/'data'/'gdshowsdb'
    
yaml_files = [item for item in current_directory.glob('*.yaml')]


with open(yaml_files[0], "r", encoding="utf-8") as f: 
    data = yaml.safe_load(f)

print('*** yaml_file: ',yaml_files[0])


df = pd.json_normalize(data)

print(df.head(2))