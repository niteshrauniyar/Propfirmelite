# =========================================================
# FUTURISTIC PROP FIRM AFFILIATE WEBSITE
# SINGLE FILE VERSION - app.py
# =========================================================
#
# INSTALL:
# pip install streamlit plotly pandas
#
# RUN:
# streamlit run app.py
#
# =========================================================

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import sqlite3
import random
import time
import math

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Quantum Prop Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# DATABASE
# =========================================================

conn = sqlite3.connect("affiliate.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS firms(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    discount TEXT,
    payout TEXT,
    price TEXT,
    rating REAL,
    affiliate TEXT
)
""")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM firms")
count = cursor.fetchone()[0]

if count == 0:
    demo_data = [
        ("FTMO", "10% OFF", "90%", "$155", 4.9, "https://ftmo.com"),
        ("FundingPips", "15% OFF", "95%", "$99", 4.8, "https://fundingpips.com"),
        ("Blue Guardian", "12% OFF", "90%", "$129", 4.7, "https://blueguardian.com"),
        ("Alpha Capital", "20% OFF", "85%", "$89", 4.6, "https://alphacapitalgroup.uk"),
        ("The5ers", "5% OFF", "100%", "$39", 4.8, "https://the5ers.com"),
        ("E8 Funding", "18% OFF", "80%", "$120", 4.5, "https://e8markets.com"),
    ]

    cursor.executemany("""
    INSERT INTO firms(name, discount, payout, price, rating, affiliate)
    VALUES(?,?,?,?,?,?)
    """, demo_data)

    conn.commit()

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_sql("SELECT * FROM firms", conn)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
GOOGLE FONT
===================================================== */

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;800&display=swap');

/* =====================================================
GLOBAL
===================================================== */

html, body, [class*="css"]{
    font-family: 'Orbitron', sans-serif;
    background: #030712;
    color: white;
    scroll-behavior: smooth;
}

/* HIDE STREAMLIT */

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* =====================================================
MAIN APP
===================================================== */

.stApp{
    background:
    radial-gradient(circle at top left, rgba(0,255,255,0.12), transparent 25%),
    radial-gradient(circle at bottom right, rgba(168,85,247,0.15), transparent 25%),
    linear-gradient(180deg,#030712,#020617);
    overflow-x:hidden;
}

/* =====================================================
PARTICLES
===================================================== */

.particles{
    position:fixed;
    width:100%;
    height:100%;
    top:0;
    left:0;
    z-index:-1;
    overflow:hidden;
}

.particles span{
    position:absolute;
    width:4px;
    height:4px;
    background:#00F5FF;
    border-radius:50%;
    box-shadow:0 0 20px #00F5FF;
    animation: float 15s linear infinite;
}

@keyframes float{
    0%{
        transform:translateY(100vh) scale(0);
        opacity:0;
    }
    10%{
        opacity:1;
    }
    100%{
        transform:translateY(-10vh) scale(1);
        opacity:0;
    }
}

/* =====================================================
NAVBAR
===================================================== */

.navbar{
    position:fixed;
    top:0;
    width:100%;
    padding:20px 50px;
    z-index:999;
    backdrop-filter: blur(20px);
    background:rgba(255,255,255,0.03);
    border-bottom:1px solid rgba(255,255,255,0.08);
}

.logo{
    font-size:28px;
    font-weight:800;
    background:linear-gradient(90deg,#00F5FF,#A855F7);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* =====================================================
HERO SECTION
===================================================== */

.hero{
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    text-align:center;
    position:relative;
}

.hero-title{
    font-size:6rem;
    font-weight:800;
    line-height:1.1;
    background:linear-gradient(90deg,#00F5FF,#FFFFFF,#A855F7);
    background-size:300%;
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation: gradientMove 8s linear infinite;
}

@keyframes gradientMove{
    0%{background-position:0%;}
    100%{background-position:300%;}
}

.hero-sub{
    max-width:900px;
    font-size:1.3rem;
    opacity:0.8;
    margin-top:20px;
}

.glow-btn{
    padding:18px 40px;
    border:none;
    border-radius:18px;
    margin:12px;
    cursor:pointer;
    font-weight:700;
    font-size:1rem;
    background:linear-gradient(135deg,#00F5FF,#A855F7);
    color:white;
    transition:0.4s;
    box-shadow:0 0 30px rgba(0,255,255,0.35);
}

.glow-btn:hover{
    transform:translateY(-7px) scale(1.05);
    box-shadow:0 0 60px rgba(0,255,255,0.8);
}

/* =====================================================
SECTION TITLE
===================================================== */

.section-title{
    text-align:center;
    font-size:3.5rem;
    margin-top:100px;
    margin-bottom:60px;
    font-weight:800;
    background:linear-gradient(90deg,#00F5FF,#FFFFFF);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* =====================================================
GLASS CARD
===================================================== */

.glass{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:24px;
    backdrop-filter:blur(25px);
    padding:30px;
    transition:0.5s;
    overflow:hidden;
    position:relative;
}

.glass:hover{
    transform:translateY(-10px);
    border:1px solid #00F5FF;
    box-shadow:0 0 40px rgba(0,255,255,0.35);
}

/* =====================================================
STAT BOX
===================================================== */

.stat{
    text-align:center;
    padding:40px;
}

.stat h1{
    font-size:3rem;
    color:#00F5FF;
}

/* =====================================================
TICKER
===================================================== */

.ticker{
    width:100%;
    overflow:hidden;
    white-space:nowrap;
    background:rgba(255,255,255,0.05);
    border-top:1px solid rgba(255,255,255,0.08);
    border-bottom:1px solid rgba(255,255,255,0.08);
    padding:14px 0;
}

.ticker span{
    display:inline-block;
    padding-left:100%;
    animation:ticker 25s linear infinite;
    color:#00F5FF;
    font-weight:700;
}

@keyframes ticker{
    0%{transform:translateX(0);}
    100%{transform:translateX(-100%);}
}

/* =====================================================
FOOTER
===================================================== */

.footer{
    margin-top:120px;
    text-align:center;
    padding:80px 20px;
    border-top:1px solid rgba(255,255,255,0.08);
}

/* =====================================================
LOADING SCREEN
===================================================== */

.loader{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:#020617;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:99999;
    animation:hideLoader 3s forwards;
}

.loader h1{
    font-size:4rem;
    color:#00F5FF;
    animation:pulse 1.5s infinite;
}

@keyframes pulse{
    0%{opacity:0.4;}
    50%{opacity:1;}
    100%{opacity:0.4;}
}

@keyframes hideLoader{
    0%{opacity:1;}
    90%{opacity:1;}
    100%{
        opacity:0;
        visibility:hidden;
    }
}

/* =====================================================
MOBILE
===================================================== */

@media(max-width:768px){

    .hero-title{
        font-size:2.8rem;
    }

    .hero-sub{
        font-size:1rem;
        padding:0 20px;
    }

    .section-title{
        font-size:2rem;
    }

    .navbar{
        padding:20px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOADING SCREEN
# =========================================================

st.markdown("""
<div class="loader">
    <h1>LOADING...</h1>
