import streamlit as st
import Functions


todos = Functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        if todo not in todos:
            if '\n' not in todos[-1]:
                todos.append('\n'+todo)
            else:
                todos.append(todo)
            Functions.set_todos(todos)
            st.session_state["new_todo"] = ""

st.title("My ToDo App")
st.subheader("This is my todo App.")
st.write("This App is to increase your <b>productivity.</b>", unsafe_allow_html=True)

if st.button("¡Tareas completadas!"):
    # Crear una nueva lista solo con los todos no seleccionados
    todos = [todo for todo in todos if not st.session_state.get(todo)]
    Functions.set_todos(todos)
    st.session_state["new_todo"] = ""
    st.rerun()


for todo in todos:
    st.checkbox(label=todo, key=todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""




