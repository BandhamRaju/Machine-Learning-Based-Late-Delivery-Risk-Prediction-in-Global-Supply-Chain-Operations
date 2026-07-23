#=========================================================
# SUPPLY CHAIN OVERVIEW
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

    page_title="Supply Chain Overview",

    page_icon="📊",

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
# LOAD DATASET
#=========================================================

df = load_data()
#=========================================================
# DATA VALIDATION
#=========================================================

if df is None:

    st.error("Dataset not found.")

    st.stop()


#=========================================================
# PAGE TITLE
#=========================================================

st.title("📊 Supply Chain Overview")


st.markdown("""

### Business Question

> What is happening in our global supply chain operations?

""")


st.divider()


#=========================================================
# DYNAMIC FILTERS
#=========================================================

st.subheader("Filters")


filter1,filter2,filter3 = st.columns(3)



#---------------------------------------------------------
# MARKET FILTER
#---------------------------------------------------------

if "Market" in df.columns:

    selected_market = st.selectbox(

        "Market",

        ["All Markets"]

        +

        sorted(

            df["Market"]

            .dropna()

            .unique()

            .tolist()

        )

    )

else:

    selected_market = "All Markets"



#---------------------------------------------------------
# SHIPPING FILTER
#---------------------------------------------------------

if "Shipping Mode" in df.columns:

    selected_shipping = st.selectbox(

        "Shipping Mode",

        ["All Modes"]

        +

        sorted(

            df["Shipping Mode"]

            .dropna()

            .unique()

            .tolist()

        )

    )

else:

    selected_shipping = "All Modes"



#---------------------------------------------------------
# CATEGORY FILTER
#---------------------------------------------------------

if "Category Name" in df.columns:

    selected_category = st.selectbox(

        "Category",

        ["All Categories"]

        +

        sorted(

            df["Category Name"]

            .dropna()

            .unique()

            .tolist()

        )

    )

else:

    selected_category = "All Categories"



#=========================================================
# APPLY FILTERS
#=========================================================

filtered_df = df.copy()



#---------------------------------------------------------

if selected_market != "All Markets":

    filtered_df = filtered_df[

        filtered_df["Market"]

        ==

        selected_market

    ]



#---------------------------------------------------------

if selected_shipping != "All Modes":

    filtered_df = filtered_df[

        filtered_df["Shipping Mode"]

        ==

        selected_shipping

    ]



#---------------------------------------------------------

if selected_category != "All Categories":

    filtered_df = filtered_df[

        filtered_df["Category Name"]

        ==

        selected_category

    ]


st.divider()

#=========================================================
# KPI CALCULATIONS
#=========================================================


total_orders = len(filtered_df)


#---------------------------------------------------------

if "Sales" in filtered_df.columns:

    total_sales = round(

        filtered_df["Sales"].sum(),

        2

    )

else:

    total_sales = 0


#---------------------------------------------------------

if "Late_delivery_risk" in filtered_df.columns:

    total_late_orders = int(

        filtered_df["Late_delivery_risk"]

        .sum()

    )

else:

    total_late_orders = 0



#---------------------------------------------------------

if "Market" in filtered_df.columns:

    total_markets = (

        filtered_df["Market"]

        .nunique()

    )

else:

    total_markets = 0



#---------------------------------------------------------

if "Category Name" in filtered_df.columns:

    total_categories = (

        filtered_df["Category Name"]

        .nunique()

    )

else:

    total_categories = 0



#---------------------------------------------------------

if "Shipping Mode" in filtered_df.columns:

    total_shipping = (

        filtered_df["Shipping Mode"]

        .nunique()

    )

else:

    total_shipping = 0



#=========================================================
# DISPLAY KPIs
#=========================================================

st.subheader(
    "Live Supply Chain Metrics"
)


k1,k2,k3 = st.columns(3)


with k1:

    st.metric(

        "Total Orders",

        f"{total_orders:,}"

    )


with k2:

    st.metric(

        "Total Sales",

        f"${total_sales:,.2f}"

    )


