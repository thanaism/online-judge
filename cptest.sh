#!/bin/zsh

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

if [ $# = 2 ];then
    script_name=$2
    oj test -c "pypy3 ${script_name}.py" -d test/${problem_name//-/_}
else
    oj test -c "pypy3 ${problem_name}.py" -d test/${problem_name//-/_}
fi
