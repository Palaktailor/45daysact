# # pip install straemlit
# python lib 
# webpages for ml and data science projects 
# no requirement of html and css
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt
import time 

st.set_page_config(
    page_title= "streamlit function demo",
    page_icon= "😁",              # stream lit icon 
    layout= "centered"
)

# title and text elements
st.title("hello world")
st.header("1. text elements")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,'code'text")
st.code("print('hi beautiful')",language= "python")
st.latex(r"a^2+b^2 = c^2") # to show formula
st.divider() # ye line kheck dega

##metrics and messages
st.header("2.metrics and messages")

st.metric(label = "revenue" , value = 1234,delta = "+10%" , delta_color = "inverse") # --normal 
st.error("this is a warning message")
st.info( " this is a info message")
st.success( " this is a success message")
st.exception( ValueError(" this is a exception message"))

st.divider()

st.header("data display")
df = pd.DataFrame(np.random.randn(10,2),columns = ["a","b"])
st.dataframe(df)
st.table(df.head(5))
st.json(df.to_dict())

st.divider()

#charts 
st.header({"4.CHARTS"})
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x='index' , y = 'a')
st.altair_chart(chart,use_container_width = True )
fig, ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()
## make a ui for the dataset used bikes using streamlit
##Widgets
st.header("S.widgets")
with st.form("input form"):
#   password = st.
  name = st.text_input("Enter your name :")
  age = st.number_input("Enter your age:")
  mood = st.radio("Select your mood ",{'happy', 'sad' , 'neutral'})
  languages = st.multiselect("Select your languages",{'English','hindi','french'}) ## you have to pass your inputs here in the tuple only
  submit =  st.form_submit_button("Submit")
  if submit :
     st.success(f"name :{name}, age : {age} , languages :{languages}, mood : {mood} ,")


##
# col1,col2 , col3 = st.columns(3)
col1,col2 , col3 = st.columns([2,1,1])
with col1:
    name = st.text_input("Enter your name :")
    age = st.number_input("Enter your age:")
with col2:
     mood = st.radio("Select your mood ",{'happy', 'sad' , 'neutral'})
     languages = st.multiselect("Select your languages",{'English','hindi','french'})
with col3:
    st.success(f"moood :{mood}")
    

    #we can divide form into multiple columns
    # for that first define form then columns

# with st.form("input form"):
#     col1,col2 , col3 = st.columns([2,1,1])
#     with col1:
#        name = st.text_input("Enter your name :")
#        age = st.number_input("Enter your age:")
#     with col2:
#         mood = st.radio("Select your mood ",{'happy', 'sad' , 'neutral'})
#         languages = st.multiselect("Select your languages",{'English','hindi','french'})
#     with col3:
#        st.success(f"moood :{mood}")
#     if submit :
#         st.success(f"name :{name}, age : {age} , languages :{languages}, mood : {mood} ,")
    
# 
col11 , col12 = st.columns(2)
with col11:
    number = st.slider("Select a number",0,100)
with col12:
    colour = st.color_picker("Select colour")


st.text_area("Enter your message ")
st.date_input("Select a date ")
st.time_input("select a time ")
st.file_uploader("upload your file ")
st.divider()

##media
st.header("6,media")
st.image("C:/Users/user/Downloads/download (15).jpg", caption = "goals", width = 100) ## use always forward slash(/)
st.video("C:/Users/user/OneDrive/Pictures/Snapchat-1537646748.mp4" , width = 200)
# st.audio()


## sidebar and input

st.sidebar.header("sidebar header")
st.sidebar.write("this is a sidebar text")
st.sidebar.button("click me")
option = st.sidebar.selectbox("select an option" , {"option 1","option 2"})

with st.container():
    st.write("this is a container")

with st.expander("expander header"):
    st.write("this is expander header")

with st.spinner("loading data ..."):
    time.sleep(3)
    # st.success("data loaded")
    st.toast("toast message",icon = "✌️")

st.page_link("https://streamlit.io/", label = "streamlit website" , icon = "👌")

