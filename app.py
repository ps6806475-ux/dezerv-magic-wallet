import streamlit as st

st.set_page_config(page_title="The Magic Wallet", page_icon="👛", layout="wide")

# --- Colorful UI CSS ---
st.markdown("""
<style>
    .stApp { background-color: #f7f9fc; }
    .wallet-box { background-color: #ff9f43; color: white; font-size: 24px; font-weight: bold; text-align: center; padding: 20px; border-radius: 20px; border: 4px solid #fff; }
    .jar { padding: 15px; border-radius: 15px; text-align: center; color: white; font-weight: bold; }
    .jar-spend { background-color: #ff6b6b; }
    .jar-save { background-color: #1dd1a1; }
    .jar-give { background-color: #ff9f43; }
    .time-machine { background-color: #2c3e50; color: #34e7e4; padding: 20px; border-radius: 25px; text-align: center; border: 2px solid #34e7e4; }
</style>
""", unsafe_allow_html=True)

st.title("The Magic Wallet! 👛✨")

# --- Virtual Wallet ---
if 'total_savings' not in st.session_state:
    st.session_state.total_savings = 0.0

st.markdown(f"<div class='wallet-box'>Your Virtual Wallet Balance 🏦 <br> ₹ {st.session_state.total_savings:,.2f}</div><br>", unsafe_allow_html=True)

# --- SECTION 1: The 3 Jars ---
st.header("1️⃣ Payday! 💵")
pocket_money = st.number_input("How much pocket money did you get? (₹)", min_value=0.0, step=100.0)

if st.button("Split My Money!"):
    if pocket_money > 0:
        st.balloons()
        st.session_state.total_savings += (pocket_money * 0.40)
        
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f"<div class='jar jar-spend'>🍦 Spend Now (50%)<br>₹{pocket_money*0.5:.0f}</div>", unsafe_allow_html=True)
        with c2: st.markdown(f"<div class='jar jar-save'>🎯 Save for Later (40%)<br>₹{pocket_money*0.4:.0f}</div>", unsafe_allow_html=True)
        with c3: st.markdown(f"<div class='jar jar-give'>🎁 Give/Donate (10%)<br>₹{pocket_money*0.1:.0f}</div>", unsafe_allow_html=True)
        st.success("Money split! Your 40% savings was added to the Virtual Wallet above.")

st.markdown("---")

# --- SECTION 2: Dream Wish ---
st.header("2️⃣ Dream Wish 🚀")
wish = st.text_input("What is your dream toy?")
price = st.number_input("How much does it cost? (₹)", min_value=1.0, value=2000.0, step=100.0)

if price > 0 and wish:
    progress = min(st.session_state.total_savings / price, 1.0)
    st.write(f"**Progress toward your {wish}:**")
    st.progress(progress)
    if progress >= 1.0: st.success(f"🎉 You saved enough for the {wish}! 🎉")

st.markdown("---")

# --- SECTION 3: Time Machine ---
st.header("3️⃣ The Time Machine 🛸")
leftover = st.session_state.total_savings - price

if leftover > 0:
    st.markdown(f"<div class='time-machine'>You have ₹{leftover:,.0f} of Leftover Magic!<br>Let's grow it!</div><br>", unsafe_allow_html=True)
    age = st.number_input("Your age now?", min_value=5, max_value=20, value=10)
    target = st.slider("Time Travel to Age:", min_value=age, max_value=21, value=18)
    
    years = target - age
    if years > 0:
        future = leftover * (1.08 ** years)
        st.write(f"### In {years} years, your leftover money becomes: **₹{future:,.0f}** 🚀")
else:
    st.info("Save past your Dream Wish price to unlock the Time Machine!")
