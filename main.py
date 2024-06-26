import streamlit as st
import base64
from st_clickable_images import clickable_images

images = []
for file in ["logo.jpg", "opening.jpg"]:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/jpeg;base64,{encoded}")

# Create a container
with st.container():
    # Display clickable images in a flexbox layout
    clicked = clickable_images(
        images,
        titles=[f"Image #{str(i)}" for i in range(len(images))],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "1%", "height": "200px", "width": "48%"}
    )

st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

st.logo('logo.jpg')
st.header('FT Local Kitchen & Bar', divider = 'grey')
st.sidebar.header('FT Local Kitchen & Bar')

def main():
  with st.container(height = 200, border = None):
    col1, col2 = st.columns([1, 3])
    col1.image('logo.jpg')
    col2.image('banner.jpg')

  st.subheader('Daily Tasks')
  st.caption('Start your day with the opening tasks.')
  with st.container(height = 200, border = None):
    col1, col2 = st.columns(2)
    col1.image('opening.jpg', caption = 'Opening Tasks')
    col2.image('closing.jpg', caption = 'Closing Tasks')

  st.subheader('Utilities')
  with st.container(height = 200, border = None):
    col1, col2 = st.columns(2)
    col1.image('inventory.jpg', caption = 'Inventory')
    col2.image('service.jpeg', caption = 'Service Expectations')



if __name__ == "__main__":
  main()
