import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from python.predict import predict_attrition

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# --------------------------------------------------
# CLEAN PROFESSIONAL CSS
# --------------------------------------------------
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Global Reset & Typography */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Background */
.stApp {
    background-color: #F7F8FA;
    color: #1F2937;
}

/* Keep sidebar always visible - hide collapse button */
button[kind="header"] {
    display: none !important;
}

[data-testid="collapsedControl"] {
    display: none !important;
}

section[data-testid="stSidebarNav"] button {
    display: none !important;
}

/* Force sidebar to stay visible */
section[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    width: 21rem !important;
    min-width: 21rem !important;
    max-width: 21rem !important;
    transform: none !important;
    transition: none !important;
}

section[data-testid="stSidebar"] > div {
    width: 21rem !important;
    transform: none !important;
}

/* Adjust main content to account for sidebar */
.main .block-container {
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Simple Header */
.page-header {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 24px 28px;
    margin-bottom: 24px;
}
.page-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #1F2937;
    margin-bottom: 6px;
}
.page-subtitle {
    font-size: 0.95rem;
    color: #6B7280;
    line-height: 1.5;
}

/* Card Components */
.hr-card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 20px 24px;
    margin-bottom: 16px;
}

.module-card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 24px;
    height: 100%;
}

/* KPI Cards */
.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 18px 20px;
}

.kpi-label {
    font-size: 0.8rem;
    font-weight: 500;
    color: #6B7280;
    margin-bottom: 6px;
}
.kpi-value {
    font-size: 1.75rem;
    font-weight: 700;
    color: #1F2937;
    line-height: 1.1;
}
.kpi-sub {
    font-size: 0.8rem;
    font-weight: 400;
    color: #9CA3AF;
    margin-top: 4px;
}

