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
    if df.loc[df['Date'] == today, time][0] == 'Done':
      st.info('Looks like you have completed the tasks today.')
    else:
      st.info('Hmm, Looks like you have to complete the tasks yet.')
  return df

def submit_eod_report(conn, today_sales, comp_sales, bookings, events, reviews, inv_update):
  with st.status('Submitting, please wait...', expanded = True):
    today = today_date_string()
    act_df = get_df(conn, "Activities")
    if today in list(act_df['Date'].values):
      act_df.loc[act_df['Date'] == today, 'Bookings'] = bookings
      act_df.loc[act_df['Date'] == today, 'Events'] = events
      act_df.loc[act_df['Date'] == today, 'Reviews'] = reviews
      act_df.loc[act_df['Date'] == today, 'Inventory Update'] = inv_update
    else:
      new_row = {'Date': today, 'Bookings': bookings, 'Events': events, 'Reviews': reviews, 'Inventory Update': inv_update}
      act_df = act_df.append(new_row, ignore_index=True)
    update_worksheet(conn, 'Activities', act_df)
    
    sales_df = get_df(conn, "Sales")
    if today in list(sales_df['Date'].values):
      sales_df.loc[sales_df['Date'] == today, 'Actual Sale'] = today_sales
      sales_df.loc[sales_df['Date'] == today, 'Comparison Sale'] = comp_sales
      sales_df.loc[sales_df['Date'] == today, 'Variance'] = today_sales - comp_sales
    else:
      new_row = {'Date': today, 'Actual Sale': today_sales, 'Comparison Sale': comp_sales, 'Variance': today_sales - comp_sales}
      sales_df = sales_df.append(new_row, ignore_index=True)
    update_worksheet(conn, 'Sales', sales_df)
    st.success('Successfully submitted!')
  
def day_reports(conn):
  st.subheader('EOD Report', divider = 'grey')
  st.warning('Done for the day?')
  with st.container(border = True):
    today_sales = st.number_input('Enter today\'s sales in $:', min_value = 0.0)
    comp_sales = st.number_input('Enter same day last week\'s sales in $:', min_value = 0.0)
    bookings = st.number_input('Number of bookings/Table reservations made today:', min_value = 0)
    events = st.number_input('Number of Events held today:', min_value = 0)
    reviews = st.number_input('Number of Google Reviews today:', min_value = 0)
    inv_update = st.selectbox('Did you update the inventory today', options = ['No', 'Yes'])
    if st.button('Submit EOD report', type = 'primary', use_container_width = True):
      submit_eod_report(conn, today_sales, comp_sales, bookings, events, reviews, inv_update)

if __name__ == "__main__":
  st.header('Closing Tasks')
  conn = get_connection()
  df = get_df(conn, "Activities")
  check_completion(df, 'Closing Tasks')
  tasks = get_tasks('closing.txt')
  c1, c2 = st.columns([2, 1])
  with c1:
    display_tasks(df, tasks, 'Closing Tasks')
  with c2:
    day_reports(conn)
