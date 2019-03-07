function run_test() {
    PYTHONPATH=$PYTHONPATH:src python3 $1    
}

run_test test/generate_prompt_test.py
run_test test/transient_verbs_test.py