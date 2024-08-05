import os

def analyze_smart_contracts(contract_path):

    os.system(f'slither {contract_path} --checklist')
contract_path = 'path/to/your/smart_contract.sol'

analyze_smart_contracts(contract_path)
