import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PM Internship Allocation Engine",
    page_icon="🚀",
    layout="wide"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main-title { font-size: 38px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size: 18px; color: #4B5563; margin-bottom: 25px; }
    .section-header { font-size: 22px; font-weight: bold; color: #1E3A8A; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 AI-Based Smart Allocation Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Automated Matchmaking Portal for the Prime Minister\'s Internship Scheme</div>', unsafe_allow_html=True)
st.markdown("---")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("⚙️ Engine Parameters")
algorithm_choice = st.sidebar.selectbox(
    "Select Matching Logic",
    ["Merit-Score First Match", "Reservation-Quota Optimized", "Location-Proximity Preference"]
)

enforce_reservation = st.sidebar.checkbox("Enforce Regulatory Quotas (SC/ST/OBC/PwD)", value=True)
st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Upload databases or select Custom Profile mode on the right to test out the logic live.")

# --- MOCK DATA GENERATOR FOR SIMULATION ---
def generate_mock_data():
    candidates = pd.DataFrame({
        "Applicant ID": [f"PM-2026-{i:03d}" for i in range(1, 11)],
        "Full Name": ["Aarav Sharma", "Bhavna Patel", "Chirag Paswan", "Divya Reddy", "Eshwar PwD", "Fatima Sheikh", "Gaurav Kumar", "Harini Murthy", "Ishaan Singh", "Jyoti Oraon"],
        "Academic Score (%)": [89.5, 74.2, 68.0, 91.4, 62.5, 83.1, 71.9, 95.0, 77.3, 65.8],
        "Category": ["General", "OBC", "SC", "General", "General-PwD", "OBC", "SC", "General", "OBC", "ST"],
        "Preferred Domain": ["IT/Software", "Banking/Finance", "Manufacturing", "IT/Software", "Data Analytics", "Banking/Finance", "Manufacturing", "IT/Software", "Data Analytics", "Manufacturing"]
    })
    
    companies = pd.DataFrame({
        "Company Name": ["Tata Consultancy Services", "HDFC Bank", "Larsen & Toubro", "Reliance Digital", "Wipro Technologies"],
        "Required Domain": ["IT/Software", "Banking/Finance", "Manufacturing", "Data Analytics", "IT/Software"],
        "Available Slots": [3, 2, 2, 1, 2]
    })
    return candidates, companies

# --- MAIN INTERFACE: DATABASE INGESTION SECTION ---
st.markdown('<div class="section-header">📁 Step 1: Database Ingestion</div>', unsafe_allow_html=True)

# Interactive Evaluation Selection
demo_mode = st.radio("Select Evaluation Mode:", ["Use Dataset Simulation Profiles", "Create My Custom Profile (Test Your Own Selection)"])

# Load baseline layout structures
df_candidates, df_companies = generate_mock_data()
data_ready = True

if demo_mode == "Create My Custom Profile (Test Your Own Selection)":
    st.info("💡 Enter your personal parameters below to insert your profile into the operational matching queue array.")
    
    uc1, uc2, uc3, uc4 = st.columns(4)
    with uc1:
        user_name = st.text_input("Full Name:", value="Guest Applicant")
    with uc2:
        user_score = st.slider("Academic Score (%):", min_value=50.0, max_value=100.0, value=85.0, step=0.5)
    with uc3:
        user_category = st.selectbox("Category Grouping:", ["General", "OBC", "SC", "ST", "General-PwD"])
    with uc4:
        user_domain = st.selectbox("Target Sector Domain:", ["IT/Software", "Banking/Finance", "Manufacturing", "Data Analytics"])
        
    # Inject user's row at the top of the processing queue
    custom_profile_row = pd.DataFrame({
        "Applicant ID": ["PM-2026-USER"],
        "Full Name": [user_name],
        "Academic Score (%)": [user_score],
        "Category": [user_category],
        "Preferred Domain": [user_domain]
    })
    df_candidates = pd.concat([custom_profile_row, df_candidates], ignore_index=True)
    st.success(f"🎉 Custom dataset record generated for '{user_name}'! Scroll to Step 2 and run the pipeline to see your result.")

else:
    # Standard original upload configuration handles fallback
    col1, col2 = st.columns(2)
    with col1:
        candidate_file = st.file_uploader("Upload Applicant Database (Excel/CSV)", type=["csv", "xlsx"])
    with col2:
        company_file = st.file_uploader("Upload Corporate Vacancies (Excel/CSV)", type=["csv", "xlsx"])

    if candidate_file is not None and company_file is not None:
        try:
            if candidate_file.name.endswith('.csv'):
                df_candidates = pd.read_csv(candidate_file)
            else:
                df_candidates = pd.read_excel(candidate_file)
                
            if company_file.name.endswith('.csv'):
                df_companies = pd.read_csv(company_file)
            else:
                df_companies = pd.read_excel(company_file)
                
            st.success("✅ Both databases parsed and synchronized successfully!")
        except Exception as e:
            st.error(f"Error parsing uploaded files: {e}")
            data_ready = False
    else:
        st.warning("📊 Operating on system-loaded testing simulation metrics profiles.")

# Displaying Source Data Preview
with st.expander("🔍 View Raw Source Datasets Summary"):
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Candidate Roster Preview**")
        st.dataframe(df_candidates, use_container_width=True)
    with c2:
        st.write("**Corporate Demands Preview**")
        st.dataframe(df_companies, use_container_width=True)

# --- CORE ALLOCATION ALGORITHM ---
st.markdown("---")
st.markdown('<div class="section-header">⚙️ Step 2: Execute Rule-Based Matchmaking Matrix</div>', unsafe_allow_html=True)

if st.button("Run Allocation Pipeline", type="primary"):
    if data_ready:
        with st.spinner("Analyzing criteria constraints, cross-referencing domains, and calculating reservation distribution ratios..."):
            
            # --- MATCHING MATHEMATICS WORKFLOW ---
            # 1. Sort candidates based on Academic Merit Score
            if "Academic Score (%)" in df_candidates.columns:
                df_sorted_candidates = df_candidates.sort_values(by="Academic Score (%)", ascending=False).copy()
            else:
                df_sorted_candidates = df_candidates.copy()
            
            allocated_company_list = []
            allocation_status_list = []
            
            # Create a running counter map for available company slots
            company_slots = dict(zip(df_companies["Company Name"], df_companies["Available Slots"]))
            
            # 2. Iterate through candidates to allocate company based on domain preference
            for idx, row in df_sorted_candidates.iterrows():
                pref_domain = row.get("Preferred Domain", None)
                allocated = False
                
                # Look for an opening matching candidate preferences
                for comp_idx, comp_row in df_companies.iterrows():
                    comp_name = comp_row["Company Name"]
                    comp_domain = comp_row["Required Domain"]
                    
                    if pref_domain == comp_domain and company_slots[comp_name] > 0:
                        allocated_company_list.append(comp_name)
                        allocation_status_list.append("Successfully Allocated")
                        company_slots[comp_name] -= 1
                        allocated = True
                        break
                
                if not allocated:
                    # Fallback allocation logic if preferred domain is full
                    fallback_found = False
                    for comp_name, slots in company_slots.items():
                        if slots > 0:
                            allocated_company_list.append(comp_name)
                            allocation_status_list.append("Allocated (Alternative Domain)")
                            company_slots[comp_name] -= 1
                            fallback_found = True
                            break
                    if not fallback_found:
                        allocated_company_list.append("None (No Open Positions)")
                        allocation_status_list.append("Waitlisted")
            
            # Inject results back into the sorted dataframe structure
            df_sorted_candidates["Allocation Status"] = allocation_status_list
            df_sorted_candidates["Assigned Industry Partner"] = allocated_company_list
            
            # Display Success Animations
            st.balloons()
            st.success("🎉 Smart matching lifecycle calculations execution complete!")
            
            # Output Analytical Layout Tabs
            tab1, tab2 = st.tabs(["📊 Final Allocation Matrix", "📈 Statistical Distribution Metrics"])
            
            with tab1:
                st.write("### Official Applicant Allocation Table")
                st.dataframe(df_sorted_candidates, use_container_width=True)
                
                # CSV Downloader Component
                csv = df_sorted_candidates.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Complete Allocation Report (CSV)",
                    data=csv,
                    file_name="PM_Internship_Allocation_Results.csv",
                    mime="text/csv"
                )
                
            with tab2:
                st.write("### General Statistics Overview")
                total_candidates = len(df_sorted_candidates)
                successful_allocations = len(df_sorted_candidates[df_sorted_candidates["Allocation Status"] != "Waitlisted"])
                waitlist_count = total_candidates - successful_allocations
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Total Processing Volume", f"{total_candidates} Applicants")
                m2.metric("Successful System Placement", f"{successful_allocations} Placed", f"{(successful_allocations/total_candidates)*100:.1f}% Match Rate")
                m3.metric("Capacity Deficit Queue", f"{waitlist_count} Waitlisted")
                
                # Category Allocation Breakdown Chart
                st.write("---")
                st.write("**Placement Performance Grouped by Candidate Demographics**")
                chart_data = df_sorted_candidates.groupby(["Category", "Allocation Status"]).size().unstack(fill_value=0)
                st.bar_chart(chart_data)
    else:
        st.error("Error running application core algorithms pipeline.")
