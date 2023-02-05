import streamlit as st
import fileHandler

todos = fileHandler.getTodos()

def add_todo():
    todo = st.session_state["new_todo"]
    todo = todo+"\n"
    todos.append(todo)
    fileHandler.writeTodos(todos)


st.title("My Todo App")
st.subheader("This is a todo list app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        del st.session_state[todo]
        fileHandler.writeTodos(todos)
        st.experimental_rerun()

st.text_input(label="", value="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")



