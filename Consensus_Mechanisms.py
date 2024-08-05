class Network:
    def __init__(self, consensus_algorithm, properties):
        self.consensus_algorithm = consensus_algorithm
        self.properties = properties

def analyze_pow_consensus(properties):
    vulnerabilities = []
    if properties.get('mining_power_distribution', {}).get('centralized', False):
        vulnerabilities.append('Mining power is highly centralized, increasing risk of 51% attacks.')
   
    if properties.get('difficulty_adjustment_algorithm', '') not in ['DGW', 'KGW']:
        vulnerabilities.append('Difficulty adjustment algorithm may be vulnerable to manipulation.')

    return vulnerabilities

def analyze_pos_consensus(properties):
    vulnerabilities = []
 
    if properties.get('staking_mechanism', '') == 'weak':
        vulnerabilities.append('Staking mechanism is weak, increasing risk of "nothing at stake" problem.')
    
    if properties.get('slashing_conditions', '') == 'lenient':
        vulnerabilities.append('Slashing conditions are too lenient, reducing penalties for misbehavior.')

    return vulnerabilities

def analyze_consensus_mechanism(network):
    vulnerabilities = []

    if network.consensus_algorithm == 'PoW':
        vulnerabilities.extend(analyze_pow_consensus(network.properties))
    elif network.consensus_algorithm == 'PoS':
        vulnerabilities.extend(analyze_pos_consensus(network.properties))
    else:
        vulnerabilities.append('Unknown consensus algorithm. Manual review required.')

    return vulnerabilities

network_pow = Network(
    consensus_algorithm='PoW',
    properties={
        'mining_power_distribution': {'centralized': True},
        'difficulty_adjustment_algorithm': 'Simple'
    }
)

network_pos = Network(
    consensus_algorithm='PoS',
    properties={
        'staking_mechanism': 'weak',
        'slashing_conditions': 'lenient'
    }
)

print("Analyzing PoW Consensus Mechanism:")
vulnerabilities_pow = analyze_consensus_mechanism(network_pow)
for v in vulnerabilities_pow:
    print(v)

print("\nAnalyzing PoS Consensus Mechanism:")
vulnerabilities_pos = analyze_consensus_mechanism(network_pos)
for v in vulnerabilities_pos:
    print(v)
