import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)

todos = functions.get_todos()

st.title("Spick n' Speck Cleaning Solutions")
st.subheader("These are the current outstanding todo's")
st.write("Lets get these done Chop - Chop !")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo ", placeholder="Add new Todo....",
              on_change=add_todo, key='new_todo')

