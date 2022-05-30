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

function testWithFile() {
    #result=$(./koak ./testFiles/input/$1 > ./log)
    ./koak ./testFiles/input/$1 > ./log
    result=$(cat ./log)
    exitValue=$?
    #echo $result > log
    expected=$(cat ./testFiles/expected/$1)
    diff=$(diff -y log ./testFiles/expected/$1)
    #inputContent=$(cat ./testFiles/input/$1)

    if [ $exitValue = 0 ];
        then if [[ "$result" == "$expected" ]];
            then nbTestsOK=$((nbTestsOK + 1))
                 echo -e "$TITLEOK""\n---------- $1 ----------\n""$UNTITLEOK"
                 #echo -e "$BOLD""File content:\n""$UNBOLD""'$inputContent'"
                 #echo -e "$BOLD""\nResult:\n""$UNBOLD""'$result'"
                 
        else
            nbTestsKO=$((nbTestsKO + 1))
            echo -e "$TITLEKO""\n---------- $1 ----------\n""$UNTITLEKO"
            echo -e "$diff"
            #echo -e "$BOLD""File content:\n""$UNBOLD""'$inputContent'"
            #echo -e "$BOLD""\nExpected:\n""$UNBOLD""'$expected'"
            #echo -e "\n$BOLD""But got:\n""$UNBOLD""'$result'"
        fi
    else
        nbTestsKO=$((nbTestsKO + 1))
        echo -e "$TITLEKO""\n---------- $1 ----------\n""$UNTITLEKO"
        #echo -e "$BOLD""File content:\n""$UNBOLD""'$inputContent'"
        echo -e "\t$BOLD""Exited with value $exitValue""$UNBOLD"
    fi
}

function launchAllTests() {
    testWithFile "Arithmetics" 
    testWithFile "Variables"
    testWithFile "Functions"
    testWithFile "IfElse"
    testWithFile "While"
    testWithFile "For"

    echo -e "$BOLD""\n--------------------\n""$UNBOLD"
    echo -e "$BOLD""tests OK: $nbTestsOK""$UNBOLD"
    echo -e "$BOLD""tests KO: $nbTestsKO""$UNBOLD"

}

launchAllTests
rm -f log
echo
