const zokrates = require('zokrates-js');
const fs = require('fs');
const path = require('path');
const { performance } = require('perf_hooks');

// Path to the directory containing ZoKrates programs
const programDirectory = "./test_bst1_10.zok";

// Function to measure compilation time
async function compileProgram(programPath) {
    const source = fs.readFileSync(programPath, 'utf8');
    let startTime = performance.now();
    const artifacts = zokrates.compile(source);
    let compileTime = performance.now() - startTime;
    return { artifacts, compileTime };
}

// Function to execute the program and measure execution time
async function executeProgram(artifacts, programPath) {
    let startTime = performance.now();
    const { witness } = zokrates.computeWitness(artifacts, [{   "sgn": true,   "v": "10" }, {   "sgn": true,   "v": "10" }]);
    let executionTime = performance.now() - startTime;
    return { witness, executionTime };
}

// Function to generate proof and extract proof size and number of constraints
async function generateProofAndExtractMetrics(artifacts) {
    const keypair = zokrates.setup(artifacts.program);
    const proof = zokrates.generateProof(artifacts.program, artifacts.witness, keypair.pk);

    // Example of extracting proof size and constraints
    const proofSize = JSON.stringify(proof).length;
    const numConstraints = artifacts.program.length; // Modify this based on how you define number of constraints

    return { proofSize, numConstraints };
}

// Main function to batch test ZoKrates programs
async function batchTestZokratesPrograms() {
    let results = [];

    for (const program of fs.readdirSync(programDirectory)) {
        const programPath = path.join(programDirectory, program);
        const { artifacts, compileTime } = await compileProgram(programPath);
        const { witness, executionTime } = await executeProgram(artifacts, programPath);
        const { proofSize, numConstraints } = await generateProofAndExtractMetrics(artifacts);

        results.push({
            program,
            compileTime,
            executionTime,
            proofSize,
            numConstraints
        });
    }

    // Write results to a JSON file
    fs.writeFileSync('zokrates_test_results.json', JSON.stringify(results, null, 4));
}

batchTestZokratesPrograms();
