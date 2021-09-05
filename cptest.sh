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

# activate venv python
source .venv/bin/activate

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${dir_name}/.test/${problem_name//-/_} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

if [ $extension = "cpp" ]; then
    g++ ${file_path} && oj test -d ${dir_name}/.test/${problem_name//-/_}
elif [ $extension = "rs" ]; then
    # export RUST_BACKTRACE=1
    cd rust && cargo build --release --bin ${problem_name} && cd .. && oj test -c "rust/target/release/${problem_name}" -d ${dir_name}/.test/${problem_name//-/_} 
else
    oj test -c "python ${file_path}" -d ${dir_name}/.test/${problem_name//-/_}
    # oj test -e 1e-6 -c "python ${file_path}" -d ${dir_name}/test/${problem_name//-/_}
fi

