import streamlit as st

def inject_ui_engine():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
        
        :root {
            --neon-primary: #00f2ff;
            --neon-secondary: #7000ff;
            --bg-deep: #030303;
            --glass: rgba(255, 255, 255, 0.03);
            --border: rgba(255, 255, 255, 0.08);
        }

        .stApp { background: var(--bg-deep); font-family: 'Plus Jakarta Sans', sans-serif; }

        /* Animated Aurora Background */
        .aurora-bg {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at 20% 30%, rgba(0, 242, 255, 0.05) 0%, transparent 40%),
                        radial-gradient(circle at 80% 70%, rgba(112, 0, 255, 0.05) 0%, transparent 40%);
            z-index: -1;
        }

        /* High-End Glass Cards */
        .glass-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 2rem;
            transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
            position: relative;
            overflow: hidden;
        }

        .glass-card:hover {
            border-color: var(--neon-primary);
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 20px rgba(0, 242, 255, 0.1);
        }

        /* Neon Button */
        .cta-button {
            background: linear-gradient(90deg, var(--neon-primary), var(--neon-secondary));
            color: white; border: none; padding: 12px 32px;
            border-radius: 12px; font-weight: 700; cursor: pointer;
            transition: 0.3s; width: 100%; text-transform: uppercase;
        }
        .cta-button:hover { filter: brightness(1.2); box-shadow: 0 0 20px rgba(0, 242, 255, 0.5); }

        /* Hide Streamlit Clutter */
        #MainMenu, footer, header { visibility: hidden; }
    </style>
    <div class="aurora-bg"></div>
    """, unsafe_allow_html=True)
