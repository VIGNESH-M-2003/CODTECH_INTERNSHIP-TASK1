import socket
def analyze_network_infrastructure(nodes):
    vulnerabilities = []
    for node in nodes:
        try:
            socket.create_connection((node['ip'], node['port']), timeout=5)
        except Exception as e:
            vulnerabilities.append(f"Node {node['ip']}:{node['port']} is unreachable or misconfigured. Error: {e}")
    return vulnerabilities
nodes = [
    {'ip': '192.168.1.1', 'port': 30303},
    {'ip': '192.168.1.2', 'port': 30303},
]
vulnerabilities = analyze_network_infrastructure(nodes)
for v in vulnerabilities:
    print(v)
