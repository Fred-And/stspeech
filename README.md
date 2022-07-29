# Speech Recognition WebApp

## This is a Speech recognition WebApp focused on the aviation segment.

The main goal of this application is to develop a friendly environment for the pilot to learn everything he/she needs to know before start flying and talking with the ATC.

### Streamlit

For this application I'm using a Python framework called Streamlit, which allows me to easily create, host and deploy a website on the internet using Python. It's focus is the Data Science segment, but as I was already familiar with it's structure, I ended up choosing it and adapting all the functions for my need.

### HTML & CSS

I found that even though Streamlit is a powerful tool, I could do it better using HTML and CSS, thats why the majority of Streamlit functions I call are ``` st.markdown() ```. This function through ```unsafe_allow_html=True``` allows me to basically write a HTML/CSS code as a string and it'll read as if it was actually a HTML/CSS. This way I was able to achieve a better looking website.
