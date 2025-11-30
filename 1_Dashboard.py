import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from utils.enhanced_nav import navigation_with_auth, set_page_name

# Set current page name for highlighting
set_page_name("Dashboard")

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

# --- SIMPLE AUTH CHECK ---
def ensure_logged_in():
    if not st.session_state.get("logged_in"):
        st.switch_page("pages/Loginpage.py")  # redirect to login page

ensure_logged_in()

# Call navigation for authenticated users (returns current theme colors)
theme = navigation_with_auth()

# --- DISABLE BLACK & WHITE THEME ON THIS PAGE ---
if "bw_theme" in st.session_state:
    st.session_state["bw_theme"] = False

# --- ENHANCED CSS STYLING WITH HOVER EFFECTS ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {{display: none !important;}}
    
    body {{
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, {theme['background']} 0%, #302B63 50%, #24243e 100%);
        color: {theme['text']};
    }}

    .main .block-container {{
        padding: 2rem 1rem;
        max-width: 1200px;
        margin: 0 auto;
    }}

    .dashboard-header {{
        background: linear-gradient(135deg, {theme['primary']} 0%, {theme['secondary']} 100%);
        padding: 40px;
        border-radius: 25px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }}

    .dashboard-header:hover {{
        transform: translateY(-3px);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
        background: linear-gradient(135deg, {theme['secondary']} 0%, {theme['primary']} 100%);
    }}

    .dashboard-card {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: all 0.3s ease;
    }}

    .dashboard-card:hover {{
        background: rgba(255, 255, 255, 0.12);
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(31, 38, 135, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.25);
    }}

    .dashboard-stats {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
    }}

    .stat-card {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }}

    .stat-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.5s;
    }}

    .stat-card:hover::before {{
        left: 100%;
    }}

    .stat-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba({theme['primary'][1:3]}, {theme['primary'][3:5]}, {theme['primary'][5:7]}, 0.5);
        background: rgba(255, 255, 255, 0.15);
    }}

    .stat-card:hover .stat-number {{
        color: #fff;
        text-shadow: 0 0 20px {theme['primary']};
        transform: scale(1.1);
    }}

    .stat-number {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {theme['primary']};
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }}

    .stat-label {{
        font-size: 1.1rem;
        opacity: 0.8;
        transition: all 0.3s ease;
    }}

    .stat-card:hover .stat-label {{
        opacity: 1;
        font-weight: 600;
    }}

    .iframe-container {{
        border-radius: 15px; 
        overflow: hidden; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
        border: 1px solid rgba(255,255,255,0.1);
        margin-top: 20px;
        transition: all 0.3s ease;
        position: relative;
    }}

    .iframe-container:hover {{
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.2);
    }}

    /* Hide Power BI branding and controls */
    .iframe-container iframe {{
        border-radius: 15px;
    }}

    /* Additional hover effects for feature cards */
    .feature-card {{
        padding: 20px;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }}

    .feature-card:hover {{
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-3px);
        border: 1px solid rgba({theme['primary'][1:3]}, {theme['primary'][3:5]}, {theme['primary'][5:7]}, 0.3);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }}

    .feature-card h4 {{
        transition: all 0.3s ease;
    }}

    .feature-card:hover h4 {{
        color: {theme['primary']} !important;
    }}

    /* Animated gradient border effect */
    @keyframes gradient-border {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}

    .animated-border {{
        background: linear-gradient(-45deg, {theme['primary']}, {theme['secondary']}, {theme['primary']}, {theme['secondary']});
        background-size: 400% 400%;
        animation: gradient-border 3s ease infinite;
        padding: 2px;
        border-radius: 17px;
    }}

    .animated-border .iframe-container {{
        background: #1a1a2e;
        margin: 0;
    }}

    /* Pulse effect for important elements */
    @keyframes pulse {{
        0% {{
            box-shadow: 0 0 0 0 rgba({theme['primary'][1:3]}, {theme['primary'][3:5]}, {theme['primary'][5:7]}, 0.7);
        }}
        70% {{
            box-shadow: 0 0 0 10px rgba({theme['primary'][1:3]}, {theme['primary'][3:5]}, {theme['primary'][5:7]}, 0);
        }}
        100% {{
            box-shadow: 0 0 0 0 rgba({theme['primary'][1:3]}, {theme['primary'][3:5]}, {theme['primary'][5:7]}, 0);
        }}
    }}

    .pulse-effect {{
        animation: pulse 2s infinite;
    }}

    /* Smooth scroll behavior */
    html {{
        scroll-behavior: smooth;
    }}

    /* Custom scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
    }}

    ::-webkit-scrollbar-track {{
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
    }}

    ::-webkit-scrollbar-thumb {{
        background: {theme['primary']};
        border-radius: 10px;
    }}

    ::-webkit-scrollbar-thumb:hover {{
        background: {theme['secondary']};
    }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="dashboard-header">
    <h1>📊 Interactive Analytics Dashboard</h1>
    <p style="margin: 10px 0 0 0; font-size: 1.2rem; opacity: 0.9;">
        Explore comprehensive data insights with our advanced analytics platform
    </p>
</div>
""", unsafe_allow_html=True)

# --- QUICK STATS SECTION ---
st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
st.markdown("""
<div class="dashboard-stats">
    <div class="stat-card pulse-effect">
        <div class="stat-number">195+</div>
        <div class="stat-label">Countries Covered</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">2.1M+</div>
        <div class="stat-label">Data Points</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">24/7</div>
        <div class="stat-label">Real-time Updates</div>
    </div>
    <div class="stat-card pulse-effect">
        <div class="stat-number">99.9%</div>
        <div class="stat-label">Uptime Guarantee</div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- POWER BI DASHBOARD SECTION ---
st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)

# The public URL to your Power BI report
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZjE3NDI4NWQtOTA5OC00MzFlLWJmOTAtNDdkYWY3MjM0MDM2IiwidCI6ImZhODQ5MTk4LTc5N2EtNDgyYS1iYmIxLTYwZWMwZTQyNmZmNCJ9&pageName=b24cc4cc9db51e55479a"

# Enhanced iframe code with branding removal
iframe_code = f'''
    <div class="animated-border">
        <div class="iframe-container">
            <iframe title="Travel Analytics Dashboard" 
                    width="100%" 
                    height="650" 
                    src="{power_bi_url}&chromeless=1&hideNavigation=true" 
                    frameborder="0" 
                    allowFullScreen="true"
                    style="border-radius: 15px; display: block;"
                    sandbox="allow-scripts allow-same-origin allow-popups allow-forms">
            </iframe>
        </div>
    </div>
    <style>
        /* Additional CSS to hide Power BI branding */
        iframe[title*="Power BI"], iframe[src*="powerbi"] {{
            filter: none !important;
        }}
        
        /* Hide any Power BI watermarks or logos */
        .iframe-container iframe::after {{
            content: '';
            position: absolute;
            bottom: 0;
            right: 0;
            width: 200px;
            height: 50px;
            background: #1a1a2e;
            z-index: 1000;
        }}
    </style>
