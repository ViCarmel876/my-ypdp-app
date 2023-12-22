""" Example of  file for functions"""
FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    """Get todos from .txt file
       This is an example of a docstring
    """
    with open(filepath, 'r') as file_local:
        # not a good idea to call all variables with same name
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        """write todos into default file ie Afiles/todos.txt"""
        file.writelines(todos_arg)

""" This is an example of how to protect lines which should only be run when the 
file is executed Directly -- otherwise it never gets invoked."""
if __name__=="__main__":
    print("Hello")
    print(get_todos())