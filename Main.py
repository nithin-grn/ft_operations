import streamlit as st
import base64
from st_clickable_images import clickable_images
from st_pages import show_pages_from_config

st.logo('logo.jpg')
st.header('FT Local Kitchen & Bar', divider = 'grey')
st.sidebar.header('FT Local Kitchen & Bar')


show_pages_from_config(".streamlit/pages_sections.toml")

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('styles.css')

# Add JavaScript to detect mobile view and show a message
st.markdown("""
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        function checkScreenSize() {
            if (window.innerWidth <= 768) {
                document.getElementById('overlay').style.display = 'block';
            } else {
                document.getElementById('overlay').style.display = 'none';
            }
        }
        checkScreenSize();
        window.addEventListener('resize', checkScreenSize);
    });
    </script>
    """, unsafe_allow_html=True)

# Add custom CSS for the overlay message
st.markdown("""
    <style>
    #overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        text-align: center;
        z-index: 9999;
        display: none;
    }
    #overlay-content {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    </style>
    """, unsafe_allow_html=True)

# HTML for the overlay message
st.markdown("""
    <div id="overlay">
        <div id="overlay-content">
            <h1>Desktop Only</h1>
            <p>This application is only available on desktop devices. Please switch to a desktop view.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
        

def main():
  # Path to your local image
  image_path = 'banner2.jpg'
  image_data = get_image_as_base64(image_path)
  
  # Display the image using HTML with the responsive class
  with st.container():
    st.markdown(f'<img src="data:image/jpeg;base64,{image_data}" alt="Responsive Image" class="responsive">', unsafe_allow_html=True)

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
