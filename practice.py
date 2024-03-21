import streamlit as st

# Display Lottie animation
st.sidebar.markdown(
    """
    <style>
        #lottie-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 100px;
            height: 100px;
        }
    </style>
    """
    , unsafe_allow_html=True
)

st.sidebar.text("Your Streamlit App")

st.sidebar.markdown(
    """
    <div id="lottie-container">
        <script src="https://cdn.jsdelivr.net/npm/@lottiefiles/lottie-player.js"></script>
        <lottie-player
            id="lottie-player"
            src="https://assets5.lottiefiles.com/packages/lf20_BrL2CZ.json"
            background="transparent"
            speed="1"
            style="width: 100%; height: 100%;"
            loop
            autoplay
        ></lottie-player>
    </div>
    """
    , unsafe_allow_html=True
)
