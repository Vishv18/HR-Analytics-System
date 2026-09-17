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
    page_title="HR Analytics & Workforce Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM HUMANIZED CSS DESIGN SYSTEM
# --------------------------------------------------
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Global Reset & Typography */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Background */
.stApp {
    background-color: #090D14;
    color: #E2E8F0;
}

/* Header & Banner Styling */
.hero-container {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 24px;
    backdrop-filter: blur(12px);
}
.hero-title {
    font-size: 1.85rem;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: -0.025em;
    margin-bottom: 6px;
}
.hero-subtitle {
    font-size: 0.95rem;
    color: #94A3B8;
    max-width: 750px;
    line-height: 1.5;
}

/* Card Components */
.hr-card {
    background: #0F172A;
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 16px;
}

.hr-card-interactive {
    background: #0F172A;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 24px;
    height: 100%;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
.hr-card-interactive:hover {
    border-color: rgba(99, 102, 241, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 12px 20px -8px rgba(0, 0, 0, 0.5);
}

/* Custom Metric / KPI Cards */
.kpi-card {
    background: #0F172A;
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 12px;
    padding: 18px 20px;
    position: relative;
    overflow: hidden;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: #6366F1;
}
.kpi-card.emerald::before { background: #10B981; }
.kpi-card.rose::before { background: #F43F5E; }
.kpi-card.amber::before { background: #F59E0B; }
.kpi-card.indigo::before { background: #6366F1; }
.kpi-card.cyan::before { background: #06B6D4; }

.kpi-label {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #94A3B8;
    margin-bottom: 6px;
}
.kpi-value {
    font-size: 1.8rem;
    font-weight: 800;
    color: #F8FAFC;
    line-height: 1.1;
}
.kpi-sub {
    font-size: 0.8rem;
    font-weight: 500;
    color: #64748B;
    margin-top: 6px;
}

/* Badges */
.badge {
    display: inline-flex;
    align-items: center;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
}
.badge-indigo { background: rgba(99, 102, 241, 0.15); color: #818CF8; border: 1px solid rgba(99, 102, 241, 0.3); }
.badge-emerald { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }
.badge-rose { background: rgba(244, 63, 94, 0.15); color: #FB7185; border: 1px solid rgba(244, 63, 94, 0.3); }
.badge-amber { background: rgba(245, 158, 11, 0.15); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.3); }

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #06090E;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.sidebar-brand {
    padding: 12px 4px 20px 4px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    margin-bottom: 16px;
}
.sidebar-title {
    font-size: 1.1rem;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: -0.01em;
}
.sidebar-subtitle {
    font-size: 0.75rem;
    color: #64748B;
    font-weight: 500;
}

/* Tabs Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: #0F172A;
    padding: 6px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.06);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 0.88rem;
    font-weight: 600;
    color: #94A3B8;
    border: none !important;
}

.stTabs [aria-selected="true"] {
    background-color: #1E293B !important;
    color: #F8FAFC !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

/* Input Fields & Buttons */
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
    background-color: #0F172A !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
    border-radius: 8px !important;
    color: #F8FAFC !important;
}

.stButton > button {
    background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%);
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 10px 24px;
    font-weight: 600;
    letter-spacing: 0.01em;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
    box-shadow: 0 6px 16px rgba(79, 70, 229, 0.35);
    transform: translateY(-1px);
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
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Plus Jakarta Sans, sans-serif', color='#94A3B8', size=12),
        margin=dict(l=20, r=20, t=40, b=20),
        height=height,
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.05)',
            zeroline=False,
            tickfont=dict(color='#94A3B8')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.05)',
            zeroline=False,
            tickfont=dict(color='#94A3B8')
        ),
        legend=dict(
            font=dict(color='#CBD5E1', size=11),
            bgcolor='rgba(15, 23, 42, 0.6)',
            bordercolor='rgba(255, 255, 255, 0.08)',
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
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="background: linear-gradient(135deg, #6366F1, #4F46E5); padding: 8px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 1.2rem; color: white;">⚡</span>
                </div>
                <div>
                    <div class="sidebar-title">HR Analytics</div>
                    <div class="sidebar-subtitle">Workforce Intelligence</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Analytics & Power BI",
            "Risk Prediction",
            "Employee Directory",
            "About System"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="padding: 12px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px;">
            <div style="font-size: 0.72rem; color: #64748B; font-weight: 600; text-transform: uppercase;">Dataset Status</div>
            <div style="font-size: 0.85rem; color: #34D399; font-weight: 600; margin-top: 2px;">● 1,470 Employees Loaded</div>
        </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# 1. OVERVIEW (HOME)
# --------------------------------------------------
if page == "Overview":
    st.markdown("""
        <div class="hero-container">
            <div class="badge badge-indigo" style="margin-bottom: 10px;">Enterprise Analytics</div>
            <div class="hero-title">Workforce Retention & Attrition Intelligence</div>
            <div class="hero-subtitle">
                An integrated platform connecting key HR metrics, predictive risk modeling, and interactive Power BI executive reporting to minimize employee churn.
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
                <div class="kpi-card indigo">
                    <div class="kpi-label">TOTAL WORKFORCE</div>
                    <div class="kpi-value">{total_emp:,}</div>
                    <div class="kpi-sub">Active Records</div>
                </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
                <div class="kpi-card rose">
                    <div class="kpi-label">TOTAL ATTRITION</div>
                    <div class="kpi-value">{attr_count:,}</div>
                    <div class="kpi-sub">Departed Staff</div>
                </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
                <div class="kpi-card amber">
                    <div class="kpi-label">ATTRITION RATE</div>
                    <div class="kpi-value">{attr_rate:.1f}%</div>
                    <div class="kpi-sub">Benchmark: 15.0%</div>
                </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown(f"""
                <div class="kpi-card emerald">
                    <div class="kpi-label">AVG MONTHLY SALARY</div>
                    <div class="kpi-value">${avg_income:,.0f}</div>
                    <div class="kpi-sub">Across All Roles</div>
                </div>
            """, unsafe_allow_html=True)
        with m5:
            st.markdown(f"""
                <div class="kpi-card cyan">
                    <div class="kpi-label">AVG TENURE</div>
                    <div class="kpi-value">{avg_tenure:.1f} yrs</div>
                    <div class="kpi-sub">Company Average</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Core Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="hr-card-interactive">
                <div class="badge badge-indigo" style="margin-bottom: 12px;">Visual Reporting</div>
                <h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 8px;">Power BI Analytics</h4>
                <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 16px;">
                    Explore interactive department breakdowns, overtime impact, salary dynamics, and live embedded Power BI web dashboards.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="hr-card-interactive">
                <div class="badge badge-rose" style="margin-bottom: 12px;">Machine Learning</div>
                <h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 8px;">Risk Prediction Engine</h4>
                <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 16px;">
                    Evaluate individual employee parameters through our trained ML pipeline to calculate flight risk probabilities.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="hr-card-interactive">
                <div class="badge badge-emerald" style="margin-bottom: 12px;">Workforce Search</div>
                <h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 8px;">Employee Directory</h4>
                <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 16px;">
                    Lookup team profiles, review individual engagement indices, and inspect historical performance metrics.
                </p>
            </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# 2. ANALYTICS & POWER BI
# --------------------------------------------------
elif page == "Analytics & Power BI":
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="color: #F8FAFC; font-weight: 800; margin-bottom: 4px;">Analytics & Power BI Dashboard</h2>
            <div style="color: #94A3B8; font-size: 0.9rem;">Interactive data exploration, department filters, and cloud report integration</div>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "Interactive Dashboard",
        "Power BI Cloud Embed",
        "Desktop File (.PBIX)"
    ])

    # ----------------------------------------------
    # TAB 1: INTERACTIVE DASHBOARD
    # ----------------------------------------------
    with tab1:
        if df_raw is not None:
            # Filters container
            with st.container():
                st.markdown('<div class="hr-card" style="padding: 16px 20px;">', unsafe_allow_html=True)
                f_col1, f_col2, f_col3 = st.columns(3)
                
                dept_options = ["All Departments"] + list(df_raw['Department'].unique())
                with f_col1:
                    selected_dept = st.selectbox("Department Filter", dept_options)
                
                gender_options = ["All Genders"] + list(df_raw['Gender'].unique())
                with f_col2:
                    selected_gender = st.selectbox("Gender Filter", gender_options)
                
                overtime_options = ["All OverTime Status"] + list(df_raw['OverTime'].unique())
                with f_col3:
                    selected_overtime = st.selectbox("OverTime Filter", overtime_options)
                st.markdown('</div>', unsafe_allow_html=True)

            # Filter logic
            df_filtered = df_raw.copy()
            if selected_dept != "All Departments":
                df_filtered = df_filtered[df_filtered['Department'] == selected_dept]
            if selected_gender != "All Genders":
                df_filtered = df_filtered[df_filtered['Gender'] == selected_gender]
            if selected_overtime != "All OverTime Status":
                df_filtered = df_filtered[df_filtered['OverTime'] == selected_overtime]

            # KPI Bar
            total_emp = len(df_filtered)
            attr_count = df_filtered['Attrition_Num'].sum()
            attr_rate = (attr_count / total_emp * 100) if total_emp > 0 else 0
            avg_income = df_filtered['MonthlyIncome'].mean() if total_emp > 0 else 0
            avg_tenure = df_filtered['YearsAtCompany'].mean() if total_emp > 0 else 0

            k1, k2, k3, k4, k5 = st.columns(5)
            with k1:
                st.markdown(f"""
                    <div class="kpi-card indigo">
                        <div class="kpi-label">FILTERED COUNT</div>
                        <div class="kpi-value">{total_emp:,}</div>
                    </div>
                """, unsafe_allow_html=True)
            with k2:
                st.markdown(f"""
                    <div class="kpi-card rose">
                        <div class="kpi-label">ATTRITION COUNT</div>
                        <div class="kpi-value">{attr_count:,}</div>
                    </div>
                """, unsafe_allow_html=True)
            with k3:
                st.markdown(f"""
                    <div class="kpi-card amber">
                        <div class="kpi-label">ATTRITION RATE</div>
                        <div class="kpi-value">{attr_rate:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)
            with k4:
                st.markdown(f"""
                    <div class="kpi-card emerald">
                        <div class="kpi-label">AVG MONTHLY INCOME</div>
                        <div class="kpi-value">${avg_income:,.0f}</div>
                    </div>
                """, unsafe_allow_html=True)
            with k5:
                st.markdown(f"""
                    <div class="kpi-card cyan">
                        <div class="kpi-label">AVG TENURE</div>
                        <div class="kpi-value">{avg_tenure:.1f} Yrs</div>
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
                    title="<b>Department Attrition Rate (%)</b>",
                    color='Department',
                    color_discrete_sequence=['#6366F1', '#EC4899', '#10B981']
                )
                fig_dept.update_traces(texttemplate='%{text}%', textposition='outside', marker_line_color='rgba(255,255,255,0.1)', marker_line_width=1)
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
                    title="<b>OverTime vs. Attrition Count</b>",
                    color_discrete_map={'Yes': '#F43F5E', 'No': '#6366F1'}
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
                    title="<b>Monthly Income Distribution by Job Role</b>",
                    color_discrete_map={'Yes': '#F43F5E', 'No': '#10B981'}
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
                    title="<b>Satisfaction vs. Work-Life Balance Matrix</b>",
                    labels={'JobSatisfaction': 'Job Satisfaction (1-4)', 'WorkLifeBalance': 'Work-Life Balance (1-4)'},
                    color_discrete_map={'Yes': '#F43F5E', 'No': '#6366F1'},
                    size_max=36
                )
                fig_sat = apply_plotly_theme(fig_sat, height=420)
                st.plotly_chart(fig_sat, use_container_width=True)

            # Table View
            with st.expander("📋 View Filtered Dataset Records"):
                st.dataframe(
                    df_filtered[['EmployeeNumber', 'Age', 'Department', 'JobRole', 'MonthlyIncome', 'OverTime', 'JobSatisfaction', 'Attrition']],
                    use_container_width=True
                )
        else:
            st.error("Could not locate `data/raw/HR-Employee-Attrition.csv`.")

    # ----------------------------------------------
    # TAB 2: POWER BI EMBED
    # ----------------------------------------------
    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        col_embed, col_guide = st.columns([2, 1])

        with col_embed:
            st.markdown("""
                <div class="hr-card">
                    <h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 6px;">Live Power BI Service Frame</h4>
                    <p style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 16px;">
                        Paste your Power BI 'Publish to Web' public URL or iframe code to stream your cloud dashboard.
                    </p>
                </div>
            """, unsafe_allow_html=True)

            default_embed_url = st.text_input(
                "Power BI Public Embed URL:",
                placeholder="https://app.powerbi.com/view?r=eyJrIjoi...",
                help="Paste the published web URL or iframe link here."
            )

            iframe_height = st.slider("Viewer Frame Height (px)", min_value=400, max_value=900, value=600, step=50)

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
                    <div style="border: 2px dashed rgba(255,255,255,0.1); border-radius: 12px; padding: 40px; text-align: center; background-color: #0F172A; color: #94A3B8; font-family: 'Plus Jakarta Sans', sans-serif; height: {iframe_height-60}px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                        <div style="font-size: 2.5rem; margin-bottom: 12px;">📊</div>
                        <h3 style="color: #F8FAFC; margin-bottom: 8px; font-weight: 700;">Power BI Live Embed Container</h3>
                        <p style="max-width: 500px; font-size: 14px; line-height: 1.5; color: #64748B;">
                            Paste your published Power BI Web report URL in the field above to render your live report.
                        </p>
                    </div>
                    ''',
                    height=iframe_height
                )

        with col_guide:
            st.markdown("""
                <div class="hr-card">
                    <h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 12px;">Publishing Checklist</h4>
                    <ol style="color: #94A3B8; font-size: 0.85rem; line-height: 1.7; padding-left: 18px; margin: 0;">
                        <li>Open <code style="color: #818CF8;">HR_Analytics_Dashboard.pbix</code> in Power BI Desktop.</li>
                        <li>Click <b>Publish</b> to upload to your Power BI Workspace.</li>
                        <li>Open the report in Power BI Cloud (<code style="color: #818CF8;">app.powerbi.com</code>).</li>
                        <li>Navigate to <b>File ➔ Embed report ➔ Publish to Web</b>.</li>
                        <li>Copy the generated web link and paste it on the left!</li>
                    </ol>
                </div>
            """, unsafe_allow_html=True)

    # ----------------------------------------------
    # TAB 3: DOWNLOAD PBIX FILE
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
                st.markdown(f"""
                    <div class="hr-card">
                        <div class="badge badge-emerald" style="margin-bottom: 8px;">Ready for Download</div>
                        <h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 6px;">HR_Analytics_Dashboard.pbix</h4>
                        <div style="color: #94A3B8; font-size: 0.88rem; line-height: 1.6;">
                            Contains native DAX measures, data relationships, custom themes, and page layouts.<br>
                            <b>File Size:</b> {file_size_mb:.2f} MB
                        </div>
                    </div>
                """, unsafe_allow_html=True)

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
            st.error("PBIX project file missing.")

# --------------------------------------------------
# 3. RISK PREDICTION
# --------------------------------------------------
elif page == "Risk Prediction":
    st.markdown("""
        <div style="margin-bottom: 24px;">
            <h2 style="color: #F8FAFC; font-weight: 800; margin-bottom: 4px;">Employee Attrition Risk Predictor</h2>
            <div style="color: #94A3B8; font-size: 0.9rem;">Input key employee parameters to compute ML-driven flight risk probabilities</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="hr-card">', unsafe_allow_html=True)
        st.markdown('<h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 16px;">Demographics & Role</h4>', unsafe_allow_html=True)
        age = st.number_input("Employee Age", min_value=18, max_value=70, value=32)
        department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
        job_role = st.selectbox("Job Role", [
            "Sales Executive", "Research Scientist", "Laboratory Technician",
            "Manufacturing Director", "Healthcare Representative", "Manager",
            "Sales Representative", "Research Director", "Human Resources"
        ])
        monthly_income = st.number_input("Monthly Salary ($)", min_value=1000, max_value=100000, value=5500, step=500)
        job_level = st.selectbox("Job Level (1 - 5)", [1, 2, 3, 4, 5], index=1)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="hr-card">', unsafe_allow_html=True)
        st.markdown('<h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 16px;">Engagement & Dynamics</h4>', unsafe_allow_html=True)
        overtime = st.selectbox("OverTime Required", ["Yes", "No"], index=1)
        job_satisfaction = st.select_slider("Job Satisfaction Rating", options=[1, 2, 3, 4], value=3, help="1: Low ➔ 4: High")
        work_life_balance = st.select_slider("Work-Life Balance Rating", options=[1, 2, 3, 4], value=3, help="1: Low ➔ 4: High")
        years_at_company = st.number_input("Years at Company", min_value=0, max_value=50, value=4)
        business_travel = st.selectbox("Business Travel Frequency", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Calculate Risk Probability", use_container_width=True):
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
            badge_class = "badge-rose"
            status_text = "High Flight Risk"
            card_border = "rgba(244, 63, 94, 0.4)"
        elif probability >= 0.30:
            badge_class = "badge-amber"
            status_text = "Moderate Risk"
            card_border = "rgba(245, 158, 11, 0.4)"
        else:
            badge_class = "badge-emerald"
            status_text = "Low Risk"
            card_border = "rgba(16, 185, 129, 0.4)"

        st.markdown(f"""
            <div style="background: #0F172A; border: 1px solid {card_border}; border-radius: 16px; padding: 28px; text-align: center;">
                <div class="badge {badge_class}" style="margin-bottom: 12px; font-size: 0.85rem; padding: 4px 14px;">{status_text}</div>
                <div style="font-size: 3rem; font-weight: 800; color: #F8FAFC; line-height: 1;">{risk_pct:.1f}%</div>
                <div style="font-size: 0.9rem; color: #94A3B8; margin-top: 8px;">Calculated Attrition Probability Score</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Actionable HR Recommendations")
        
        recs = []
        if overtime == "Yes":
            recs.append("● **Overtime Pressure**: Employee works recurring overtime. Consider reviewing task distribution or offering flex-time arrangements.")
        if job_satisfaction <= 2:
            recs.append("● **Low Job Satisfaction**: Conduct an internal 1-on-1 check-in to identify role friction points or growth aspirations.")
        if work_life_balance <= 2:
            recs.append("● **Work-Life Imbalance**: Risk of burnout. Evaluate hybrid work flexibility or project workload re-allocation.")
        if monthly_income < 3500:
            recs.append("● **Compensation Audit**: Current monthly salary is below market average for this role level. Consider benchmark review.")

        if not recs:
            recs.append("● **Positive Engagement Indicators**: Employee parameters indicate stable satisfaction and balanced workload. Maintain regular check-ins.")

        for r in recs:
            st.markdown(f"<div style='background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 12px 16px; border-radius: 10px; margin-bottom: 8px; color: #CBD5E1; font-size: 0.9rem;'>{r}</div>", unsafe_allow_html=True)

# --------------------------------------------------
# 4. EMPLOYEE DIRECTORY
# --------------------------------------------------
elif page == "Employee Directory":
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="color: #F8FAFC; font-weight: 800; margin-bottom: 4px;">Employee Directory & Profiles</h2>
            <div style="color: #94A3B8; font-size: 0.9rem;">Lookup individual employee records, engagement scores, and risk evaluation</div>
        </div>
    """, unsafe_allow_html=True)

    if df_raw is not None:
        emp_ids = sorted(df_raw['EmployeeNumber'].unique())
        selected_id = st.selectbox("Select Employee ID to Inspect", emp_ids, index=0)

        emp_row = df_raw[df_raw['EmployeeNumber'] == selected_id].iloc[0]

        # Calculate live risk for selected employee
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

        st.markdown("<br>", unsafe_allow_html=True)

        col_head1, col_head2 = st.columns([2, 1])

        with col_head1:
            st.markdown(f"""
                <div class="hr-card">
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <div style="background: linear-gradient(135deg, #4F46E5, #4338CA); width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: 800; color: white;">
                            #{emp_row['EmployeeNumber']}
                        </div>
                        <div>
                            <div style="font-size: 1.3rem; font-weight: 800; color: #F8FAFC;">Employee #{emp_row['EmployeeNumber']}</div>
                            <div style="font-size: 0.9rem; color: #94A3B8;">{emp_row['JobRole']} | <span style="color: #818CF8;">{emp_row['Department']}</span></div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col_head2:
            badge_type = "badge-rose" if prob >= 0.5 else ("badge-amber" if prob >= 0.3 else "badge-emerald")
            st.markdown(f"""
                <div class="hr-card" style="text-align: center;">
                    <div class="badge {badge_type}">Predicted Attrition Risk</div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: #F8FAFC; margin-top: 4px;">{risk_score:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("### Profile Overview")
        p1, p2, p3, p4 = st.columns(4)
        with p1:
            st.markdown(f"""
                <div class="kpi-card indigo">
                    <div class="kpi-label">AGE & TENURE</div>
                    <div class="kpi-value">{emp_row['Age']} yrs</div>
                    <div class="kpi-sub">{emp_row['YearsAtCompany']} Yrs at Company</div>
                </div>
            """, unsafe_allow_html=True)
        with p2:
            st.markdown(f"""
                <div class="kpi-card emerald">
                    <div class="kpi-label">MONTHLY COMPENSATION</div>
                    <div class="kpi-value">${emp_row['MonthlyIncome']:,}</div>
                    <div class="kpi-sub">Job Level {emp_row['JobLevel']}</div>
                </div>
            """, unsafe_allow_html=True)
        with p3:
            st.markdown(f"""
                <div class="kpi-card amber">
                    <div class="kpi-label">SATISFACTION RATING</div>
                    <div class="kpi-value">{emp_row['JobSatisfaction']} / 4</div>
                    <div class="kpi-sub">Work-Life Balance: {emp_row['WorkLifeBalance']}/4</div>
                </div>
            """, unsafe_allow_html=True)
        with p4:
            st.markdown(f"""
                <div class="kpi-card cyan">
                    <div class="kpi-label">OVERTIME STATUS</div>
                    <div class="kpi-value">{emp_row['OverTime']}</div>
                    <div class="kpi-sub">Travel: {emp_row['BusinessTravel']}</div>
                </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# 5. ABOUT
# --------------------------------------------------
elif page == "About System":
    st.markdown("""
        <div style="margin-bottom: 24px;">
            <h2 style="color: #F8FAFC; font-weight: 800; margin-bottom: 4px;">About HR Analytics Intelligence</h2>
            <div style="color: #94A3B8; font-size: 0.9rem;">System architecture, underlying ML models, and data pipeline specs</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="hr-card">
            <h4 style="color: #F8FAFC; font-weight: 700; margin-bottom: 10px;">Platform Architecture</h4>
            <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.6;">
                Built to serve modern HR operations, this application unifies transactional dataset analytics with predictive attrition models. 
                By providing proactive risk assessments before resignations occur, HR leaders can implement targeted retention strategies.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Technical Stack")
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.markdown("""
            <div class="hr-card">
                <div class="badge badge-indigo" style="margin-bottom: 8px;">Frontend</div>
                <div style="color: #F8FAFC; font-weight: 700;">Streamlit & Custom CSS</div>
            </div>
        """, unsafe_allow_html=True)
    with t2:
        st.markdown("""
            <div class="hr-card">
                <div class="badge badge-emerald" style="margin-bottom: 8px;">Data Engine</div>
                <div style="color: #F8FAFC; font-weight: 700;">Pandas & Plotly</div>
            </div>
        """, unsafe_allow_html=True)
    with t3:
        st.markdown("""
            <div class="hr-card">
                <div class="badge badge-rose" style="margin-bottom: 8px;">Machine Learning</div>
                <div style="color: #F8FAFC; font-weight: 700;">Scikit-Learn Pipeline</div>
            </div>
        """, unsafe_allow_html=True)
    with t4:
        st.markdown("""
            <div class="hr-card">
                <div class="badge badge-amber" style="margin-bottom: 8px;">BI Integration</div>
                <div style="color: #F8FAFC; font-weight: 700;">Power BI Desktop & Web</div>
            </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("<br><hr style='border-color: rgba(255,255,255,0.06);'><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #475569; font-size: 0.8rem; font-weight: 500;">
        HR Analytics & Retention Intelligence Platform
    </div>
""", unsafe_allow_html=True)