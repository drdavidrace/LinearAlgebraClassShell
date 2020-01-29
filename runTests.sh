#!/usr/bin/env bash
echo "Running the tests"
tests=("read_config_la")
test_dir="./Test"
for t in "${tests[@]}";
do
    pushd .
        cd ${test_dir}
        python -m unittest ${t}
    popd
done