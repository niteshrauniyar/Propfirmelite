# app.py
# Run: streamlit run app.py

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PropElite",
    page_icon="⚡",
    layout="wide"
)

# -------------------------
# DATA
# -------------------------

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
        "accounts": ["$10K","$25K","$50K","$100K","$200K"],
        "profitSplit": "90%",
        "maxFunding": "$400K",
        "challenge": "2-Phase",
        "features": ["Instant Payouts","Free Retry","Scaling Plan","MetaTrader 4/5"],
        "rating": 4.9,
        "reviews": 12400,
        "tag": "BEST SELLER",
        "tagColor": "#FFD700",
    },
    {
        "id": 2,
        "name": "MyForexFunds",
        "logo": "MFF",
        "color": "#00FF88",
        "badge": "⚡ Fastest Payout",
        "discount": "15% OFF",
        "originalPrice": "$129",
        "price": "$109",
        "accounts": ["$5K","$10K","$25K","$50K","$100K"],
        "profitSplit": "85%",
        "maxFunding": "$300K",
        "challenge": "1-Phase",
        "features": ["Weekly Payouts","No Min Days","News Trading","All Strategies"],
        "rating": 4.7,
        "reviews": 8900,
        "tag": "FASTEST",
        "tagColor": "#00FF88",
    },
    {
        "id": 3,
        "name": "The Funded Trader",
        "logo": "TFT",
        "color": "#FF6B35",
        "badge": "🔥 High Scaling",
        "discount": "12% OFF",
        "originalPrice": "$175",
        "price": "$154",
        "accounts": ["$25K","$50K","$100K","$200K"],
        "profitSplit": "90%",
        "maxFunding": "$1.5M",
        "challenge": "2-Phase",
        "features": ["$1.5M Scaling","Bi-Weekly Pay","Royal Program","Copy Trading"],
        "rating": 4.8,
        "reviews": 6700,
        "tag": "TOP SCALING",
        "tagColor": "#FF6B35",
    },
    {
        "id": 4,
        "name": "Apex Trader",
        "logo": "APX",
        "color": "#A855F7",
        "badge": "💎 Futures Elite",
        "discount": "20% OFF",
        "originalPrice": "$167",
        "price": "$133",
        "accounts": ["$25K","$50K","$100K","$150K","$250K"],
        "profitSplit": "100%",
        "maxFunding": "$250K",
        "challenge": "1-Phase",
        "features": ["100% Payout","Futures Only","No Daily Loss","CME Traded"],
        "rating": 4.6,
        "reviews": 5200,
        "tag": "100% SPLIT",
        "tagColor": "#A855F7",
    },
]

stats = [
    {"label": "Traders Funded", "value": "250,000+"},
    {"label": "Total Payouts", "value": "$85M+"},
    {"label": "Firms Reviewed", "value": "40+"},
    {"label": "Avg Profit Split", "value": "87%"},
]

testimonials = [
    {
        "name": "Alex R.",
        "country": "🇺🇸 USA",
        "text": "Used the FTMO discount code from this site — saved $30 and passed first try.",
        "amount": "$12,400 earned"
    },
    {
        "name": "Priya M.",
        "country": "🇮🇳 India",
        "text": "TFT's scaling to $1.5M is real. This platform gave me exactly what I needed.",
        "amount": "$8,200 earned"
    },
    {
        "name": "James K.",
        "country": "🇬🇧 UK",
        "text": "Apex Trader's 100% split is no joke. Found it here, funded in 3 weeks.",
        "amount": "$21,000 earned"
    },
]

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

html, body, [class*="css"]  {
    background: linear-gradient(160deg,#07070f 0%,#0b0b18 60%,#080f18 100%);
    color: white;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 68px;
    font-weight: 900;
    text-align: center;
    line-height: 1.1;
    margin-bottom: 10px;
}

.gradient-text {
    background: linear-gradient(90deg,#00D4FF,#A855F7,#FF6B35,#00FF88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    text-align: center;
    color: #999;
    font-size: 18px;
    max-width: 800px;
    margin: auto;
    line-height: 1.8;
}

.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 24px;
    transition: 0.3s;
    height: 100%;
}

.card:hover {
    border: 1px solid #00D4FF;
    transform: translateY(-6px);
}

.tag {
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 700;
}

.price {
    font-size: 34px;
    font-weight: 900;
}

.stat-box {
    background: rgba(255,255,255,0.03);
    border-radius: 16px;
    text-align: center;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.08);
}

