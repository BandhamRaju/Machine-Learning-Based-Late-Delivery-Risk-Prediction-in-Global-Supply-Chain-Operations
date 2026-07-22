#=========================================================
# LATE DELIVERY RISK PREDICTION
#=========================================================

import streamlit as st
import pandas as pd
import joblib
import os


#=========================================================
# PAGE CONFIGURATION
#=========================================================

st.set_page_config(

    page_title="Late Delivery Risk Prediction",

    page_icon="🚚",

    layout="wide"

)


#=========================================================
# LOAD MODEL
#=========================================================

@st.cache_resource
def load_model():

    return joblib.load(

        os.path.join(
            "models",
            "random_forest.pkl"
        )

    )


#=========================================================
# LOAD PREPROCESSOR
#=========================================================

@st.cache_resource
def load_preprocessor():

    return joblib.load(

        os.path.join(
            "models",
            "preprocessor.pkl"
        )

    )


#=========================================================
# LOAD DATASET
#=========================================================

@st.cache_data
def load_data():

    return pd.read_csv(

        os.path.join(
            "data",
            "cleaned_supply_chain_dataset.csv"
        )

    )

#=========================================================
# AUTO FILL REMAINING FEATURES
#=========================================================

def get_default_values(df):

    return{


    #------------------------------
    # CATEGORICAL FEATURES
    #------------------------------

    "Type":
    df["Type"].mode()[0],

    "Customer City":
    df["Customer City"].mode()[0],

    "Customer Country":
    df["Customer Country"].mode()[0],

    "Customer State":
    df["Customer State"].mode()[0],

    "Department Name":
    df["Department Name"].mode()[0],

    "Order City":
    df["Order City"].mode()[0],

    "Order Country":
    df["Order Country"].mode()[0],

    "Order Region":
    df["Order Region"].mode()[0],

    "Order State":
    df["Order State"].mode()[0],


    #------------------------------
    # NUMERICAL FEATURES
    #------------------------------

    "Benefit per order":
    float(df["Benefit per order"].median()),

    "Category Id":
    int(df["Category Id"].median()),

    "Department Id":
    int(df["Department Id"].median()),

    "Latitude":
    float(df["Latitude"].mean()),

    "Longitude":
    float(df["Longitude"].mean()),

    "Order Item Discount":
    float(df["Order Item Discount"].median()),

    "Order Item Product Price":
    float(df["Order Item Product Price"].median()),

    "Order Item Profit Ratio":
    float(df["Order Item Profit Ratio"].median()),

    "Order Item Total":
    float(df["Order Item Total"].median()),

    "Order Profit Per Order":
    float(df["Order Profit Per Order"].median()),

    "Product Price":
    float(df["Product Price"].median()),

    "Sales per customer":
    float(df["Sales per customer"].median())

    }


#=========================================================
# LOAD FILES
#=========================================================

try:

    model = load_model()

    preprocessor = load_preprocessor()

    df = load_data()


except Exception as e:

    st.error(e)

    st.stop()


#=========================================================
# PAGE TITLE
#=========================================================

st.title("🚚 Late Delivery Risk Prediction")


st.markdown("""

### Business Question

> Will this order get delivered late?

""")


st.divider()


#=========================================================
# ORDER CONFIGURATION
#=========================================================

st.subheader(

    "Order Configuration"

)


col1,col2 = st.columns(2)


#---------------------------------------------------------
# SHIPPING MODE
#---------------------------------------------------------

with col1:

    shipping_mode = st.selectbox(

        "Shipping Mode",

        sorted(

            df["Shipping Mode"]

            .dropna()

            .unique()

        )

    )


#---------------------------------------------------------
# MARKET
#---------------------------------------------------------

with col2:

    market = st.selectbox(

        "Market",

        sorted(

            df["Market"]

            .dropna()

            .unique()

        )

    )


#---------------------------------------------------------
# CATEGORY NAME
#---------------------------------------------------------

with col1:

    category_name = st.selectbox(

        "Category Name",

        sorted(

            df["Category Name"]

            .dropna()

            .unique()

        )

    )


#---------------------------------------------------------
# CUSTOMER SEGMENT
#---------------------------------------------------------

with col2:

    customer_segment = st.selectbox(

        "Customer Segment",

        sorted(

            df["Customer Segment"]

            .dropna()

            .unique()

        )

    )


#---------------------------------------------------------
# SALES
#---------------------------------------------------------

with col1:

    sales = st.number_input(

        "Sales",

        min_value=1.0,

        value=500.0

    )


#---------------------------------------------------------
# QUANTITY
#---------------------------------------------------------

