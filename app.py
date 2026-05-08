# app.py
# RUN THIS:
# streamlit run app.py

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PropElite",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------------
# DATA
# -----------------------------------

firms = [
    {
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
        "features": [
            "Instant Payouts",
            "Free Retry",
            "Scaling Plan"
        ],
        "rating": 4.9,
        "reviews": 12400,
        "tag": "BEST SELLER",
        "tagColor": "#FFD700",
    },

    {
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
        "features": [
            "Scaling",
            "Bi Weekly Pay",
            "Copy Trading"
        ],
        "rating": 4.8,
        "reviews": 6700,
        "tag": "TOP SCALING",
        "tagColor": "#FF6B35",
    },

    {
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
        "features": [
            "100% Split",
            "Futures",
            "No Daily Loss"
        ],
        "rating": 4.6,
        "reviews": 5200,
        "tag": "100% SPLIT",
        "tagColor": "#A855F7",
    }
]

# -----------------------------------
# PAGE CSS
# -----------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    background: linear-gradient(
        160deg,
        #07070f 0%,
        #0b0b18 60%,
        #081018 100%
    );
    color: white;
}

.block-container {
    padding-top: 1rem;
}

.title {
    font-size: 70px;
    font-weight: 900;
    text-align: center;
    line-height: 1.1;
}