</div>
""", unsafe_allow_html=True)

# =========================================================
# PARTICLES
# =========================================================

particles = '<div class="particles">'

for i in range(120):
    left = random.randint(0, 100)
    duration = random.randint(8, 20)
    size = random.randint(2, 6)

    particles += f"""
    <span style="
    left:{left}%;
    width:{size}px;
    height:{size}px;
    animation-duration:{duration}s;
    "></span>
    """

particles += '</div>'

st.markdown(particles, unsafe_allow_html=True)

# =========================================================
# NAVBAR
# =========================================================

st.markdown("""
<div class="navbar">
    <div class="logo">
        QUANTUM PROP HUB
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

<h1 class="hero-title">
GET FUNDED &<br>
START TRADING<br>
LIKE A PRO
</h1>

<p class="hero-sub">
The world's most futuristic prop firm affiliate platform.
Built with cinematic fintech animations, AI-powered analytics,
luxury cyberpunk design, and conversion-focused UI.
</p>

<div style="margin-top:40px;">
<button class="glow-btn">
START CHALLENGE
</button>

<button class="glow-btn">
COMPARE FIRMS
</button>
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# LIVE TICKER
# =========================================================

st.markdown("""
<div class="ticker">
<span>
🚀 FTMO funded 1,240 traders today |
💰 FundingPips paid $2.8M this week |
🔥 Gold bullish breakout detected |
⚡ Instant funding now available |
📈 95% payout systems activated |
🏆 Best prop firms ranked live
</span>
</div>
""", unsafe_allow_html=True)

