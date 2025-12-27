def adjacency_list():
    adjacency = {
        'A': ['B', 'C', 'D'],
        'B': [],
        'C': ['E', 'F', 'G'],
        'D': ['H'],
        'E': [],
        'F': ['I'],
        'G': [],
        'H': ['J', 'K'],
        'I': ['L', 'M'],
        'J': [],
        'K': [],
        'L': [],
        'M': [],
    }
    return adjacency

def adjacency_to_path(adjacency):
    children = []
    for node in adjacency:
        children_list = adjacency[node]
        for child in children_list:
            children.append(child)
    root = 0
    for node in adjacency:
        index = False
        for child in children:
            if node == child:
                index = True
        if index == False:
            root = node
    path_dict = {}

    def tour(adjacency_node, adjacency_path):
        if adjacency_path == '':
            materialized_path = str(adjacency_node)
        else:
            materialized_path = f'{adjacency_node}, {adjacency_path}'

        path_dict[adjacency_node] = materialized_path
        children_dr = adjacency.get(adjacency_node, [])
        for child in children_dr:
            tour(child, materialized_path)

    if root != None:
        tour(root, '')
    return path_dict

def materialized_path():
    path = {
        'A': 'A',
        'B': 'B, A',
        'C': 'C, A',
        'E': 'E, C, A',
        'F': 'F, C, A',
        'I': 'I, F, C, A',
        'L': 'L, I, F, C, A',
        'M': 'M, I, F, C, A',
        'G': 'G, C, A',
        'D': 'D, A',
        'H': 'H, D, A',
        'J': 'J, H, D, A',
        'K': 'K, H, D, A',
    }
    return path

def path_to_adjacency(path):
    adjacency = {}
    nodes = list(path.keys())
    for node in nodes:
        materialized = path[node]
        parts = materialized.split(',')

        if len(parts) == 1:
            if node not in adjacency:
                adjacency[node] = []
        else:
            parent = parts[1]

            if parent not in adjacency:
                adjacency[parent] = []

            if node not in adjacency[parent]:
                adjacency[parent].append(node)

            if node not in adjacency:
                adjacency[node] = []
    return adjacency


if __name__ == "__main__":
    print(f'Изначальный список смежности: \n{adjacency_list()}')
    print('Переход списка смежности в материализованный путь')
    print(f'Полученый материализованный путь: \n{adjacency_to_path(adjacency_list())}')

    print(f'Изначальный материализованный путь\n {materialized_path()}')
    print(f'Переход из материализованного пути в список смежности')
    print(f'Полученный список смежности\n {path_to_adjacency(materialized_path())}')