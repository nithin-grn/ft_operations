import streamlit as st

def split_list(input_list, chunk_size=5):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def display_categories():
  st.subheader('Pick a Category', divider = 'grey')
  chunk_size = 5
  categories = ['Apple', 'Orange', 'Mango', 'Banana', 'Guava', 'Jackie', 'Passionfruit']
  list_categories = split_list(categories, chunk_size)
  with st.container():
    for cat in list_categories:
      cols = st.columns(chunk_size)
      for idx, c in enumerate(cat):
        cols[idx].image('logo.jpg')
        cols[idx].button(c, use_container_width=True, type = 'primary', key = f'btn_{c}', on_click=set_selected_category, args=(c,))

def set_selected_category(category):
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = category

def display_items():
    if 'selected_category' in st.session_state:
        category = st.session_state.selected_category
        st.subheader(f'{category}', divider = 'grey')

def reset_category():
    if 'selected_category' in st.session_state:
        del st.session_state.selected_category

if __name__ == "__main__":
  reset_category()
  st.header('Inventory')
  display_categories()
  display_items()
  

