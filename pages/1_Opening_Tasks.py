import streamlit as st
import auxillaries as ax

if __name__ == "__main__":
  st.header('Opening Tasks')
  tasks = ax.get_tasks('opening.txt')
  ax.display_tasks(tasks 'Opening Tasks')
