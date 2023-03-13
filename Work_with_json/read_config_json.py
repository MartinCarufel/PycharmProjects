import json

config_path = r"config2.json"

with open(config_path) as config_file:
    config = json.load(config_file)
    config1 = config['first block']
    config2 = config['second block']

BLOCK1_KEY1 = config1['Key1']
BLOCK1_KEY2 = config1['Key2']

print("Block 1: {}, {}".format(BLOCK1_KEY1, BLOCK1_KEY2))


BLOCK2_KEY1 = config2['Block2 key 1']
BLOCK2_KEY2 = config2['Block2 key 2']
print("Block 2: {}, {}".format(BLOCK2_KEY1, BLOCK2_KEY2))