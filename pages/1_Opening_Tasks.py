import streamlit as st

def get_tasks():
  with open('opening.txt', 'r') as f:
    tasks = [task.strip() for task in f.readlines()]
  return tasks

def display_tasks(tasks):
  for task in tasks:
    name, description = task.split('-')
    checked = st.checkbox(name)
    st.write(description)
    if checked:
      continue
    else:
      break

# def display_tasks(tasks):
#   st.write(tasks)
#   for idx, task in enumerate(tasks):
#     name, description = task.split('-')
#     st.subheader(f"Task {idx + 1}: {name.strip()}")
#     st.write(f"{description}")
#     if st.button(f"Task {idx + 1} Completed"):
#       continue
#     break

if __name__ == "__main__":
  st.header('Opening Tasks')
  tasks = get_tasks()
  display_tasks(tasks)
