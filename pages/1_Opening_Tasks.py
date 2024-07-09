import streamlit as st

def get_tasks():
  with open('opening.txt', 'r') as f:
    tasks = [task.strip() for task in f.readlines()]
  return tasks

def display_tasks(tasks):
  for task in tasks:
    if st.checkbox(task):
      continue
    else:
      break

if __name__ == "__main__":
  st.header('Opening Tasks')
  tasks = get_tasks()
  display_tasks(tasks)
