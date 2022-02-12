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
export PATH="$HOME/.cargo/bin:$PATH"

# activate venv python
source .venv/bin/activate

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${dir_name}/.test/${problem_name//-/_} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

if [ $extension = "cpp" ]; then
    g++ ${file_path} -std=c++14 && oj test -e 1e-7 -d ${dir_name}/.test/${problem_name//-/_}
elif [ $extension = "rs" ]; then
    # export RUST_BACKTRACE=1
    cd ${dir_name} && cargo build --release --bin ${problem_name} && cd - && oj test -e 1e-7 -c "${dir_name}/../../target/release/${problem_name}" -d ${dir_name}/.test/${problem_name//-/_} 
elif [ $extension = "rb" ]; then
    oj test -e 1e-7 -c "ruby ${file_path}" -d ${dir_name}/.test/${problem_name//-/_} 
elif [ $extension = "hs" ]; then
    output_dir=${dir_name}/.output
    ghc ${file_path} -o ${output_dir}/${problem_name} -outputdir ${output_dir} -no-keep-hi-files -no-keep-o-files 
    oj test -e 1e-7 -c "${output_dir}/${problem_name}" -d ${dir_name}/.test/${problem_name//-/_}  
elif [ $extension = "py" ]; then
    black $file_path
    oj test -e 1e-7 -c "python ${file_path}" -d ${dir_name}/.test/${problem_name//-/_}
    # oj test -e 1e-6 -c "python ${file_path}" -d ${dir_name}/test/${problem_name//-/_}
elif [ $extension = "pl" ]; then
    oj test -e 1e-7 -c "perl ${file_path}" -d ${dir_name}/.test/${problem_name//-/_}
elif [ $extension = "dart" ]; then
    oj test -e 1e-7 -c "dart ${file_path}" -d ${dir_name}/.test/${problem_name//-/_}
fi