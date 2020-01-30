#!/usr/bin/env bash
echo "Running the tests"
tests=("test_read_config_init" "test_read_matrix_data")
test_dir="./Test"
for t in "${tests[@]}";
do
    pushd .
        cd ${test_dir}
        python -m unittest ${t}
    popd
done