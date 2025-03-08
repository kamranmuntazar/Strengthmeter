import streamlit as st
import time
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("🔵 Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("🟢 Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("🟠 Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("🟣 Add at least one special character (!, @, #, etc.).")

    return strength, feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")
confirm_password = st.text_input("Confirm your password:", type="password")

if password and confirm_password:
    if password != confirm_password:
        st.error("❌ Passwords do not match! Please try again.")
    else:
        with st.spinner("Analyzing password... 🔍"):
            time.sleep(2)  # Simulating loading time

        strength, feedback = check_password_strength(password)
        st.progress(strength * 20)  # Strength in percentage (out of 5 levels)

        # Display feedback messages
        if strength == 5:
            st.success("🎉 Strong Password! Well Done! 🚀")
            st.toast("🎈 Your password is secure!")
            st.balloons()  # Celebrate strong password
        elif strength >= 3:
            st.warning("⚠ Moderate Password! Try adding more security.")
            for msg in feedback:
                st.write(f"❗ {msg}")
        else:
            st.error("❌ Weak Password! Improve security.")
            for msg in feedback:
                st.write(f"⚠ {msg}")

# Extra Fun Elements
with st.expander("🔎 Password Strength Criteria"):
    st.write("""
    - ✅ At least 8 characters  
    - 🔠 At least one uppercase letter  
    - 🔡 At least one lowercase letter  
    - 🔢 At least one number  
    - 🔣 At least one special character (!, @, #, etc.)  
    """)

st.snow()  # Adds a fun snowfall effect