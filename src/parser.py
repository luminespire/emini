def get_name(content: str):
    tokens = content.split('```')
    return '-'.join(tokens[0].split()[2:]).lower()


def get_names(content: str):
    tokens = content.split()
    return tokens[2], tokens[3]


def get_matrix(content: str):
    tokens = content.split('```')
    return tokens[1].strip()


def get_string(content: str):
    tokens = content.split()
    return ' '.join(tokens[2:])