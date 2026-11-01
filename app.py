import streamlit as st
import random

st.set_page_config(page_title="The Magic Wallet", page_icon="🦄", layout="wide")

# --- Super Colorful UI & Bug Fixes ---
st.markdown("""
<style>
    /* Super colorful gradient background */
    .stApp { 
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%); 
        color: #1a1a2e; 
    }
    /* Force all text to be dark and readable */
    h1, h2, h3, p, span, label, div { color: #1a1a2e; font-family: 'Comic Sans MS', cursive, sans-serif; }
    
    /* Massive, glowing colorful boxes */
    .wallet-box { 
        background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%); 
        color: white !important; 
        font-size: 35px; 
        font-weight: bold; 
        text-align: center; 
        padding: 30px; 
        border-radius: 25px; 
        border: 5px dashed #fff; 
        box-shadow: 5px 5px 20px rgba(0,0,0,0.3); 
    }
    .wallet-box span { color: white !important; }
    
    /* 3 Jars styling with popping colors */
    .jar { padding: 20px; border-radius: 20px; text-align: center; color: white !important; font-weight: 900; font-size: 22px; box-shadow: 4px 4px 15px rgba(0,0,0,0.2); border: 3px solid white; }
    .jar-spend { background-color: #ff0844; } /* Bright Red */
    .jar-save { background-color: #0ba360; }  /* Bright Green */
    .jar-give { background-color: #ffb199; }  /* Bright Orange */
    
    /* Futuristic glowing Time Machine */
    .time-machine { 
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%); 
        padding: 30px; 
        border-radius: 30px; 
        text-align: center; 
        border: 5px solid #fff; 
        box-shadow: 0px 0px 25px #00f2fe; 
    }
    .time-machine span, .time-machine h3, .time-machine div, .time-machine b { color: #fff !important; text-shadow: 1px 1px 2px #000; }
    
    /* Dynamic message box */
    .magic-message {
        background-color: #ffeaa7;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        border: 3px dashed #fdcb6e;
        color: #d63031 !important;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Main Title with GIF
colT1, colT2 = st.columns([3, 1])
with colT1:
    st.title("🦄 The Magic Wallet! 🌈✨")
    st.write("### *Learn to save, spend, and grow your money!* 🚀")
with colT2:
    st.image("https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif", width=150)

if 'total_savings' not in st.session_state:
    st.session_state.total_savings = 0.0

wallet_placeholder = st.empty()

st.markdown("---")

# --- SECTION 1: Payday ---
st.header("1️⃣ Payday! 💵💳")
pocket_money = st.number_input("How much pocket money did you get? (₹)", min_value=0.0, step=100.0)

if st.button("✨ Split My Money! ✨"):
    if pocket_money > 0:
        st.session_state.total_savings += (pocket_money * 0.40)
        
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f"<div class='jar jar-spend'>🍦 Spend Now<br><br>₹{pocket_money*0.5:.0f}</div>", unsafe_allow_html=True)
        with c2: st.markdown(f"<div class='jar jar-save'>🎯 Save for Later<br><br>₹{pocket_money*0.4:.0f}</div>", unsafe_allow_html=True)
        with c3: st.markdown(f"<div class='jar jar-give'>🎁 Give/Donate<br><br>₹{pocket_money*0.1:.0f}</div>", unsafe_allow_html=True)
        
        st.success("🎉 Awesome! Your savings were added to the Virtual Wallet!")
        st.balloons()

wallet_placeholder.markdown(f"<div class='wallet-box'>🏦 Your Virtual Wallet Balance 🏦 <br> ₹ {st.session_state.total_savings:,.2f}</div><br>", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION 2: Dream Wish ---
st.header("2️⃣ Dream Wish 🚀🧸")
colA, colB = st.columns(2)
with colA: wish = st.text_input("What is your dream toy? (e.g. Remote Car 🏎️)")
with colB: price = st.number_input("How much does it cost? (₹)", min_value=1.0, value=2000.0, step=100.0)

if price > 0 and wish:
    progress = min(st.session_state.total_savings / price, 1.0)
    st.write(f"**Progress toward your {wish}:**")
    st.progress(progress)
    
    if progress >= 1.0: 
        st.success(f"🎊 YAY! You saved enough for the {wish}! 🎊")
        st.snow()

st.markdown("---")

# --- SECTION 3: Time Machine ---
st.header("3️⃣ The Time Machine 🛸⏳")
leftover = st.session_state.total_savings - price

if leftover > 0:
    st.markdown(f"<div class='time-machine'>👽 You have <b>₹{leftover:,.0f}</b> of Leftover Magic!<br>Let's grow it in the future! 🌌</div><br>", unsafe_allow_html=True)
    
    st.write("**👉 Enter your age below and hit the Enter button!**")
    age = st.number_input("Your age now? 👦👧", min_value=5, max_value=20, value=10)
    target = st.slider("Time Travel to Age: 🚀", min_value=age, max_value=21, value=18)
    
    years = target - age
    if years > 0:
        future = leftover * (1.08 ** years)
        st.write(f"### 🤯 In {years} years, your leftover money becomes: **₹{future:,.0f}** 💰")
        st.image("https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif", width=250)
else:
    st.info("🔒 **Unlock Alert:** When you reach your dream and save extra money, the magical Time Machine will unlock right here!")

# --- Dynamic Moral Message at the End ---
messages = [
    "Superstar saver! Growing your money today gives you wings tomorrow. 💸✨",
    "Smart move! Every rupee you save is a little worker building your future. 🧱🚀",
    "Magic happens when you wait! Keep investing and watch your wealth zoom! 🎢🌟",
    "Patience pays! The money you don't spend today turns into treasure tomorrow. 🗺️💎",
    "You are a money master! Saving and reinvesting is your secret superpower. 🦸‍♂️⚡"
]
selected_message = random.choice(messages)
st.markdown(f"<div class='magic-message'>💌 Magic Message for You:<br>{selected_message}</div>", unsafe_allow_html=True)
