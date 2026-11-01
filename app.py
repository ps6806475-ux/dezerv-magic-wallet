import streamlit as st
import random

# --- Page Config ---
st.set_page_config(page_title="The Magic Wallet", page_icon="🦄", layout="wide")

# --- Dynamic GIF Selector (Strictly Money, Savings, and Kids) ---
if 'main_gif' not in st.session_state:
    # Piggy banks and wallets
    st.session_state.main_gif = random.choice([
        "https://media.giphy.com/media/xTiTnqUxyWbsAXq7Ju/giphy.gif", 
        "https://media.giphy.com/media/26xBsZZO2M2K1RjAA/giphy.gif",
        "https://media.giphy.com/media/l4pT26eA0Vb6Nn32w/giphy.gif"
    ])
    # Coins, jumping money, and growing coin plants
    st.session_state.sidebar_gif = random.choice([
        "https://media.giphy.com/media/3o6gDWzmAzrpi5DQU8/giphy.gif",
        "https://media.giphy.com/media/xT1XGLtjjDfqIjJCO4/giphy.gif",
        "https://media.giphy.com/media/ZGH8VtTZMxgw5OqDiW/giphy.gif"
    ])
    # Money trees and magical growth for the Time Machine
    st.session_state.time_gif = random.choice([
        "https://media.giphy.com/media/VTxmwaCEwSlZm/giphy.gif",
        "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
        "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif"
    ])

