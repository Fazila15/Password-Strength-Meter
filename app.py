import streamlit as st
import re
import requests
from streamlit_lottie import st_lottie

# Load Lottie Animation
def load_lottie_url(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

# Function to Check Password Strength
def check_password_strength(password):
    length = len(password)
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([has_lower, has_upper, has_digit, has_special])
    strength_levels = [
        ("Too Short ❌", "#FF4C4C", 0),
        ("Weak ⚠️", "#FF964C", 25),
        ("Moderate 🟡", "#FFD700", 50),
        ("Strong ✅", "#50C878", 75),
        ("Very Strong 🔥", "#007F00", 100)
    ]

    if length < 6:
        return strength_levels[0]
    elif length < 8 or score == 1:
        return strength_levels[1]
    elif score == 2:
        return strength_levels[2]
    elif score == 3:
        return strength_levels[3]
    else:
        return strength_levels[4]

# Load Security Animation
lottie_url = "https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_security = load_lottie_url(lottie_url)

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="wide")

# Page Title and Description with Gradient Background
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #0073E6, #50C878) !important;
            color: white;
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
        }
        .container {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
        .header {
            text-align: center;
            font-size: 38px;
            font-weight: 700;
            background: linear-gradient(to right, #0073E6, #50C878);
            -webkit-background-clip: text;
            color: transparent;
            text-transform: uppercase;
        }
        .subheader { 
            text-align: center; 
            font-size: 22px; 
            color: #444;
            font-weight: 500;
        }
        .footer { 
            text-align: center; 
            font-size: 16px; 
            color: #0073E6;
            font-weight: 500;
        }
        .password-box { 
            text-align: center; 
            font-size: 24px; 
            font-weight: bold; 
            transition: all 0.5s ease;
        }
        .gradient-bar {
            height: 12px; 
            border-radius: 10px; 
            transition: all 0.5s ease;
        }
        .password-input {
            text-align: center;
            font-size: 20px;
            padding: 12px;
            font-weight: 500;
        }
        .suggestions { 
            font-size: 16px; 
            color: #444;
        }
        hr {
            border-top: 1px solid #fff;
        }
        .animation-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 30px;
        }
    </style>
    <div class="header">Password Strength Meter By Fazila Malik</div>
    <div class="subheader">Check your password security in real-time!</div>
""", unsafe_allow_html=True)

# Display Best Password Practices at the Top
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #0073E6;'>💡 Best Practices for Creating a Strong Password</h3>", unsafe_allow_html=True)

st.markdown("""
- Use at least **12-16 characters** for better security.
- Include **uppercase & lowercase letters** (A-Z, a-z).
- Add **numbers** (0-9) and **special characters** (!, @, #, etc.).
- **Avoid common words, sequences**, or personal information.
- **Don't reuse passwords** across different accounts.
- **Use passphrases** for added security, e.g., `Sunset!In#Tokyo2024`.
- **Enable two-factor authentication (2FA)** for extra protection.
- **Never share your password** with anyone!
""", unsafe_allow_html=True)

# Show Lottie Animation in Center
st.markdown("<div class='animation-container'>", unsafe_allow_html=True)
if lottie_security:
    st_lottie(lottie_security, speed=1, width=250, height=250)
st.markdown("</div>", unsafe_allow_html=True)

# Password Input Section in a Card Style
password = st.text_input("Enter your password:", key="password")

if password:
    strength, color, score = check_password_strength(password)

    # Display Strength Meter
    st.markdown(f"""
        <div class="password-box" style="color: {color};">
            {strength}
        </div>
        <div class="gradient-bar" style="background: linear-gradient(to right, {color} {score}%, #D3D3D3 {score}%);"></div>
    """, unsafe_allow_html=True)

    # Password Improvement Suggestions
    st.subheader("🔹 How to Improve Your Password")
    suggestions = []
    if len(password) < 12:
        suggestions.append("- Use at least **12+ characters** for better security.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("- Add **uppercase letters** (A-Z).")
    if not re.search(r"[a-z]", password):
        suggestions.append("- Add **lowercase letters** (a-z).")
    if not re.search(r"[0-9]", password):
        suggestions.append("- Include **numbers** (0-9).")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("- Use **special characters** (!, @, #, etc.).")

    if suggestions:
        for suggestion in suggestions:
            st.markdown(f"✅ {suggestion}", unsafe_allow_html=True)
    else:
        st.success("Your password is **Ultra Strong**! 🚀")

# Footer Section
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>💙 Built with Streamlit | Ultra Secure Password Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Made By Fazila Malik💙</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
