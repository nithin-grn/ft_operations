import streamlit as st

def main():
  st.header('FT Local Kitchen & Bar', divider = 'grey')
  with st.container(height = 200, border = None):
    col1, col2 = st.columns([1, 3])
    col1.image('logo.jpg')
    col2.image('banner.jpg')

if __name__ == "__main__":
  main()
