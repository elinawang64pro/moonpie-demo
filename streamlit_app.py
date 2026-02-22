import streamlit as st

if 'sos_triggered' not in st.session_state:
    st.session_state.sos_triggered = False

st.set_page_config(page_title="Baymax", layout="centered")
st.title("🌙 Baymax Band: Emotional Connection for the Elderly")

col_slider, col_gesture = st.columns([1, 1])

with col_slider:
    emg = st.slider("Simulated EMG Signal Strength", 0, 100, 20)

with col_gesture:
    st.subheader("👋 Hand Gesture")

    if emg < 30:
        hand_emoji = "🖐️"
        hand_text = "Relaxed open hand"
        hand_detail = "No action"
    elif emg < 70:
        hand_emoji = "🤏"
        hand_text = "Gentle squeeze"
        hand_detail = "Intent: 'Call family'"
    else:
        hand_emoji = "✊"
        hand_text = "Tight fist"
        hand_detail = "Intent: 'Emergency SOS'"

    st.markdown(f"<div style='font-size:80px; text-align:center'>{hand_emoji}</div>", unsafe_allow_html=True)
    st.markdown(f"**{hand_text}**  \n{hand_detail}  \nEMG: {emg}")

if emg < 30:
    base_state = "Calm"
    base_color = "#87CEEB"
    base_message = "How are you today?"
    base_button = "View Family Photos"
elif emg < 70:
    base_state = "Missing"
    base_color = "#FFA07A"
    base_message = "❤️ Missing your family?"
    base_button = "Video Call"
else:
    base_state = "Emergency"
    base_color = "#FF4444"
    base_message = "🚨 Emergency detected!"
    base_button = "Call Emergency Contact"

if st.session_state.sos_triggered:
    current_color = "#FF4444"
    current_state = "Emergency (SOS)"
    current_message = "🚨 SOS Activated!"
    current_button = "SOS Emergency"
else:
    current_color = base_color
    current_state = base_state
    current_message = base_message
    current_button = base_button

if emg < 70 and st.session_state.sos_triggered:
    st.session_state.sos_triggered = False

st.markdown(f"""
<style>
html, body, .stApp, .stMarkdown, .stText, div, p, h1, h2, h3, h4, h5, h6, span, button, label, .stSlider label, .stButton button {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif !important;
}}
.stApp {{
    background-color: {current_color};
    transition: background-color 0.5s;
}}
</style>
""", unsafe_allow_html=True)

# ===== 状态标题和主按钮（使用 current 变量） =====
st.header(f"Current State: {current_state}")
st.subheader(current_message)

if st.button(current_button, use_container_width=True):
    if "Missing" in current_state:
        st.success("Initiating video call...")
        st.image("https://via.placeholder.com/300x200?text=Family+Video", use_column_width=True)
    elif "Emergency" in current_state:
        st.error("Emergency contact notified. Location shared.")
    else:
        st.info("Displaying family photos...")


if emg >= 70 or st.session_state.sos_triggered:
    with st.container():
        st.markdown("---")
        st.error("🚨 **SOS MODE ACTIVATED**")
        st.markdown("**Calling 911 and emergency contacts...**")
        if st.button("❌ Cancel SOS", use_container_width=True):
            st.session_state.sos_triggered = False
            st.rerun()

st.markdown("---")
st.subheader("🗣️ Calling Children Right Now!")
voice = st.text_input("Say something... (simulated)", placeholder="e.g., Baymax take me home")
if voice:
    st.success("Navigating home. Family notified.")

st.markdown("---")
st.subheader("🖐️ Simulate Gestures on Band")
col1, col2 = st.columns(2)
with col1:
    if st.button("👆 Gentle Tap (轻按 → Call Kids)", use_container_width=True):
        st.success("Initiating video call...")
        st.image("https://via.placeholder.com/300x200?text=Family+Video", use_column_width=True)
with col2:
    if st.button("👇 Firm Press (重按 → SOS)", use_container_width=True, type="primary"):
        st.session_state.sos_triggered = True
        st.error("🚨 SOS triggered! Emergency contacts notified.")
        st.rerun()

# ===== 重置 SOS 按钮（备用，但卡片中已有取消按钮） =====
if st.session_state.get("sos_triggered", False):
    if st.button("✅ Clear SOS", use_container_width=True):
        st.session_state.sos_triggered = False
        st.rerun()