with k3:

    st.metric(

        "Late Deliveries",

        f"{total_late_orders:,}"

    )



k4,k5,k6 = st.columns(3)


with k4:

    st.metric(

        "Markets",

        total_markets

    )


with k5:

    st.metric(

        "Categories",

        total_categories

    )


with k6:

    st.metric(

        "Shipping Modes",

        total_shipping

    )


st.divider()

#=========================================================
# ANALYTICS CENTER
#=========================================================

st.subheader(
    "Supply Chain Analytics Center"
)



tab1,tab2,tab3,tab4 = st.tabs(

    [

        "Sales Analytics",

        "Market Analytics",

        "Shipping Analytics",

        "Risk Analytics"

    ]

)



#=========================================================
# SALES ANALYTICS
#=========================================================


with tab1:

    if (

        "Category Name" in filtered_df.columns

        and

        "Sales" in filtered_df.columns

    ):


        category_sales = (

            filtered_df

            .groupby("Category Name")["Sales"]

            .sum()

            .reset_index()

            .sort_values(

                by="Sales",

                ascending=False

            )

        )


        fig = px.bar(

            category_sales,

            x="Category Name",

            y="Sales",

            color="Sales",

            title="Sales by Category"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )




#=========================================================
# MARKET ANALYSIS
#=========================================================


with tab2:


    if (

        "Market" in filtered_df.columns

        and

        "Sales" in filtered_df.columns

    ):


        market_sales = (

            filtered_df

            .groupby("Market")["Sales"]

            .sum()

            .reset_index()

        )


        fig = px.bar(

            market_sales,

            x="Market",

            y="Sales",

            color="Sales",

            title="Sales by Market"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



#=========================================================
# SHIPPING ANALYSIS
#=========================================================


with tab3:


    if "Shipping Mode" in filtered_df.columns:


        shipping = (

            filtered_df

            ["Shipping Mode"]

            .value_counts()

            .reset_index()

        )


        shipping.columns = [

            "Shipping Mode",

            "Orders"

        ]


        fig = px.pie(

            shipping,

            names="Shipping Mode",

            values="Orders",

            title="Shipping Mode Distribution"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



#=========================================================
# RISK ANALYSIS
#=========================================================


with tab4:


    if "Late_delivery_risk" in filtered_df.columns:


        risk = (

            filtered_df

            ["Late_delivery_risk"]

            .value_counts()

            .reset_index()

        )


        risk.columns = [

            "Risk",

            "Orders"

        ]


        fig = px.pie(

            risk,

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
# EXECUTIVE INSIGHTS
#=========================================================

st.subheader(
    "Executive Insights"
)



i1,i2 = st.columns(2)



#---------------------------------------------------------

with i1:


    if (

        "Market" in filtered_df.columns

        and

        "Sales" in filtered_df.columns

    ):


        highest_market = (

            filtered_df

            .groupby("Market")["Sales"]

            .sum()

            .idxmax()

        )


        st.success(

            f"Highest Revenue Market : {highest_market}"

        )



#---------------------------------------------------------

    if (

        "Category Name" in filtered_df.columns

        and

        "Sales" in filtered_df.columns

    ):


        highest_category = (

            filtered_df

            .groupby("Category Name")["Sales"]

            .sum()

            .idxmax()

        )


        st.success(

            f"Highest Revenue Category : {highest_category}"

        )




#---------------------------------------------------------

with i2:


    if total_orders > 0:


        average_sales = round(

            total_sales /

            total_orders,

            2

        )


        st.info(

            f"Average Sales Per Order : ${average_sales}"

        )



#---------------------------------------------------------

    if total_orders > 0:


        risk_percentage = round(

            (

                total_late_orders

                /

                total_orders

            )*100,

            2

        )


        st.info(

            f"Late Delivery Percentage : {risk_percentage}%"

        )



st.divider()


#=========================================================
# PAGE FOOTER
#=========================================================


st.caption(

    "Supply Chain Overview Dashboard | "

    "Dynamic • Interactive • Business Driven"

)
