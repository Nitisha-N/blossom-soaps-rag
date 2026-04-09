import sys
sys.path.append("/home/ubuntu")
import streamlit as st
from backend.rag_service import retrieve_and_generate

st.set_page_config(page_title="Blossom Soaps", layout="wide")

# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- CLEAR CHAT ----------
def clear_chat():
    st.session_state.messages = []

# ---------- UI STYLE ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0d0b1f, #1a0f2e);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 600;
    color: #f7c6ff;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #c9a4ff;
    margin-bottom: 30px;
}

.chat-box {
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 12px;
}

.user {
    background: linear-gradient(90deg, #7b2ff7, #f107a3);
    color: white;
    text-align: right;
}

.bot {
    background: #1f1b2e;
    color: #e6e6e6;
}

.button {
    background-color: #5a189a;
    color: white;
    border-radius: 8px;
    padding: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">Blossom Soaps</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Employee FAQs</div>', unsafe_allow_html=True)

# ---------- SOURCE NAME CLEAN ----------
def format_source(name):
    mapping = {
        "hr_policy.txt": "HR Policy Document",
        "leave_policy.txt": "Leave Policy",
        "employee_benefits.txt": "Employee Benefits Guide",
        "code_of_conduct.txt": "Code of Conduct",
        "work_from_home.txt": "Work From Home Policy"
    }
    return mapping.get(name, name.replace("_", " ").title())

# ---------- CHAT DISPLAY ----------
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "bot"

    st.markdown(
        f'<div class="chat-box {role_class}">{msg["content"]}</div>',
        unsafe_allow_html=True
    )

    if msg["role"] == "assistant" and "sources" in msg:
        with st.expander("Sources"):
            for src in msg["sources"]:
                st.markdown(f"**{format_source(src['file'])}**")
                st.caption(src["content"])

# ---------- INPUT ----------
query = st.chat_input("Ask a question about company policies")

if query:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    # Get response
    answer, sources = retrieve_and_generate(query)

    # Add bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources
    })

    st.rerun()
