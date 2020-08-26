import yaml


with open("../../data/test_calculator_data.yml", 'r') as f:
    data = yaml.safe_load(f)
    adddatas = data['add'].values()
    addids = data['add'].keys()
    subdatas = data['sub'].values()
    subids = data['sub'].keys()
    muldatas = data['mul'].values()
    mulids = data['mul'].keys()
    divdatas = data['div'].values()
    divids = data['div'].keys()

