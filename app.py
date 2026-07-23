#=========================================================
# MACHINE LEARNING BASED LATE DELIVERY RISK PREDICTION
# IN GLOBAL SUPPLY CHAIN OPERATIONS
#=========================================================
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import tempfile
import os
import gdown

#=========================================================
# PAGE CONFIGURATION
#=========================================================

st.set_page_config(
    page_title="Supply Chain Risk Intelligence",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


#=========================================================
# CUSTOM CSS
#=========================================================

st.markdown("""

<style>

.main{
    background-color:#0E1117;
}


.block-container{
    padding-top:2rem;
}


h1,h2,h3,h4{
    color:white;
}


div[data-testid="metric-container"]{

    background-color:#1b2631;
    padding:20px;
    border-radius:15px;
    border:1px solid #2c3e50;

}


.sidebar .sidebar-content{

    background:#111827;

}


.big-font{

    font-size:55px;
    font-weight:bold;
    text-align:center;

}


.small-font{

    font-size:22px;
    text-align:center;
    color:#BFC9CA;

}


</style>

""",unsafe_allow_html=True)



#=========================================================
# LOAD DATASET
#=========================================================
@st.cache_data
def load_data():

    url="https://drive.google.com/uc?id=1OQsEqjJrqw4Aa0gsXuprlwlvKaDpq1pI"


    temp_dir=tempfile.gettempdir()


    output=os.path.join(

        temp_dir,

        "cleaned_supply_chain_dataset.csv"

    )


    if not os.path.exists(output):

        gdown.download(

            url,

            output,

            quiet=False

        )


    return pd.read_csv(
    output,
    encoding="latin1"
)
#=========================================================
# DATA VALIDATION
#=========================================================
#=========================================================
# LOAD DATASET
#=========================================================

try:

    df = load_data()

except Exception as e:

    st.error(

        f"Dataset could not be loaded : {e}"

    )

    st.stop()

#=========================================================
# PROJECT TITLE
#=========================================================


st.markdown("""

<div class='big-font'>

📦 Supply Chain Risk Intelligence System

</div>

""",unsafe_allow_html=True)



st.markdown("""

<div class='small-font'>

Machine Learning Based Late Delivery Risk Prediction
in Global Supply Chain Operations

</div>

""",unsafe_allow_html=True)



st.divider()

#=========================================================
# PROJECT OVERVIEW
#=========================================================


st.header("Project Overview")


st.markdown(
"""

This project analyzes global supply chain operations and
predicts the probability of late deliveries using Machine
Learning models. The system combines Supply Chain Analytics,
Business Intelligence, and Risk Prediction techniques to
support data-driven operational decisions.

"""
)


st.info(
"""

### Project Objectives

- Analyze supply chain performance across products and regions.
- Identify factors influencing late deliveries.
- Predict late delivery risks using Machine Learning models.
- Evaluate model performance using classification metrics.
- Detect high-risk orders and operational bottlenecks.
- Generate business intelligence insights for decision making.

"""
)


st.divider()



#=========================================================
# DATASET INFORMATION
#=========================================================


st.header("Dataset Information")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        label="Total Records",
        value=f"{len(df):,}"
    )


with col2:

    st.metric(
        label="Total Features",
        value=f"{df.shape[1]}"
    )


with col3:

    missing_values = int(df.isnull().sum().sum())

    st.metric(
        label="Missing Values",
        value=f"{missing_values:,}"
    )



st.divider()



#=========================================================
# DATA PREVIEW
#=========================================================


st.header("Dataset Preview")


st.dataframe(
    df.head(10),
    use_container_width=True
)


st.divider()

#=========================================================
# KEY PERFORMANCE INDICATORS
#=========================================================

st.header("Supply Chain Performance Summary")


#---------------------------------------------------------
# KPI CALCULATIONS
#---------------------------------------------------------

total_sales = round(df["Sales"].sum(), 2)

total_orders = len(df)

average_sales = round(df["Sales"].mean(), 2)

total_products = df["Category Name"].nunique()



#---------------------------------------------------------
# KPI CARDS
#---------------------------------------------------------

k1, k2, k3, k4 = st.columns(4)


