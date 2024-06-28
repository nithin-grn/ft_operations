import streamlit as st

def split_list(input_list, chunk_size=5):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def display_categories():
  st.subheader('Pick a Category')
  chunk_size = 5
  categories = ['Apple', 'Orange', 'Mango', 'Banana', 'Guava', 'Jackie', 'Passionfruit']
  list_categories = split_list(categories, chunk_size)
  with st.container():
    for cat in list_categories:
      cols = st.columns(chunk_size)
      for idx, c in enumerate(cat):
        cols[idx].image('logo.jpg')
        cols[idx].button(c, use_container_width=True, type = 'primary', key = f'btn_{c}', on_click = display_items, kwargs = {'category': c})

def display_items(category):
  st.write(f'{category}\'s items')

if __name__ == "__main__":
  st.header('Inventory')
  display_categories()
  

