import streamlit as st
from styles import inject_ui_engine
from database import get_all_firms
import components as ui
import streamlit.components.v1 as v1

# Page Settings & SEO
st.set_page_config(page_title="Midnight Elite | Prop Analytics", layout="wide")

# Inject Styles and Animations
inject_ui_engine()

# --- GSAP GLOBAL ANIMATION SCRIPT ---
v1.html("""
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
<script>
    const reveal = () => {
        const parent = window.parent.document;
        gsap.registerPlugin(ScrollTrigger);
        
        parent.querySelectorAll('.glass-card').forEach((card) => {
            gsap.from(card, {
                scrollTrigger: { trigger: card, start: "top 90%" },
                y: 50, opacity: 0, duration: 1, ease: "power4.out"
            });
        });
    };
    setTimeout(reveal, 1000);
</script>
""", height=0)

# --- NAVBAR ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0;">
        <h2 style="margin: 0; font-weight: 800; letter-spacing: -1px;">MIDNIGHT<span style="color: #00f2ff;">ELITE</span></h2>
        <div style="display: flex; gap: 30px; align-items: center; color: #888;">
            <span>Firms</span><span>Tools</span><span>Leaderboard</span>
            <button class="cta-button" style="padding: 8px 20px; font-size: 0.8rem;">Join Community</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- RENDER SECTIONS ---
ui.hero_section()
ui.stats_counter()

st.write("##")
st.markdown("### 🏆 Top <span style='color:#00f2ff'>Ranked</span> Firms", unsafe_allow_html=True)

# Firm Grid
firms = get_all_firms()
cols = st.columns(3)
for i, firm in enumerate(firms):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="glass-card">
                <div style="background: rgba(0,242,255,0.05); padding: 5px 12px; border-radius: 6px; display: inline-block; font-size: 0.7rem; color: #00f2ff; margin-bottom: 15px;">
                    {firm[7].upper()}
                </div>
                <h2 style="margin: 0;">{firm[1]}</h2>
                <p style="color: #555;">Trust Score: {firm[5]}/5.0</p>
                <div style="margin: 20px 0; border-top: 1px solid var(--border); padding-top: 15px;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.9rem;">
                        <span style="color: #888;">Profit Split</span>
                        <span>{firm[3]}</span>
                    </div>
                </div>
                <button class="cta-button">Claim {firm[2]}</button>
            </div>
        """, unsafe_allow_html=True)

st.write("##")
c1, c2 = st.columns([2, 1])
with c1:
    ui.economic_calendar()
with c2:
    st.markdown("### 🤖 Trading <span style='color:#7000ff'>AI</span> Assistant", unsafe_allow_html=True)
    with st.container(border=True):
        st.text_input("Ask about evaluation rules...")
        st.button("Analyze Strategy", use_container_width=True)

# --- FOOTER ---
st.markdown("""
    <div style="margin-top: 100px; padding: 50px 0; border-top: 1px solid var(--border); text-align: center; color: #444;">
        <p>© 2026 Midnight Elite Markets. High-Frequency Affiliate Architecture.</p>
    </div>
""", unsafe_allow_html=True)
