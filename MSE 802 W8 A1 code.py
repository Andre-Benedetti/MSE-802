import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable warnings for insecure requests
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Configuration
my_quokka = 'quokka1'
request_http = 'http://{}.quokkacomputing.com/qsim/qasm'.format(my_quokka)

def run_quantum_tasks():
    # Task 1: 1-bit Coin Flip (H on q[0])
    # Task 2: 2-bit Random Number (H on q[1] and q[2])
    # Uses 3 qubits total to keep the experiments separate in one script
    program = """
    OPENQASM 2.0;
    include "qelib1.inc";
    qreg q[3];
    creg coin[1];
    creg rng[2];
    
    // Coin Flip Logic
    h q[0];
    measure q[0] -> coin[0];
    
    // 2-Bit RNG Logic
    h q[1];
    h q[2];
    measure q[1] -> rng[0];
    measure q[2] -> rng[1];
    """

    data = {
        'script': program,
        'count': 1 
    }

    try:
        result = requests.post(request_http, json=data, verify=False)
        if result.status_code == 200:
            json_obj = json.loads(result.content)
            
            # Extracting results based on the Quokka's nested list structure
            # Quokka returns registers in the order they are declared
            # coin result is at index 0, rng result is at index 1
            coin_bit = json_obj['result']['coin'][0][0]
            rng_bits = json_obj['result']['rng'][0] 
            
            # Convert [0, 1] list to string "01"
            rng_string = "".join(map(str, rng_bits))
            
            coin_result = "Heads" if coin_bit == 0 else "Tails"
            return coin_result, rng_string
        else:
            return None, None
    except Exception as e:
        print(f"Connection Error: {e}")
        return None, None

# Statistics Trackers
stats_coin = {"Heads": 0, "Tails": 0}
stats_rng = {"00": 0, "01": 0, "10": 0, "11": 0}
trials = 100 

print(f"Connecting to {request_http}...")
print(f"Running {trials} Quantum Experiments...\n")

for i in range(trials):
    coin, rng = run_quantum_tasks()
    if coin and rng:
        stats_coin[coin] += 1
        stats_rng[rng] += 1
        print(f"Trial {i+1}: Coin -> {coin} | 2-Bit RNG -> {rng}")

# Final Results Output
print("\n" + "="*35)
print("       FINAL QUANTUM REPORT")
print("="*35)
print("COIN FLIP STATS:")
for key, val in stats_coin.items():
    print(f" - {key}: {val} times")

print("\n2-BIT RANDOM NUMBER STATS:")
for key, val in stats_rng.items():
    print(f" - {key}: {val} times")
print("="*35)