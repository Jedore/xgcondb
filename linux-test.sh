#!/bin/bash

if [ $# -eq 0 ]; then
    echo "./linux-test.sh <xgcondb version>"
    exit 1
fi

versions="3.6.15 3.7.17 3.8.18 3.9.18 3.10.13 3.11.6"

succeed=()
fail=()
for ver in $versions; do
    echo "##########################          Test for $ver         ###############################"
    echo "----------------------- Prepare env" 
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    pyenv virtualenv $ver test
    pyenv activate test

    new_ver=$(echo "$ver" | awk -F '.' '{print $1$2}')

    if [ "$new_ver" = "36" ]; then
	    pip install -U pip
    fi

    echo "----------------------- Install xgcondb" 
    pip uninstall -y xgcondb
    if [ "$new_ver" = "36" ] || [ "$new_ver" = "37" ]; then
	pip install dist/xgcondb-$1-cp${new_ver}-cp${new_ver}m-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
    else
	pip install dist/xgcondb-$1-cp${new_ver}-cp${new_ver}-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
    fi

    echo "----------------------- Test xgcondb" 
    result=$(python tests/__init__.py)

    case "$result" in
        *"Succeeded"*)
	    succeed[${#succeed[@]}]=$ver
	    ;;
        *"Failed!"*)
	    fail[${#fail[@]}]=$ver
	    ;;
    esac

    echo "----------------------- Remove env" 
    pyenv virtualenv-delete -f test

done

echo "**************************** Result ******************************"
echo "Succeeded: ${succeed[*]}"
echo "Failed: ${fail[*]}"
