function run_test() {
    PYTHONPATH=$PYTHONPATH:src python3 $1    
}

set -e

run_test test/generate_prompt_test.py
run_test test/software_pidgin_test.py
run_test test/verb_test.py

set +e

GREEN='\033[0;32m'
NC='\033[0m' # No Color
echo -e "\n${GREEN}=== All tests passed ===${NC}\n"