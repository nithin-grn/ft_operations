import streamlit as st
from auxillaries import *

def split_list(input_list, chunk_size=5):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def get_categories(conn, area):
  df = get_df(conn, f'{area}_Inventory')
  return get_columns(df)

def get_items_from_category(df, category):
    return df[category]

def get_stock_dict(conn, area, category):
    df = get_df(conn, f'{area}_Inventory')
    items = get_items_from_category(df, category)
    stock_dict = {}
    for item in items:
        status = st.selectbox(options = ['In stock', 'Low in stock', 'Out of stock'], index=None, placeholder="Current Stock level...", label_visibility = "collapsed")
        stock_dict[item] = status
    return stock_dict

def display_categories(conn, area):
  st.subheader('Pick a Category', divider = 'grey')
  chunk_size = 5
  categories = get_categories(conn, area)
  list_categories = split_list(categories, chunk_size)
  with st.container(border = True):
    for cat in list_categories:
      cols = st.columns(chunk_size)
      for idx, c in enumerate(cat):
        cols[idx].image('logo.jpg')
        cols[idx].button(c, use_container_width=True, type = 'primary', key = f'btn_{c}', on_click=set_selected_category, args=(c, area))

def set_selected_category(category, area):
    if area == 'Kitchen':
        st.session_state.selected_kitchen_category = category
    else:
        st.session_state.selected_bar_category = category

def display_kitchen_items(conn):
    if 'selected_kitchen_category' in st.session_state:
        category = st.session_state.selected_kitchen_category
        st.subheader(f'{category}', divider = 'grey')
        stock_dict = get_stock_dict(conn, 'Kitchen', category)

def display_bar_items(conn):
    if 'selected_bar_category' in st.session_state:
        category = st.session_state.selected_bar_category
        st.subheader(f'{category}', divider = 'grey')
        stock_dict = get_stock_dict(conn, 'Bar', category)

if __name__ == "__main__":
  st.header('Inventory')
  conn = get_connection()
  kitchen, bar = st.tabs(['Kitchen', 'Bar'])
  with kitchen:
    display_categories(conn, 'Kitchen')
    display_kitchen_items()
  with bar:
    display_categories(conn, 'Bar')
    display_bar_items()

  

