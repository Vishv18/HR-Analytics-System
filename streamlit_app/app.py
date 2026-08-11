import streamlit as st

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
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.title("HR Analytics System")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Attrition Prediction",
        "Employee Profile",
        "About"
    ]
)

# --------------------------------------------------
# HOME
# --------------------------------------------------

if page == "Home":

    st.title("👥 HR Analytics System")

    st.subheader(
        "Employee Attrition Intelligence"
    )

    st.write(
        """
        Welcome to the HR Analytics System.

        This application is designed to assist HR teams
        in understanding and evaluating employee attrition
        risk through an interactive web interface.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
            ### 🔮 Attrition Prediction

            Enter employee details and evaluate
            their potential attrition risk.
            """
        )

    with col2:
        st.info(
            """
            ### 👤 Employee Profile

            View and manage employee-related
            information.
            """
        )

    with col3:
        st.info(
            """
            ### 📊 Data Driven

            Use employee information to support
            HR decision-making.
            """
        )

    st.divider()

    st.subheader("How the System Works")

    st.write(
        """
        1. HR enters employee information.
        2. The system processes the information.
        3. A machine-learning model will evaluate
           the employee's attrition risk.
        4. The application will display the predicted
           risk and relevant information.
        """
    )

# --------------------------------------------------
# ATTRITION PREDICTION
# --------------------------------------------------

elif page == "Attrition Prediction":

    st.title("🔮 Employee Attrition Prediction")

    st.write(
        """
        Enter the employee's information below.
        The attrition prediction model will be
        integrated into this page later.
        """
    )

    st.divider()

    st.subheader("Employee Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=70,
            value=30
        )

        department = st.selectbox(
            "Department",
            [
                "Sales",
                "Research & Development",
                "Human Resources"
            ]
        )

        job_role = st.selectbox(
            "Job Role",
            [
                "Sales Executive",
                "Research Scientist",
                "Laboratory Technician",
                "Manufacturing Director",
                "Healthcare Representative",
                "Manager",
                "Sales Representative",
                "Research Director",
                "Human Resources"
            ]
        )

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=1000,
            max_value=100000,
            value=5000
        )

        job_level = st.selectbox(
            "Job Level",
            [1, 2, 3, 4, 5]
        )

    with col2:

        overtime = st.selectbox(
            "Overtime",
            ["Yes", "No"]
        )

        job_satisfaction = st.selectbox(
            "Job Satisfaction",
            [1, 2, 3, 4]
        )

        work_life_balance = st.selectbox(
            "Work-Life Balance",
            [1, 2, 3, 4]
        )

        years_at_company = st.number_input(
            "Years at Company",
            min_value=0,
            max_value=50,
            value=3
        )

        business_travel = st.selectbox(
            "Business Travel",
            [
                "Travel_Rarely",
                "Travel_Frequently",
                "Non-Travel"
            ]
        )

    st.divider()

    if st.button(
        "🔮 Predict Attrition Risk",
        use_container_width=True
    ):

        st.warning(
            """
            Machine-learning prediction is not connected yet.

            This interface is ready for the model integration.
            """
        )

# --------------------------------------------------
# EMPLOYEE PROFILE
# --------------------------------------------------

elif page == "Employee Profile":

    st.title("👤 Employee Profile")

    st.write(
        """
        This section will allow HR users to search for
        and view individual employee information.
        """
    )

    st.divider()

    employee_id = st.text_input(
        "Enter Employee ID"
    )

    if st.button("Search Employee"):

        if employee_id:

            st.info(
                f"Employee profile for ID **{employee_id}** "
                "will be displayed here."
            )

        else:

            st.warning(
                "Please enter an Employee ID."
            )

# --------------------------------------------------
# ABOUT
# --------------------------------------------------

elif page == "About":

    st.title("ℹ️ About the System")

    st.write(
        """
        ### HR Analytics System

        The HR Analytics System is designed to support
        employee attrition analysis and HR decision-making.

        Power BI is used separately for historical workforce
        analysis and reporting.

        This Streamlit application is designed as an
        interactive HR application where employee information
        can be entered and evaluated.

        Machine-learning based attrition prediction will be
        integrated in a later stage.
        """
    )

    st.divider()

    st.subheader("Technology Stack")

    st.write(
        """
        - Python
        - Streamlit
        - Pandas
        - MySQL
        - Machine Learning
        - Power BI
        """
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "HR Analytics System | SGP Data Analytics Project"
)