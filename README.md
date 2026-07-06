# AI-Based Smart Allocation Engine for PM Internship Scheme

An intelligent, data-driven matching platform built to automate and optimize the allocation of candidates to various corporate roles under the Prime Minister's Internship Scheme. This engine replaces manual processing with scalable algorithms to ensure fair, efficient, and highly compatible candidate placements.

---

## 🚀 Features

* **Intelligent Skill Matching:** Uses Natural Language Processing (NLP) to parse applicant resumes/profiles against corporate job descriptions.
* **Multi-Constraint Optimization:** Dynamically balances candidate geographic preferences, reservation/quota rules, and industry prerequisites.
* **High-Throughput Scale:** Architected to handle high volumes of concurrent applications during the national application window.
* **Bias Mitigation:** Ensures an equitable and objective selection process using blind-matching parameters.

## 🛠️ Tech Stack

* **Backend / Engine:** Python, Scikit-Learn, Pandas (or your preferred language)
* **Matching Logic:** [e.g., Stable Marriage Algorithm, Linear Programming, or Cosine Similarity]
* **Database:** [e.g., PostgreSQL, MongoDB]

## 📋 Prerequisites

Before running this project locally, ensure you have the following installed:
* Python 3.10 or higher
* Git

## 🎮 Live Sandbox Demo Guide

The application features a **Self-Service Interactive Demo Mode** allowing visitors to evaluate the rule-based matchmaking matrix using their own profile details in real-time without uploading files.

### How to Test Your Own Allocation:
1. **Access the Live Web Application:** Go directly to https://pm-internship-scheme.streamlit.app to open the portal.
2. **Switch Evaluation Modes:** In **Step 1: Database Ingestion**, toggle the radio option from *“Use Dataset Simulation Profiles”* to **“Create My Custom Profile”**.
3. **Configure Your Parameters:** * Input your custom **Full Name**.
   * Adjust the slider to set your **Academic Score (%)**.
   * Pick your **Demographic Category** (General, OBC, SC, ST, PwD) to test the reservation logic.
   * Pick your target industry **Career Domain**.
4. **Trigger the Core Pipeline:** Scroll down to Step 2 and click the red **"Run Allocation Pipeline"** button.
5. **Verify the Output Matrix:** * Check the **📊 Final Allocation Matrix** tab to see your custom profile injected into the queue along with your dynamic **Assigned Industry Partner**.
   * Check the **📈 Statistical Distribution Metrics** tab to see how your profile dynamically shifts the structural demographic graphs!

---

## ⚙️ Installation & Setup

Follow these steps to run the allocation engine locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Monashri8127/AI-Based-Smart-Allocation-Engine-for-PM-Internship-Scheme.git](https://github.com/Monashri8127/AI-Based-Smart-Allocation-Engine-for-PM-Internship-Scheme.git)
   cd AI-Based-Smart-Allocation-Engine-for-PM-Internship-Scheme
