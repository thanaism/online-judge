#!/bin/zsh
file_path=$1
# echo $(pwd)
# echo $(dirname ${file_name})
file_name=$(basename ${file_path})
dir_name=$(dirname ${file_path})
# echo ${dir_name}
# echo ${file_name}
problem_name=${file_name%.*}
# echo ${problem_name}
test_dir=${dir_name}/test/${problem_name//-/_}
# echo ${test_dir}
base_url=${problem_name%_*}

# activate venv python
source .venv/bin/activate

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${dir_name}/test/${problem_name//-/_} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

# if [ $# = 2 ];then
#     script_name=$2
#     oj test -c "pypy3 ${script_name}.py" -d test/${problem_name//-/_}
# else
# echo ${dir_name}/test/${problem_name//-/_}
    oj test -c "python ${file_path}" -d ${dir_name}/test/${problem_name//-/_}
# fi
