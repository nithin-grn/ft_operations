import streamlit as st
from auxillaries import *

def get_tasks(filename):
  with open(filename, 'r') as f:
    tasks = [task.strip() for task in f.readlines()]
  return tasks

def label_activity(df, time):
  today = today_date_string()
  if today in list(df['Date'].values):
    df.loc[df['Date'] == today, time] = 'Done'
  else:
    new_row = {'Date': today, 'Opening Tasks': 'Done'}
    df = df.append(new_row, ignore_index=True)
  return df

def submit_update(df, time):
  with st.status('Submitting, please wait...'):
    df = label_activity(df, time)
    update_worksheet(conn, 'Activities', df)
    st.success("Submitted!")

def display_tasks(df, tasks, time):
  for idx, task in enumerate(tasks):
    with st.container(border = True):
      name, description = task.split('-')
      checked = st.checkbox(f":red-background[Task {idx + 1}: {name}]")
      st.write(description)
    if checked:
      if idx + 1 == len(tasks):
        if st.button("Submit", type = "primary", use_container_width = True):
          submit_update(df, time)
      continue
    else:
      break

def check_completion(df, time):
  today = today_date_string()
  if today in list(df['Date'].values):
    if df.loc[df['Date'] == today, time] == 'Done':
      st.info('Looks like you have completed the tasks today.')
  return df

if __name__ == "__main__":
  st.header('Opening Tasks')
  conn = get_connection()
  df = get_df(conn, "Activities")
  check_completion(df, 'Opening Tasks')
  tasks = get_tasks('opening.txt')
  display_tasks(df, tasks, 'Opening Tasks')
