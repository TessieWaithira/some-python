import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project directory' + directory)
        os.makedirs(directory)

create_project_dir('Tessie')
