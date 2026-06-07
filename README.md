# 🛡️ Hybrid Fintech Risk & Fraud Optimization Engine

An end-to-end, multi-layered transaction risk evaluation pipeline designed to balance user checkout friction against financial fraud losses. This project mirrors the foundational architecture used in industry-standard risk systems like Stripe Radar, Visa Advanced Authorization, and Microsoft Conditional Access.

## 🚀 How It Works (The 2-Step Dynamic Pipeline)

Instead of forcing a heavy, static 2-step verification (OTP/MFA) wall on every single transaction, this engine acts as an adaptive filter—evaluating risk profiles in real-time to ensure seamless checkouts for trusted traffic while automatically deploying identity challenges for high-risk anomalies.

### 🛑 Layer 1: The Deterministic Filter (The Check-Valve)
The first line of defense enforces hard, unyielding business logic constraints without computational overhead. Transactions are immediately scrutinized against absolute operational limits:
* **Absolute Capital Ceiling:** Instant hard blocks on any unverified transactions exceeding threshold limits (e.g., 1,000,000 INR).
* **Geographic Velocity Check:** Instant isolation of accounts showing geographic impossibility (e.g., a single device attempting transactions across separate continents within a 60-second window).

### 🧠 Layer 2: The Probabilistic ML Classifier (The Simulation Engine)
Transactions passing through Layer 1 enter a predictive machine learning environment. Utilizing a trained `RandomForestClassifier` mapping multi-variable correlations (Transaction Amount, Temporal Wavefront/Hour, and Device Trust Telemetry), the backend computes a granular fraud risk score from 0.00% to 100.00%.

### 🎛️ The PM Control Panel (The Factor of Safety)
The core business leverage of this platform is an interactive dashboard that empowers a Product Manager to dynamically calibrate the company's risk appetite:
* **High-Security Mode (Low Risk Threshold):** Minimizes fraud leakage but increases customer friction (higher false positives / user insults).
* **Smooth-UX Mode (High Risk Threshold):** Maximizes conversion rates and system flow velocity but tolerates calculated risk margins.

If the calculated Machine Learning fraud score stays safely below the PM's threshold, the transaction path goes green and resolves to an instant **APPROVE** with zero user friction. If the score breaches the threshold, the system dynamically drops an intermediate security wall, shifting its action path to **TRIGGER_CHALLENGE** (forcing a temporary hold until 2-Step Verification/MFA is cleared).

## 🛠️ Tech Stack & Architecture
* **Backend Core:** Python 3, NumPy, Pandas
* **Predictive Compute:** Scikit-Learn (RandomForest Machine Learning Framework)
* **Frontend Interface:** Streamlit (UI Engine)
* **Edge Delivery:** Cloudflare Tunnels (`cloudflared` reverse-proxy infrastructure)
