
ROOT_DIR=$(cd "$(dirname "$0")/.."; pwd -P)

cd $ROOT_DIR

rm -rf _build

python3 scripts/remove_code_input_cells.py
jupyter-book build docs #--config ../_config.yml --toc ../_toc.yml
ghp-import -n -p -f _build/html