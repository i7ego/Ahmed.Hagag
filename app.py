import requests
import streamlit as st
#from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="Ahmed Hagag", page_icon=":star:", layout="wide")


# def load_lottieurl(url):
#    r = requests.get(url)
#    if r.status_code != 200:
#        return None
#   return r.json()

# use local css


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ----load assits ----
# ottie_coding = load_lottieurl(
#    "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/Untitled.jpg")
img_lottie_animation = Image.open("images/Untitled1.jpg")
img_me = Image.open("images/work.jpg")

# -------- Header -----
with st.container():
    st.subheader("Hi,I am Ahmed Hagag :wave:")
    st.title("My Webpage")
    st.write(" I'm a web developer with in-depth experience in UI/UX design. In a nutshell, I create websites that help organizations address business challenges and meet their needs. I manage everything from website navigation and layout to a company's web hosting and security architecture. My expertise lies within front-end web apps, and the main languages in my tech stack are JavaScript, React, and of course HTML/CSS. I’m a lifelong learner (currently taking a course on building AI chatbots with Python!) and love to read, run, and find new bubble tea shops in Cairo City.  ")
    st.write("[Learn More >](https://i7ego.github.io/Portfolio/)")

# -------what i do----

with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        """
            I can do many things like
            - I can make web site by JS and Python,
            - I can make desktop program by python,
            - I can make a Penetration test for you web site,
            - I can make scan for you network and vulnerabilities discovered,
            - I can fixed your system os like windows , linux and ios.
            """
    with right_column:
        st.image(img_me)


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Currency-Conversion")
        st.write(
            """
            I used in this project to bring a currency converter API, it's constantly being updated
            """
        )
        st.markdown(
            "[See More...](https://i7ego.github.io/Currency-Conversion)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Youtube Downloader")
        st.write("""
        I created this web site by HTML, css , JavaScript you can download videos from youtube and convert it to mp4 and mp3 """
                 )
        st.markdown("[See more...](https://i7ego.github.io/youtubedownload/)")
# -----COntact---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
# Document
    contact_form = """
    <form action="https://fabform.io/f/pc33wkP" method="POST">
        <input type="text" name="First Name" placeholder="Your  First Name" required >
        <input type="text" name="Last Name" placeholder="Your Last Name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>  
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
