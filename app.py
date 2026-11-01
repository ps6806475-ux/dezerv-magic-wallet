import streamlit as st

st.set_page_config(page_title="The Magic Wallet", page_icon="👛", layout="wide")

# --- UI Fixes & Bright Styling ---
st.markdown("""
<style>
    /* Force light background and dark readable text */
    .stApp { background-color: #f4f9ff; color: #1a1a2e; }
    h1, h2, h3, p, span, label, div { color: #1a1a2e; }
    
    /* Make the boxes pop with thicker borders and shadows */
    .wallet-box { background-color: #ff9f43; color: white !important; font-size: 30px; font-weight: bold; text-align: center; padding: 25px; border-radius: 20px; border: 4px dashed #ff2a2a; box-shadow: 5px 5px 15px rgba(0,0,0,0.2); }
    .wallet-box span { color: white !important; }
    
    .jar { padding: 20px; border-radius: 15px; text-align: center; color: white !important; font-weight: bold; font-size: 20px; box-shadow: 3px 3px 10px rgba(0,0,0,0.2); border: 2px solid white; }
    .jar-spend { background-color: #ff6b6b; }
    .jar-save { background-color: #1dd1a1; }
    .jar-give { background-color: #ff9f43; }
    
    .time-machine { background-color: #2c3e50; padding: 25px; border-radius: 25px; text-align: center; border: 4px solid #34e7e4; box-shadow: 0px 0px 20px #34e7e4; }
    .time-machine span, .time-machine h3, .time-machine div { color: #34e7e4 !important; }
</style>
""", unsafe_allow_html=True)

st.title("👛 The Magic Wallet! ✨🎨")
st.write("### *Learn to save, spend, and grow your money!* 🚀")

# --- Virtual Wallet Setup ---
if 'total_savings' not in st.session_state:
    st.session_state.total_savings = 0.0

# BUG FIX: We use st.empty() as a "placeholder" so we can update the wallet AFTER the math runs!
wallet_placeholder = st.empty()

# Adding a fun animated doodle
st.markdown("<center><img src='https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif' width='200' style='border-radius:20px; margin-bottom: 20px;'></center>", unsafe_allow_html=True)

# --- SECTION 1: The 3 Jars ---
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

# BUG FIX: Update the wallet box here at the bottom so it includes the new math!
wallet_placeholder.markdown(f"<div class='wallet-box'>🏦 Your Virtual Wallet Balance 🏦 <br> ₹ {st.session_state.total_savings:,.2f}</div><br>", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION 2: Dream Wish ---
st.header("2️⃣ Dream Wish 🚀🧸")
colA, colB = st.columns(2)
with colA: wish = st.text_input("What is your dream toy? (e.g. Skateboard 🛹)")
with colB: price = st.number_input("How much does it cost? (₹)", min_value=1.0, value=2000.0, step=100.0)

if price > 0 and wish:
    progress = min(st.session_state.total_savings / price, 1.0)
    st.write(f"**Progress toward your {wish}:**")
    st.progress(progress)
    
    if progress >= 1.0: 
        st.success(f"🎊 YAY! You saved enough for the {wish}! 🎊")
        st.snow()  # NEW ANIMATION ADDED!

st.markdown("---")

# --- SECTION 3: Time Machine ---
st.header("3️⃣ The Time Machine 🛸⏳")
leftover = st.session_state.total_savings - price

if leftover > 0:
    st.markdown(f"<div class='time-machine'>👽 You have <b>₹{leftover:,.0f}</b> of Leftover Magic!<br>Let's grow it in the future! 🌌</div><br>", unsafe_allow_html=True)
    age = st.number_input("Your age now? 👦👧", min_value=5, max_value=20, value=10)
    target = st.slider("Time Travel to Age: 🚀", min_value=age, max_value=21, value=18)
    
    years = target - age
    if years > 0:
        future = leftover * (1.08 ** years)
        st.write(f"### 🤯 In {years} years, your leftover money becomes: **₹{future:,.0f}** 💰")
        st.image("https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif", width=250) # NEW GIF ADDED!
else:
    st.info("💡 Keep saving! Save past your Dream Wish price to unlock the magical Time Machine!")
