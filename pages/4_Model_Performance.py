#=========================================================
# MODEL PERFORMANCE DASHBOARD
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

    page_title="Model Performance",

    page_icon="🤖",

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
# PAGE TITLE
#=========================================================

st.title("🤖 Model Performance Dashboard")


st.markdown(
"""

### Business Question

> Which Machine Learning model performs the best for predicting late deliveries?

"""
)


st.divider()
st.divider()


#=========================================================
# LOAD FILES
#=========================================================

df = load_data()

dataset_size = len(df)


#=========================================================
# MODEL INFORMATION
#=========================================================

k1,k2,k3=st.columns(3)


with k1:

    st.metric(

        "Models Compared",

        3

    )


with k2:

    st.metric(

        "Dataset Records",

        f"{dataset_size:,}"

    )


with k3:

    st.metric(

        "ML Features Used",

        28

    )


st.divider()

#=========================================================
# MODEL METRICS
#=========================================================


# NOTE:
# Replace these values later if exported
# from model_metrics.csv

try:

    metrics_df=pd.read_csv(

        os.path.join(
            "exports",
            "model_metrics.csv"
        )

    )


except:


    st.error(

        "model_metrics.csv not found."

    )

    st.stop()

st.subheader(
    "Model Comparison Metrics"
)



st.dataframe(

    metrics_df,

    use_container_width=True

)



st.divider()


#=========================================================
# MODEL COMPARISON GRAPH
#=========================================================


st.subheader(
    "Accuracy Comparison"
)



fig = px.bar(

    metrics_df,

    x="Model",

    y="Accuracy",

    color="Accuracy",

    text_auto=".4f"

)


fig.update_layout(

    height=500

)


st.plotly_chart(

    fig,

    use_container_width=True

)


st.divider()

#=========================================================
# ROC AUC COMPARISON
#=========================================================


st.subheader(
    "ROC-AUC Comparison"
)



fig = px.bar(

    metrics_df,

    x="Model",

    y="ROC AUC",

    color="ROC AUC",

    text_auto=".4f"

)


fig.update_layout(

    height=500

)


st.plotly_chart(

    fig,

    use_container_width=True

)


st.divider()

#=========================================================
# BEST MODEL
#=========================================================


st.subheader(
    "Best Performing Model"
)



try:


    best_model = (

        metrics_df

        .sort_values(

            by="Accuracy",

            ascending=False

        )

        .iloc[0]

    )


    st.success(

        f"""
        Best Performing Model

        Model :
        {best_model['Model']}


        Accuracy :
        {round(best_model['Accuracy'],4)}


        ROC AUC :
        {round(best_model['ROC AUC'],4)}

        """

        )

except:

    st.warning(

        "Model Metrics not available."

    )


st.divider()

#=========================================================
# BUSINESS INSIGHTS
#=========================================================


st.subheader(
    "Key Business Insights"
)


st.info(
    """

    • Machine Learning enables early identification of late delivery risks.

    • Comparing multiple models improves prediction reliability.

    • High performing models support better operational decisions.

    • Accurate risk prediction enables proactive supply chain management.

    • Early risk identification can help reduce delivery delays and improve customer satisfaction.
    """
)



st.divider()



#=========================================================
# FOOTER
#=========================================================


st.caption(
"Supply Chain Analytics | "

" Machine Learning | "

" Late Delivery Risk Prediction"
)