/* Badges */
.badge {
    display: inline-flex;
    align-items: center;
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 500;
}
.badge-low { background: #D1FAE5; color: #065F46; }
.badge-moderate { background: #FEF3C7; color: #92400E; }
.badge-high { background: #FEE2E2; color: #991B1B; }
.badge-yes { background: #FEE2E2; color: #991B1B; }
.badge-no { background: #D1FAE5; color: #065F46; }

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E5E7EB;
}

section[data-testid="stSidebar"] * {
    color: #1F2937 !important;
}

.sidebar-brand {
    padding: 16px 8px 20px 8px;
    border-bottom: 1px solid #E5E7EB;
    margin-bottom: 20px;
}
.sidebar-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #1F2937;
    margin-bottom: 2px;
}
.sidebar-subtitle {
    font-size: 0.85rem;
    color: #6B7280;
    font-weight: 400;
}

/* Radio button styling */
section[data-testid="stSidebar"] .stRadio > div {
    gap: 4px;
}

section[data-testid="stSidebar"] .stRadio label {
    background-color: transparent;
    padding: 8px 12px;
    border-radius: 6px;
    cursor: pointer;
    display: flex !important;
    align-items: center;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background-color: #F9FAFB;
}

section[data-testid="stSidebar"] .stRadio label span {
    color: #1F2937 !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
}

section[data-testid="stSidebar"] .stRadio input:checked + label {
    background-color: #EFF6FF;
}

section[data-testid="stSidebar"] .stRadio input:checked + label span {
    color: #2563EB !important;
    font-weight: 600 !important;
}

/* Tabs Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background-color: #F9FAFB;
    padding: 4px;
    border-radius: 8px;
    border: 1px solid #E5E7EB;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 0.9rem;
    font-weight: 500;
    color: #6B7280;
    border: none !important;
}

.stTabs [aria-selected="true"] {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* Buttons */
.stButton > button {
    background: #2563EB;
    color: #FFFFFF;
    border: none;
    border-radius: 6px;
    padding: 10px 24px;
    font-weight: 500;
}
.stButton > button:hover {
    background: #1D4ED8;
}

/* Form labels - ensure they're visible */
.stNumberInput > label,
.stSelectbox > label,
.stSlider > label {
    color: #374151 !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    margin-bottom: 8px !important;
    display: block !important;
}

/* Input fields styling */
input[type="number"],
div[data-baseweb="select"],
div[data-baseweb="slider"] {
    border: 1px solid #D1D5DB !important;
    border-radius: 6px !important;
}

/* Sidebar toggle button styling */
button[kind="header"] {
    background-color: #2563EB !important;
    color: white !important;
    border-radius: 6px !important;
    padding: 8px 12px !important;
    border: none !important;
}

button[kind="header"]:hover {
    background-color: #1D4ED8 !important;
}

/* Ensure toggle button is always visible */
[data-testid="collapsedControl"] {
    display: block !important;
    position: fixed !important;
    top: 0.5rem !important;
    left: 0.5rem !important;
    z-index: 999999 !important;
    background-color: #2563EB !important;
    color: white !important;
    border-radius: 6px !important;
    padding: 12px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    cursor: pointer !important;
}

[data-testid="collapsedControl"]:hover {
    background-color: #1D4ED8 !important;
}

[data-testid="collapsedControl"] svg {
    color: white !important;
    fill: white !important;
}

/* Make sure sidebar toggle in header is visible */
.css-1cypcdb, [data-testid="stSidebarCollapse"] {
    display: block !important;
}

/* Hide default clutter */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --------------------------------------------------
# PLOTLY THEME HELPERS
# --------------------------------------------------
def apply_plotly_theme(fig, height=380):
    fig.update_layout(
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font=dict(family='Inter, sans-serif', color='#6B7280', size=12),
        margin=dict(l=20, r=20, t=40, b=20),
        height=height,
        xaxis=dict(
            showgrid=True,
            gridcolor='#F3F4F6',
            zeroline=False,
            tickfont=dict(color='#6B7280')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='#F3F4F6',
            zeroline=False,
            tickfont=dict(color='#6B7280')
        ),
        legend=dict(
            font=dict(color='#1F2937', size=11),
            bgcolor='#FFFFFF',
            bordercolor='#E5E7EB',
            borderwidth=1
        )
    )
    return fig

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
with st.sidebar:
    st.markdown("""
        <div class="sidebar-brand">
            <div class="sidebar-title">HR Analytics</div>
            <div class="sidebar-subtitle">Workforce & Attrition Analysis</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Navigation**")

    page = st.radio(
        "",
        [
            "Overview",
            "Analytics",
            "Risk Prediction",
            "Employee Directory",
            "About"
        ],
        label_visibility="collapsed"
    )

# --------------------------------------------------
# 1. OVERVIEW (HOME)
# --------------------------------------------------
if page == "Overview":
    st.markdown("""
        <div class="page-header">
            <div class="page-title">HR Analytics Dashboard</div>
            <div class="page-subtitle">
                Overview of employee workforce, attrition, salary and tenure metrics.
            </div>
        </div>
    """, unsafe_allow_html=True)

    if df_raw is not None:
        total_emp = len(df_raw)
        attr_count = df_raw['Attrition_Num'].sum()
        attr_rate = (attr_count / total_emp * 100) if total_emp > 0 else 0
        avg_income = df_raw['MonthlyIncome'].mean()
        avg_tenure = df_raw['YearsAtCompany'].mean()

        m1, m2, m3, m4, m5 = st.columns(5)
        with m1:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">Total employees</div>
                    <div class="kpi-value">{total_emp:,}</div>
                </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">Employees left</div>
                    <div class="kpi-value">{attr_count:,}</div>
                </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">Attrition rate</div>
                    <div class="kpi-value">{attr_rate:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">Average monthly income</div>
                    <div class="kpi-value">${avg_income:,.0f}</div>
                </div>
            """, unsafe_allow_html=True)
        with m5:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">Average tenure</div>
                    <div class="kpi-value">{avg_tenure:.1f} yrs</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="module-card">
                <h4 style="color: #1F2937; font-weight: 600; margin-bottom: 8px;">Power BI Dashboard</h4>
                <p style="color: #6B7280; font-size: 0.9rem; line-height: 1.5;">
                    Explore workforce and attrition trends.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="module-card">
                <h4 style="color: #1F2937; font-weight: 600; margin-bottom: 8px;">Attrition Risk Prediction</h4>
                <p style="color: #6B7280; font-size: 0.9rem; line-height: 1.5;">
                    Estimate attrition risk using the trained ML model.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="module-card">
                <h4 style="color: #1F2937; font-weight: 600; margin-bottom: 8px;">Employee Directory</h4>
                <p style="color: #6B7280; font-size: 0.9rem; line-height: 1.5;">
                    Search and review employee-level information.
                </p>
            </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# 2. ANALYTICS
# --------------------------------------------------
elif page == "Analytics":
    st.markdown("""
        <div class="page-header">
            <div class="page-title">Analytics</div>
            <div class="page-subtitle">Interactive data exploration and Power BI report integration</div>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "Interactive Dashboard",
        "Power BI Web Report",
        "Download Report (.PBIX)"
    ])

    # ----------------------------------------------
    # TAB 1: INTERACTIVE DASHBOARD
    # ----------------------------------------------
    with tab1:
        if df_raw is not None:
            # Filters
            f_col1, f_col2, f_col3 = st.columns(3)
            
            dept_options = ["All Departments"] + list(df_raw['Department'].unique())
            with f_col1:
                selected_dept = st.selectbox("Department", dept_options)
            
            gender_options = ["All Genders"] + list(df_raw['Gender'].unique())
            with f_col2:
                selected_gender = st.selectbox("Gender", gender_options)
            
            overtime_options = ["All OverTime Status"] + list(df_raw['OverTime'].unique())
            with f_col3:
                selected_overtime = st.selectbox("OverTime", overtime_options)

            # Filter logic
            df_filtered = df_raw.copy()
            if selected_dept != "All Departments":
                df_filtered = df_filtered[df_filtered['Department'] == selected_dept]
            if selected_gender != "All Genders":
                df_filtered = df_filtered[df_filtered['Gender'] == selected_gender]
            if selected_overtime != "All OverTime Status":
                df_filtered = df_filtered[df_filtered['OverTime'] == selected_overtime]

            st.markdown("<br>", unsafe_allow_html=True)

            # KPI Bar
            total_emp = len(df_filtered)
            attr_count = df_filtered['Attrition_Num'].sum()
            attr_rate = (attr_count / total_emp * 100) if total_emp > 0 else 0
            avg_income = df_filtered['MonthlyIncome'].mean() if total_emp > 0 else 0
            avg_tenure = df_filtered['YearsAtCompany'].mean() if total_emp > 0 else 0

            k1, k2, k3, k4, k5 = st.columns(5)
            with k1:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Filtered count</div>
                        <div class="kpi-value">{total_emp:,}</div>
                    </div>
                """, unsafe_allow_html=True)
            with k2:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Attrition count</div>
                        <div class="kpi-value">{attr_count:,}</div>
                    </div>
                """, unsafe_allow_html=True)
            with k3:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Attrition rate</div>
                        <div class="kpi-value">{attr_rate:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)
            with k4:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Avg monthly income</div>
                        <div class="kpi-value">${avg_income:,.0f}</div>
                    </div>
                """, unsafe_allow_html=True)
            with k5:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Avg tenure</div>
                        <div class="kpi-value">{avg_tenure:.1f} yrs</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Chart Row 1
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
                    title="Attrition rate by department",
                    color='Department',
                    color_discrete_sequence=['#2563EB', '#DC2626', '#16A34A']
                )
                fig_dept.update_traces(texttemplate='%{text}%', textposition='outside')
                fig_dept = apply_plotly_theme(fig_dept)
                st.plotly_chart(fig_dept, use_container_width=True)

            with c2:
                ot_summary = df_filtered.groupby(['OverTime', 'Attrition']).size().reset_index(name='Count')
                fig_ot = px.bar(
                    ot_summary,
                    x='OverTime',
                    y='Count',
                    color='Attrition',
                    barmode='group',
                    title="Overtime and attrition",
                    color_discrete_map={'Yes': '#DC2626', 'No': '#2563EB'}
                )
                fig_ot = apply_plotly_theme(fig_ot)
                st.plotly_chart(fig_ot, use_container_width=True)

            # Chart Row 2
            c3, c4 = st.columns(2)

            with c3:
                fig_income = px.box(
                    df_filtered,
                    x='JobRole',
                    y='MonthlyIncome',
                    color='Attrition',
                    title="Monthly income by job role",
                    color_discrete_map={'Yes': '#DC2626', 'No': '#16A34A'}
                )
                fig_income = apply_plotly_theme(fig_income, height=420)
                fig_income.update_layout(xaxis_tickangle=-35)
                st.plotly_chart(fig_income, use_container_width=True)

            with c4:
                sat_summary = df_filtered.groupby(['JobSatisfaction', 'WorkLifeBalance', 'Attrition']).size().reset_index(name='EmployeeCount')
                fig_sat = px.scatter(
                    sat_summary,
                    x='JobSatisfaction',
                    y='WorkLifeBalance',
                    size='EmployeeCount',
                    color='Attrition',
                    title="Job satisfaction and work-life balance",
                    labels={'JobSatisfaction': 'Job Satisfaction (1-4)', 'WorkLifeBalance': 'Work-Life Balance (1-4)'},
                    color_discrete_map={'Yes': '#DC2626', 'No': '#2563EB'},
                    size_max=36
                )
                fig_sat = apply_plotly_theme(fig_sat, height=420)
                st.plotly_chart(fig_sat, use_container_width=True)

            # Table View
            with st.expander("View filtered dataset"):
                st.dataframe(
                    df_filtered[['EmployeeNumber', 'Age', 'Department', 'JobRole', 'MonthlyIncome', 'OverTime', 'JobSatisfaction', 'Attrition']],
                    use_container_width=True
                )
        else:
            st.error("Could not locate data/raw/HR-Employee-Attrition.csv")

    # ----------------------------------------------
    # TAB 2: POWER BI WEB REPORT
    # ----------------------------------------------
    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        col_embed, col_guide = st.columns([2, 1])

        with col_embed:
            st.markdown("#### Power BI Web Report")
            st.markdown("Paste your Power BI publish to web URL or iframe code below.")

            default_embed_url = st.text_input(
                "Power BI Public URL:",
                placeholder="https://app.powerbi.com/view?r=eyJrIjoi...",
                label_visibility="collapsed"
            )

            iframe_height = st.slider("Report height (px)", min_value=400, max_value=900, value=600, step=50)

            if default_embed_url:
                if "<iframe" in default_embed_url:
                    import re
                    match = re.search(r'src=["\']([^"\']+)["\']', default_embed_url)
                    if match:
                        default_embed_url = match.group(1)

                components.html(
                    f'<iframe title="PowerBI Report" width="100%" height="{iframe_height}px" src="{default_embed_url}" frameborder="0" allowFullScreen="true"></iframe>',
                    height=iframe_height + 10
                )
            else:
                components.html(
                    f'''
                    <div style="border: 2px dashed #E5E7EB; border-radius: 8px; padding: 40px; text-align: center; background-color: #FFFFFF; color: #6B7280; font-family: 'Inter', sans-serif; height: {iframe_height-60}px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                        <div style="font-size: 2.5rem; margin-bottom: 12px;">📊</div>
                        <h3 style="color: #1F2937; margin-bottom: 8px; font-weight: 600;">Power BI Report Viewer</h3>
                        <p style="max-width: 500px; font-size: 14px; line-height: 1.5; color: #6B7280;">
                            Paste your published Power BI web report URL in the field above to display your live report.
                        </p>
                    </div>
                    ''',
                    height=iframe_height
                )

        with col_guide:
            st.markdown("#### How to publish the report")
            st.markdown("""
                1. Open HR_Analytics_Dashboard.pbix in Power BI Desktop
                2. Click Publish to upload to your Power BI workspace
                3. Open the report in Power BI Cloud (app.powerbi.com)
                4. Navigate to File → Embed report → Publish to web
                5. Copy the generated web link and paste it in the field
            """, unsafe_allow_html=True)

    # ----------------------------------------------
    # TAB 3: DOWNLOAD REPORT
    # ----------------------------------------------
    with tab3:
        st.markdown("<br>", unsafe_allow_html=True)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pbix_path = os.path.join(base_dir, "..", "dashboard", "HR_Analytics_Dashboard.pbix")
        if not os.path.exists(pbix_path):
            pbix_path = os.path.abspath("dashboard/HR_Analytics_Dashboard.pbix")

        if os.path.exists(pbix_path):
            file_size_mb = os.path.getsize(pbix_path) / (1024 * 1024)
            
            c_info, c_btn = st.columns([2, 1])
            with c_info:
                st.markdown("#### HR_Analytics_Dashboard.pbix")
                st.markdown(f"""
                    Contains DAX measures, data relationships, and custom visualizations.
                    
                    **File size:** {file_size_mb:.2f} MB
                """)

            with c_btn:
                with open(pbix_path, "rb") as f:
                    pbix_bytes = f.read()
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.download_button(
                    label="Download .PBIX File",
                    data=pbix_bytes,
                    file_name="HR_Analytics_Dashboard.pbix",
                    mime="application/octet-stream",
                    use_container_width=True
                )
        else:
            st.error("PBIX file not found.")

# --------------------------------------------------
# 3. RISK PREDICTION
# --------------------------------------------------
elif page == "Risk Prediction":
    st.markdown("""
        <div class="page-header">
            <div class="page-title">Employee Attrition Risk</div>
            <div class="page-subtitle">Enter employee details to estimate attrition risk using the trained model.</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Demographics & Role")
        age = st.number_input("Age", min_value=18, max_value=70, value=32, key="age_input")
        department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"], key="dept_input")
        job_role = st.selectbox("Job Role", [
            "Sales Executive", "Research Scientist", "Laboratory Technician",
            "Manufacturing Director", "Healthcare Representative", "Manager",
            "Sales Representative", "Research Director", "Human Resources"
        ], key="role_input")
        monthly_income = st.number_input("Monthly income ($)", min_value=1000, max_value=100000, value=5500, step=500, key="income_input")
        job_level = st.selectbox("Job level", [1, 2, 3, 4, 5], index=1, key="level_input")

    with col2:
        st.markdown("#### Work Environment")
        overtime = st.selectbox("OverTime", ["Yes", "No"], index=1, key="overtime_input")
        job_satisfaction = st.select_slider("Job satisfaction", options=[1, 2, 3, 4], value=3, help="1: Low → 4: High", key="satisfaction_input")
        work_life_balance = st.select_slider("Work-life balance", options=[1, 2, 3, 4], value=3, help="1: Low → 4: High", key="balance_input")
        years_at_company = st.number_input("Years at company", min_value=0, max_value=50, value=4, key="years_input")
        business_travel = st.selectbox("Business travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"], key="travel_input")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Calculate Risk", use_container_width=True):
        employee_data = {
            "Age": age,
            "Department": department,
            "JobRole": job_role,
            "MonthlyIncome": monthly_income,
            "JobLevel": job_level,
            "OverTime": overtime,
            "JobSatisfaction": job_satisfaction,
            "WorkLifeBalance": work_life_balance,
            "YearsAtCompany": years_at_company,
            "BusinessTravel": business_travel
        }
        prediction, probability = predict_attrition(employee_data)
        risk_pct = probability * 100

        st.markdown("<br>", unsafe_allow_html=True)

        if probability >= 0.50:
            badge_class = "badge-high"
            status_text = "High risk"
        elif probability >= 0.30:
            badge_class = "badge-moderate"
            status_text = "Moderate risk"
        else:
            badge_class = "badge-low" 
            status_text = "Low risk"

        st.markdown(f"""
            <div style="background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 8px; padding: 28px; text-align: center;">
                <div style="font-size: 0.85rem; color: #6B7280; margin-bottom: 8px;">Estimated attrition risk</div>
                <div style="font-size: 3rem; font-weight: 700; color: #1F2937; line-height: 1;">{risk_pct:.1f}%</div>
                <div class="{badge_class}" style="margin-top: 12px;">Status: {status_text}</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(
            "<div style='font-size: 0.85rem; color: #6B7280; text-align: center; margin-top: 12px;'>"
            "This is a model estimate based on the employee attributes provided.</div>",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Suggested HR follow-up")
        
        recs = []
        if overtime == "Yes":
            recs.append("**Overtime pressure**: Employee works recurring overtime. Consider reviewing task distribution or offering flexible arrangements.")
        if job_satisfaction <= 2:
            recs.append("**Low job satisfaction**: Conduct a 1-on-1 check-in to identify role friction points or growth aspirations.")
        if work_life_balance <= 2:
            recs.append("**Work-life imbalance**: Risk of burnout. Evaluate hybrid work flexibility or project workload reallocation.")
        if monthly_income < 3500:
            recs.append("**Compensation review**: Current monthly salary is below market average for this role level. Consider benchmark review.")

        if not recs:
            recs.append("**Positive indicators**: Employee parameters indicate stable satisfaction and balanced workload. Maintain regular check-ins.")

        for r in recs:
            st.markdown(f"- {r}")

# --------------------------------------------------
# 4. EMPLOYEE DIRECTORY
# --------------------------------------------------
elif page == "Employee Directory":
    st.markdown("""
        <div class="page-header">
            <div class="page-title">Employee Directory</div>
            <div class="page-subtitle">Search for an employee using their Employee ID.</div>
        </div>
    """, unsafe_allow_html=True)

    if df_raw is not None:
        search_col, btn_col = st.columns([3, 1])
        with search_col:
            employee_id = st.text_input("Employee ID", placeholder="e.g. 42", label_visibility="collapsed")
        with btn_col:
            search_clicked = st.button("Search", use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if search_clicked:
            if not employee_id.strip():
                st.warning("Please enter an Employee ID.")
            else:
                employee_match = df_raw[
                    df_raw["EmployeeNumber"].astype(str) == employee_id.strip()
                ]

                if employee_match.empty:
                    st.error("Employee not found.")
                else:
                    emp_row = employee_match.iloc[0]

                    # Calculate live risk for the matched employee
                    emp_dict = {
                        "Age": emp_row['Age'],
                        "Department": emp_row['Department'],
                        "JobRole": emp_row['JobRole'],
                        "MonthlyIncome": emp_row['MonthlyIncome'],
                        "JobLevel": emp_row['JobLevel'],
                        "OverTime": emp_row['OverTime'],
                        "JobSatisfaction": emp_row['JobSatisfaction'],
                        "WorkLifeBalance": emp_row['WorkLifeBalance'],
                        "YearsAtCompany": emp_row['YearsAtCompany'],
                        "BusinessTravel": emp_row['BusinessTravel']
                    }
                    pred, prob = predict_attrition(emp_dict)
                    risk_score = prob * 100
                    if prob >= 0.50:
                        badge_type = "badge-high"
                        risk_label = "High risk"
                    elif prob >= 0.30:
                        badge_type = "badge-moderate"
                        risk_label = "Moderate risk"
                    else:
                        badge_type = "badge-low"
                        risk_label = "Low risk"

                    # Employee header
                    st.markdown(f"""
                        <div class="hr-card">
                            <h3 style="color: #1F2937; font-weight: 600; margin-bottom: 4px;">Employee #{emp_row['EmployeeNumber']}</h3>
                            <div style="color: #6B7280; font-size: 0.95rem;">{emp_row['JobRole']} | {emp_row['Department']}</div>
                        </div>
                    """, unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)

                    # Risk section
                    st.markdown("#### Model-estimated attrition risk")
                    st.markdown(f"""
                        <div class="hr-card" style="text-align: center; padding: 20px;">
                            <div style="font-size: 2rem; font-weight: 700; color: #1F2937; margin-bottom: 8px;">{risk_score:.1f}%</div>
                            <div class="{badge_type}">{risk_label}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(
                        "<div style='font-size: 0.8rem; color: #6B7280; margin-top: 8px; margin-bottom: 20px;'>"
                        "Risk estimate generated by the trained attrition model.</div>",
                        unsafe_allow_html=True
                    )

                    # Employee details
                    st.markdown("#### Employee details")
                    i1, i2, i3 = st.columns(3)
                    with i1:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Age</div>
                                <div class="kpi-value">{emp_row['Age']} yrs</div>
                            </div>
                        """, unsafe_allow_html=True)
                    with i2:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Department</div>
                                <div class="kpi-value" style="font-size: 1.15rem;">{emp_row['Department']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                    with i3:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Job role</div>
                                <div class="kpi-value" style="font-size: 1.15rem;">{emp_row['JobRole']}</div>
                            </div>
                        """, unsafe_allow_html=True)

                    st.markdown("#### Compensation & tenure")
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Monthly income</div>
                                <div class="kpi-value">${emp_row['MonthlyIncome']:,}</div>
                            </div>
                        """, unsafe_allow_html=True)
                    with c2:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Job level</div>
                                <div class="kpi-value">{emp_row['JobLevel']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                    with c3:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Years at company</div>
                                <div class="kpi-value">{emp_row['YearsAtCompany']}</div>
                            </div>
                        """, unsafe_allow_html=True)

                    st.markdown("#### Work environment")
                    e1, e2, e3, e4 = st.columns(4)
                    with e1:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Job satisfaction</div>
                                <div class="kpi-value">{emp_row['JobSatisfaction']} / 4</div>
                            </div>
                        """, unsafe_allow_html=True)
                    with e2:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Work-life balance</div>
                                <div class="kpi-value">{emp_row['WorkLifeBalance']} / 4</div>
                            </div>
                        """, unsafe_allow_html=True)
                    with e3:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Overtime</div>
                                <div class="kpi-value" style="font-size: 1.2rem;">{emp_row['OverTime']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                    with e4:
                        st.markdown(f"""
                            <div class="kpi-card">
                                <div class="kpi-label">Business travel</div>
                                <div class="kpi-value" style="font-size: 1rem;">{emp_row['BusinessTravel']}</div>
                            </div>
                        """, unsafe_allow_html=True)

                    st.markdown("#### Attrition status")
                    attr_badge = "badge-yes" if str(emp_row['Attrition']).strip().lower() == "yes" else "badge-no"
                    attr_text = "Yes" if str(emp_row['Attrition']).strip().lower() == "yes" else "No"
                    st.markdown(f"""
                        <div class="hr-card">
                            <span class="{attr_badge}">Attrition: {attr_text}</span>
                        </div>
                    """, unsafe_allow_html=True)

# --------------------------------------------------
# 5. ABOUT
# --------------------------------------------------
elif page == "About":
    st.markdown("""
        <div class="page-header">
            <div class="page-title">About the Project</div>
            <div class="page-subtitle">HR analytics project combining SQL, Python, Power BI, Machine Learning, and Streamlit</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        This project analyzes employee attrition using multiple data analysis and visualization approaches. 
        The system combines database analysis, statistical modeling, and interactive reporting to provide insights into workforce retention.
    """)

    st.markdown("#### Technologies")
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.markdown("""
            <div class="hr-card">
                <div style="color: #1F2937; font-weight: 600; margin-bottom: 4px;">Frontend</div>
                <div style="color: #6B7280; font-size: 0.9rem;">Streamlit</div>
            </div>
        """, unsafe_allow_html=True)
    with t2:
        st.markdown("""
            <div class="hr-card">
                <div style="color: #1F2937; font-weight: 600; margin-bottom: 4px;">Data Analysis</div>
                <div style="color: #6B7280; font-size: 0.9rem;">Pandas & Plotly</div>
            </div>
        """, unsafe_allow_html=True)
    with t3:
        st.markdown("""
            <div class="hr-card">
                <div style="color: #1F2937; font-weight: 600; margin-bottom: 4px;">Machine Learning</div>
                <div style="color: #6B7280; font-size: 0.9rem;">Scikit-Learn</div>
            </div>
        """, unsafe_allow_html=True)
    with t4:
        st.markdown("""
            <div class="hr-card">
                <div style="color: #1F2937; font-weight: 600; margin-bottom: 4px;">Business Intelligence</div>
                <div style="color: #6B7280; font-size: 0.9rem;">Power BI</div>
            </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("<br><hr style='border-color: #E5E7EB;'><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #9CA3AF; font-size: 0.85rem;">
        HR Analytics & Workforce Analysis
    </div>
""", unsafe_allow_html=True)