import subprocess
import time
import os
import json

# Path to the directory containing ZoKrates programs
# program_directory = "./program"
program_directory = "./programs"
top_directory = "."

# Function to get the size of a file
def get_file_size(file_path):
    return os.path.getsize(file_path)

# Function to measure compilation time
def compile_program(program_path):
    start_time = time.time()
    compile_output = subprocess.run(["zokrates", "compile", "-i", program_path])
    end_time = time.time()
    output_file_path = os.path.join(top_directory, 'out')
    circuit_size = get_file_size(output_file_path)
    return end_time - start_time, circuit_size

# Function to execute the program and measure execution time
def execute_program(program_path):
    # input_path = "./input/bst1_instr.txt"
    start_time = time.time()
    subprocess.run(["zokrates", "compute-witness", "-a", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "1", "120000000000", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "0", "999990000000000", "1", "0", "1", "120000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "120000000000", "1", "237083333333", "1", "137236662431", "1", "45000000000", "1", "480000000000", "1", "270000000000", "1", "46927487", "0", "7371047090", "1", "39616811999", "0", "999990000000000", "1", "2845000000000", "1", "90000000000", "1", "30000000000", "1", "300000000000", "1", "216333076528", "1", "60000000000", "1", "480000000000", "1", "360000000000", "0", "11520696383", "0", "999990000000000", "1", "124899959968", "0", "999990000000000", "1", "900000000000", "1", "120000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "1", "0", "1", "120000000000", "1", "14375000000", "1", "18748105965", "0", "13125000000", "1", "58750000000", "1", "10937500000", "1", "13243043144", "1", "23144633775", "1", "5412112013", "0", "999990000000000", "1", "172500000000", "1", "0", "1", "0", "1", "0", "1", "120000000000", "1", "11250000000", "1", "15539539013", "0", "10000000000", "1", "35000000000", "1", "10000000000", "1", "1349120194", "0", "16114048443", "1", "4485878516", "0", "999990000000000", "1", "135000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "120000000000", "1", "206666666667", "1", "116410975219", "1", "40000000000", "1", "410000000000", "1", "190000000000", "1", "2704624217", "0", "8533157216", "1", "33604953940", "0", "999990000000000", "1", "2480000000000", "1", "0", "1", "0", "1", "120000000000", "1", "9711116667", "1", "772883982", "1", "7750000000", "1", "10516700000", "1", "9900000000", "0", "18014988221", "1", "34374169066", "1", "223112388", "0", "999990000000000", "1", "116533400000", "1", "120000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "100000000000", "1", "6500283200", "1", "4423064851", "1", "684960000", "1", "10000000000", "1", "9694145000", "0", "5319033723", "0", "21158715016", "1", "1398695917", "0", "999990000000000", "1", "65002832000", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "120000000000", "1", "0", "1", "0", "1", "0", "1", "0"])
    return time.time() - start_time

# Function to generate proof and extract proof size and number of constraints
def generate_proof(program_path):
    subprocess.run(["zokrates", "setup"])
    subprocess.run(["zokrates", "export-verifier"])
    start_time = time.time()
    proof_output = subprocess.run(["zokrates", "generate-proof"])
    end_time = time.time()
    # Example of extracting proof size and constraints from the output
    # This depends on the format of the output from ZoKrates
    output_file_path = os.path.join(top_directory, 'proof.json')
    proof_size = get_file_size(output_file_path)
    
    return proof_size

def verify_proof(program_path):
    start_time = time.time()
    subprocess.run(["zokrates", "verify"])
    end_time = time.time()
    
    return end_time - start_time


# Main function to batch test ZoKrates programs
def batch_test_zokrates_programs():
    results = []

    for program in os.listdir(program_directory):
        # Skip hidden files and directories
        if program.startswith('.') or os.path.isdir(os.path.join(program_directory, program)):
            continue

        program_path = os.path.join(program_directory, program)
        compile_time, circuit_size = compile_program(program_path)
        execution_time = execute_program(program_path)
        proof_size = generate_proof(program_path)
        verification_time = verify_proof(program_path)

        results.append({
            "program": program,
            "compile_time": compile_time,
            "circuit_size": circuit_size,
            "execution_time": execution_time,
            "proof_size": proof_size,
            "verification_time": verification_time
        })
        # Write results to a JSON file
        with open(f'zokrates_test_results{program}.json', 'w') as file:
            json.dump(results, file, indent=4)

    # Write results to a JSON file
    with open('zokrates_test_results.json', 'w') as file:
        json.dump(results, file, indent=4)

batch_test_zokrates_programs()