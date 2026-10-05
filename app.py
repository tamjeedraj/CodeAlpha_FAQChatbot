import streamlit as st

from agent import FAQAgent


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="FAQ AI Agent",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# CSS
# -----------------------------

st.markdown(
    """
    <style>

    .title {
        font-size: 42px;
        font-weight: 700;
        color: #4F46E5;
    }

    .subtitle {
        color: #6B7280;
        font-size: 17px;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Load Agent
# -----------------------------

@st.cache_resource
def load_agent():

    return FAQAgent()


try:

    agent = load_agent()

except Exception as error:

    st.error(
        f"Application initialization failed: {error}"
    )

    st.stop()


# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("🤖 FAQ Assistant")

    st.write(
        "Ask questions and get instant answers."
    )

    st.divider()

    st.write(
        f"📚 Available FAQs: "
        f"**{len(agent.retriever.faqs)}**"
    )

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.write(
        f"📚 FAQs available: "
        f"**{len(agent.retriever.faqs)}**"
    )

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
        key="clear_chat_button"
    ):

        st.session_state.messages = []

        st.rerun()


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="title">'
    '🤖 FAQ AI Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'RAG-powered FAQ chatbot'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Welcome
# -----------------------------

if not st.session_state.messages:

    st.info(
        "👋 Welcome! Ask me anything about "
        "the FAQ knowledge base."
    )


# -----------------------------
# Chat History
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if (
            message["role"] == "assistant"
            and "confidence" in message
        ):

            st.caption(
                f"🎯 Retrieval confidence: "
                f"{message['confidence']:.1%}"
            )

            sources = message.get(
                "sources",
                []
            )

            if sources:

                with st.expander(
                    "🔎 View retrieved FAQs"
                ):

                    for source in sources:

                        st.write(
                            f"**{source['faq']['question']}**"
                        )

                        st.caption(
                            f"Similarity: "
                            f"{source['score']:.1%}"
                        )


# -----------------------------
# Chat Input
# -----------------------------

user_question = st.chat_input(
    "💬 Ask your question..."
)


if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.spinner(
        "🤖 Thinking..."
    ):

        result = agent.run(
            user_question
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "confidence": result["confidence"],
            "sources": result["sources"]
        }
    )

    st.rerun()