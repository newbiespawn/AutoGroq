import streamlit as st 
from agent_management import display_agents
from ui_utils import    display_discussion_and_whiteboard, display_download_button, display_user_input, display_rephrased_request, display_reset_and_upload_buttons, display_user_request_input


def main(): 
    st.markdown("""
        <style>
        /* General styles */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }

        /* Sidebar styles */
        .sidebar .sidebar-content {
            background-color: #ffffff !important;
            padding: 20px !important;
            border-radius: 5px !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
        }

        .sidebar .st-emotion-cache-k7vsyb h1 {
            font-size: 12px !important;
            font-weight: bold !important;
            color: #007bff !important;
        }

        .sidebar h2 {
            font-size: 16px !important;
            color: #666666 !important;
        }

        .sidebar .stButton button {
            display: block !important;
            width: 100% !important;
            padding: 10px !important;
            background-color: #007bff !important;
            color: #ffffff !important;
            text-align: center !important;
            text-decoration: none !important;
            border-radius: 5px !important;
            transition: background-color 0.3s !important;
        }

        .sidebar .stButton button:hover {
            background-color: #0056b3 !important;
        }

        .sidebar a {
            display: block !important;
            color: #007bff !important;
            text-decoration: none !important;
        }

        .sidebar a:hover {
            text-decoration: underline !important;
        }

        /* Main content styles */
        .main .stTextInput input {
            width: 100% !important;
            padding: 10px !important;
            border: 1px solid #cccccc !important;
            border-radius: 5px !important;
        }

        .main .stTextArea textarea {
            width: 100% !important;
            padding: 10px !important;
            border: 1px solid #cccccc !important;
            border-radius: 5px !important;
            resize: none !important;
        }

        .main .stButton button {
            padding: 10px 20px !important;
            background-color: #dc3545 !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 5px !important;
            cursor: pointer !important;
            transition: background-color 0.3s !important;
        }

        .main .stButton button:hover {
            background-color: #c82333 !important;
        }

        .main h1 {
            font-size: 32px !important;
            font-weight: bold !important;
            color: #007bff !important;
        }

        /* Model selection styles */
        .main .stSelectbox select {
            width: 100% !important;
            padding: 10px !important;
            border: 1px solid #cccccc !important;
            border-radius: 5px !important;
        }

        /* Error message styles */
        .main .stAlert {
            color: #dc3545 !important;
        }
        </style>
        """, unsafe_allow_html=True)
    
    model_token_limits = { 
        'mixtral-8x7b-32768': 32768, 
        'llama3-70b-8192': 8192, 
        'llama3-8b-8192': 8192, 
        'gemma-7b-it': 8192 
    } 
    
    col1, col2, col3 = st.columns([2, 5, 3]) 
    with col3: 
        selected_model = st.selectbox( 
            'Select Model', 
            options=list(model_token_limits.keys()), 
            index=0, 
            key='model_selection' 
        ) 
        st.session_state.model = selected_model 
        st.session_state.max_tokens = model_token_limits[selected_model] 
        
    st.title("AutoGroq") 
        
    # Ensure default values for session state are set     
    if "discussion" not in st.session_state: 
        st.session_state.discussion = ""
    if "whiteboard" not in st.session_state: 
        st.session_state.whiteboard = "" # Apply CSS classes to elements 
    
    with st.sidebar: 
        st.markdown('<div class="sidebar">', unsafe_allow_html=True) 
        st.markdown('</div>', unsafe_allow_html=True) 

    display_agents() 
    
    with st.container(): 
        st.markdown('<div class="main">', unsafe_allow_html=True) 
        display_user_request_input() 
        display_rephrased_request() 
        st.markdown('<div class="discussion-whiteboard">', unsafe_allow_html=True) 
        display_discussion_and_whiteboard() 
        st.markdown('</div>', unsafe_allow_html=True) 
        st.markdown('<div class="user-input">', unsafe_allow_html=True) 
        display_user_input() 
        st.markdown('</div>', unsafe_allow_html=True) 
        display_reset_and_upload_buttons() 
        st.markdown('</div>', unsafe_allow_html=True) 

    display_download_button()        
    
if __name__ == "__main__": 
    main()