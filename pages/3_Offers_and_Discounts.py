import streamlit as st

def display_offer(name, when, desc):
    with st.container(border = True):
        st.title(name)
        st.divider()
        st.header(when)
        st.subheader(desc)

if __name__ == "__main__":
    st.header('Offers and Discounts')
    c1, c2 = st.columns(2)
    with c1:
        display_offer('Buy 1 Get 1', 'Tuesday to Thursday', 'Buy 1 Get 1 free burger')
    with c2:
        display_offer('Beer Discount', 'Friday to Sunday', '50% Flat off on Tap Beer')
