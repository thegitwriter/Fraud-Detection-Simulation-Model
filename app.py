import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# --- PAGE SETUP ---
st.set_page_config(page_title="Fintech Risk & Fraud Engine", layout="wide")
st.title("🛡️ Hybrid Fintech Risk & Fraud Optimization Engine")
st.caption("Tunnel-optimized stable deployment: combining deterministic rules with probabilistic Machine Learning.")

# --- SIDEBAR: PRODUCT MANAGEMENT RISK CONTROLS ---
st.sidebar.header("🎛️ Product Control Panel")
st.sidebar.markdown("Adjust the risk threshold using numeric inputs to bypass localtunnel widget limitations.")

pm_threshold = st.sidebar.number_input(
    "Probabilistic ML Risk Threshold (0.10 to 0.90)", 
    min_value=0.10, max_value=0.90, value=0.50, step=0.05
)

# --- CACHED MODEL TRAINING ---
@st.cache_resource
def train_backend_engine():
    np.random.seed(42)
    n_samples = 1500
    amounts = np.random.exponential(scale=5000, size=n_samples)
    times = np.random.uniform(0, 24, size=n_samples)
    device_scores = np.random.uniform(20, 100, size=n_samples)
    
    is_fraud = np.where((amounts > 15000) & (times > 23) & (device_scores < 40), 1, 0)
    noise = np.random.choice([0, 1], p=[0.96, 0.04], size=n_samples)
    is_fraud = np.logical_or(is_fraud, noise).astype(int)
    
    X = pd.DataFrame({'amount': amounts, 'time_of_day': times, 'device_trust': device_scores})
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, is_fraud)
    return model

model = train_backend_engine()

# --- LIVE INCOMING TRANSACTION INPUTS ---
st.header("💳 Simulate a Live Inbound Transaction")
col1, col2, col3, col4 = st.columns(4)

with col1:
    tx_amount = st.number_input("Transaction Amount (INR)", min_value=10, max_value=2000000, value=4500)
with col2:
    tx_time = st.selectbox("Time of Transaction (Hour Block)", list(range(24)), index=14)
with col3:
    tx_device = st.number_input("Device Trust Score (0-100)", min_value=0, max_value=100, value=85)
with col4:
    tx_location = st.selectbox("Current Location", ["Mumbai", "Delhi", "London", "New York"])

historical_location = "Mumbai" if tx_location != "London" else "Mumbai" 

# --- EXECUTE HYBRID DEFENSE LIFECYCLE ---
st.subheader("⚡ Real-Time Pipeline Evaluation")

# LAYER 1: DETERMINISTIC RULES CHECK
st.markdown("### `Layer 1: Deterministic Filter`")
if tx_amount > 1000000:
    st.error("🚨 CRITICAL BLOCK: Transaction exceeds absolute unverified platform cap (1,000,000 INR).")
    st.info("System Action: HARD_BLOCK | Reason: Absolute Risk Ceiling Enforced.")
elif tx_location == "London" and historical_location == "Mumbai":
    st.error("🚨 CRITICAL BLOCK: Geographic Impossibility Detected.")
    st.info("System Action: HARD_BLOCK | Reason: Device jumped across continents in under 60 seconds.")
else:
    st.success("✅ Passed Layer 1 rules engine cleanly. Routing traffic to Probabilistic Machine Learning Compute...")
    
    # LAYER 2: PROBABILISTIC MACHINE LEARNING SCORES
    st.markdown("### `Layer 2: Probabilistic ML Score`")
    input_data = pd.DataFrame([[tx_amount, tx_time, tx_device]], columns=['amount', 'time_of_day', 'device_trust'])
    fraud_probability = model.predict_proba(input_data)[0][1]
    
    st.metric("Calculated Fraud Risk Probability", f"{fraud_probability * 100:.2f}%")
    
    if fraud_probability >= pm_threshold:
        st.warning(f"⚠️ Transaction Risk ({fraud_probability*100:.1f}%) exceeds your set PM threshold ({pm_threshold*100:.1f}%).")
        st.info("🎯 Suggested Action: TRIGGER_CHALLENGE (Deploy Step-Up Multi-Factor Authentication/OTP to verify identity).")
    else:
        st.success(f"🚀 Transaction Risk ({fraud_probability*100:.1f}%) stays within your risk appetite limit ({pm_threshold*100:.1f}%).")
        st.info("🎯 Suggested Action: APPROVE (Instant checkout execution with zero user friction).")
