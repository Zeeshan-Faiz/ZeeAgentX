import streamlit as st
from utils.api_utils import upload_document, list_documents, delete_document

def display_sidebar():
    # Add custom CSS for sidebar styling
    st.markdown("""
    <style>
    /* Sidebar glassmorphic styling */
    .stSidebar > div:first-child {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.08) 0%, 
            rgba(255, 215, 0, 0.05) 50%, 
            rgba(255, 248, 220, 0.03) 100%);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    /* Dark mode sidebar */
    @media (prefers-color-scheme: dark) {
        .stSidebar > div:first-child {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.12) 0%, 
                rgba(255, 140, 0, 0.08) 50%, 
                rgba(255, 215, 0, 0.05) 100%);
        }
        
        .sidebar-header {
            color: #ffffff !important;
            background: linear-gradient(135deg, #FFB347, #FFD700);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
    }
    
    /* Light mode sidebar */
    @media (prefers-color-scheme: light) {
        .sidebar-header {
            color: #FF8C00 !important;
            background: linear-gradient(135deg, #FF8C00, #FFB347);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
    }
    
    /* Uniform header styling */
    .sidebar-header {
        font-size: 18px !important;
        font-weight: 600 !important;
        font-family: "Segoe UI", "Inter", -apple-system, BlinkMacSystemFont, sans-serif !important;
        margin-bottom: 10px !important;
        text-shadow: 0 2px 4px rgba(255, 165, 0, 0.2);
        letter-spacing: 0.5px;
    }
    
    /* Glassmorphic button styles */
    .stButton > button {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.1) 0%, 
            rgba(255, 215, 0, 0.08) 100%) !important;
        border: 1px solid rgba(255, 165, 0, 0.3) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        color: #FF8C00 !important;
        font-weight: 500 !important;
        font-family: "Segoe UI", sans-serif !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 2px 8px rgba(255, 165, 0, 0.1) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.2) 0%, 
            rgba(255, 215, 0, 0.15) 100%) !important;
        border: 1px solid rgba(255, 165, 0, 0.5) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 165, 0, 0.2) !important;
        color: #FF6347 !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
        box-shadow: 0 2px 8px rgba(255, 165, 0, 0.15) !important;
    }
    
    /* Dark mode button adjustments */
    @media (prefers-color-scheme: dark) {
        .stButton > button {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.15) 0%, 
                rgba(255, 215, 0, 0.12) 100%) !important;
            color: #FFD700 !important;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.25) 0%, 
                rgba(255, 215, 0, 0.2) 100%) !important;
            color: #FFFFFF !important;
        }
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: rgba(255, 165, 0, 0.05) !important;
        border: 1px solid rgba(255, 165, 0, 0.2) !important;
        border-radius: 8px !important;
        backdrop-filter: blur(4px) !important;
    }
    
    /* Comprehensive File uploader styling */
    .stFileUploader > div {
        background: rgba(255, 165, 0, 0.05) !important;
        border: 2px dashed rgba(255, 165, 0, 0.3) !important;
        border-radius: 8px !important;
        backdrop-filter: blur(4px) !important;
    }
    
    /* File uploader drag area */
    .stFileUploader > div > div {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.08) 0%, 
            rgba(255, 215, 0, 0.05) 100%) !important;
        border: 2px dashed rgba(255, 165, 0, 0.4) !important;
        border-radius: 8px !important;
        backdrop-filter: blur(6px) !important;
        transition: all 0.3s ease !important;
    }
    
    /* File uploader on hover */
    .stFileUploader > div > div:hover {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.12) 0%, 
            rgba(255, 215, 0, 0.08) 100%) !important;
        border: 2px dashed rgba(255, 165, 0, 0.6) !important;
        transform: translateY(-1px) !important;
    }
    
    /* File uploader text */
    .stFileUploader > div > div > div {
        color: #FF8C00 !important;
        font-weight: 500 !important;
        font-family: "Segoe UI", sans-serif !important;
    }
    
    /* File uploader button */
    .stFileUploader button {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.15) 0%, 
            rgba(255, 215, 0, 0.12) 100%) !important;
        border: 1px solid rgba(255, 165, 0, 0.4) !important;
        border-radius: 6px !important;
        color: #FF8C00 !important;
        font-weight: 500 !important;
        backdrop-filter: blur(4px) !important;
        transition: all 0.3s ease !important;
    }
    
    /* File uploader button hover */
    .stFileUploader button:hover {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.25) 0%, 
            rgba(255, 215, 0, 0.2) 100%) !important;
        border: 1px solid rgba(255, 165, 0, 0.6) !important;
        color: #FF6347 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(255, 165, 0, 0.15) !important;
    }
    
    /* File uploader when file is selected */
    .stFileUploader [data-testid="stFileUploaderFileName"] {
        background: rgba(255, 165, 0, 0.1) !important;
        border: 1px solid rgba(255, 165, 0, 0.3) !important;
        border-radius: 6px !important;
        color: #FF8C00 !important;
        font-weight: 500 !important;
        padding: 4px 8px !important;
        backdrop-filter: blur(4px) !important;
    }
    
    /* Dark mode file uploader adjustments */
    @media (prefers-color-scheme: dark) {
        .stFileUploader > div > div {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.12) 0%, 
                rgba(255, 215, 0, 0.08) 100%) !important;
            border-color: rgba(255, 165, 0, 0.5) !important;
        }
        
        .stFileUploader > div > div:hover {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.18) 0%, 
                rgba(255, 215, 0, 0.12) 100%) !important;
            border-color: rgba(255, 165, 0, 0.7) !important;
        }
        
        .stFileUploader > div > div > div {
            color: #FFD700 !important;
        }
        
        .stFileUploader button {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.2) 0%, 
                rgba(255, 215, 0, 0.15) 100%) !important;
            color: #FFD700 !important;
        }
        
        .stFileUploader button:hover {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.3) 0%, 
                rgba(255, 215, 0, 0.25) 100%) !important;
            color: #FFFFFF !important;
        }
        
        .stFileUploader [data-testid="stFileUploaderFileName"] {
            background: rgba(255, 165, 0, 0.15) !important;
            color: #FFD700 !important;
        }
    }
    
    /* Document text styling */
    .document-text {
        background: rgba(255, 165, 0, 0.08) !important;
        border-left: 3px solid rgba(255, 165, 0, 0.5) !important;
        padding: 8px 12px !important;
        border-radius: 0 8px 8px 0 !important;
        margin: 4px 0 !important;
        font-family: "Segoe UI", sans-serif !important;
        backdrop-filter: blur(4px) !important;
    }
    
    @media (prefers-color-scheme: dark) {
        .document-text {
            background: rgba(255, 165, 0, 0.12) !important;
            color: #ffffff !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar: Model Selection
    model_display_to_value = {
        "OpenAI GPT-4.1": "openai/gpt-4.1",
        "OpenAI GPT-4.1 Mini": "openai/gpt-4.1-mini",
        "OpenAI GPT-4o": "openai/gpt-4o",
        "OpenAI GPT-4o Mini": "openai/gpt-4o-mini"
    }

    st.sidebar.markdown('<h3 class="sidebar-header">Select Model</h3>', unsafe_allow_html=True)
    selected_display = st.sidebar.selectbox("", options=list(model_display_to_value.keys()), label_visibility="collapsed")
    st.session_state.model = model_display_to_value[selected_display]

    # Sidebar: Upload Document
    st.sidebar.markdown('<h3 class="sidebar-header">Upload Document</h3>', unsafe_allow_html=True)
    uploaded_file = st.sidebar.file_uploader("Choose a file", help="",label_visibility="collapsed")
    if uploaded_file is not None:
        if st.sidebar.button("Upload"):
            with st.spinner("Uploading..."):
                upload_response = upload_document(uploaded_file)
                if upload_response:
                    st.sidebar.success(f"File '{uploaded_file.name}' uploaded successfully with ID {upload_response['file_id']}.")
                    st.session_state.documents = list_documents()  # Refresh the list after upload

    # Sidebar: List Documents
    st.sidebar.markdown('<h3 class="sidebar-header"></h3>', unsafe_allow_html=True)
    if st.sidebar.button("Refresh Documents"):
        with st.spinner("Refreshing..."):
            st.session_state.documents = list_documents()

    # Initialize document list if not present
    if "documents" not in st.session_state:
        st.session_state.documents = list_documents()

    documents = st.session_state.documents
    if documents:
        for doc in documents:
            st.sidebar.markdown(f'<div class="document-text">📄 {doc["filename"]}</div>', unsafe_allow_html=True)
        
        # Delete Document
        st.sidebar.markdown('<h3 class="sidebar-header">Select Document to delete</h3>', unsafe_allow_html=True)
        selected_file_id = st.sidebar.selectbox("", options=[doc['id'] for doc in documents], format_func=lambda x: next(doc['filename'] for doc in documents if doc['id'] == x), label_visibility="collapsed")
        if st.sidebar.button("Delete Document"):
            with st.spinner("Deleting..."):
                delete_response = delete_document(selected_file_id)
                if delete_response:
                    st.sidebar.success(f"Document with ID {selected_file_id} deleted successfully.")
                    st.session_state.documents = list_documents()  # Refresh the list after deletion
                else:
                    st.sidebar.error(f"Failed to delete document with ID {selected_file_id}.")