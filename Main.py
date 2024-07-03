import streamlit as st
import base64
from st_clickable_images import clickable_images
from st_pages import show_pages_from_config
from auxillaries import *

st.logo('logo.jpg')
st.header('FT Local Kitchen & Bar', divider = 'grey')
st.sidebar.header('FT Local Kitchen & Bar')

# show_pages_from_config(".streamlit/pages_sections.toml")

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('styles.css')

# Function to get image data from local file
def get_image_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_clickable_images(files):
    images = []
    for file in files:
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")
    return images

def reminders():
  day = which_day(today_date_string())
  st.info(day)
        

def main():
  # Path to your local image
  image_path = 'banner2.jpg'
  image_data = get_image_as_base64(image_path)
  
  # Display the image using HTML with the responsive class
  with st.container():
    st.markdown(f'<img src="data:image/jpeg;base64,{image_data}" alt="Responsive Image" class="responsive">', unsafe_allow_html=True)

  reminders()
  
  st.subheader('Daily Tasks')
  st.caption('Start your day with the opening tasks.')
  images = get_clickable_images(['opening.jpg', 'closing.jpg'])
  with st.container():
        # Display clickable images in a flexbox layout
        clicked = clickable_images(
            images,
            titles=[f"Click here for tasks" for i in range(len(images))],
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
            # div_style = {"display": "flex", "flex-direction": "column", "justify-content": "center", "align-items": "center"},
            img_style={"margin": "1%", "height": "200px", "width": "48%"}
        )
  c1, c2 = st.columns(2)
  c1.markdown("<div style='text-align: center;'><b>Opening Tasks</b></div>", unsafe_allow_html=True)
  c2.markdown("<div style='text-align: center;'><b>Closing Tasks</b></div>", unsafe_allow_html=True)
  if clicked > -1:
      st.switch_page("pages/1_Opening_Tasks.py") if clicked == 0 else (st.switch_page("pages/2_Closing_Tasks.py") if clicked == 1 else None)

  st.subheader('Utilities')
  images = get_clickable_images(['inventory.jpg', 'service.jpeg'])
  with st.container():
        # Display clickable images in a flexbox layout
        clicked = clickable_images(
            images,
            titles=[f"Click here for tasks" for i in range(len(images))],
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
            img_style={"margin": "1%", "height": "200px", "width": "48%"}
        )
  c1, c2 = st.columns(2)
  c1.markdown("<div style='text-align: center;'><b>Inventory</b></div>", unsafe_allow_html=True)
  c2.markdown("<div style='text-align: center;'><b>Service Expectations</b></div>", unsafe_allow_html=True)
  if clicked > -1:
      st.switch_page("pages/3_Inventory.py") if clicked == 0 else (st.switch_page("pages/4_Service_Expectations.py") if clicked == 1 else None)




if __name__ == "__main__":
  main()
