import streamlit as st
import fileHandler

todos = fileHandler.getTodos()

st.title("My Todo App")
st.subheader("This is a todo list app.")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "", value="", placeholder="Add new todo...")

