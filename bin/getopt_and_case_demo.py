#/bin/bash
verbose='false'
aflag=''
bflag=''
files=''
while getopts 'abf:v' flag; do
    case "${flag}" in
        a) aflag='true' ;;
        b) bflag='true' ;;
        f) files="${OPTARG}" ;;
        v) verbose='true' ;;
        *) error "Unexpected option ${flag}" ;;
    esac
done
# 多行写法，适用于部分或全部分支较为复杂的场景。
case "${expression}" in
    a)
        variable="xxx"
        some_command "${variable}" "${other_expr}"
        ;;
    absolute)
        actions="relative"
        another_command "${actions}" "${other_expr}"
        ;;
    *)
        error "Unexpected expression '${expression}'"
        ;;
esac
