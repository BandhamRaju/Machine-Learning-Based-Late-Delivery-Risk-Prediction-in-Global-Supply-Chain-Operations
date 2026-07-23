#=========================================================
# HIGH RISK INTELLIGENCE CENTER
#=========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import tempfile
import gdown
#=========================================================
# PAGE CONFIGURATION
#=========================================================

st.set_page_config(

    page_title="High Risk Intelligence",

    page_icon="⚠️",

    layout="wide"

)


#=========================================================
# LOAD DATASET
#=========================================================
@st.cache_data
def load_data():

    url = "https://drive.google.com/uc?id=1OQsEqjJrqw4Aa0gsXuprlwlvKaDpq1pI"


    temp_dir = tempfile.gettempdir()


    output = os.path.join(

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
# LOAD DATA
#=========================================================

df = load_data()



#=========================================================
# PAGE TITLE
#=========================================================

st.title("⚠️ High Risk Intelligence Center")


st.markdown(
"""

### Business Question

> Why are deliveries getting delayed?

"""
)


st.divider()

#=========================================================
# CREATE HIGH RISK DATAFRAME
#=========================================================


if "Late_delivery_risk" in df.columns:

    risk_df = df[

        df["Late_delivery_risk"] == 1

    ]

else:

    risk_df = df.copy()



#=========================================================
# KPI CALCULATIONS
#=========================================================


total_orders = len(df)


total_late_orders = len(risk_df)



late_delivery_percentage = round(

    (total_late_orders/total_orders)*100,

    2

)



#---------------------------------------------------------

if "Market" in risk_df.columns:

    total_markets = (

        risk_df["Market"]

        .nunique()

    )

else:

    total_markets = 0



#---------------------------------------------------------

if "Category Name" in risk_df.columns:

    total_categories = (

        risk_df["Category Name"]

        .nunique()

    )

else:

    total_categories = 0



#=========================================================
# DISPLAY KPIs
#=========================================================


st.subheader(
    "Risk Summary"
)


k1,k2 = st.columns(2)


with k1:

    st.metric(

        "Late Deliveries",

        f"{total_late_orders:,}"

    )


with k2:

    st.metric(

        "Late Delivery Percentage",

        f"{late_delivery_percentage}%"

    )




k3,k4 = st.columns(2)


with k3:

    st.metric(

        "Markets Affected",

        total_markets

    )


with k4:

    st.metric(

        "Categories Affected",

        total_categories

    )


st.divider()

#=========================================================
# TOP RISK MARKETS
#=========================================================


st.subheader(
    "High Risk Analytics Center"
)



tab1,tab2,tab3,tab4 = st.tabs(

    [

        "Risk Markets",

        "Risk Categories",

        "Shipping Risk",

        "Risk Distribution"

    ]

)



#=========================================================
# TOP RISK MARKETS
#=========================================================


with tab1:


    if "Market" in risk_df.columns:


        market_df = (

            risk_df

            ["Market"]

            .value_counts()

            .reset_index()

        )


        market_df.columns = [

            "Market",

            "Late Deliveries"

        ]


        fig = px.bar(

            market_df,

            x="Market",

            y="Late Deliveries",

            color="Late Deliveries",

            title="Top High Risk Markets"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )

#=========================================================
# TOP RISK CATEGORIES
#=========================================================


with tab2:


    if "Category Name" in risk_df.columns:


        category_df = (

            risk_df

            ["Category Name"]

            .value_counts()

            .reset_index()

        )


        category_df.columns = [

            "Category",

            "Late Deliveries"

        ]


        fig = px.bar(

            category_df,

            x="Category",

            y="Late Deliveries",

            color="Late Deliveries",

            title="High Risk Categories"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



#=========================================================
# SHIPPING ANALYSIS
#=========================================================


with tab3:


    if "Shipping Mode" in risk_df.columns:


        shipping_df = (

            risk_df

            ["Shipping Mode"]

            .value_counts()

            .reset_index()

        )


        shipping_df.columns = [

            "Shipping Mode",

            "Late Deliveries"

        ]


        fig = px.pie(

            shipping_df,

            names="Shipping Mode",

            values="Late Deliveries",

            title="Shipping Risk Analysis"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



#=========================================================
# RISK DISTRIBUTION
#=========================================================


with tab4:


    if "Late_delivery_risk" in df.columns:


        distribution_df = (

            df

            ["Late_delivery_risk"]

            .value_counts()

            .reset_index()

        )


        distribution_df.columns = [

            "Risk",

            "Orders"

        ]


        fig = px.pie(

            distribution_df,

            names="Risk",

            values="Orders",

            title="Late Delivery Distribution"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )


st.divider()

#=========================================================
# RISK CONTRIBUTORS
#=========================================================


st.subheader(
    "Risk Contributors"
)



c1,c2 = st.columns(2)



#---------------------------------------------------------

with c1:


    if "Market" in risk_df.columns:


        highest_market = (

            risk_df

            ["Market"]

            .value_counts()

            .idxmax()

        )


        st.success(

            f"Highest Risk Market : {highest_market}"

        )



#---------------------------------------------------------

    if "Category Name" in risk_df.columns:


        highest_category = (

            risk_df

            ["Category Name"]

            .value_counts()

            .idxmax()

        )


        st.success(

            f"Highest Risk Category : {highest_category}"

        )



#---------------------------------------------------------

with c2:


    if "Shipping Mode" in risk_df.columns:


        highest_shipping = (

            risk_df

            ["Shipping Mode"]

            .value_counts()

            .idxmax()

        )


        st.info(

            f"Highest Risk Shipping Mode : {highest_shipping}"

        )



#---------------------------------------------------------

    st.info(

        f"Highest Risk Percentage : {late_delivery_percentage}%"

    )


st.divider()

#=========================================================
# EXECUTIVE RECOMMENDATIONS
#=========================================================


st.subheader(
    "Executive Recommendations"
)



if late_delivery_percentage >=50:


    st.error(
    """

    • Increase Shipment Monitoring.

    • Prioritize High Risk Orders.

    • Increase Buffer Days.

    • Optimize Shipping Strategies.

    """
    )



elif late_delivery_percentage >=30:


    st.warning(
    """

    • Review Risk Contributors.

    • Monitor High Risk Markets.

    • Improve Inventory Planning.

    • Maintain Shipment Monitoring.

    """
    )



else:


    st.success(
    """

    • Current Strategy Appears Effective.

    • Continue Standard Monitoring.

    • Maintain Existing Shipping Policies.

    """
    )



st.divider()



#=========================================================
# FOOTER
#=========================================================


st.caption(

    "High Risk Intelligence Center | "

    "Dynamic • Interactive • Risk Driven"

)

