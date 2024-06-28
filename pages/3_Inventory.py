import streamlit as st

def split_list(input_list, chunk_size=5):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def display_categories():
  categories = ['Apple', 'Orange', 'Mango', 'Banana', 'Guava', 'Jackie', 'Passionfruit']
  list_categories = split_list(categories)
  with st.container():
    for cat in list_categories:
      cols = st.columns(len(cat))
      for idx, col in enumerate(cols):
        col.image('logo.jpg')
        col.button(categories[idx], use_container_width=True, type = 'primary')

if __name__ == "__main__":
  st.header('Inventory')
  display_categories()