.gradient {
    background: linear-gradient(
        90deg,
        #00D4FF,
        #A855F7,
        #FF6B35,
        #00FF88
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align:center;
    color:#888;
    font-size:18px;
    max-width:800px;
    margin:auto;
    line-height:1.8;
}

.stat-box {
    background: rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    padding:25px;
    text-align:center;
}

.stat-number {
    color:#00D4FF;
    font-size:32px;
    font-weight:900;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HERO SECTION
# -----------------------------------

st.markdown("""
<div style='text-align:center;padding-top:30px;'>

<div style='
display:inline-block;
padding:8px 20px;
border-radius:20px;
background:rgba(0,212,255,0.08);
border:1px solid rgba(0,212,255,0.25);
color:#00D4FF;
font-size:12px;
font-weight:700;
margin-bottom:30px;
'>
🔥 EXCLUSIVE DISCOUNTS
</div>

<div class='title'>
Get Funded Fast.<br>
<span class='gradient'>
Trade With Confidence.
</span>
</div>

<div class='subtitle'>
Compare the world's best prop firms,
unlock exclusive discount codes,
and get funded up to $1.5M.
</div>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------
# STATS
# -----------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-number'>250K+</div>
        <div style='color:#777;'>Traders Funded</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-number'>$85M+</div>
        <div style='color:#777;'>Total Payouts</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-number'>40+</div>
        <div style='color:#777;'>Firms Reviewed</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='stat-box'>
        <div class='stat-number'>87%</div>
        <div style='color:#777;'>Avg Profit Split</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------
# SORT
# -----------------------------------

sort_by = st.selectbox(
    "Sort By",
    ["Top Rated", "Highest Split", "Best Discount"]
)

if sort_by == "Top Rated":
    firms = sorted(
        firms,
        key=lambda x: x["rating"],
        reverse=True
    )

elif sort_by == "Highest Split":
    firms = sorted(
        firms,
        key=lambda x: int(
            x["profitSplit"].replace("%","")
        ),
        reverse=True
    )

elif sort_by == "Best Discount":
    firms = sorted(
        firms,
        key=lambda x: int(
            x["discount"].replace("% OFF","")
        ),
        reverse=True
    )

# -----------------------------------
# CARDS
# -----------------------------------

st.subheader("🔥 Top Prop Firms")

for firm in firms:

    features_html = ""

    for f in firm["features"]:
        features_html += f"""
        <span style="
            background:rgba(255,255,255,0.06);
            padding:5px 10px;
            border-radius:20px;
            font-size:11px;
            display:inline-block;
            margin:3px;
            color:white;
        ">
        ✓ {f}
        </span>
        """

    accounts_html = ""

    for a in firm["accounts"]:
        accounts_html += f"""
        <span style="
            background:rgba(255,255,255,0.06);
            padding:5px 10px;
            border-radius:10px;
            font-size:11px;
            display:inline-block;
            margin:3px;
            color:white;
        ">
        {a}
        </span>
        """

    html = f"""
    <div style="
        background:#111827;
        border:1px solid #1f2937;
        border-radius:24px;
        padding:24px;
        margin-bottom:20px;
        color:white;
        font-family:sans-serif;
    ">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
        ">

            <div>

                <div style="
                    font-size:24px;
                    font-weight:900;
                    color:{firm["color"]};
                ">
                    {firm["logo"]}
                </div>

                <div style="
                    font-size:28px;
                    font-weight:800;
                    margin-top:5px;
                ">
                    {firm["name"]}
                </div>

                <div style="
                    color:{firm["color"]};
                    font-size:13px;
                    margin-top:5px;
                ">
                    {firm["badge"]}
                </div>

                <div style="
                    color:#9ca3af;
                    font-size:12px;
                    margin-top:5px;
                ">
                    ⭐ {firm["rating"]} ({firm["reviews"]:,} reviews)
                </div>

            </div>

            <div style="
                background:{firm["tagColor"]}22;
                color:{firm["tagColor"]};
                padding:8px 14px;
                border-radius:20px;
                font-size:11px;
                font-weight:700;
            ">
                {firm["tag"]}
            </div>

        </div>

        <hr style="
            border-color:#1f2937;
            margin:20px 0;
        ">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
        ">

            <div>

                <div style="
                    color:#6b7280;
                    font-size:12px;
                ">
                    Starting From
                </div>

                <div style="
                    font-size:38px;
                    font-weight:900;
                    margin-top:5px;
                ">
                    {firm["price"]}
                </div>

                <div style="
                    color:#6b7280;
                    text-decoration:line-through;
                ">
                    {firm["originalPrice"]}
                </div>

            </div>

            <div style="
                background:#FFD70022;
                color:#FFD700;
                padding:10px 16px;
                border-radius:12px;
                font-weight:800;
            ">
                {firm["discount"]}
            </div>

        </div>

        <div style="
            margin-top:20px;
            line-height:2;
        ">

            <div>
                <span style="color:#9ca3af;">
                    Profit Split:
                </span>

                <b>
                    {firm["profitSplit"]}
                </b>
            </div>

            <div>
                <span style="color:#9ca3af;">
                    Max Funding:
                </span>

                <b>
                    {firm["maxFunding"]}
                </b>
            </div>

            <div>
                <span style="color:#9ca3af;">
                    Challenge:
                </span>

                <b>
                    {firm["challenge"]}
                </b>
            </div>

        </div>

        <div style="margin-top:20px;">
            {features_html}
        </div>

        <div style="
            margin-top:20px;
            background:rgba(0,212,255,0.08);
            border:1px dashed rgba(0,212,255,0.3);
            border-radius:12px;
            padding:12px;
        ">

            <div style="
                color:#00D4FF;
                font-weight:700;
                font-size:13px;
            ">
                Promo Code:
                ELITE{firm["name"][:4].upper()}10
            </div>

        </div>

        <div style="margin-top:20px;">
            {accounts_html}
        </div>

    </div>
    """

    components.html(
        html,
        height=550,
        scrolling=False
    )

    st.button(
        f"Get Funded → {firm['name']}"
    )

# -----------------------------------
# FOOTER
# -----------------------------------

st.write("")
st.write("")

st.markdown("""
<div style='
text-align:center;
padding:40px;
color:#666;
'>

<div style='
font-size:28px;
font-weight:900;
background:linear-gradient(
90deg,
#00D4FF,
#A855F7
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
'>
⚡ PropElite
</div>

<div style='margin-top:15px;font-size:13px;'>
Trading involves risk.<br>
Always do your own research.
</div>

<div style='margin-top:10px;font-size:12px;'>
© 2026 PropElite
</div>

</div>
""", unsafe_allow_html=True)
