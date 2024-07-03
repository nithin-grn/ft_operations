import streamlit as st
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

def today_date_string():
  today = datetime.today()
  today_str = today.strftime('%d-%m-%Y')
  return today_str

def what_day(string_date):
  date_obj = datetime.strptime(string_date, '%d-%m-%Y')
  day_of_week = today.strftime('%A')
  return day_of_week

def get_connection():
  # Create a connection object.
  conn = st.connection("gsheets", type=GSheetsConnection)
  return conn
  
def get_df(conn, sheet_name):
  df = conn.read(
      worksheet=sheet_name,
      ttl="10m"
  )
  return df

def get_columns(df):
  return df.columns.tolist()