.stat-value {
    color: #00D4FF;
    font-size: 28px;
    font-weight: 900;
}

.feature {
    background: rgba(255,255,255,0.06);
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 11px;
    display: inline-block;
    margin: 3px;
}

.review-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
}

.footer {
    text-align:center;
    color:#666;
    margin-top:50px;
    font-size:12px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HERO
# -------------------------

st.markdown("""
<div style='text-align:center; margin-top:20px;'>

<div style='display:inline-block;
background:rgba(0,212,255,0.08);
border:1px solid rgba(0,212,255,0.25);
padding:8px 20px;
border-radius:20px;
font-size:13px;
color:#00D4FF;
margin-bottom:20px;'>
🔥 EXCLUSIVE DISCOUNTS — UP TO 20% OFF
</div>

<div class='main-title'>
Get Funded Fast.<br>
<span class='gradient-text'>Trade With Confidence.</span>
</div>

<div class='hero-sub'>
Compare the world's best prop firm challenges, unlock exclusive discount codes,
and get funded up to <b>$1.5M</b> with industry-leading profit splits.
</div>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# -------------------------
# STATS
# -------------------------

cols = st.columns(4)

for col, stat in zip(cols, stats):
    with col:
        st.markdown(f"""
        <div class='stat-box'>
            <div class='stat-value'>{stat['value']}</div>
            <div style='color:#777;font-size:13px;'>{stat['label']}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# -------------------------
# SORT
# -------------------------

sort_option = st.selectbox(
    "Sort By",
    ["Top Rated", "Best Discount", "Highest Split"]
)

if sort_option == "Top Rated":
    firms = sorted(firms, key=lambda x: x["rating"], reverse=True)

elif sort_option == "Best Discount":
    firms = sorted(
        firms,
        key=lambda x: int(x["discount"].replace("% OFF", "")),
        reverse=True
    )

elif sort_option == "Highest Split":
    firms = sorted(
        firms,
        key=lambda x: int(x["profitSplit"].replace("%", "")),
        reverse=True
    )

# -------------------------
# FIRM CARDS
# -------------------------

st.subheader("🔥 Top Prop Firms")

cols = st.columns(2)

for i, firm in enumerate(firms):

    with cols[i % 2]:

        features_html = "".join([
            f"<span class='feature'>✓ {f}</span>"
            for f in firm["features"]
        ])

        accounts_html = "".join([
            f"<span class='feature'>{a}</span>"
            for a in firm["accounts"]
        ])

        stars = "⭐" * int(firm["rating"])

        st.markdown(f"""
        <div class='card'>

            <div style='display:flex;justify-content:space-between;align-items:center;'>

                <div>
                    <div style='font-size:24px;font-weight:900;color:{firm["color"]};'>
                        {firm["logo"]}
                    </div>

                    <div style='font-size:22px;font-weight:800;'>
                        {firm["name"]}
                    </div>

                    <div style='color:{firm["color"]};font-size:13px;'>
                        {firm["badge"]}
                    </div>

                    <div style='font-size:12px;color:#999;margin-top:4px;'>
                        {stars} {firm["rating"]} ({firm["reviews"]:,} reviews)
                    </div>
                </div>

                <div class='tag'
                style='background:{firm["tagColor"]}22;color:{firm["tagColor"]};'>
                    {firm["tag"]}
                </div>

            </div>

            <hr style='border-color:#222;margin:18px 0;'>

            <div style='display:flex;justify-content:space-between;align-items:center;'>

                <div>
                    <div style='color:#777;font-size:12px;'>Starting From</div>
                    <div class='price'>{firm["price"]}</div>
                    <div style='color:#666;text-decoration:line-through;'>
                        {firm["originalPrice"]}
                    </div>
                </div>

                <div style='
                    background:#FFD70022;
                    color:#FFD700;
                    padding:10px 16px;
                    border-radius:12px;
                    font-weight:800;
                '>
                    {firm["discount"]}
                </div>

            </div>

            <div style='margin-top:18px;'>

                <div style='display:flex;justify-content:space-between;margin-bottom:8px;'>
                    <span style='color:#777;'>Profit Split</span>
                    <b>{firm["profitSplit"]}</b>
                </div>

                <div style='display:flex;justify-content:space-between;margin-bottom:8px;'>
                    <span style='color:#777;'>Max Funding</span>
                    <b>{firm["maxFunding"]}</b>
                </div>

                <div style='display:flex;justify-content:space-between;'>
                    <span style='color:#777;'>Challenge</span>
                    <b>{firm["challenge"]}</b>
                </div>

            </div>

            <div style='margin-top:18px;'>
                {features_html}
            </div>

            <div style='margin-top:18px;'>
                <div style='color:#00D4FF;font-weight:700;margin-bottom:8px;'>
                    Promo Code: ELITE{firm["name"][:4].upper()}10
                </div>
            </div>

            <div style='margin-top:10px;'>
                {accounts_html}
            </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Get Funded → {firm['name']}", key=firm["id"]):
            st.success(f"Selected {firm['name']}")

# -------------------------
# COMPARISON TABLE
# -------------------------

st.write("")
st.write("")
st.subheader("⚖️ Compare Firms")

compare_df = pd.DataFrame([
    {
        "Firm": f["name"],
        "Profit Split": f["profitSplit"],
        "Max Funding": f["maxFunding"],
        "Challenge": f["challenge"],
        "Price": f["price"],
        "Rating": f["rating"],
    }
    for f in firms
])

st.dataframe(compare_df, use_container_width=True)

# -------------------------
# TESTIMONIALS
# -------------------------

st.write("")
st.write("")
st.subheader("💬 Real Traders. Real Results.")

tcols = st.columns(3)

for col, t in zip(tcols, testimonials):
    with col:
        st.markdown(f"""
        <div class='review-box'>

            <div style='font-size:18px;font-weight:700;'>
                {t["name"]}
            </div>

            <div style='color:#888;font-size:12px;margin-bottom:12px;'>
                {t["country"]}
            </div>

            <div style='color:#bbb;line-height:1.7;font-size:13px;'>
                "{t["text"]}"
            </div>

            <div style='
                margin-top:16px;
                background:rgba(0,255,136,0.08);
                border:1px solid rgba(0,255,136,0.18);
                color:#00FF88;
                padding:8px 12px;
                border-radius:10px;
                font-weight:700;
                font-size:12px;
            '>
                💰 {t["amount"]}
            </div>

        </div>
        """, unsafe_allow_html=True)

# -------------------------
# CTA
# -------------------------

st.write("")
st.write("")

st.markdown("""
<div style='
text-align:center;
padding:50px 20px;
background:rgba(255,255,255,0.03);
border-radius:24px;
border:1px solid rgba(255,255,255,0.08);
'>

<div style='color:#A855F7;font-weight:700;letter-spacing:3px;font-size:12px;'>
LIMITED TIME OFFER
</div>

<div style='font-size:42px;font-weight:900;margin-top:10px;'>
Ready to Trade Firm Capital?
</div>

<div style='color:#888;margin-top:12px;font-size:15px;'>
Use our exclusive discount codes and save on your first challenge today.
</div>

</div>
""", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------

st.markdown("""
<div class='footer'>

<div style='font-size:22px;font-weight:900;
background:linear-gradient(90deg,#00D4FF,#A855F7);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;'>
⚡ PropElite
</div>

<div style='margin-top:12px;'>
This website contains affiliate links. We may earn a commission on purchases.
Trading involves risk. Always DYOR.
</div>

<div style='margin-top:8px;'>
© 2026 PropElite Affiliate. All rights reserved.
</div>

</div>
""", unsafe_allow_html=True)