# --- Extreme Colorful UI, CSS, & Animations ---
st.markdown("""
<style>
    /* Super vibrant animated gradient background */
    .stApp { 
        background: linear-gradient(-45deg, #ff9a9e, #fecfef, #a1c4fd, #c2e9fb);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #1a1a2e; 
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #fff3e0 !important;
        border-right: 5px dashed #ff9933;
    }
    
    /* 1. MOBILE FIX: Force Jars to stay side-by-side on mobile */
    div[data-testid="column"] { min-width: 30% !important; flex-wrap: nowrap; }
    
    /* Force playful fonts */
    h1, h2, h3, p, span, label, div { 
        color: #1a1a2e; 
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Marker Felt', sans-serif; 
    }
    
    /* Glowing Virtual Wallet Box */
    .wallet-box { 
        background: linear-gradient(135deg, #FF9933 0%, #FF3366 100%); 
        color: white !important; 
        font-size: 40px; 
        font-weight: 900; 
        text-align: center; 
        padding: 30px; 
        border-radius: 30px; 
        border: 6px dashed #fff; 
        box-shadow: 8px 8px 25px rgba(0,0,0,0.4); 
    }
    .wallet-box span { color: white !important; }
    
    /* 3 Jars styling with popping neon colors */
    .jar { 
        padding: 25px; 
        border-radius: 25px; 
        text-align: center; 
        color: white !important; 
        font-weight: 900; 
        font-size: 26px; 
        box-shadow: 5px 5px 20px rgba(0,0,0,0.3); 
        border: 4px solid white; 
    }
    .jar-spend { background-color: #ff0055; } 
    .jar-save { background-color: #00cc66; }  
    .jar-give { background-color: #ffaa00; }  
    
    /* Futuristic glowing Time Machine */
    .time-machine { 
        background: linear-gradient(to right, #00c6ff 0%, #0072ff 100%); 
        padding: 35px; 
        border-radius: 35px; 
        text-align: center; 
        border: 6px solid #fff; 
        box-shadow: 0px 0px 30px #00c6ff; 
    }
    .time-machine span, .time-machine h3, .time-machine div, .time-machine b { color: #fff !important; text-shadow: 2px 2px 4px #000; }
    
    /* Dynamic message and joke boxes */
    .magic-message {
        background: linear-gradient(45deg, #ffeaa7, #fdcb6e);
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        border: 5px dashed #ff7675;
        color: #d63031 !important;
        margin-top: 20px;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
    }
    .joke-box {
        background: linear-gradient(45deg, #a8e063, #56ab2f);
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        border: 5px dashed #fff;
        color: #fff !important;
        margin-top: 20px;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
    }
    .parent-note {
        background-color: #ffcccc;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: #990000 !important;
        font-weight: bold;
        font-size: 20px;
        border: 3px solid #ff0000;
        margin-top: 20px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: Story & Instructions ---
with st.sidebar:
    st.header("📖 How to Play!")
    st.image(st.session_state.sidebar_gif, width=200)
    st.write("### Meet Rahul! 👦")
    st.write("Rahul got **₹1000** for his pocket money. He doesn't want to just spend it all at once!")
    st.write("Here is his Magic Trick:")
    st.write("🍦 **₹500 (50%)** goes to his Spend Jar for snacks and fun today.")
    st.write("🎯 **₹400 (40%)** goes to his Save Jar to buy a big toy later.")
    st.write("🎁 **₹100 (10%)** goes to his Give Jar to buy a gift for his little sister.")
    st.write("---")
    st.write("### 🛸 The Time Machine")
    st.write("When Rahul saves enough for his toy, he puts his leftover money into the **Time Machine** to watch it grow bigger and bigger for his future!")
    st.write("### 👉 Now it's YOUR turn!")

# --- Header & Initialization ---
colT1, colT2 = st.columns([3, 1])
with colT1:
    st.title("🦄 The Magic Wallet! 🌈✨")
    st.write("### *Learn to save, spend, and grow your money!* 🚀")
with colT2:
    st.image(st.session_state.main_gif, width=180)

if 'total_savings' not in st.session_state:
    st.session_state.total_savings = 0.0
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

wallet_placeholder = st.empty()
badge_placeholder = st.empty()

st.markdown("---")

# --- SECTION 1: Payday ---
st.header("1️⃣ Payday! 💵💳")
pocket_money = st.number_input("How much pocket money did you get? (₹)", min_value=0.0, step=100.0)

if st.button("✨ Split My Money! ✨"):
    if pocket_money > 0:
        st.session_state.total_savings = (pocket_money * 0.40)
        st.session_state.show_results = True
        
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f"<div class='jar jar-spend'>🍦 Spend Now<br><br>₹{pocket_money*0.5:.0f}</div>", unsafe_allow_html=True)
        with c2: st.markdown(f"<div class='jar jar-save'>🎯 Save for Later<br><br>₹{pocket_money*0.4:.0f}</div>", unsafe_allow_html=True)
        with c3: st.markdown(f"<div class='jar jar-give'>🎁 Give/Donate<br><br>₹{pocket_money*0.1:.0f}</div>", unsafe_allow_html=True)
        
        st.success("🎉 WOOOHOOO! Money split successfully!")
        st.balloons()

wallet_placeholder.markdown(f"<div class='wallet-box'>🏦 Your Virtual Wallet Balance 🏦 <br> ₹ {st.session_state.total_savings:,.2f}</div><br>", unsafe_allow_html=True)

# 2. GAMIFICATION BADGES 
savings = st.session_state.total_savings
if savings == 0:
    badge_placeholder.info("🌟 Rank: Beginner Saver! Let's get started!")
elif savings < 2000:
    badge_placeholder.success("🥉 Rank: Bronze Coin Collector!")
elif savings < 5000:
    badge_placeholder.success("🥈 Rank: Silver Piggy Bank Master!")
else:
    badge_placeholder.success("🥇 Rank: Gold Diamond Investor! 💎")

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
    
    st.write("### 👉 Enter your age below and hit the Enter button! ⌨️")
    age = st.number_input("Your age now? 👦👧", min_value=5, max_value=20, value=10)
    target = st.slider("Time Travel to Age: 🚀", min_value=age, max_value=21, value=18)
    
    years = target - age
    if years > 0:
        future = leftover * (1.08 ** years)
        st.write(f"### 🤯 By investing in a bank at **8% compound interest**, in {years} years your money grows to: **₹{future:,.0f}** 💰")
        st.image(st.session_state.time_gif, width=250)
        st.markdown("<div class='parent-note'>🛑 Important Note: Real investing is serious business! Always take your parents' guidance before investing any real money. 👨‍👩‍👧‍👦</div>", unsafe_allow_html=True)
else:
    st.info("🔒 **Unlock Alert:** When you reach your dream and save extra money, the magical Time Machine will unlock right here!")

# --- SECTION 4: Dynamic Messages & Jokes ---
if st.session_state.show_results:
    st.markdown("---")
    
    messages = [
        "Superstar saver! Growing your money today gives you wings tomorrow. 💸✨",
        "Smart move! Every rupee you save is a little worker building your future. 🧱🚀",
        "Magic happens when you wait! Keep investing and watch your wealth zoom! 🎢🌟",
        "Patience pays! The money you don't spend today turns into treasure tomorrow. 🗺️💎",
        "You are a money master! Saving and reinvesting is your secret superpower. 🦸‍♂️⚡"
    ]
    
    jokes = [
        "Why did the kid throw his clock out the window? \n\nBecause he wanted to see time fly! ⏰🕊️",
        "What do you call a bear with no teeth? \n\nA gummy bear! 🐻🍬",
        "Why did the math book look sad? \n\nBecause it had too many problems! 📘😢",
        "What do you call cheese that isn't yours? \n\nNacho cheese! 🧀😂",
        "Why can't you give Elsa a balloon? \n\nBecause she will let it go! 🎈❄️",
        "What do you call a dinosaur that is sleeping? \n\nA dino-snore! 🦕💤"
    ]
    
    selected_message = random.choice(messages)
    selected_joke = random.choice(jokes)
    
    st.markdown(f"<div class='magic-message'>💌 Magic Money Lesson:<br><br>{selected_message}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='joke-box'>😂 Bonus Joke For You:<br><br>{selected_joke}</div>", unsafe_allow_html=True)
    
    if st.button("🔄 Click Here to Restart App!"):
        st.session_state.clear()
        st.rerun()

# 3. DOWNLOADABLE CERTIFICATE
st.markdown("---")
certificate_text = f"""
🌟 THE MAGIC WALLET CERTIFICATE 🌟
----------------------------------
Official Savings Balance: ₹ {st.session_state.total_savings:,.2f}
Status: Certified Money Master!
Keep saving, keep growing! 🚀
"""
st.download_button(
    label="📥 Download My Savings Certificate!",
    data=certificate_text,
    file_name="magic_wallet_certificate.txt",
    mime="text/plain"
)
