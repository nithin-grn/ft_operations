import streamlit as st

def display_categories():
  categories = ['Apple', 'Orange', 'Mango', 'Banana', 'Guava', 'Jackie', 'Passionfruit']
  cols = st.columns(len(categories))
  for idx, col in enumerate(cols):
    col.image('logo.jpg')
    col.write(categories[idx])

if __name__ == "__main__":
  st.header('Inventory')
  display_categories()
