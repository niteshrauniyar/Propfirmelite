import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import pandas as pd
import sqlite3
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Midnight Markets | Prop Firm Elite",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DATABASE LOGIC ---
def init_db():
    conn = sqlite3.connect('prop_firms.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS firms 
                 (name TEXT, discount TEXT, split TEXT, price TEXT, rating REAL, link TEXT)''')
    # Seed data if empty
    c.execute("SELECT count(*) FROM firms")
    if c.fetchone()[0] == 0:
        firms = [
            ('FundingPips', '5% OFF', '80/20', '$399', 4.9, 'https://link.com'),
            ('FTMO', 'NONE', '90/10', '€540', 4.8, 'https://link.com'),
            ('Blue Guardian', '10% OFF', '85/15', '$497', 4.7, 'https://link.com')
        ]
        c.executemany("INSERT INTO firms VALUES (?,?,?,?,?,?)", firms)
    conn.commit()
    conn.close()

init_db()

# --- CSS INJECTION ---
def local_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        
        :root {
            --bg-dark: #050505;
            --neon-blue: #00f2ff;
            --glass-bg: rgba(255, 255, 255, 0.03);
            --border: rgba(255, 255, 255, 0.1);
        }

        .main { background-color: var(--bg-dark); color: white; font-family: 'Inter', sans-serif; }
        
        /* Glassmorphism Cards */
        .prop-card {
            background: var(--glass-bg);
            backdrop-filter: blur(15px);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 25px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-align: center;
        }
        .prop-card:hover {
            transform: translateY(-12px);
            border-color: var(--neon-blue);
            box-shadow: 0 0 30px rgba(0, 242, 255, 0.2);
        }

        /* Neon Buttons */
        .neon-btn {
            background: linear-gradient(45deg, #00f2ff, #0066ff);
            border: none;
            color: black;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
        }

        /* Animated Background Gradients */
        .gradient-bg {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at 50% 50%, #101014 0%, #050505 100%);
            z-index: -1;
        }

        /* Hide Streamlit elements */
        #MainMenu, footer, header {visibility: hidden;}
    </style>
    <div class="gradient-bg"></div>
    """, unsafe_allow_html=True)

local_css()

# --- GSAP ANIMATION WRAPPER ---
components.html("""
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script>
        window.parent.document.addEventListener('DOMContentLoaded', () => {
            gsap.from(".prop-card", {
                duration: 1, 
                y: 50, 
                opacity: 0, 
                stagger: 0.2, 
                ease: "power4.out"
            });
        });
    </script>
""", height=0)

# --- SECTIONS ---

def hero_section():
    st.markdown(f"""
        <div style="text-align: center; padding: 100px 0 50px 0;">
            <h1 style="font-size: 4rem; font-weight: 800; margin-bottom: 10px; background: -webkit-linear-gradient(#fff, #666); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Get Funded. Trade Like a Pro.
            </h1>
            <p style="color: #888; font-size: 1.2rem; margin-bottom: 30px;">
                Access the world's top Prop Firm challenges with exclusive discounts and institutional analytics.
            </p>
            <button class="neon-btn">Explore Challenges ↓</button>
        </div>
    """, unsafe_allow_html=True)

def prop_firm_grid():
    conn = sqlite3.connect('prop_firms.db')
    df = pd.read_sql_query("SELECT * FROM firms", conn)
    
    cols = st.columns(len(df))
    for i, row in df.iterrows():
        with cols[i]:
            st.markdown(f"""
                <div class="prop-card">
                    <h2 style="color: var(--neon-blue); margin-bottom: 5px;">{row['name']}</h2>
                    <p style="font-size: 0.9rem; color: #aaa;">Rating: ⭐ {row['rating']}</p>
                    <hr style="border: 0.5px solid var(--border); margin: 15px 0;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                        <span>Profit Split</span>
                        <span style="color: #00ff88;">{row['split']}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
                        <span>Starting At</span>
                        <span style="font-weight: 700;">{row['price']}</span>
                    </div>
                    <div style="background: rgba(0,242,255,0.1); padding: 10px; border-radius: 10px; margin-bottom: 15px;">
                        <code style="color: var(--neon-blue);">{row['discount']}</code>
                    </div>
                    <a href="{row['link']}" target="_blank" style="text-decoration: none;">
                        <button class="neon-btn" style="width: 100%; font-size: 0.8rem;">Claim Challenge</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

def trading_dashboard_preview():
    st.markdown("### <span style='color:#00f2ff'>Institutional</span> Dashboard Preview", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 2])
    
    with c1:
        st.markdown("""
            <div class="prop-card">
                <p style="color: #888; font-size: 0.8rem;">CURRENT EQUITY</p>
                <h2 style="margin: 0;">$104,240.50</h2>
                <p style="color: #00ff88; font-size: 0.8rem;">+4.24% Today</p>
            </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
            <div class="prop-card">
                <p style="color: #888; font-size: 0.8rem;">WIN RATE</p>
                <h2 style="margin: 0;">68.4%</h2>
                <div style="width: 100%; background: #222; height: 8px; border-radius: 10px; margin-top: 10px;">
                    <div style="width: 68%; background: var(--neon-blue); height: 100%; border-radius: 10px; box-shadow: 0 0 10px var(--neon-blue);"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        # Plotly Cinematic Chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=[100, 102, 101, 105, 104, 108], mode='lines', fill='tozeroy', 
                               line=dict(color='#00f2ff', width=3),
                               fillcolor='rgba(0, 242, 255, 0.1)'))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0), height=150,
            xaxis=dict(visible=False), yaxis=dict(visible=False)
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def earnings_calculator():
    st.markdown("### <span style='color:#00f2ff'>Affiliate</span> Earning Potential", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="prop-card">', unsafe_allow_html=True)
        col_in, col_out = st.columns(2)
        with col_in:
            refs = st.slider("Number of Referrals per month", 1, 500, 50)
            avg_comm = st.select_slider("Average Challenge Commission", options=[10, 25, 50, 100], value=50)
        with col_out:
            total = refs * avg_comm
            st.markdown(f"""
                <div style="text-align: center;">
                    <p style="color: #888;">ESTIMATED MONTHLY EARNINGS</p>
                    <h1 style="font-size: 4rem; color: #00ff88;">${total:,}</h1>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN RENDER ---
hero_section()
st.write("---")
prop_firm_grid()
st.write("---")
trading_dashboard_preview()
st.write("---")
earnings_calculator()

# --- NOTIFICATION POPUP (JavaScript) ---
components.html("""
    <div id="notif" style="position: fixed; bottom: 20px; right: 20px; background: rgba(0,242,255,0.1); backdrop-filter: blur(10px); border: 1px solid #00f2ff; padding: 15px; border-radius: 10px; color: white; display: none; font-family: sans-serif; font-size: 0.8rem; z-index: 9999;">
        ⚡ <b>New Payout:</b> Trader just received $4,200 from FundingPips!
    </div>
    <script>
        setTimeout(() => {
            document.getElementById('notif').style.display = 'block';
            setTimeout(() => { document.getElementById('notif').style.display = 'none'; }, 5000);
        }, 3000);
    </script>
""", height=100)
