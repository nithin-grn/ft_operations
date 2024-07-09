import streamlit as st
from streamlit_gsheets import GSheetsConnection
from datetime import datetime
import pytz

def get_tasks(filename):
  with open(filename, 'r') as f:
    tasks = [task.strip() for task in f.readlines()]
  return tasks

def label_activity(df, time):
  today = today_date_string()
  st.write(today)
  # st.write(type(df['Date'].values[0]))
  if today in list(df['Date'].values):
    st.write('Yes')
    df.loc[df['Date'] == today, time] = 'Done'
  st.write(df)
  

def submit_update(time):
  conn = get_connection()
  df = get_df(conn, "Activities")
  label_activity(df, time)
  st.write("Submitted!")

def display_tasks(tasks, time):
  for idx, task in enumerate(tasks):
    with st.container(border = True):
      name, description = task.split('-')
      checked = st.checkbox(f":red-background[Task {idx + 1}: {name}]")
      st.write(description)
    if checked:
      if idx + 1 == len(tasks):
        if st.button("Submit", type = "primary", use_container_width = True):
          submit_update(time)
      continue
    else:
      break

def today_date_string():
  utc_now = datetime.utcnow()
  tz = pytz.timezone('Australia/Melbourne')
  today = utc_now.replace(tzinfo=pytz.utc).astimezone(tz)
  today_str = today.strftime('%d-%m-%Y')
  return today_str

def what_day(string_date):
  date_obj = datetime.strptime(string_date, '%d-%m-%Y')
  day_of_week = date_obj.strftime('%A')
  return day_of_week

def get_connection():
  # Create a connection object.
  conn = st.connection("gsheets", type=GSheetsConnection)
  return conn
  
def get_df(conn, sheet_name):
  df = conn.read(
      worksheet=sheet_name,
      ttl=0
  )
  return df

def get_columns(df):
  return df.columns.tolist()

def update_worksheet(conn, wsheet, df):
  conn.update(
            worksheet=wsheet,
            data=df,
        )
