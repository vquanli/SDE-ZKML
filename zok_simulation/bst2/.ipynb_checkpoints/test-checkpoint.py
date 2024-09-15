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
    subprocess.run(["zokrates", "compute-witness", "-a", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "1", "30000000000", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "0", "999990000000000", "1", "0", "0", "999990000000000", "1", "0", "1", "30000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "30000000000", "1", "75000000000", "1", "5000000000", "1", "70000000000", "1", "80000000000", "1", "75000000000", "1", "0", "0", "999990000000000", "1", "2886751346", "0", "999990000000000", "1", "225000000000", "1", "30000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "30000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "0", "1", "0", "1", "30000000000", "1", "38958333333", "1", "18480705028", "1", "18750000000", "1", "55000000000", "1", "43125000000", "0", "9629985893", "0", "999990000000000", "1", "10669840023", "0", "999990000000000", "1", "116875000000", "1", "0", "1", "0", "1", "0", "1", "30000000000", "0", "36666666667", "1", "7637626158", "0", "45000000000", "0", "30000000000", "0", "35000000000", "0", "9352195296", "0", "999990000000000", "1", "4409585518", "0", "999990000000000", "0", "110000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "30000000000", "1", "526666666667", "1", "51316014394", "1", "470000000000", "1", "570000000000", "1", "540000000000", "0", "10902905798", "0", "999990000000000", "1", "29627314724", "0", "999990000000000", "1", "1580000000000", "1", "0", "1", "0", "1", "30000000000", "1", "8072223333", "1", "250188966", "1", "7783330000", "1", "8216670000", "1", "8216670000", "0", "17320508076", "0", "999990000000000", "1", "144446667", "0", "999990000000000", "1", "24216670000", "1", "30000000000", "1", "0", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "0", "999990000000000", "1", "0", "1", "30000000000", "1", "734548333", "1", "494164088", "1", "398812000", "1", "1301990000", "1", "502843000", "1", "16460937501", "0", "999990000000000", "1", "285305769", "0", "999990000000000", "1", "2203645000", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "30000000000", "1", "0", "1", "0", "1", "0", "1", "0"])
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