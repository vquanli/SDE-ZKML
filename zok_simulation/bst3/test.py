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
    subprocess.run(["zokrates", "compute-witness", "-a", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "1", "60000000000", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "0", "999990000000000", "1", "0", "1", "60000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "60000000000", "0", "5000000000", "1", "24289915603", "0", "45000000000", "1", "25000000000", "0", "2500000000", "0", "7065078870", "1", "6700660730", "1", "9916316520", "0", "999990000000000", "0", "30000000000", "1", "60000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "60000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "1", "0", "1", "60000000000", "1", "16979166667", "1", "37262616711", "0", "25625000000", "1", "75000000000", "1", "15625000000", "1", "5383005473", "0", "5317769302", "1", "15212399571", "0", "999990000000000", "1", "101875000000", "1", "10000000000", "1", "0", "1", "0", "1", "50000000000", "1", "44000000000", "1", "44777226354", "1", "5000000000", "1", "115000000000", "1", "25000000000", "1", "12597693548", "1", "9017667801", "1", "20024984395", "0", "999990000000000", "1", "220000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "60000000000", "1", "293333333333", "1", "179629247804", "1", "50000000000", "1", "530000000000", "1", "295000000000", "0", "476992579", "0", "11830531555", "1", "73333333333", "0", "999990000000000", "1", "1760000000000", "1", "0", "1", "0", "1", "60000000000", "1", "7077783333", "1", "2140978523", "1", "4350000000", "1", "10516700000", "1", "6916665000", "1", "5634540641", "1", "3855904415", "1", "874050822", "0", "999990000000000", "1", "42466700000", "1", "60000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "60000000000", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "0", "999990000000000", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "60000000000", "1", "0", "1", "0", "1", "0", "1", "0"])
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
    with open('zokrates_test_results.json', 'w') as file:
        json.dump(results, file, indent=4)

batch_test_zokrates_programs()