#=========================================================
# BUSINESS INTELLIGENCE DASHBOARD
#=========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import os

import gdown

#=========================================================
# PAGE CONFIGURATION
#=========================================================

st.set_page_config(

    page_title="Business Intelligence",

    page_icon="📈",

    layout="wide"

)



#=========================================================
# LOAD DATASET
#=========================================================

@st.cache_data
def load_data():

    file_path = os.path.join(

        "data",

        "cleaned_supply_chain_dataset.csv"

    )

    return pd.read_csv(file_path)



#=========================================================
# LOAD DATA
#=========================================================

df = load_data()



#=========================================================
# PAGE TITLE
#=========================================================

st.title("📈 Business Intelligence Dashboard")


st.markdown(
"""

### Business Question

> What business actions should we take?

"""
)


st.divider()
#=========================================================
# EXECUTIVE KPIs
#=========================================================


total_sales = round(

    df["Sales"].sum(),

    2

)


total_orders = len(df)


average_sales = round(

    df["Sales"].mean(),

    2

)


late_orders = (

    df["Late_delivery_risk"]

    .sum()

)



markets = (

    df["Market"]

    .nunique()

)


categories = (

    df["Category Name"]

    .nunique()

)



st.subheader(
    "Executive KPIs"
)



k1,k2,k3 = st.columns(3)


k1.metric(

    "Total Sales",

    f"${total_sales:,.2f}"

)


k2.metric(

    "Total Orders",

    f"{total_orders:,}"

)


k3.metric(

    "Average Sales",

    f"${average_sales}"

)



k4,k5,k6 = st.columns(3)


k4.metric(

    "Late Deliveries",

    f"{late_orders:,}"

)


k5.metric(

    "Markets",

    markets

)


k6.metric(

    "Categories",

    categories

)



st.divider()
#=========================================================
# EXECUTIVE ANALYTICS
#=========================================================


st.subheader(
    "Executive Analytics Center"
)



tab1,tab2,tab3,tab4 = st.tabs(

    [

        "Sales Intelligence",

        "Market Intelligence",

        "Customer Intelligence",

        "Shipping Intelligence"

    ]

)



#=========================================================
# SALES
#=========================================================


with tab1:


    sales_df = (

        df.groupby(

            "Category Name"

        )["Sales"]

        .sum()

        .reset_index()

    )


    fig = px.bar(

        sales_df,

        x="Category Name",

        y="Sales",

        color="Sales",

        title="Sales Intelligence"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



#=========================================================
# MARKET
#=========================================================


with tab2:


    market_df = (

        df.groupby(

            "Market"

        )["Sales"]

        .sum()

        .reset_index()

    )


    fig = px.bar(

        market_df,

        x="Market",

        y="Sales",

        color="Sales",

        title="Market Intelligence"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )

#=========================================================
# CUSTOMER ANALYSIS
#=========================================================


with tab3:


    customer_df = (

        df.groupby(

            "Customer Segment"

        )["Sales"]

        .sum()

        .reset_index()

    )


    fig = px.pie(

        customer_df,

        names="Customer Segment",

        values="Sales",

        title="Customer Intelligence"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



#=========================================================
# SHIPPING ANALYSIS
#=========================================================


with tab4:


    shipping_df = (

        df.groupby(

            "Shipping Mode"

        )["Sales"]

        .sum()

        .reset_index()

    )


    fig = px.bar(

        shipping_df,

        x="Shipping Mode",

        y="Sales",

        color="Sales",

        title="Shipping Intelligence"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


st.divider()

#=========================================================
# EXECUTIVE INSIGHTS
#=========================================================


st.subheader(
    "Executive Insights"
)



i1,i2 = st.columns(2)



with i1:


    highest_market = (

        df.groupby(

            "Market"

        )["Sales"]

        .sum()

        .idxmax()

    )


    st.success(

        f"Highest Revenue Market : {highest_market}"

    )



    highest_category = (

        df.groupby(

            "Category Name"

        )["Sales"]

        .sum()

        .idxmax()

    )


    st.success(

        f"Highest Revenue Category : {highest_category}"

    )



with i2:


    highest_customer = (

        df.groupby(

            "Customer Segment"

        )["Sales"]

        .sum()

        .idxmax()

    )


    st.info(

        f"Highest Revenue Segment : {highest_customer}"

    )



    highest_shipping = (

        df.groupby(

            "Shipping Mode"

        )["Sales"]

        .sum()

        .idxmax()

    )


    st.info(

        f"Highest Revenue Shipping Mode : {highest_shipping}"

    )


st.divider()

#=========================================================
# BUSINESS RECOMMENDATIONS
#=========================================================


st.subheader(
    "Business Recommendations"
)



st.success(
"""

• Increase Sales Opportunities.

• Optimize Shipping Strategies.

• Reduce Late Deliveries.

• Improve Customer Satisfaction.

• Improve Supply Chain Visibility.

• Monitor High Risk Orders.

"""
)



st.divider()



#=========================================================
# PROJECT SUMMARY
#=========================================================


st.subheader(
    "Project Summary"
)



st.info(
"""

✓ Machine Learning Enabled.


✓ Late Delivery Prediction Enabled.


✓ High Risk Intelligence Enabled.


✓ Business Intelligence Enabled.


✓ Interactive Analytics Enabled.


✓ Executive Decision Support Enabled.


"""
)



st.divider()



#=========================================================
# FOOTER
#=========================================================


st.caption(

    "Business Intelligence Dashboard | "

    "Executive • Interactive • Dynamic"

)



