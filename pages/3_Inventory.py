import streamlit as st
from auxillaries import *

def split_list(input_list, chunk_size=5):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def get_categories(conn, type):
  df = get_df(conn, f'{type}_Inventory')
  return get_columns(df)

def display_categories(conn, type):
  st.subheader('Pick a Category', divider = 'grey')
  chunk_size = 5
  categories = get_categories(conn, type)
  list_categories = split_list(categories, chunk_size)
  with st.container(border = True):
    for cat in list_categories:
      cols = st.columns(chunk_size)
      for idx, c in enumerate(cat):
        cols[idx].image('logo.jpg')
        cols[idx].button(c, use_container_width=True, type = 'primary', key = f'btn_{c}', on_click=set_selected_category, args=(c, type))

def set_selected_category(category, type):
    if type == 'Kitchen':
        st.session_state.selected_kitchen_category = category
    else:
        st.session_state.selected_bar_category = category

def display_kitchen_items():
    if 'selected_kitchen_category' in st.session_state:
        kitchen_category = st.session_state.selected_kitchen_category
        st.subheader(f'{category}', divider = 'grey')

def display_bar_items()
    if 'selected_bar_category' in st.session_state:
        category = st.session_state.selected_bar_category
        st.subheader(f'{category}', divider = 'grey')

if __name__ == "__main__":
  st.header('Inventory')
  conn = get_connection()
  kitchen, bar = st.tabs(['Kitchen', 'Bar'])
  with kitchen:
    display_categories(conn, type)
    display_kitchen_items()
  with bar:
    display_categories(conn, type)
    display_bar_items()

  

