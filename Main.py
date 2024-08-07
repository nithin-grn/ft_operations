import streamlit as st
import base64
from st_clickable_images import clickable_images
from st_pages import show_pages_from_config
from auxillaries import *

st.set_page_config(
    page_title="FT Operations",
    page_icon="🗒️",
    layout="centered",
    initial_sidebar_state="expanded",
    # menu_items={
    #     # 'Get Help': 'https://www.extremelycoolapp.com/help',
    #     # 'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

st.logo('logo.jpg')
st.header('FT Local Kitchen & Bar', divider = 'grey')
st.sidebar.header('FT Local Kitchen & Bar')

reminders = []

      
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

def check_reminders():
  inv_reminder()

def inv_reminder():
  day = what_day(today_date_string())
  if day in ['Thursday', 'Sunday']:
    reminders.append('Please ensure to update the inventory today.')

def display_reminders():
  if len(reminders) > 0:
    with st.expander('Reminders ⚠️', expanded = True):
      st.info('\n\n'.join(reminders))
              

def main():
  # Path to your local image
  image_path = 'banner2.jpg'
  image_data = get_image_as_base64(image_path)
  
  # Display the image using HTML with the responsive class
  with st.container():
    st.markdown(f'<img src="data:image/jpeg;base64,{image_data}" alt="Responsive Image" class="responsive">', unsafe_allow_html=True)

  display_reminders()

  # st.subheader('Daily Tasks')
  # st.caption('Start your day with the opening tasks.')
  # c1, c2 = st.columns(2)
  # with c1:
  #   st.image('opening.jpg')
  #   st.page_link("pages/1_Opening_Tasks.py", label="Opening Tasks", icon="🌅", use_container_width = True)
  # with c2:
  #   st.image('closing.jpg')
  #   st.page_link("pages/2_Closing_Tasks.py", label="Closing Tasks", icon="🌇", use_container_width = True)
  
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
  c1.markdown("<div style='text-align: center;'><b>Offers and Discounts</b></div>", unsafe_allow_html=True)
  c2.markdown("<div style='text-align: center;'><b>Service Expectations</b></div>", unsafe_allow_html=True)
  if clicked > -1:
      st.switch_page("pages/3_Offers_and_Discounts.py") if clicked == 0 else (st.switch_page("pages/4_Service_Expectations.py") if clicked == 1 else None)


check_reminders()

@st.experimental_dialog("Today's reminders 🙂")
def disp_reminders():
    display_reminders()
    if st.button("Okay"):
        st.session_state.saw = True
        st.rerun()

if __name__ == "__main__":
  if "saw" not in st.session_state and len(reminders) > 0:
        disp_reminders()
  main()
