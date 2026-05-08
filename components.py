import streamlit as st

def hero_section():
    st.markdown("""
        <div style="text-align: center; padding: 120px 0 60px 0;" class="reveal">
            <h1 style="font-size: 5rem; font-weight: 800; line-height: 1.1; margin-bottom: 20px;">
                The Future of <br>
                <span style="background: linear-gradient(90deg, #00f2ff, #7000ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Prop Trading</span>
            </h1>
            <p style="color: #888; font-size: 1.4rem; max-width: 700px; margin: 0 auto 40px auto;">
                Verified insights, exclusive discounts, and institutional tools for the modern funded trader.
            </p>
            <div style="display: flex; gap: 20px; justify-content: center;">
                <button class="cta-button" style="width: auto;">View Firms</button>
                <button class="cta-button" style="width: auto; background: transparent; border: 1px solid var(--border);">Trading Tools</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

def stats_counter():
    cols = st.columns(4)
    data = [("Traders Funded", "12.4K+"), ("Total Payouts", "$42M+"), ("Daily Volume", "$1.2B"), ("Success Rate", "14%")]
    for i, (label, val) in enumerate(data):
        with cols[i]:
            st.markdown(f"""
                <div class="glass-card" style="text-align: center; padding: 1.5rem;">
                    <h2 style="color: #00f2ff; margin-bottom: 0;">{val}</h2>
                    <p style="color: #666; font-size: 0.8rem; margin: 0;">{label}</p>
                </div>
            """, unsafe_allow_html=True)

def economic_calendar():
    st.markdown("### 📅 Market <span style='color:#00f2ff'>Pulse</span>", unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
            <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border); padding: 10px 0;">
                <span>🔴 Non-Farm Payrolls</span>
                <span style="color: #ff4b4b;">High Volatility</span>
            </div>
            <div style="display: flex; justify-content: space-between; padding: 10px 0;">
                <span>🟡 FOMC Minutes</span>
                <span style="color: #ffaa00;">Medium Volatility</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

