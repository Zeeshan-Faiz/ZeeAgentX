import streamlit as st
from components.sidebar import display_sidebar
from components.chat_ui import display_chat_interface

st.markdown(
    """
    <style>
    @media (prefers-color-scheme: dark) {
        .themed-box {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.15) 0%, 
                rgba(255, 140, 0, 0.12) 50%, 
                rgba(255, 215, 0, 0.08) 100%);
            border: 1px solid rgba(255, 165, 0, 0.3);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 
                0 8px 32px rgba(255, 165, 0, 0.1),
                inset 0 1px 0 rgba(255, 215, 0, 0.2);
            color: #ffffff;
        }
        
        .themed-box h1 {
            background: linear-gradient(135deg, #FFB347, #FFD700, #FF8C00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 20px rgba(255, 165, 0, 0.3);
        }
        
        .themed-box p {
            background: linear-gradient(135deg, #FFB347, #FFD700, #FF8C00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 15px rgba(255, 165, 0, 0.2);
            opacity: 0.85;
        }
    }
    
    @media (prefers-color-scheme: light) {
        .themed-box {
            background: linear-gradient(135deg, 
                rgba(255, 165, 0, 0.08) 0%, 
                rgba(255, 215, 0, 0.06) 50%, 
                rgba(255, 248, 220, 0.12) 100%);
            border: 1px solid rgba(255, 165, 0, 0.25);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            box-shadow: 
                0 4px 20px rgba(255, 165, 0, 0.08),
                inset 0 1px 0 rgba(255, 255, 255, 0.4);
            color: #2c2c2c;
        }
        
        .themed-box h1 {
            background: linear-gradient(135deg, #FF8C00, #FFB347, #FF6347);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 15px rgba(255, 140, 0, 0.2);
        }
        
        .themed-box p {
            background: linear-gradient(135deg, #FF8C00, #FFB347, #FF6347);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 12px rgba(255, 140, 0, 0.15);
            opacity: 0.8;
        }
    }
    
    .themed-box {
        position: relative;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .themed-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 215, 0, 0.1), 
            transparent);
        transition: left 0.5s;
    }
    
    .themed-box:hover::before {
        left: 100%;
    }
    
    .themed-box:hover {
        transform: translateY(-2px);
        box-shadow: 
            0 12px 40px rgba(255, 165, 0, 0.15),
            inset 0 1px 0 rgba(255, 215, 0, 0.3);
    }
    </style>
    <div class="themed-box" style='
        border-radius: 30px; 
        padding: 20px 30px; 
        margin-bottom: 15px; 
        text-align: center;
    '>
        <h1 style='
            font-family: "Segoe UI", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
            font-weight: 700;
            letter-spacing: -0.5px;
            margin-bottom: 5px;
        '>ZeeAgentX 🐦‍🔥</h1>
        <p style='
            font-size: 20px;
            font-weight: 500;
            margin: 0;
            letter-spacing: 0.5px;
        '>Talk to one AI that reasons, retrieves and responds.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
            "role": "assistant",
            "avatar": "🐦‍🔥",
            "content": (
                "**Hi there! I'm ZeeAgentX — your unified AI assistant.**\n\n"
                "I combine the power of **ZeeNova ❄️** (a real-world AI agent with tool-use, planning and reasoning) and **ZeePT 📒** (document-aware RAG). "
                "Just ask me anything, I've got you covered!"
            )
        })

if "session_id" not in st.session_state:
    st.session_state.session_id = None

# Display the sidebar
display_sidebar()

# Display the chat interface
display_chat_interface()