import streamlit as st
from streamlit_chat import message
from streamlit_Utilities import *

openapi_key = st.secrets["open_ai_key"]
# openai.api_key = api_key.key
openai.api_key = openapi_key

SerpAPIWrapper.serp_api_key = st.secrets["serp_api_key"]

# from instadev import *
if 'instagram' not in st.session_state:
    st.session_state['instagram'] = []
    st.session_state['instagramImage'] = []
if 'twitter' not in st.session_state:
    st.session_state['twitter'] = []
    st.session_state['twitterImage'] = []
if 'facebook' not in st.session_state:
    st.session_state['facebook'] = []
    st.session_state['faceebokImage'] = []
if 'linkedin' not in st.session_state:
    st.session_state['linkedin'] = []
    st.session_state['linkedinImage'] = []
if 'blogPost' not in st.session_state:
    st.session_state['blogPost'] = []
    st.session_state['blogImage'] = []
    st.session_state['blogTitle'] = []
    st.session_state['blogStructure'] = []
    st.session_state['blogContent'] = []
    st.session_state['blogSEO'] = []
    st.session_state['blogLinks'] = []
#intiallze state
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked=False
def callback():
    st.session_state.button_clicked=True
st.title('Content Generator Demo')
prompt = st.text_input('Write your prompt to generate the social media content')

insta_button, twitter_button, facebook_button, linkedIn_button, blog_Title,blog_structure,blog_content,blog_image,blog_SEO,blog_Links = st.columns(10)

if prompt:
    with insta_button:
        if st.button("Instagram"):
            st.session_state['instagram'] = generate_Instagram_content(prompt)
            instaRefineText=TextRefine(prompt)
            st.session_state['instagramImage']=generate_thumbnail_background(instaRefineText)
            # newRespone=TextRefine(prompt)
    with twitter_button:
        if st.button("XTweet"):
            st.session_state['twitter'] = generate_Twitter_content(prompt)
            twiitwerRefineText=TextRefine(prompt)
            st.session_state['twitterImage']=generate_thumbnail_background(twiitwerRefineText)
            # newRespone=TextRefine(prompt)

    with facebook_button:
        if st.button("FaceBook"):
            text= generate_Facebook_content(prompt)
            #removing left emojis
            st.session_state['facebook'] =remove_emojis(text)
            fbRefineText=TextRefine(prompt)
            st.session_state['faceebokImage']=generate_thumbnail_background(fbRefineText)
            # newRespone=TextRefine(prompt)
    with linkedIn_button:
        if st.button("LinkedIn"):
            text=generate_LinkedIn_content(prompt)
            st.session_state['linkedin'] =remove_emojis(text)
            linkedinRefineText=TextRefine(prompt)
            st.session_state['linkedinImage']=generate_thumbnail_background(linkedinRefineText)
            # newRespone=TextRefine(prompt)
    # with blog_Title:
    #     if st.button("Blog Title   "):
    #         st.session_state['blogTitle']=blogMultiTitleGenerator(prompt)
    #         # response_dict = eval(st.session_state['blogTitle'])
    # with blog_structure:
    #     if st.button("Blog Strcuture        "):
    #         st.session_state['blogStructure'] = generate_Blog_Structure(prompt)
    # with blog_content:
    #     if st.button("Blog Content       "):
    #         st.session_state['blogContent'] = generate_Blog_Content(prompt, st.session_state['blogStructure'])
    # with blog_SEO:
    #     if st.button("Blog SEO        "):
    #         st.session_state['blogSEO']=generate_Blog_SEO(prompt)
    # with blog_image:
    #     if st.button("Blog Image        "):
    #         blogRefineText=blogMultiPromptGenerator(prompt,st.session_state['blogContent'])
    #         st.session_state['blogImage']=generate_multi_thumbnail_background(blogRefineText)
    # with blog_Links:
    #     if st.button("Blog Links"):
    #         blogLink=topic_generate(prompt)
    #         st.session_state['blogLinks']=blog_repo_links(blogLink)
if prompt:
    with blog_Title:
        if st.button("Blog Title"):
            st.session_state['blogTitle']=blogMultiTitleGenerator(prompt)
            # response_dict = eval(st.session_state['blogTitle'])
    with blog_structure:
        if st.button("Blog Strcuture"):
            st.session_state['blogStructure'] = generate_Blog_Structure(prompt)
    with blog_content:
        if st.button("Blog Content"):
            st.session_state['blogContent'] = generate_Blog_Content(prompt, st.session_state['blogStructure'])
    with blog_SEO:
        if st.button("Blog SEO"):
            st.session_state['blogSEO']=generate_Blog_SEO(prompt)
    with blog_image:
        if st.button("Blog Image"):
            blogRefineText=blogMultiPromptGenerator(prompt,st.session_state['blogContent'])
            st.session_state['blogImage']=generate_multi_thumbnail_background(blogRefineText)

if st.session_state['twitter']:
    st.write("Twitter")
    message(st.session_state['twitter'])
    st.image(st.session_state['twitterImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)
if st.session_state['instagram']:
    st.write("Instagram")
    message(st.session_state['instagram'])
    st.image(st.session_state['instagramImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)
if st.session_state['facebook']:
    st.write("Facebook")
    message(st.session_state['facebook'])
    st.image( st.session_state['faceebokImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)
if st.session_state['linkedin']:
    st.write("LinkedIn")
    message(st.session_state['linkedin'])
    st.image(st.session_state['linkedinImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)
if st.session_state['blogTitle']:
    st.write("Blog Title")
    for i in range(0,5):
        message(st.session_state['blogTitle'][i])
if st.session_state['blogStructure']:
    st.write("Blog Structure")
    message(st.session_state['blogStructure'])
if st.session_state['blogContent']:
    st.write("Blog Content")
    message(st.session_state['blogContent'])
if st.session_state['blogImage']:
    st.write("Blog Image")
    for i in range(0,3): 
        st.image(st.session_state['blogImage'][i],caption='Generated Image',use_column_width=True)
if st.session_state['blogSEO']:
    st.write("Blog SEO")
    message(st.session_state['blogSEO'])
# if st.session_state['blogLinks']:
#     st.write("Blog Links")
#     message(st.session_state['blogLinks'])