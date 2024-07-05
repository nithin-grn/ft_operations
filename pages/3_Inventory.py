import streamlit as st
from auxillaries import *
import pandas as pd

today = today_date_string()
options = ['In stock', 'Low in stock', 'Out of stock']

def split_list(input_list, chunk_size=5):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def get_items_from_category(df, category):
    return df[category].dropna()

def get_existing_stock(conn, area):
    return get_df(conn, f'{area}_Stock')

def get_stock_dict(conn, area, category):
    df = get_df(conn, f'{area}_Inventory')
    items = get_items_from_category(df, category)
    stock_dict = {}
    existing_df = get_existing_stock(conn, area)
    existing_dates = get_existing_dates(existing_df) 
    st.write(existing_dates, today)
    for item in items:
        c1, c2 = st.columns(2)
        c1.write(item)
        default_index = None
        if today in existing_dates:
            value = existing_df.loc[existing_df['Items'] == item, today].iloc[0]
            if pd.notna(value):
                st.write(value)
                default_index = options.index(value)
        st.write(default_index)
        status = c2.selectbox('Current Stock Level', options = options , index = default_index, label_visibility = "collapsed", key = f'{area}-{item}-{default_index}')
        stock_dict[item] = status
    return stock_dict

def display_categories(conn, area):
  st.subheader('Pick a Category', divider = 'grey')
  chunk_size = 5
  df = get_df(conn, f'{area}_Inventory')
  categories = get_columns(df)
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

def get_existing_dates(df):
    return get_columns(df)[1:]

def submit_stock(conn, area, stock_dict):
  with st.status('Updating...', expanded = True) as status:
    df = get_df(conn, f'{area}_Stock')
    dates = get_existing_dates(df)
    if today in dates:
      df[today] = df['Items'].map(stock_dict).fillna(df[today])
    else:
      df[today] = None
      df[today] = df['Items'].map(stock_dict).fillna(df[today])
    update_worksheet(conn, f'{area}_Stock', df)
    status.update(label="Successfully submitted!", state="complete", expanded=False)

def display_kitchen_items(conn):
    if 'selected_kitchen_category' in st.session_state:
      category = st.session_state.selected_kitchen_category
      st.subheader(f'{category}', divider = 'grey')
      stock_dict = get_stock_dict(conn, 'Kitchen', category)
      if len(stock_dict) > 0:
        if st.button('Submit', key = 'kitchen_submit', type = 'primary', use_container_width = True):
            submit_stock(conn, 'Kitchen', stock_dict)
      else:
        st.info('No items listed in this category')

def display_bar_items(conn):
    if 'selected_bar_category' in st.session_state:
      category = st.session_state.selected_bar_category
      st.subheader(f'{category}', divider = 'grey')
      stock_dict = get_stock_dict(conn, 'Bar', category)
      if len(stock_dict) > 0:
        if st.button('Submit', key = 'bar_submit', type = 'primary', use_container_width = True):
            submit_stock(conn, 'Bar', stock_dict)
      else:
        st.info('No items listed in this category')

if __name__ == "__main__":
  st.header('Inventory')
  conn = get_connection()
  kitchen, bar = st.tabs(['Kitchen', 'Bar'])
  with kitchen:
    display_categories(conn, 'Kitchen')
    display_kitchen_items(conn)
  with bar:
    display_categories(conn, 'Bar')
    display_bar_items(conn)

  

