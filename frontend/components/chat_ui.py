import streamlit as st
from utils.api_utils import get_api_response

def display_chat_interface():
    # Add custom CSS for chat input styling
    st.markdown("""
    <style>
    /* Chat input container styling */
    .stChatInput > div {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.08) 0%, 
            rgba(255, 215, 0, 0.05) 50%, 
            rgba(255, 248, 220, 0.03) 100%) !important;
        border: 1.5px solid rgba(255, 165, 0, 0.3) !important;
        border-radius: 25px !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 15px rgba(255, 165, 0, 0.1) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Chat input field - Enhanced targeting */
    .stChatInput input,
    .stChatInput textarea,
    .stChatInput > div > div > div > div > input,
    .stChatInput [data-testid="stChatInput"] input {
        background: transparent !important;
        border: none !important;
        color: #333333 !important;
        font-family: "Segoe UI", "Inter", -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-size: 15px !important;
        padding: 12px 20px !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    .stChatInput input::placeholder,
    .stChatInput textarea::placeholder,
    .stChatInput > div > div > div > div > input::placeholder {
        color: rgba(255, 140, 0, 0.7) !important;
        font-weight: 500 !important;
    }
    
    /* Remove any blue focus states */
    .stChatInput input:focus,
    .stChatInput textarea:focus,
    .stChatInput > div > div > div > div > input:focus {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    /* Chat input hover effect */
    .stChatInput > div:hover {
        border: 1.5px solid rgba(255, 165, 0, 0.5) !important;
        box-shadow: 0 6px 25px rgba(255, 165, 0, 0.15) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Chat input focus effect */
    .stChatInput > div:focus-within {
        border: 1.5px solid rgba(255, 165, 0, 0.6) !important;
        box-shadow: 
            0 6px 25px rgba(255, 165, 0, 0.2) !important,
            0 0 0 3px rgba(255, 165, 0, 0.1) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Send button styling */
    .stChatInput button {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.9) 0%, 
            rgba(255, 140, 0, 0.8) 100%) !important;
        border: none !important;
        border-radius: 50% !important;
        color: white !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 2px 8px rgba(255, 165, 0, 0.3) !important;
    }
    
    .stChatInput button:hover {
        background: linear-gradient(135deg, 
            rgba(255, 140, 0, 1) 0%, 
            rgba(255, 165, 0, 0.9) 100%) !important;
        transform: scale(1.05) !important;
        box-shadow: 0 4px 15px rgba(255, 165, 0, 0.4) !important;
    }
    
    .stChatInput button:active {
        transform: scale(0.98) !important;
    }
    
    /* Dark mode adjustments */
    @media (prefers-color-scheme: dark) {
        .stChatInput > div {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.12) 0%, 
                rgba(255, 140, 0, 0.08) 50%, 
                rgba(255, 215, 0, 0.05) 100%) !important;
            border: 1.5px solid rgba(255, 165, 0, 0.4) !important;
        }
        
        .stChatInput input,
        .stChatInput textarea,
        .stChatInput > div > div > div > div > input {
            color: #ffffff !important;
            background: transparent !important;
        }
        
        .stChatInput input::placeholder,
        .stChatInput textarea::placeholder,
        .stChatInput > div > div > div > div > input::placeholder {
            color: rgba(255, 215, 0, 0.8) !important;
        }
        
        .stChatInput input:focus,
        .stChatInput textarea:focus,
        .stChatInput > div > div > div > div > input:focus {
            background: transparent !important;
            box-shadow: none !important;
        }
        
        .stChatInput > div:hover {
            border: 1.5px solid rgba(255, 165, 0, 0.6) !important;
            box-shadow: 0 6px 25px rgba(255, 165, 0, 0.2) !important;
        }
        
        .stChatInput > div:focus-within {
            border: 1.5px solid rgba(255, 215, 0, 0.7) !important;
            box-shadow: 
                0 6px 25px rgba(255, 165, 0, 0.25) !important,
                0 0 0 3px rgba(255, 215, 0, 0.15) !important;
        }
    }
    
    /* Chat message styling enhancements */
    .stChatMessage {
        border-radius: 15px !important;
        margin-bottom: 10px !important;
    }
    
    /* User message styling */
    .stChatMessage[data-testid*="user"] {
        background: linear-gradient(135deg, 
            rgba(255, 165, 0, 0.08) 0%, 
            rgba(255, 215, 0, 0.05) 100%) !important;
        border: 1px solid rgba(255, 165, 0, 0.2) !important;
        backdrop-filter: blur(5px) !important;
        -webkit-backdrop-filter: blur(5px) !important;
    }
    
    /* Assistant message styling */
    .stChatMessage[data-testid*="assistant"] {
        background: linear-gradient(135deg, 
            rgba(255, 248, 220, 0.1) 0%, 
            rgba(255, 228, 181, 0.05) 100%) !important;
        border: 1px solid rgba(255, 165, 0, 0.15) !important;
        backdrop-filter: blur(5px) !important;
        -webkit-backdrop-filter: blur(5px) !important;
    }
    
    @media (prefers-color-scheme: dark) {
        .stChatMessage[data-testid*="user"] {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.12) 0%, 
                rgba(255, 140, 0, 0.08) 100%) !important;
            border: 1px solid rgba(255, 165, 0, 0.25) !important;
        }
        
        .stChatMessage[data-testid*="assistant"] {
            background: linear-gradient(135deg, 
                rgba(255, 215, 0, 0.08) 0%, 
                rgba(255, 248, 220, 0.05) 100%) !important;
            border: 1px solid rgba(255, 215, 0, 0.2) !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display message history with custom avatars
    for message in st.session_state.messages:
        avatar = "🧑‍💻" if message["role"] == "user" else "🐦‍🔥"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Input box
    if prompt := st.chat_input("Ask anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(prompt)

        with st.spinner("Thinking..."):
            response = get_api_response(prompt, st.session_state.session_id, st.session_state.model)

            if response:
                st.session_state.session_id = response.get("session_id")
                st.session_state.messages.append({"role": "assistant", "content": response["answer"]})
                with st.chat_message("assistant", avatar="🐦‍🔥"):
                    st.markdown(response["answer"])
            else:
                st.error("Failed to get a response from the API. Please try again.")