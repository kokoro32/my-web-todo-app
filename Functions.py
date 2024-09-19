FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as archivo_local:
        todos_local = archivo_local.readlines()
    return todos_local


# print(help(get_todos))


def set_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as archivo_local:
        archivo_local.writelines(todos_arg)


# print("Hola, me colé en tu modulo Functions")
if __name__ == "__main__":
    print("Solo me ejecuto cuando se ejecuta mi programa desde el archivo donde estoy")