import streamlit as st
import base64
from st_clickable_images import clickable_images


st.logo('logo.jpg')
st.header('FT Local Kitchen & Bar', divider = 'grey')
st.sidebar.header('FT Local Kitchen & Bar')

def get_clickable_images(files):
    images = []
    for file in files:
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")
    return images
        

def main():
  with st.container(height = 200, border = None):
    col1, col2 = st.columns([1, 3])
    col1.image('logo.jpg')
    col2.image('banner.jpg')

  st.subheader('Daily Tasks')
  st.caption('Start your day with the opening tasks.')
  images = get_clickable_images(['opening.jpg', 'closing.jpg'])
  with st.container():
        # Display clickable images in a flexbox layout
        clicked = clickable_images(
            images,
            titles=[f"Click here for tasks" for i in range(len(images))],
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
            img_style={"margin": "1%", "height": "200px", "width": "48%"}
        )
  c1, c2 = st.columns(2)
  c1.markdown("<div style='text-align: center;'><b>Opening Tasks</b></div>", unsafe_allow_html=True)
  c2.markdown("<div style='text-align: center;'><b>Closing Tasks</b></div>", unsafe_allow_html=True)
  if clicked > -1:
      st.switch_page("1_Opening_Tasks.py") if clicked == 0 else (st.switch_page("2_Closing_Tasks.py") if clicked == 1 else None)

  st.subheader('Utilities')
  with st.container(height = 200, border = None):
    col1, col2 = st.columns(2)
    col1.image('inventory.jpg', caption = 'Inventory')
    col2.image('service.jpeg', caption = 'Service Expectations')



if __name__ == "__main__":
  main()
