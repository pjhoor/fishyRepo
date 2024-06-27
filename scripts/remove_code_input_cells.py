
"""
This script is used to ensure that every code cell in story.ipynb
is hidden before deploying. It achieves this by adding the 'remove_input'
metadata to each cell.
"""

import nbformat as nbf
from os import path

ROOT_DIR = path.realpath(path.join(path.dirname(__file__), '..'))

DATASTORY_NB_FILEPATH = path.join(ROOT_DIR, 'docs', 'story.ipynb')

if __name__ == '__main__':
    ntbk = nbf.read(DATASTORY_NB_FILEPATH, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        # Retrieve existing cell tags.
        cell_tags = cell.get('metadata', {}).get('tags', [])

        if 'hide_input' in cell_tags:
            cell_tags.remove('hide_input')
        
        if 'hide-input' not in cell_tags:
            cell_tags.append('hide-input')

        cell['metadata']['tags'] = cell_tags

    nbf.write(ntbk, DATASTORY_NB_FILEPATH)

print('NOTE: Some files might have been changed, run "git status" to see which files have changed.')
