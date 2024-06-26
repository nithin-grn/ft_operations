import streamlit as st

def main():
  st.heading('FT Local Kitchen & Bar', divider = 'black')
  with st.container(height = 200):
    col1, col2 = st.columns([1, 3])
    col1.image('logo.jpg')
    col2.image('banner.jpg')

if __name__ == "__main__":
  main()
