import yaml

with open('config.yaml', 'r+') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    data['related_hosts']['network'] = {'host': 'google.com', 'port': 8000}
    yaml_file.seek(0)
    yaml.dump(data, yaml_file)
