import os
# Auto-File-Folder-Structure-Generator.py
# Manually reviewed code and tested - works as intended. 

## So this is super useful and time saving, automating the repetitive boring work
    # that kills the creative process before you even start coding. 

## This file was generated by AI to automate the creation
    # of the file/directory structure for my AID project.
    # However it should work in practice for any coding project in theory.

## Initial Process
    # 1 First I gave it my initial goals for the project.
    # 2 Next I asked it to generate a file/folder structure for the project code and data.
    # 3 I then asked it to rewrite including the suggestions it mentioned in the previous step.
    # 4 Finally, I instructed the AI to create a script to automate the file creation.
    # 5 Run this script in the dir where you want to create the project files/folders.

def create_folder_structure(base_path):
    paths = [
        'docs',
        'src/modules/drafting',
        'src/modules/design',
        'src/modules/optimization',
        'src/utils',
        'tests',
        'data/input',
        'data/output/2d',
        'data/output/3d',
        'data/training/2d',
        'data/training/3d',
        'models/2d',
        'models/3d',
        'interface/static',
        'interface/templates',
    ]

    for path in paths:
        os.makedirs(os.path.join(base_path, path), exist_ok=True)

    files = [
        'docs/README.md',
        'docs/CONTRIBUTING.md',
        'docs/USAGE.md',
        'docs/LICENSE',
        'src/main.py',
        'src/modules/drafting/__init__.py',
        'src/modules/drafting/2d.py',
        'src/modules/drafting/3d.py',
        'src/modules/design/__init__.py',
        'src/modules/design/floorplan.py',
        'src/modules/design/elevation.py',
        'src/modules/optimization/__init__.py',
        'src/modules/optimization/token_optimizer.py',
        'src/utils/__init__.py',
        'src/utils/data_utils.py',
        'src/utils/model_utils.py',
        'tests/test_drafting.py',
        'tests/test_design.py',
        'tests/test_optimization.py',
        '.gitignore',
        'requirements.txt',
        'setup.py',
    ]

    for file in files:
        open(os.path.join(base_path, file), 'a').close()

if __name__ == "__main__":
    create_folder_structure('AID')