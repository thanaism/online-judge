#!/bin/bash
file_path=$1
file_name=$(basename ${file_path})
dir_name=$(dirname ${file_path})
extension=${file_name##*.}
echo $extension
problem_name=${file_name%.*}
test_dir=${dir_name}/.test/${problem_name//-/_}
base_url=${problem_name%_*}

# GNU time
export PATH="/usr/local/opt/gnu-time/libexec/gnubin:$PATH"

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${dir_name}/.test/${problem_name//-/_} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

if [ $extension = "py" ]; then
    source .venv/bin/activate
    black $file_path
    deactivate
    oj test -e 1e-7 -c "pypy ${file_path}" -d ${dir_name}/.test/${problem_name//-/_}
fi