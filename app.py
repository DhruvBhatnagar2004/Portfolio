import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottie(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
   
local_css("styles/style.css")


lottie_coding=load_lottie("https://lottie.host/74e75ddc-c992-48cb-9a78-97debf4ce1ab/Iq40Zo4Oeq.json")
img_landing=Image.open('images/landingpage.png')
img_teach=Image.open('images/teachboardonline.png')
img_game=Image.open('images/game.png')
img_data=Image.open('images/data.png')

with st.container():
    st.header("Hi, I am Dhruv Bhatnagar 🎯")
    st.title("A Python Developer From India")
    st.write("Passionate coder with a interest on Data Analysis and Machine Learning. Eager to begin a career as a Python developer to grow and apply skills.")
    st.write("[Learn More>](https://github.com/DhruvBhatnagar2004)")

with st.container():
    st.write("---")
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            '''
            -Passionate BCA Student: Dedicated to data science analysis and visualization.
            
            -Multi-Language Proficiency: Skilled in C, C++, Java, HTML, and Python, with a focus on Python for its simplicity and versatility.
            
            -ML and AI Enthusiast: Aspires to pioneer intelligent systems and predictive models, seeing ML and AI as drivers of innovation.
            
            -Continuous Learner: Actively seeks growth in data science, ML, and AI, recognizing them as leading-edge technologies.
            
            -Networking Pro: Open to connecting with professionals for collaboration and opportunities in data science, ML, and AI.
            '''
        )
        st.write("[Learn More>](https://www.linkedin.com/in/dhruv-bhatnagar-59434b29a/)")
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")    

# Showcase Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_landing)
    
    with text_column:
        st.subheader("A MultiModal Voice Assistant")
        st.write(
            """
            -Worked in a team of four in the development of a multimodal virtual assistant.
            
            -Spearheaded the AI component, collaborating and utilizing Gemini API keys.
            
            -Engineered a robust model capable of generating coherent responses to user queries.
            """
        )
        st.write("[Learn More>](https://github.com/DhruvBhatnagar2004/AirHub)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_teach)
    
    with text_column:
        st.subheader("TeachBoardOnline")
        st.write(
            """
            -Solved the issue of absence of digital boards in online classes improving teaching effectiveness.
            
            -Enhanced TeachBoardOnline with Python, sockets, OpenCV, and MediaPipe for real-time teaching solutions.
            
            -Streamlined IP address management and data serialization for efficient content delivery.
            """
        )
        st.write("[Learn More>](https://github.com/DhruvBhatnagar2004/TeachBoardOnline)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_game)
    
    with text_column:
        st.subheader("2D MultiLevel Game")
        st.write(
            """
            -Played a pivotal role as a level designer and game developer in a hackathon project and increased the productivity by 75%.
            
            -Designed and developed multiple levels, including player mechanics, movements, and scoring systems.
            
            -Demonstrated proficiency in game development tools and techniques, resulting in a fully functional 2D multilevel game.
            """
        )
        st.write("[Learn More>](https://github.com/DhruvBhatnagar2004/JAMSHACK-Hackathon)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_data)
    
    with text_column:
        st.subheader("Web Scrapper")
        st.write(
            """
            -Independently developed a Python web scraper utilizing requests, Beautiful Soup, and Pandas.
            
            -Extracted data from Wikipedia to compile information on top companies.
            
            -Organized and presented data in a structured tabular format, enhancing accessibility and analysis capabilities.
            """
        )
        st.write("[Learn More>](https://github.com/DhruvBhatnagar2004/Web-Scrapper)")
        
#connect
with st.container():
    st.write("---")
    st.header("Connect With Me")
    st.write("##")
    github_url = "https://github.com/DhruvBhatnagar2004"
    linkedin_url = "https://www.linkedin.com/in/dhruv-bhatnagar-59434b29a/"

    # Display GitHub icon and button
    github_icon = "github.png"  # Example GitHub icon URL
    st.image(github_icon, width=50)
    st.link_button("Connect on GitHub", github_url)
    
    
    # Display LinkedIn icon and button
    linkedin_icon = "linkedin.png"  # Example LinkedIn icon URL
    st.image(linkedin_icon, width=50)
    st.link_button("Connect on LinkedIn", linkedin_url)

        
        
#contact me
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
    
    contact_form= """
     <form action="https://formsubmit.co/dhruvbhat1k@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
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
        