with k1:

    st.metric(

        label="Total Sales",

        value=f"${total_sales:,.2f}"

    )


with k2:

    st.metric(

        label="Total Orders",

        value=f"{total_orders:,}"

    )


with k3:

    st.metric(

        label="Average Sales",

        value=f"${average_sales:,.2f}"

    )


with k4:

    st.metric(

        label="Product Categories",

        value=f"{total_products:,}"

    )


st.info(
"""

### KPI Description

The KPI cards provide a high-level overview of supply chain
performance. These metrics summarize total sales generated,
overall order volume, average sales per transaction, and the
number of product categories present within the dataset.

"""
)


st.divider()



#=========================================================
# LATE DELIVERY OVERVIEW
#=========================================================


st.header("Late Delivery Risk Overview")


#---------------------------------------------------------
# CALCULATIONS
#---------------------------------------------------------

if "Late_delivery_risk" in df.columns:

    total_late_orders = int(df["Late_delivery_risk"].sum())

    late_delivery_percentage = round(

        (total_late_orders / len(df))*100,2

    )

else:

    total_late_orders = 0

    late_delivery_percentage = 0



col1, col2 = st.columns(2)


with col1:

    st.metric(

        label="Late Deliveries",

        value=f"{total_late_orders:,}"

    )


with col2:

    st.metric(

        label="Late Delivery Percentage",

        value=f"{late_delivery_percentage}%"

    )



st.success(
"""

The late delivery metrics provide an overall assessment of
operational performance by measuring the proportion of orders
that experienced delayed deliveries across the supply chain.

"""
)


st.divider()

#=========================================================
# PROJECT WORKFLOW
#=========================================================


st.header("Project Workflow")


st.info(
"""

1. Dataset Collection

↓

2. Data Cleaning & Preprocessing

↓

3. Feature Engineering

↓

4. Exploratory Data Analysis

↓

5. Machine Learning Modeling

↓

6. Late Delivery Risk Prediction

↓

7. Supply Chain Analytics

↓

8. High Risk Intelligence

↓

9. Business Intelligence

↓

10. Executive Recommendations

"""
)


st.divider()



#=========================================================
# TECHNOLOGIES USED
#=========================================================


st.header("Technologies Used")


t1,t2,t3,t4 = st.columns(4)


with t1:

    st.success(
        "Python"
    )

    st.success(
        "Pandas"
    )


with t2:

    st.success(
        "Plotly"
    )

    st.success(
        "NumPy"
    )



with t3:

    st.success(
        "Scikit-Learn"
    )

    st.success(
        "Streamlit"
    )


with t4:

    st.success(
        "Machine Learning"
    )

    st.success(
        "Business Intelligence"
    )



st.divider()



#=========================================================
# PROJECT MODULES
#=========================================================


st.header("Project Modules")


st.markdown(
"""

The application consists of five interactive modules.


"""
)


m1,m2 = st.columns(2)


with m1:


    st.info(
        "Supply Chain Overview"
    )


    st.info(
        "Late Delivery Risk Prediction"
    )


    st.info(
        "Model Performance Evaluation"
    )



with m2:


    st.info(
        "High Risk Intelligence"
    )


    st.info(
        "Business Intelligence Dashboard"
    )


#=========================================================
# NAVIGATION GUIDE
#=========================================================


st.header("Dashboard Navigation")


st.success(
"""
Supply Chain Overview

↓

Explore supply chain performance,
sales analytics and late delivery trends.
"""
)



st.success(
"""
Risk Prediction

↓

Predict the probability of
late deliveries using Machine Learning.
"""
)



st.success(
"""
Model Performance

↓

Compare the performance of
Machine Learning models.
"""
)



st.success(
"""
High Risk Intelligence

↓

Identify the major contributors
to delivery delays.
"""
)



st.success(
"""
Business Intelligence

↓

Generate executive level
business insights and recommendations.
"""
)


st.divider()



#=========================================================
# FOOTER
#=========================================================


st.markdown(
"""

<center>

### Supply Chain Risk Intelligence System


Developed using


Python • Streamlit • Plotly • Scikit-Learn • Machine Learning


© 2026 Bandham Raju


</center>

""",
unsafe_allow_html=True
)





