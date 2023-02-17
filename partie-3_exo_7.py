
def get_file_paths(hierarchy, parent_path=''):
    file_paths = []
    for item in hierarchy:
        if item['type'] == 'file':
            file_paths.append(parent_path + '/' + item['name'])
        elif item['type'] == 'directory':
            directory_path = parent_path + '/' + item['name']
            child_paths = get_file_paths(item['children'], directory_path)
            file_paths += child_paths
    return file_paths

#dictionnaire pour la hiéarchie
hierarchy = [
    {'name': 'root', 'type': 'directory', 'children': [

        {'name': 'folder1', 'type': 'directory', 'children': [
            {'name': 'file1.txt', 'type': 'file'},
            {'name': 'file2.txt', 'type': 'file'}
        ]},

    ]}
]

file_paths = get_file_paths(hierarchy)
print(file_paths)
