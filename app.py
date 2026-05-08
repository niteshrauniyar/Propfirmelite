# app.py
# RUN: streamlit run app.py

import streamlit as st

st.set_page_config(
    page_title="PropElite",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------
# DATA
# -----------------------------

firms = [
    {
        "id": 1,
        "name": "FTMO",
        "logo": "FTMO",
        "color": "#00D4FF",
        "badge": "🏆 #1 Rated",
        "discount": "10% OFF",
        "originalPrice": "$155",
        "price": "$139",
        "accounts": ["$10K","$25K","$50K","$100K"],
        "profitSplit": "90%",
        "maxFunding": "$400K",
        "challenge": "2-Phase",
        "features": ["Instant Payouts","Free Retry","Scaling Plan"],
        "rating": 4.9,
        "reviews": 12400,
        "tag": "BEST SELLER",
        "tagColor": "#FFD700",
    },

    {
        "id": 2,
        "name": "The Funded Trader",
        "logo": "TFT",
        "color": "#FF6B35",
        "badge": "🔥 High Scaling",
        "discount": "12% OFF",
        "originalPrice": "$175",
        "price": "$154",
        "accounts": ["$25K","$50K","$100K"],
        "profitSplit": "90%",
        "maxFunding": "$1.5M",
        "challenge": "2-Phase",
        "features": ["Scaling","Bi Weekly Pay","Copy Trading"],
        "rating": 4.8,
        "reviews": 6700,
        "tag": "TOP SCALING",
        "tagColor": "#FF6B35",
    },

    {
        "id": 3,
        "name": "Apex Trader",
        "logo": "APX",
        "color": "#A855F7",
        "badge": "💎 Futures Elite",
        "discount": "20% OFF",
        "originalPrice": "$167",
        "price": "$133",
        "accounts": ["$25K","$50K","$100K"],
        "profitSplit": "100%",
        "maxFunding": "$250K",
        "challenge": "1-Phase",
        "features": ["100% Split","Futures","No Daily Loss"],
        "rating": 4.6,
        "reviews": 5200,
        "tag": "100% SPLIT",
        "tagColor": "#A855F7",
    }
]

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    background: linear-gradient(160deg,#07070f 0%,#0b0b18 60%,#081018 100%);
    color: white;
    font-family: sans-serif;
}

.block-container {
    padding-top: 1rem;
}

.hero-title {
    font-size: 64px;
    font-weight: 900;
    text-align: center;
    line-height: 1.1;
}

.gradient {
    background: linear-gradient(90deg,#00D4FF,#A855F7,#FF6B35,#00FF88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align:center;
    color:#888;
    max-width:800px;
    margin:auto;
    line-height:1.8;
    font-size:18px;
}

.stat-box {
    background: rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:18px;
    padding:20px;
    text-align:center;
}

.stat-value {
    color:#00D4FF;
    font-size:30px;
    font-weight:900;
}

.card {
    background: rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:24px;
    padding:24px;
    margin-bottom:20px;
    transition:0.3s;
}

.card:hover {
    border:1px solid #00D4FF;
}

.feature {
    background: rgba(255,255,255,0.06);
    padding:5px 10px;
    border-radius:20px;
    font-size:11px;
    display:inline-block;
    margin:3px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------

st.markdown("""
<div style='text-align:center;padding-top:30px;padding-bottom:30px;'>

<div style='
display:inline-block;
padding:8px 20px;
border-radius:20px;
background:rgba(0,212,255,0.08);
border:1px solid rgba(0,212,255,0.25);
color:#00D4FF;
font-size:12px;
font-weight:700;
margin-bottom:25px;
'>
🔥 EXCLUSIVE DISCOUNTS
</div>

<div class='hero-title'>
Get Funded Fast.<br>
<span class='gradient'>
Trade With Confidence.
</span>
</div>

<div class='subtitle'>
Compare the world's best prop firms and unlock exclusive discounts with up to $1.5M funding.
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# STATS
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-value'>250K+</div>
        <div style='color:#777;'>Traders Funded</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-value'>$85M+</div>
        <div style='color:#777;'>Total Payouts</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-value'>40+</div>
        <div style='color:#777;'>Firms Reviewed</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-value'>87%</div>
        <div style='color:#777;'>Avg Profit Split</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------
# SORT
# -----------------------------

sort_option = st.selectbox(
    "Sort By",
    ["Top Rated", "Highest Split", "Best Discount"]
)

if sort_option == "Top Rated":
    firms = sorted(firms, key=lambda x: x["rating"], reverse=True)

elif sort_option == "Highest Split":
    firms = sorted(
        firms,
        key=lambda x: int(x["profitSplit"].replace("%","")),
        reverse=True
    )

elif sort_option == "Best Discount":
    firms = sorted(
        firms,
        key=lambda x: int(x["discount"].replace("% OFF","")),
        reverse=True
    )

# -----------------------------
# TOP FIRMS
# -----------------------------

st.subheader("🔥 Top Prop Firms")

col1, col2 = st.columns(2)

for i, firm in enumerate(firms):

    features_html = ""
    for f in firm["features"]:
        features_html += f"""
        <span class='feature'>✓ {f}</span>
        """

    accounts_html = ""
    for a in firm["accounts"]:
        accounts_html += f"""
        <span class='feature'>{a}</span>
        """

    html = f"""
    <div class='card'>

        <div style='display:flex;justify-content:space-between;align-items:center;'>

            <div>

                <div style='
                    font-size:24px;
                    font-weight:900;
                    color:{firm["color"]};
                '>
                    {firm["logo"]}
                </div>

                <div style='
                    font-size:24px;
                    font-weight:800;
                    color:white;
                '>
                    {firm["name"]}
                </div>

                <div style='
                    color:{firm["color"]};
                    font-size:13px;
                '>
                    {firm["badge"]}
                </div>

                <div style='
                    margin-top:5px;
                    color:#999;
                    font-size:12px;
                '>
                    ⭐ {firm["rating"]} ({firm["reviews"]:,} reviews)
                </div>

            </div>

            <div style='
                background:{firm["tagColor"]}22;
                color:{firm["tagColor"]};
                padding:6px 12px;
                border-radius:20px;
                font-size:11px;
                font-weight:700;
            '>
                {firm["tag"]}
            </div>

        </div>

        <hr style='border-color:#222;margin:18px 0;'>

        <div style='display:flex;justify-content:space-between;align-items:center;'>

            <div>

                <div style='color:#777;font-size:12px;'>
                    Starting From
                </div>

                <div style='
                    font-size:34px;
                    font-weight:900;
                    color:white;
                '>
                    {firm["price"]}
                </div>

                <div style='
                    color:#666;
                    text-decoration:line-through;
                '>
                    {firm["originalPrice"]}
                </div>

            </div>

            <div style='
                background:#FFD70022;
                color:#FFD700;
                padding:10px 15px;
                border-radius:12px;
                font-weight:800;
            '>
                {firm["discount"]}
            </div>

        </div>

        <div style='margin-top:20px;'>

            <div style='margin-bottom:8px;'>
                <span style='color:#777;'>Profit Split:</span>
                <b style='color:white;'> {firm["profitSplit"]}</b>
            </div>

            <div style='margin-bottom:8px;'>
                <span style='color:#777;'>Max Funding:</span>
                <b style='color:white;'> {firm["maxFunding"]}</b>
            </div>

            <div>
                <span style='color:#777;'>Challenge:</span>
                <b style='color:white;'> {firm["challenge"]}</b>
            </div>

        </div>

        <div style='margin-top:20px;'>
            {features_html}
        </div>

        <div style='
            margin-top:20px;
            background:rgba(0,212,255,0.08);
            border:1px dashed rgba(0,212,255,0.3);
            border-radius:12px;
            padding:12px;
        '>

            <div style='
                color:#00D4FF;
                font-weight:700;
                font-size:13px;
            '>
                Promo Code:
                ELITE{firm["name"][:4].upper()}10
            </div>

        </div>

        <div style='margin-top:15px;'>
            {accounts_html}
        </div>

    </div>
    """

    if i % 2 == 0:
        with col1:
            st.markdown(html, unsafe_allow_html=True)
            st.button(f"Get Funded → {firm['name']}", key=firm["id"])
    else:
        with col2:
            st.markdown(html, unsafe_allow_html=True)
            st.button(f"Get Funded → {firm['name']}", key=firm["id"])

# -----------------------------
# FOOTER
# -----------------------------

st.write("")
st.write("")

st.markdown("""
<div style='
text-align:center;
padding:40px;
color:#666;
'>

<div style='
font-size:26px;
font-weight:900;
background:linear-gradient(90deg,#00D4FF,#A855F7);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
'>
⚡ PropElite
</div>

<div style='margin-top:15px;font-size:13px;'>
Trading involves risk. This website contains affiliate links.
Always do your own research.
</div>

<div style='margin-top:10px;font-size:12px;'>
© 2026 PropElite
</div>

</div>
""", unsafe_allow_html=True)
