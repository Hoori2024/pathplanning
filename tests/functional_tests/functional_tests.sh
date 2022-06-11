#!/bin/bash

BOLD="\033[1m"
UNBOLD="\033[0m"
OK="\x1b[32;01m"
UNOK="\x1b[0m"
KO="\x1b[31;01m"
UNKO="\x1b[0m"

TITLEOK="$OK""$BOLD"
UNTITLEOK="$UNOK""$UNBOLD"
TITLEKO="$KO""$BOLD"
UNTITLEKO="$UNKO""$UNBOLD"

nbTestsOK=0
nbTestsKO=0


script_dir=`dirname -- "$0"`

expected_outputs_dir=/expected_outputs
inputs_dir=/inputs

log_path="$script_dir/logs"


function testWithFiles() {
    testname=$1

    python3 ./src/parcellisation.py "$script_dir/$inputs_dir/$testname" > "$log_path"
    result=$(cat $log_path)
    exitValue=$?

    expected=$(cat $script_dir/$expected_outputs_dir/$testname)
    diff=$(diff -y  $log_path $script_dir/$expected_outputs_dir/$testname)

    if [ $exitValue = 0 ];
        then if [[ "$result" == "$expected" ]];
            then nbTestsOK=$((nbTestsOK + 1))
                echo -e "$TITLEOK""\n---------- $1 ----------\n""$UNTITLEOK"
        else
            nbTestsKO=$((nbTestsKO + 1))
            echo -e "$TITLEKO""\n---------- $1 ----------\n""$UNTITLEKO"
            echo -e "$diff"
        fi
    else
        nbTestsKO=$((nbTestsKO + 1))
        echo -e "$TITLEKO""\n---------- $1 ----------\n""$UNTITLEKO"
        echo -e "\t$BOLD""Exited with value $exitValue""$UNBOLD"
    fi
}

# function launchTestsErrorManagement() {

#     input_files=`ls $script_dir/$inputs_dir`

#     for filename in $input_files
#     do
#         testWithFiles $filename
#     done

#     echo -e "$BOLD""\n--------------------\n""$UNBOLD"
#     echo -e "$BOLD""Tests OK: $nbTestsOK""$UNBOLD"
#     echo -e "$BOLD""Tests KO: $nbTestsKO""$UNBOLD"

# }

function launchNormalTests() {

    input_files=`ls $script_dir/$inputs_dir`

    for filename in $input_files
    do
        testWithFiles $filename
    done

    echo -e "$BOLD""\n--------------------\n""$UNBOLD"
    echo -e "$BOLD""Tests OK: $nbTestsOK""$UNBOLD"
    echo -e "$BOLD""Tests KO: $nbTestsKO""$UNBOLD"

}

# launchTestsErrorManagement
launchNormalTests
rm -f logs
echo
