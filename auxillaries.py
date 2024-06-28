import streamlit as st
from streamlit_gsheets import GSheetsConnection

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
