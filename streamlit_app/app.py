import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="HR Analytics System",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# HELPER FUNCTIONS & DATA LOADING
# --------------------------------------------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "data", "raw", "HR-Employee-Attrition.csv")
    if not os.path.exists(csv_path):
        csv_path = os.path.abspath("data/raw/HR-Employee-Attrition.csv")
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df['Attrition_Num'] = df['Attrition'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
        return df
    return None

df_raw = load_data()

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("HR Analytics System")
st.sidebar.caption("Data Analytics & Intelligence Hub")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "📊 Power BI Dashboard",
        "🔮 Attrition Prediction",
        "👤 Employee Profile",
        "ℹ️ About"
    ]
)

# --------------------------------------------------
# HOME
# --------------------------------------------------
if page == "Home":
    st.title("👥 HR Analytics System")
    st.subheader("Employee Attrition Intelligence & Reporting")

    st.write(
        """
        Welcome to the HR Analytics System. This application provides HR teams with data-driven insights,
        interactive Power BI analytics dashboards, and machine learning models for employee attrition evaluation.
        """
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info(
            """
            ### 📊 Power BI Dashboard
            Explore interactive visuals, departmental attrition, and embedded Power BI reports.
            """
        )

    with col2:
        st.info(
            """
            ### 🔮 Attrition Prediction
            Enter employee parameters to evaluate potential attrition risk scores.
            """
        )

    with col3:
        st.info(
            """
            ### 👤 Employee Profile
            Search and view individual workforce profiles and satisfaction metrics.
            """
        )

    with col4:
        st.info(
            """
            ### 📥 Download .PBIX
            Access and download native Power BI Desktop project files (`.pbix`).
            """
        )

    st.divider()

    st.subheader("System Capabilities")
    st.markdown(
        """
        1. **Power BI Visual Analytics**: Dynamic dashboards replicating key HR metrics (Department Attrition Rate, OverTime Impact, Income Distribution).
        2. **Embedded Power BI Service**: Seamless iframe integration for published Power BI cloud reports.
        3. **Predictive Attrition Risk**: Evaluates employee risk factors to enable proactive retention strategies.
        4. **Export & Download**: Access raw data and native Power BI `.pbix` project files directly.
        """
    )

# --------------------------------------------------
# POWER BI DASHBOARD
# --------------------------------------------------
elif page == "📊 Power BI Dashboard":
    st.title("📊 Power BI Analytics Dashboard")
    st.caption("Interactive Power BI visuals, live report embedding, and report downloads")

    tab1, tab2, tab3 = st.tabs([
        "📈 Interactive Dashboard (Power BI Replica)",
        "🌐 Embed Power BI Web Report",
        "📥 Download Power BI File (.PBIX)"
    ])

    # ----------------------------------------------
    # TAB 1: REPLICA INTERACTIVE DASHBOARD
    # ----------------------------------------------
    with tab1:
        if df_raw is not None:
            # Dynamic Filters Expander
            with st.expander("🔍 Filter Dashboard Data", expanded=True):
                f_col1, f_col2, f_col3 = st.columns(3)
                
                dept_options = ["All"] + list(df_raw['Department'].unique())
                with f_col1:
                    selected_dept = st.selectbox("Department", dept_options)
                
                gender_options = ["All"] + list(df_raw['Gender'].unique())
                with f_col2:
                    selected_gender = st.selectbox("Gender", gender_options)
                
                overtime_options = ["All"] + list(df_raw['OverTime'].unique())
                with f_col3:
                    selected_overtime = st.selectbox("OverTime", overtime_options)

            # Apply filters
            df_filtered = df_raw.copy()
            if selected_dept != "All":
                df_filtered = df_filtered[df_filtered['Department'] == selected_dept]
            if selected_gender != "All":
                df_filtered = df_filtered[df_filtered['Gender'] == selected_gender]
            if selected_overtime != "All":
                df_filtered = df_filtered[df_filtered['OverTime'] == selected_overtime]

            # KPI Summary Cards
            st.markdown("### 📌 Key Performance Indicators (KPIs)")
            kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
            
            total_emp = len(df_filtered)
            attr_count = df_filtered['Attrition_Num'].sum()
            attr_rate = (attr_count / total_emp * 100) if total_emp > 0 else 0
            avg_income = df_filtered['MonthlyIncome'].mean() if total_emp > 0 else 0
            avg_tenure = df_filtered['YearsAtCompany'].mean() if total_emp > 0 else 0

            kpi1.metric("Total Employees", f"{total_emp:,}")
            kpi2.metric("Total Attrition", f"{attr_count:,}", delta=f"{attr_rate:.1f}% Rate", delta_color="inverse")
            kpi3.metric("Attrition Rate", f"{attr_rate:.1f}%")
            kpi4.metric("Avg Monthly Income", f"${avg_income:,.0f}")
            kpi5.metric("Avg Tenure", f"{avg_tenure:.1f} Yrs")

            st.divider()

            # Chart Row 1
            st.markdown("### 🏢 Department & Work Dynamics")
            c1, c2 = st.columns(2)

            with c1:
                dept_summary = df_filtered.groupby('Department').agg(
                    Total=('EmployeeNumber', 'count'),
                    Attrition=('Attrition_Num', 'sum')
                ).reset_index()
                dept_summary['Rate'] = (dept_summary['Attrition'] / dept_summary['Total'] * 100).round(1)

                fig_dept = px.bar(
                    dept_summary,
                    x='Department',
                    y='Rate',
                    text='Rate',
                    title="<b>Attrition Rate (%) by Department</b>",
                    labels={'Rate': 'Attrition Rate (%)'},
                    color='Department',
                    color_discrete_sequence=px.colors.qualitative.Set2
                )
                fig_dept.update_traces(texttemplate='%{text}%', textposition='outside')
                max_rate = dept_summary['Rate'].max() if len(dept_summary) > 0 and not pd.isna(dept_summary['Rate'].max()) else 25
                fig_dept.update_layout(showlegend=False, height=380, yaxis_range=[0, max(max_rate + 5, 25)])
                st.plotly_chart(fig_dept, use_container_width=True)

            with c2:
                ot_summary = df_filtered.groupby(['OverTime', 'Attrition']).size().reset_index(name='Count')
                fig_ot = px.bar(
                    ot_summary,
                    x='OverTime',
                    y='Count',
                    color='Attrition',
                    barmode='group',
                    title="<b>Attrition Count by OverTime Status</b>",
                    color_discrete_map={'Yes': '#EF553B', 'No': '#636EFA'}
                )
                fig_ot.update_layout(height=380)
                st.plotly_chart(fig_ot, use_container_width=True)

            # Chart Row 2
            st.markdown("### 💰 Compensation & Satisfaction Analysis")
            c3, c4 = st.columns(2)

            with c3:
                fig_income = px.box(
                    df_filtered,
                    x='JobRole',
                    y='MonthlyIncome',
                    color='Attrition',
                    title="<b>Monthly Income Distribution across Job Roles</b>",
                    color_discrete_map={'Yes': '#EF553B', 'No': '#00CC96'}
                )
                fig_income.update_layout(height=420, xaxis_tickangle=-45)
                st.plotly_chart(fig_income, use_container_width=True)

            with c4:
                sat_summary = df_filtered.groupby(['JobSatisfaction', 'WorkLifeBalance', 'Attrition']).size().reset_index(name='EmployeeCount')
                fig_sat = px.scatter(
                    sat_summary,
                    x='JobSatisfaction',
                    y='WorkLifeBalance',
                    size='EmployeeCount',
                    color='Attrition',
                    title="<b>Job Satisfaction vs. Work-Life Balance Matrix</b>",
                    labels={'JobSatisfaction': 'Job Satisfaction (1-4)', 'WorkLifeBalance': 'Work-Life Balance (1-4)'},
                    color_discrete_map={'Yes': '#EF553B', 'No': '#636EFA'},
                    size_max=40
                )
                fig_sat.update_layout(height=420)
                st.plotly_chart(fig_sat, use_container_width=True)

            # Table View
            with st.expander("📋 View Filtered Employee Dataset"):
                st.dataframe(
                    df_filtered[['EmployeeNumber', 'Age', 'Department', 'JobRole', 'MonthlyIncome', 'OverTime', 'JobSatisfaction', 'Attrition']],
                    use_container_width=True
                )
        else:
            st.error("Could not load data file `data/raw/HR-Employee-Attrition.csv`. Please check file path.")

    # ----------------------------------------------
    # TAB 2: POWER BI EMBED
    # ----------------------------------------------
    with tab2:
        st.subheader("🌐 Embed Published Power BI Web Report")
        st.write(
            "Paste your Power BI **Publish to Web** iframe URL or report link below to view your cloud-hosted Power BI dashboard live inside Streamlit."
        )

        default_embed_url = st.text_input(
            "Power BI Report Embed URL / Publish Link:",
            placeholder="https://app.powerbi.com/view?r=eyJrIjoi...",
            help="Enter a published Power BI Web URL or iframe src attribute."
        )

        iframe_height = st.slider("Embed Viewer Height (px)", min_value=400, max_value=1000, value=650, step=50)

        if default_embed_url:
            if "<iframe" in default_embed_url:
                import re
                match = re.search(r'src=["\']([^"\']+)["\']', default_embed_url)
                if match:
                    default_embed_url = match.group(1)

            st.info(f"Rendering Power BI Report from: `{default_embed_url}`")
            components.html(
                f'<iframe title="PowerBI Report" width="100%" height="{iframe_height}px" src="{default_embed_url}" frameborder="0" allowFullScreen="true"></iframe>',
                height=iframe_height + 20
            )
        else:
            st.warning("No Power BI Embed URL entered yet. Displaying preview frame below:")
            components.html(
                f'''
                <div style="border: 2px dashed #4A5568; border-radius: 8px; padding: 40px; text-align: center; background-color: #1A202C; color: #CBD5E0; font-family: sans-serif; height: {iframe_height-80}px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    <h2 style="color: #F6AD55; margin-bottom: 10px;">📊 Power BI Live Embed Container</h2>
                    <p style="max-width: 600px; font-size: 16px;">
                        Paste your Power BI Published Web Report link in the input box above to load your interactive report directly within this page.
                    </p>
                </div>
                ''',
                height=iframe_height
            )

        with st.expander("📖 Step-by-Step Guide: How to Get a Power BI Embed Link"):
            st.markdown(
                """
                1. Open **Power BI Desktop** and open your `HR_Analytics_Dashboard.pbix` file.
                2. Click **Publish** to publish the report to your **Power BI Service** workspace.
                3. Open the report in [Power BI Service (app.powerbi.com)](https://app.powerbi.com).
                4. Go to **File** ➡️ **Embed report** ➡️ **Publish to Web (public)**.
                5. Copy the generated **link** or **iframe src URL** and paste it into the input box above!
                """
            )

    # ----------------------------------------------
    # TAB 3: DOWNLOAD PBIX FILE
    # ----------------------------------------------
    with tab3:
        st.subheader("📥 Power BI Desktop File (.PBIX)")
        st.write(
            "You can download the original Power BI Desktop project file to inspect the data model, DAX measures, and custom visuals directly."
        )

        base_dir = os.path.dirname(os.path.abspath(__file__))
        pbix_path = os.path.join(base_dir, "..", "dashboard", "HR_Analytics_Dashboard.pbix")
        if not os.path.exists(pbix_path):
            pbix_path = os.path.abspath("dashboard/HR_Analytics_Dashboard.pbix")

        if os.path.exists(pbix_path):
            file_size_mb = os.path.getsize(pbix_path) / (1024 * 1024)
            
            col_info, col_btn = st.columns([2, 1])
            with col_info:
                st.success(f"✅ **HR_Analytics_Dashboard.pbix** is available for download.")
                st.write(f"- **File Path**: `dashboard/HR_Analytics_Dashboard.pbix`")
                st.write(f"- **File Size**: `{file_size_mb:.2f} MB`")
                st.write(f"- **Required Software**: Microsoft Power BI Desktop")

            with col_btn:
                with open(pbix_path, "rb") as f:
                    pbix_bytes = f.read()
                
                st.download_button(
                    label="⬇️ Download HR_Analytics_Dashboard.pbix",
                    data=pbix_bytes,
                    file_name="HR_Analytics_Dashboard.pbix",
                    mime="application/octet-stream",
                    use_container_width=True
                )
        else:
            st.error(f"PBIX file not found at `{pbix_path}`.")

# --------------------------------------------------
# ATTRITION PREDICTION
# --------------------------------------------------
elif page == "🔮 Attrition Prediction":
    st.title("🔮 Employee Attrition Prediction")
    st.write("Enter the employee's information below to evaluate potential attrition risk factors.")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=70, value=30)
        department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
        job_role = st.selectbox("Job Role", [
            "Sales Executive", "Research Scientist", "Laboratory Technician",
            "Manufacturing Director", "Healthcare Representative", "Manager",
            "Sales Representative", "Research Director", "Human Resources"
        ])
        monthly_income = st.number_input("Monthly Income ($)", min_value=1000, max_value=100000, value=5000)
        job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])

    with col2:
        overtime = st.selectbox("Overtime", ["Yes", "No"])
        job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
        work_life_balance = st.selectbox("Work-Life Balance", [1, 2, 3, 4])
        years_at_company = st.number_input("Years at Company", min_value=0, max_value=50, value=3)
        business_travel = st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])

    st.divider()
    if st.button("🔮 Predict Attrition Risk", use_container_width=True):
        st.warning("Machine-learning prediction backend interface ready for model connection.")

# --------------------------------------------------
# EMPLOYEE PROFILE
# --------------------------------------------------
elif page == "👤 Employee Profile":
    st.title("👤 Employee Profile")
    st.write("Search for and view individual employee information.")
    st.divider()

    employee_id = st.text_input("Enter Employee ID")
    if st.button("Search Employee"):
        if employee_id:
            st.info(f"Displaying profile details for Employee ID **{employee_id}**.")
        else:
            st.warning("Please enter an Employee ID.")

# --------------------------------------------------
# ABOUT
# --------------------------------------------------
elif page == "ℹ️ About":
    st.title("ℹ️ About the System")
    st.write(
        """
        ### HR Analytics System
        The HR Analytics System is designed to support employee attrition analysis, workforce metrics tracking,
        and HR decision-making through interactive Streamlit dashboards and Power BI reports.
        """
    )
    st.divider()
    st.subheader("Technology Stack")
    st.write(
        """
        - Python & Streamlit
        - Plotly & Pandas
        - Power BI (.PBIX & Embedded Service)
        - MySQL & SQLite
        """
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption("HR Analytics System | SGP Data Analytics Project")