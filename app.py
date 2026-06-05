import streamlit as st
import random
import logging
logging.getLogger("streamlit").setLevel(logging.ERROR)

st.set_page_config(
    page_title="HarryBot",
    page_icon=None,
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Cinzel:wght@400;500;600&family=IM+Fell+English:ital@0;1&display=swap');

/* ═══════════════════════════════════════════
   HOUSE COLOUR PALETTE
   Gryffindor : #9b1c1c (scarlet)  #d4a017 (gold)
   Hufflepuff : #f0b429 (yellow)   #3d2b00 (black)
   Slytherin  : #1a6b3a (green)    #a8a9ad (silver)
   Ravenclaw  : #1e3a6e (blue)     #8b7536 (bronze)
   ═══════════════════════════════════════════ */

/* ── RESET ── */
*, *::before, *::after { box-sizing: border-box; }

html, body { background: #13100e !important; color: #e8dcc8 !important; }

[data-testid="stAppViewContainer"],
[data-testid="stApp"],
.stApp,
.main                              { background: transparent !important; }
[data-testid="stHeader"]           { background: transparent !important; border: none !important; height: 0 !important; }
[data-testid="stToolbar"]          { display: none !important; }
[data-testid="stDecoration"]       { display: none !important; }
[data-testid="stStatusWidget"]     { display: none !important; }
.stDeployButton                    { display: none !important; }

/* strip Streamlit's default chat borders */
[data-testid="stChatMessage"],
[data-testid="stChatMessageContainer"],
.stChatMessage {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* ── BACKGROUND ── */
.stApp {
    background-color: #13100e !important;
    background-image:
        /* stone bricks */
        url("data:image/svg+xml,%3Csvg width='160' height='100' viewBox='0 0 160 100' xmlns='http://www.w3.org/2000/svg'%3E%3Crect x='2' y='2' width='75' height='46' rx='1' fill='none' stroke='%231e1610' stroke-width='1.2'/%3E%3Crect x='83' y='2' width='75' height='46' rx='1' fill='none' stroke='%231e1610' stroke-width='1.2'/%3E%3Crect x='2' y='52' width='50' height='46' rx='1' fill='none' stroke='%231e1610' stroke-width='1.2'/%3E%3Crect x='56' y='52' width='50' height='46' rx='1' fill='none' stroke='%231e1610' stroke-width='1.2'/%3E%3Crect x='110' y='52' width='48' height='46' rx='1' fill='none' stroke='%231e1610' stroke-width='1.2'/%3E%3C/svg%3E"),
        /* Gryffindor torch glow — left */
        radial-gradient(ellipse at 5% 30%, rgba(155,28,28,0.13) 0%, transparent 40%),
        /* Hufflepuff candle glow — right */
        radial-gradient(ellipse at 95% 65%, rgba(212,160,23,0.10) 0%, transparent 40%),
        /* Ravenclaw magic shimmer — top */
        radial-gradient(ellipse at 50% 0%,  rgba(30,58,110,0.12) 0%, transparent 35%),
        /* Slytherin dungeon mist — bottom */
        radial-gradient(ellipse at 50% 100%, rgba(26,107,58,0.10) 0%, transparent 40%),
        linear-gradient(170deg, #160e0a 0%, #13100e 50%, #0d0f13 100%);
    background-attachment: fixed;
    min-height: 100vh;
}

/* ── LAYOUT ── */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 2rem !important;
    max-width: 820px !important;
}

/* ── HEADER ── */
.hp-header {
    text-align: center;
    padding: 2rem 1rem 0.2rem 1rem;
}

.hp-crest-svg {
    display: block;
    margin: 0 auto 0.5rem auto;
    width: 52px; height: 52px;
    filter: drop-shadow(0 0 10px rgba(212,160,23,0.9)) drop-shadow(0 0 28px rgba(155,28,28,0.5));
    animation: crestPulse 3s ease-in-out infinite;
}
@keyframes crestPulse {
    0%,100% { filter: drop-shadow(0 0 10px rgba(212,160,23,0.9)) drop-shadow(0 0 28px rgba(155,28,28,0.5)); }
    50%      { filter: drop-shadow(0 0 18px rgba(240,200,40,1.0)) drop-shadow(0 0 44px rgba(200,40,40,0.7)); }
}

.hp-title {
    font-family: 'Cinzel Decorative', serif;
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: 8px;
    /* scarlet-to-gold — Gryffindor gradient */
    background: linear-gradient(135deg, #c0392b 0%, #d4a017 35%, #f5e060 55%, #d4a017 75%, #9b1c1c 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
}

.hp-subtitle {
    font-family: 'IM Fell English', serif;
    font-style: italic;
    color: #9a8060;
    font-size: 0.95rem;
    letter-spacing: 3px;
    margin-top: 6px;
    text-transform: uppercase;
}

/* house-colour ornament bar: scarlet | gold | green | blue */
.hp-ornament {
    display: flex;
    align-items: center;
    margin: 14px auto 18px auto;
    max-width: 480px;
    height: 3px;
    border-radius: 2px;
    overflow: hidden;
}
.hp-orn-g  { flex:1; height:100%; background:#9b1c1c; }  /* Gryffindor scarlet */
.hp-orn-h  { flex:1; height:100%; background:#d4a017; }  /* Hufflepuff gold    */
.hp-orn-s  { flex:1; height:100%; background:#1a6b3a; }  /* Slytherin green    */
.hp-orn-r  { flex:1; height:100%; background:#1e3a6e; }  /* Ravenclaw blue     */

/* ── CHAT BUBBLES ── */

/* BOT — Gryffindor scarlet left bar, warm dark background */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) .stChatMessageContent {
    background: linear-gradient(135deg, #2b180c 0%, #241208 100%) !important;
    border-top:    1px solid rgba(155,28,28,0.30) !important;
    border-right:  1px solid rgba(100,50,10,0.20) !important;
    border-bottom: 1px solid rgba(100,50,10,0.20) !important;
    border-left:   3px solid #9b1c1c !important;
    border-radius: 1px 10px 10px 1px !important;
    box-shadow: 0 3px 22px rgba(0,0,0,0.65) !important;
    padding: 16px 22px !important;
}

/* USER — Ravenclaw blue right bar, cool dark background */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stChatMessageContent {
    background: linear-gradient(135deg, #18203a 0%, #141d35 100%) !important;
    border-top:    1px solid rgba(30,58,110,0.35) !important;
    border-left:   1px solid rgba(20,40,80,0.20) !important;
    border-bottom: 1px solid rgba(20,40,80,0.20) !important;
    border-right:  3px solid #1e3a6e !important;
    border-radius: 10px 1px 1px 10px !important;
    box-shadow: 0 3px 22px rgba(0,0,0,0.65) !important;
    padding: 16px 22px !important;
}

/* ── MESSAGE TEXT ───────────────────────────── */
[data-testid="stChatMessage"] .stChatMessageContent,
[data-testid="stChatMessage"] .stChatMessageContent *,
[data-testid="stChatMessage"] .stMarkdown,
[data-testid="stChatMessage"] .stMarkdown *,
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div,
[data-testid="stChatMessage"] li {
    font-family: 'IM Fell English', serif !important;
    font-size: 1.08rem !important;
    color: #fff8ec !important;
    line-height: 1.80 !important;
}

[data-testid="stChatMessage"] strong {
    color: #ffd95c !important;
    font-weight: 700 !important;
}

[data-testid="stChatMessage"] em {
    color: #e6d7b2 !important;
}

/* avatars — no background ring */
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"],
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* ── CHAT INPUT ── */
[data-testid="stBottom"],
[data-testid="stChatInput"] {
    background: rgba(10,7,4,0.97) !important;
    border-top: 1px solid rgba(155,28,28,0.25) !important;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.5) !important;
}

[data-testid="stChatInput"] textarea {
    background: rgba(28,18,10,0.99) !important;
    color: #fff8ec !important;
    border: 1px solid rgba(120,60,15,0.45) !important;
    border-radius: 3px !important;
    font-family: 'IM Fell English', serif !important;
    font-size: 1rem !important;
    caret-color: #d4a017 !important;
    resize: none !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #5a4020 !important;
    font-style: italic !important;
}

[data-testid="stChatInput"] textarea:focus {
    border-color: rgba(212,160,23,0.55) !important;
    box-shadow: 0 0 14px rgba(212,160,23,0.10) !important;
    outline: none !important;
}

[data-testid="stChatInput"] button       { color: #9a7010 !important; background: transparent !important; border: none !important; }
[data-testid="stChatInput"] button:hover { color: #f0c030 !important; }

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: #0e0a08 !important;
    border-right: 1px solid rgba(155,28,28,0.20) !important;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.8rem !important;
    padding-left: 1.2rem !important;
    padding-right: 1.2rem !important;
}

/* four-house colour bar at top of sidebar */
.sidebar-houses {
    display: flex;
    height: 4px;
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 14px;
}
.sh-g { flex:1; background:#9b1c1c; }
.sh-h { flex:1; background:#d4a017; }
.sh-s { flex:1; background:#1a6b3a; }
.sh-r { flex:1; background:#1e3a6e; }

.sidebar-title {
    font-family: 'Cinzel', serif;
    font-size: 0.68rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #9a7a30;
    text-align: center;
    border-bottom: 1px solid rgba(155,28,28,0.18);
    padding-bottom: 10px;
    margin-bottom: 14px;
}

section[data-testid="stSidebar"] h3 {
    font-family: 'Cinzel', serif !important;
    color: #b08828 !important;
    font-size: 0.70rem !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid rgba(155,28,28,0.18) !important;
    padding-bottom: 5px !important;
    margin-bottom: 10px !important;
    margin-top: 2px !important;
}

section[data-testid="stSidebar"] p {
    font-family: 'IM Fell English', serif !important;
    color: #d8c6a5 !important;
    font-size: 0.88rem !important;
    line-height: 1.65 !important;
}

section[data-testid="stSidebar"] hr {
    border: none !important;
    height: 1px !important;
    background: rgba(155,28,28,0.18) !important;
    margin: 12px 0 !important;
}

/* example question buttons */
section[data-testid="stSidebar"] .stButton > button {
    background: rgba(14,9,4,0.92) !important;
    color: #a08858 !important;
    border: 1px solid rgba(100,55,10,0.28) !important;
    border-radius: 2px !important;
    font-family: 'IM Fell English', serif !important;
    font-style: italic !important;
    font-size: 0.88rem !important;
    width: 100% !important;
    text-align: left !important;
    padding: 7px 11px !important;
    line-height: 1.45 !important;
    white-space: normal !important;
    height: auto !important;
    transition: all 0.2s ease !important;
    margin-bottom: 3px !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(30,18,6,0.98) !important;
    color: #e8c050 !important;
    border-color: rgba(212,160,23,0.45) !important;
    box-shadow: 0 0 8px rgba(212,160,23,0.08) !important;
}

/* clear button — Gryffindor scarlet */
.clear-btn > button,
.clear-btn > button:focus {
    background: rgba(18,5,5,0.92) !important;
    color: #8a2828 !important;
    border: 1px solid rgba(155,28,28,0.28) !important;
    font-style: normal !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.72rem !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}
.clear-btn > button:hover {
    background: rgba(35,8,8,0.98) !important;
    color: #d04040 !important;
    border-color: rgba(155,28,28,0.55) !important;
}

/* quote block */
.hp-quote {
    font-family: 'IM Fell English', serif;
    font-style: italic;
    color: #806848;
    font-size: 0.86rem;
    text-align: center;
    line-height: 1.85;
    padding: 10px 6px 4px 6px;
}
.hp-quote-attr {
    font-size: 0.75rem;
    color: #5a4428;
    letter-spacing: 1px;
    font-style: normal;
    display: block;
    margin-top: 6px;
}

/* house badge next to quote */
.hp-house-badge {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    margin-right: 4px;
    vertical-align: middle;
}

/* ── SPINNER ── */
.stSpinner > div { border-top-color: #9b1c1c !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar       { width: 4px; }
::-webkit-scrollbar-track { background: #0e0a08; }
::-webkit-scrollbar-thumb { background: #3a1808; border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: #6a2e10; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hp-header">
    <svg class="hp-crest-svg" viewBox="0 0 48 58" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polygon points="24,2 32,18 48,18 36,30 40,48 24,40 8,48 12,30 0,18 16,18"
                 fill="none" stroke="#d4a017" stroke-width="1.4" opacity="0.5"/>
        <path d="M27 6 L18 28 L25 28 L16 52 L30 24 L23 24 Z"
              fill="#d4a017"/>
        <path d="M27 6 L18 28 L25 28 L16 52 L30 24 L23 24 Z"
              fill="#9b1c1c" opacity="0.4"/>
    </svg>
    <div class="hp-title">HARRYBOT</div>
    <div class="hp-subtitle">Oracle of the Wizarding World</div>
    <div class="hp-ornament">
        <div class="hp-orn-g"></div>
        <div class="hp-orn-h"></div>
        <div class="hp-orn-s"></div>
        <div class="hp-orn-r"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load bot
@st.cache_resource(show_spinner="Summoning HarryBot from the depths of Hogwarts...")
def get_bot():
    try:
        from chatbot import HarryBotChatbot
        return HarryBotChatbot(), None
    except FileNotFoundError as e:
        return None, str(e)
    except Exception as e:
        return None, f"Unexpected error: {e}"

bot, load_error = get_bot()

if load_error:
    st.error(f"Could not start HarryBot:\n\n{load_error}")
    st.stop()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "*Greetings, young witch or wizard.*\n\n"
                "I am **HarryBot** — keeper of knowledge from the wizarding world. "
                "Ask me anything about Harry Potter and I shall consult my enchanted dataset.\n\n"
                "*What mysteries of the magical world shall we explore today?*"
            ),
        }
    ]

# Chat history
for msg in st.session_state.messages:
    avatar = "⚡" if msg["role"] == "assistant" else "🎓"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Speak your question to the oracle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🎓"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="⚡"):
        with st.spinner("Consulting the enchanted dataset..."):
            try:
                response = bot.chat(prompt)
            except Exception as e:
                response = f"A dark spell interfered: {e}"
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    # four-house colour bar
    st.markdown("""
    <div class="sidebar-houses">
        <div class="sh-g"></div><div class="sh-h"></div>
        <div class="sh-s"></div><div class="sh-r"></div>
    </div>
    <div class="sidebar-title">The Restricted Section</div>
    """, unsafe_allow_html=True)

    st.markdown("### Incantations")
    examples = [
        "Who is Harry Potter?",
        "How old is Harry Potter?",
        "What type of creature is Buckbeak?",
        "What spell stops Dementors?",
        "Which house is Harry in?",
        "What are Horcruxes?",
        "Who is Voldemort afraid of?",
        "How old is Voldemort?",
        "How is Hermione described?",
        "What does the Marauder's Map show?",
    ]
    for ex in examples:
        if st.button(ex, key=f"example_{ex}"):
            st.session_state.messages.append({"role": "user", "content": ex})
            try:
                response = bot.chat(ex)
            except Exception as e:
                response = f"Something went wrong: {e}"
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

    st.markdown("---")
    st.markdown("### About")
    st.markdown(
        "HarryBot answers questions strictly from a curated Harry Potter dataset. "
        "It remembers recent exchanges to handle follow-up questions."
    )

    st.markdown("---")
    st.markdown("### Controls")
    with st.container():
        st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
        if st.button("Obliviate — Clear Conversation", key="clear"):
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": (
                        "*Obliviate.* The memory charm has been cast. "
                        "Ask me anything about Harry Potter."
                    ),
                }
            ]
            bot.history.clear()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Words of Wisdom")

    # Each quote tagged with its house colour
    quotes = [
        ("It takes a great deal of courage to stand up to our enemies, but a great deal more to stand up to our friends.", "Albus Dumbledore", "#9b1c1c"),
        ("Happiness can be found even in the darkest of times, if one only remembers to turn on the light.", "Albus Dumbledore", "#d4a017"),
        ("It does not do to dwell on dreams and forget to live.", "Albus Dumbledore", "#d4a017"),
        ("It is our choices, Harry, that show what we truly are, far more than our abilities.", "Albus Dumbledore", "#9b1c1c"),
        ("Words are, in my not-so-humble opinion, our most inexhaustible source of magic.", "Albus Dumbledore", "#1e3a6e"),
        ("Fear of a name increases fear of the thing itself.", "Albus Dumbledore", "#1a6b3a"),
        ("We are only as strong as we are united, as weak as we are divided.", "Albus Dumbledore", "#9b1c1c"),
        ("It matters not what someone is born, but what they grow to be.", "Albus Dumbledore", "#1a6b3a"),
        ("To the well-organised mind, death is but the next great adventure.", "Albus Dumbledore", "#1e3a6e"),
        ("Differences of habit and language are nothing at all if our aims are identical and our hearts are open.", "Albus Dumbledore", "#d4a017"),
    ]

    random.seed(len(st.session_state.messages))
    quote_text, quote_author, house_col = quotes[random.randint(0, len(quotes) - 1)]

    st.markdown(
        f'<div class="hp-quote">'
        f'<span class="hp-house-badge" style="background:{house_col};"></span>'
        f'&ldquo;{quote_text}&rdquo;'
        f'<span class="hp-quote-attr">— {quote_author}</span>'
        f'</div>',
        unsafe_allow_html=True
    )
