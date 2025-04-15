import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Initialize session state for persistent storage across reruns
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}  # {"user1_data": {"encrypted_text": "xyz", "passkey": "hashed"}}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

if 'key' not in st.session_state:
    # Generate a key (this should be stored securely in production)
    st.session_state.key = Fernet.generate_key()

cipher = Fernet(st.session_state.key)

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    
    # Loop through stored data to check for a match
    for key, value in st.session_state.stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0  # Reset failed attempts on success
            return cipher.decrypt(encrypted_text.encode()).decode()
    
    # Increment failed attempts if no match is found
    st.session_state.failed_attempts += 1
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")
    st.info("Your data is encrypted with strong cryptography and can only be accessed with the correct passkey.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            data_id = hashlib.md5(encrypted_text.encode()).hexdigest()[:8]  # Create a unique ID
            st.session_state.stored_data[data_id] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            
            st.success("✅ Data stored securely!")
            st.code(encrypted_text, language="text")
            st.info("Copy this encrypted text to retrieve your data later")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    
    # Check if too many failed attempts
    if st.session_state.failed_attempts >= 3:
        st.warning("🔒 Too many failed attempts! Please reauthorize.")
        st.session_state.failed_attempts = 0
        choice = "Login"
        st.experimental_rerun()
    else:
        encrypted_text = st.text_area("Enter Encrypted Data:")
        passkey = st.text_input("Enter Passkey:", type="password")

        if st.button("Decrypt"):
            if encrypted_text and passkey:
                decrypted_text = decrypt_data(encrypted_text, passkey)

                if decrypted_text:
                    st.success("✅ Decryption successful!")
                    st.write("Decrypted Data:")
                    st.code(decrypted_text, language="text")
                else:
                    st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - st.session_state.failed_attempts}")
            else:
                st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Hardcoded for demo, replace with proper auth
            st.session_state.failed_attempts = 0  # Reset failed attempts upon successful login
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")