import streamlit as st
from auxillaries import *

def split_list(input_list, chunk_size=5):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def get_categories(conn):
  df = get_df(conn, 'Kitchen_Inventory')
  return get_columns(df)

def display_categories(conn):
  st.subheader('Pick a Category', divider = 'grey')
  chunk_size = 5
  categories = get_categories(conn)
  list_categories = split_list(categories, chunk_size)
  with st.container(border = True):
    for cat in list_categories:
      cols = st.columns(chunk_size)
      for idx, c in enumerate(cat):
        cols[idx].image('logo.jpg')
        cols[idx].button(c, use_container_width=True, type = 'primary', key = f'btn_{c}', on_click=set_selected_category, args=(c,))

def set_selected_category(category):
    st.session_state.selected_category = category

def display_items():
    if 'selected_category' in st.session_state:
        category = st.session_state.selected_category
        st.subheader(f'{category}', divider = 'grey')

if __name__ == "__main__":
  st.header('Inventory')
  conn = get_connection()
  display_categories(conn)
  display_items()
  