'''

# Add some helpful text before the dashboard
st.markdown("""
<h3 style="color: #f5f5f5; margin-bottom: 20px; text-align: center;">
    🎯 Interactive Travel Data Visualization
</h3>
<p style="text-align: center; opacity: 0.8; margin-bottom: 30px;">
    Use the filters and controls within the dashboard to explore different aspects of travel data. 
    Click on chart elements to drill down into specific insights.
</p>
""", unsafe_allow_html=True)

# Embed the iframe in the Streamlit app
components.html(iframe_code, height=670, scrolling=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD FEATURES SECTION ---
st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
st.markdown(f"""
<h3 style="color: {theme['primary']}; margin-bottom: 20px;">🔧 Dashboard Features</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
    <div class="feature-card">
        <h4 style="color: #f5f5f5; margin-bottom: 10px;">📊 Interactive Visualizations</h4>
        <p style="opacity: 0.8;">Click, filter, and drill down into data points for detailed insights.</p>
    </div>
    <div class="feature-card">
        <h4 style="color: #f5f5f5; margin-bottom: 10px;">🔄 Real-time Data</h4>
        <p style="opacity: 0.8;">Dashboard updates automatically with the latest travel analytics.</p>
    </div>
    <div class="feature-card">
        <h4 style="color: #f5f5f5; margin-bottom: 10px;">📱 Responsive Design</h4>
        <p style="opacity: 0.8;">Optimized for viewing on desktop, tablet, and mobile devices.</p>
    </div>
    <div class="feature-card">
        <h4 style="color: #f5f5f5; margin-bottom: 10px;">📈 Export Options</h4>
        <p style="opacity: 0.8;">Export charts and data directly from the interface.</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- ENHANCED FOOTER NOTE ---
st.markdown(f"""
<div style="text-align: center; margin-top: 40px; padding: 20px; 
            background: rgba(255,255,255,0.05); border-radius: 15px; 
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s ease; cursor: pointer;"
     onmouseover="this.style.background='rgba(255,255,255,0.1)'; this.style.transform='translateY(-2px)'"
     onmouseout="this.style.background='rgba(255,255,255,0.05)'; this.style.transform='translateY(0)'">
    <p style="opacity: 0.7; margin: 0;">
        💡 <strong>Tip:</strong> For the best experience, use full-screen mode and interact directly with the visualizations.
        If you encounter any issues, please refresh the page or contact support.
    </p>
</div>
""", unsafe_allow_html=True)