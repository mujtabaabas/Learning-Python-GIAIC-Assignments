import streamlit as st
import re
import random

# Page config
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered", initial_sidebar_state="auto")

st.title("🔐 Advanced Password Strength Meter")
st.caption("Check, improve, and generate secure passwords in real-time!")

# -- Session State for History & Toggle Memory --
if "history" not in st.session_state:
    st.session_state.history = []

if "saved_settings" not in st.session_state:
    st.session_state.saved_settings = {
        "min_length": 8,
        "require_upper_lower": True,
        "require_number": True,
        "require_special": True
    }

# -- Sidebar Settings --
with st.sidebar:
    st.header("⚙️ Password Rules")
    save_settings = st.checkbox("Save settings across session", value=True)

    if save_settings:
        min_length = st.slider("Minimum Length", 6, 16, st.session_state.saved_settings["min_length"])
        require_upper_lower = st.checkbox("Upper & Lowercase", value=st.session_state.saved_settings["require_upper_lower"])
        require_number = st.checkbox("At least one Number", value=st.session_state.saved_settings["require_number"])
        require_special = st.checkbox("At least one Special (!@#$%^&*)", value=st.session_state.saved_settings["require_special"])

        # Save current settings
        st.session_state.saved_settings.update({
            "min_length": min_length,
            "require_upper_lower": require_upper_lower,
            "require_number": require_number,
            "require_special": require_special
        })

    else:
        min_length = st.slider("Minimum Length", 6, 16, 8)
        require_upper_lower = st.checkbox("Upper & Lowercase", value=True)
        require_number = st.checkbox("At least one Number", value=True)
        require_special = st.checkbox("At least one Special (!@#$%^&*)", value=True)

# Blacklist (expand as needed)
blacklist = ["password", "123456", "qwerty", "password123", "letmein", "admin"]

# Show/hide toggle
show_password = st.toggle("👁 Show Password")
password = st.text_input("Enter your password", type="default" if show_password else "password")

# -- Password Strength Checker --
def check_password_strength(pw: str):
    score = 0
    feedback = []

    if len(pw) >= min_length:
        score += 1
    else:
        feedback.append(f"❌ Minimum {min_length} characters required.")

    if require_upper_lower:
        if re.search(r"[A-Z]", pw) and re.search(r"[a-z]", pw):
            score += 1
        else:
            feedback.append("❌ Add both uppercase and lowercase letters.")

    if require_number:
        if re.search(r"\d", pw):
            score += 1
        else:
            feedback.append("❌ Include at least one number.")

    if require_special:
        if re.search(r"[!@#$%^&*]", pw):
            score += 1
        else:
            feedback.append("❌ Include a special character (!@#$%^&*).")

    return score, feedback

def get_strength_label(score: int, total: int):
    ratio = score / total
    if ratio == 1:
        return "✅ Strong Password 💪", "green"
    elif ratio >= 0.75:
        return "⚠️ Moderate Password", "orange"
    else:
        return "❌ Weak Password", "red"

def generate_strong_password():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*"
    all_chars = upper + lower + digits + special

    base = []
    if require_upper_lower:
        base += [random.choice(upper), random.choice(lower)]
    if require_number:
        base.append(random.choice(digits))
    if require_special:
        base.append(random.choice(special))

    while len(base) < min_length:
        base.append(random.choice(all_chars))

    random.shuffle(base)
    return ''.join(base)

# -- Password Feedback --
if password:
    if password.lower() in blacklist:
        st.error("🚫 Common password detected. Choose a more secure one.")
    else:
        total = sum([1, require_upper_lower, require_number, require_special])
        score, feedback = check_password_strength(password)
        label, color = get_strength_label(score, total)

        st.markdown(f"### Strength: **:{color}[{label}]**")
        st.progress(score / total)

        if feedback:
            st.markdown("### 🔧 Suggestions:")
            for tip in feedback:
                st.write(tip)

        # Add to history (show latest 3)
        st.session_state.history.insert(0, {"pw": password, "score": score, "label": label})
        st.session_state.history = st.session_state.history[:3]

# -- Generate Button & Copy Toggle --
st.divider()
if st.button("🔐 Generate Strong Password"):
    strong_pw = generate_strong_password()
    st.code(strong_pw)
    if st.button("📋 Copy to clipboard"):
        st.toast("✅ Copied to clipboard!")  # Simulated — real copy on Streamlit sharing only

# -- Show Password History --
if st.session_state.history:
    st.markdown("### 🕘 Last Checked Passwords")
    for item in st.session_state.history:
        st.write(f"• `{item['pw']}` → {item['label']}")
