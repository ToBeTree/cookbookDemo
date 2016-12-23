import yaml
try:
    with open('device.yaml', encoding='utf-8') as f:
        x = yaml.load(f)
        print(x)
except Exception as e:
    raise e
print(len(x['appium']))