# =========================================================
# PROP FIRM CARDS
# =========================================================

st.markdown("""
<h1 class="section-title">
TOP PROP FIRMS
</h1>
""", unsafe_allow_html=True)

cols = st.columns(3)

for index, row in df.iterrows():

    with cols[index % 3]:

        st.markdown(f"""
        <div class="glass">

        <h1 style="font-size:2rem;">
        {row['name']}
        </h1>

        <h2 style="color:#00F5FF;">
        {row['discount']}
        </h2>

        <hr style="border-color:rgba(255,255,255,0.1);">

        <p>💸 Profit Split: {row['payout']}</p>
        <p>💰 Challenge Fee: {row['price']}</p>
        <p>⭐ Rating: {row['rating']}</p>

        <a href="{row['affiliate']}" target="_blank">
            <button class="glow-btn">
            START NOW
            </button>
        </a>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# LIVE STATS
# =========================================================

st.markdown("""
<h1 class="section-title">
LIVE PLATFORM STATS
</h1>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

stats = [
    ("$28M+", "Total Payouts"),
    ("150K+", "Funded Traders"),
    ("91%", "Success Rate"),
    ("24/7", "AI Analytics"),
]

for col, stat in zip([s1,s2,s3,s4], stats):

    with col:

        st.markdown(f"""
        <div class="glass stat">
            <h1>{stat[0]}</h1>
            <p>{stat[1]}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# EQUITY CURVE
# =========================================================

st.markdown("""
<h1 class="section-title">
TRADING DASHBOARD PREVIEW
</h1>
""", unsafe_allow_html=True)

equity = [100000]

for i in range(60):
    equity.append(equity[-1] + random.randint(-1200, 3500))

fig = go.Figure()

fig.add_trace(go.Scatter(
    y=equity,
    mode='lines',
    line=dict(width=4),
    fill='tozeroy'
))

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white',
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# COMPARISON TABLE
# =========================================================

st.markdown("""
<h1 class="section-title">
COMPARE PROP FIRMS
</h1>
""", unsafe_allow_html=True)

search = st.text_input("Search Firm")

filtered = df

if search:
    filtered = df[df["name"].str.contains(search, case=False)]

st.dataframe(
    filtered[["name","discount","payout","price","rating"]],
    use_container_width=True
)

# =========================================================
# AFFILIATE EARNING CALCULATOR
# =========================================================

st.markdown("""
<h1 class="section-title">
AFFILIATE EARNINGS CALCULATOR
</h1>
""", unsafe_allow_html=True)

selected = st.selectbox(
    "Choose Prop Firm",
    df["name"]
)

referrals = st.slider(
    "Monthly Referrals",
    1,
    500,
    25
)

earnings = referrals * random.randint(40,120)

st.markdown(f"""
<div class="glass" style="text-align:center;">

<h2>Estimated Monthly Earnings</h2>

<h1 style="
font-size:5rem;
color:#00F5FF;
">
${earnings}
</h1>

</div>
""", unsafe_allow_html=True)

# =========================================================
# TESTIMONIALS
# =========================================================

st.markdown("""
<h1 class="section-title">
TRADER TESTIMONIALS
</h1>
""", unsafe_allow_html=True)

reviews = [
    "Best prop firm website I have ever seen.",
    "The dashboard feels like a billion-dollar fintech app.",
    "I got funded after discovering FTMO here.",
]

review_cols = st.columns(3)

for i, review in enumerate(reviews):

    with review_cols[i]:

        st.markdown(f"""
        <div class="glass">

        <h2>⭐⭐⭐⭐⭐</h2>

        <p style="margin-top:20px;">
        {review}
        </p>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# LEADERBOARD
# =========================================================

st.markdown("""
<h1 class="section-title">
TOP FIRM LEADERBOARD
</h1>
""", unsafe_allow_html=True)

leaderboard = pd.DataFrame({
    "Firm":["FTMO","FundingPips","Blue Guardian","The5ers"],
    "Trust Score":[98,96,94,92],
    "Payout Speed":["1 Day","6 Hours","12 Hours","1 Day"]
})

st.dataframe(leaderboard, use_container_width=True)

# =========================================================
# GOLD PRICE WIDGET
# =========================================================

gold_price = round(random.uniform(2300,2450),2)

st.markdown(f"""
<div class="glass" style="text-align:center;">

<h2>LIVE GOLD PRICE</h2>

<h1 style="
font-size:4rem;
color:#00F5FF;
">
XAUUSD ${gold_price}
</h1>

</div>
""", unsafe_allow_html=True)

# =========================================================
# FOREX HEATMAP MOCKUP
# =========================================================

st.markdown("""
<h1 class="section-title">
FOREX HEATMAP
</h1>
""", unsafe_allow_html=True)

heatmap_cols = st.columns(4)

pairs = [
    ("EURUSD","+1.2%"),
    ("GBPUSD","+0.8%"),
    ("USDJPY","-0.5%"),
    ("XAUUSD","+2.4%"),
]

for col, pair in zip(heatmap_cols, pairs):

    with col:

        st.markdown(f"""
        <div class="glass" style="text-align:center;">

        <h2>{pair[0]}</h2>

        <h1 style="color:#00F5FF;">
        {pair[1]}
        </h1>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ECONOMIC CALENDAR
# =========================================================

st.markdown("""
<h1 class="section-title">
ECONOMIC CALENDAR
</h1>
""", unsafe_allow_html=True)

calendar = pd.DataFrame({
    "Time":["08:30","10:00","14:00"],
    "Event":["USD CPI","FOMC Speech","Gold Inventory"],
    "Impact":["High","Medium","High"]
})

st.dataframe(calendar, use_container_width=True)

# =========================================================
# AI CHATBOT
# =========================================================

st.markdown("""
<h1 class="section-title">
AI TRADING ASSISTANT
</h1>
""", unsafe_allow_html=True)

prompt = st.text_input(
    "Ask AI about prop firms or trading..."
)

if prompt:

    responses = [
        "FTMO is best for consistency-based traders.",
        "FundingPips currently offers aggressive payout structures.",
        "Gold trading performs well during London and New York overlap.",
        "Blue Guardian has strong scaling plans.",
    ]

    st.markdown(f"""
    <div class="glass">

    <h2>🤖 AI Assistant</h2>

    <p style="margin-top:20px;">
    {random.choice(responses)}
    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# REAL-TIME NOTIFICATION
# =========================================================

notifications = [
    "🔥 Someone purchased a $100K FTMO Challenge",
    "🚀 Trader passed FundingPips in 5 days",
    "💰 $12,400 payout processed",
    "⚡ New trader funded instantly",
]

st.toast(random.choice(notifications))

# =========================================================
# SOUND EFFECT TOGGLE
# =========================================================

st.markdown("""
<h1 class="section-title">
SETTINGS
</h1>
""", unsafe_allow_html=True)

sound = st.toggle("Enable Sound Effects")

theme = st.toggle("Enable Light Mode")

if sound:
    st.success("Sound FX Enabled")

if theme:
    st.info("Light Mode Coming Soon")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

<h1 class="hero-title" style="font-size:3rem;">
QUANTUM PROP HUB
</h1>

<p style="margin-top:20px; opacity:0.8;">
Futuristic Prop Firm Affiliate Platform
Built For Elite Traders
</p>

<div style="margin-top:30px;">
🚀 AI Powered |
💸 Affiliate Optimized |
⚡ Cyberpunk Fintech UI
</div>

</div>
""", unsafe_allow_html=True)
