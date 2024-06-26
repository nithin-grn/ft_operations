import streamlit as st

st.logo('logo.jpg')
st.header('FT Local Kitchen & Bar', divider = 'grey')
st.sidebar.header('FT Local Kitchen & Bar')

def main():
  with st.container(height = 200, border = None):
    col1, col2 = st.columns([1, 3])
    col1.image('logo.jpg')
    col2.image('banner.jpg')

  st.header('Daily Tasks')
  st.caption('Start your day with the opening tasks.')
  with st.container(height = 200, border = None):
    col1, col2 = st.columns(2)
    col1.image('logo.jpg')
    col2.image('banner.jpg')

  st.header('Utilities')



if __name__ == "__main__":
  main()