with col2:

    quantity = st.number_input(

        "Order Quantity",

        min_value=1,

        value=2

    )


#---------------------------------------------------------
# DISCOUNT RATE
#---------------------------------------------------------

with col1:

    discount_rate = st.number_input(

        "Discount Rate (%)",

        min_value=0.0,

        max_value=100.0,

        value=10.0

    )


#---------------------------------------------------------
# SHIPMENT DAYS
#---------------------------------------------------------

with col2:

    shipment_days = st.number_input(

        "Shipment Days",

        min_value=1,

        value=3

    )


st.divider()


#=========================================================
# PREDICTION
#=========================================================

if st.button(

    "Predict Delivery Risk",

    use_container_width=True

):


    try:

        #=================================================
        # USER INPUT FEATURES
        #=================================================

        user_input={

        "Sales":sales,

        "Order Item Quantity":
        quantity,

        "Order Item Discount Rate":
        discount_rate,

        "Days for shipment (scheduled)":
        shipment_days,

        "Category Name":
        category_name,

        "Customer Segment":
        customer_segment,

        "Shipping Mode":
        shipping_mode,

        "Market":
        market

        }


        #=================================================
        # AUTO FILL REMAINING FEATURES
        #=================================================

        default_values=get_default_values(df)


        #=================================================
        # MERGE FEATURES
        #=================================================

        full_input={

            **default_values,

            **user_input

        }


        #=================================================
        # CREATE DATAFRAME
        #=================================================

        input_df=pd.DataFrame(

            [full_input]

        )







        
        #=================================================
        # ARRANGE COLUMN ORDER
        #=================================================

        required_columns=[

        'Type',

        'Days for shipment (scheduled)',

        'Benefit per order',

        'Sales per customer',

        'Category Id',

        'Department Id',

        'Latitude',

        'Longitude',

        'Order Item Discount',

        'Order Item Discount Rate',

        'Order Item Product Price',

        'Order Item Profit Ratio',

        'Order Item Quantity',

        'Sales',

        'Order Item Total',

        'Order Profit Per Order',

        'Product Price',

        'Category Name',

        'Customer City',

        'Customer Country',

        'Customer Segment',

        'Customer State',

        'Department Name',

        'Market',

        'Order City',

        'Order Country',

        'Order Region',

        'Order State',

        'Shipping Mode'

        ]


        input_df=input_df[

            required_columns

        ]

        

        

        #-------------------------------------------------
        # DATA PREPROCESSING
        #-------------------------------------------------

        transformed_data = (

            preprocessor

            .transform(input_df)

        )


        #-------------------------------------------------
        # PREDICTION
        #-------------------------------------------------

        prediction = (

            model

            .predict(

                transformed_data

            )[0]

        )


        probability = (

            model

            .predict_proba(

                transformed_data

            )[0][1]

        ) * 100


        st.divider()


        #=================================================
        # RESULT
        #=================================================

        st.subheader(

            "Prediction Result"

        )


        if prediction == 1:

            st.error(

                "Late Delivery Risk Detected"

            )

        else:

            st.success(

                "No Late Delivery Risk"

            )


        st.metric(

            "Probability Score",

            f"{probability:.2f}%"

        )


        #=================================================
        # RISK CATEGORY
        #=================================================

        if probability >= 70:

            risk_level = "HIGH"


        elif probability >=50:

            risk_level = "MEDIUM"


        else:

            risk_level = "LOW"



        st.metric(

            "Risk Category",

            risk_level

        )


        #=================================================
        # CONFIDENCE SCORE
        #=================================================

        st.subheader(

            "Prediction Confidence"

        )


        st.progress(

            min(

                int(probability),

                100

            )

        )


        #=================================================
        # RECOMMENDATIONS
        #=================================================

        st.subheader(

            "Business Recommendation"

        )


        if probability >=70:


            st.warning("""

            • Prioritize Shipment.

            • Increase Delivery Monitoring.

            • Review Shipping Strategy.

            """)


        elif probability >=50:


            st.info("""

            • Monitor Shipment Progress.

            • Maintain Operational Checks.

            • Review Delivery Schedule.

            """)


        else:


            st.success("""

            • Current Strategy Appears Effective.

            • Standard Monitoring is Sufficient.

            """)



        #=================================================
        # MODEL INFORMATION
        #=================================================

        st.subheader(

            "Model Information"

        )


        st.info("""

        Model Used

        • Random Forest Classifier


        Features Used

        • 8 Selected Features


        Prediction Type

        • Binary Classification


        """)


    except Exception as e:


        st.error(

            f"Prediction Failed : {e}"

        )