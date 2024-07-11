import streamlit as st

st.set_page_config(
    page_title="Offers",
    page_icon="🗒️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def display_offer(name, when, desc):
    with st.container(border = True):
        st.header(f":blue[{name}]", divider = 'blue')
        st.header(when)
        st.subheader(desc)

if __name__ == "__main__":
    st.header('Offers and Discounts', divider = 'grey')
    c1, c2, c3 = st.columns(3, vertical_alignment = 'top')
    with c1:
        display_offer('Buy 1 Get 1', 'Tuesday to Thursday', 'Buy 1 Get 1 free burger')
    with c2:
        display_offer('Beer Discount', 'Friday to Sunday', '50% Flat off on Tap Beer')
    with c3:
        display_offer('Happy Hour', 'All days 4-7 pm', 'Description')

    c1, c2 = st.columns(2, vertical_alignment = 'top')
    with c1:
        display_offer('Kids Day!', 'Sunday 4 pm', 'Kids Movie & Kids Eat for free')
    with c2:
        display_offer('Footy Screening', 'Friday 6:30 pm', 'Description')
