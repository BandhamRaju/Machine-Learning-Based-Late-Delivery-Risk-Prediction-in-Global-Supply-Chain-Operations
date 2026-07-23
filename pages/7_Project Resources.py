#=========================================================
# PROJECT RESOURCES DASHBOARD
#=========================================================

import streamlit as st
import pandas as pd
import os

import gdown
#=========================================================
# PAGE CONFIGURATION
#=========================================================

st.set_page_config(

    page_title="Project Resources",

    page_icon="📁",

    layout="wide"

)


#=========================================================
# PAGE TITLE
#=========================================================

st.title("📁 Project Resources Center")

st.markdown("""

### Business Purpose

> Access, preview and download all datasets, models, reports, exported outputs and project resources from one place.

""")

st.divider()


#=========================================================
# DOWNLOAD FUNCTION
#=========================================================

def download_file(file_path, label):

    if os.path.exists(file_path):

        with open(file_path,"rb") as file:

            st.download_button(

                label=label,

                data=file,

                file_name=os.path.basename(file_path),

                mime="application/octet-stream"

            )

    else:

        st.warning(

            f"{os.path.basename(file_path)} not found."

        )


#=========================================================
# PROJECT INFORMATION
#=========================================================

st.subheader("Project Information")

c1,c2,c3 = st.columns(3)

with c1:

    st.metric(

        "Dataset Records",

        "180,519"

    )


with c2:

    st.metric(

        "ML Features",

        "28"

    )


with c3:

    st.metric(

        "Models Used",

        "3"

    )


st.info("""

Project Title   : Machine Learning Based Late Delivery Risk Prediction in Global Supply Chain Operations.


Target Variable : Late Delivery Risk


Prediction Type : Binary Classification


Domain          : Supply Chain Analytics

""")


st.divider()


#=========================================================
# DATASETS
#=========================================================

st.subheader("Dataset Files")

dataset_files = [

    "APL_Logistics.csv",

    "cleaned_supply_chain_dataset.csv"

]


for file_name in dataset_files:

    path = os.path.join(

        "data",

        file_name

    )

    if os.path.exists(path):

        st.write(f"• {file_name}")

        download_file(

            path,

            f"Download {file_name}"

        )


st.divider()


#=========================================================
# DATASET PREVIEW
#=========================================================

st.subheader("Dataset Preview")

try:

    df = pd.read_csv(

        os.path.join(

            "data",

            "cleaned_supply_chain_dataset.csv"

        )

    )

    st.dataframe(

        df.head(10),

        use_container_width=True

    )

except:

    st.warning(

        "Dataset could not be loaded."

    )


st.divider()


#=========================================================
# EXPORTED CSV FILES
#=========================================================

st.subheader("Exported Outputs")


export_files = [

    "feature_importance.csv",

    "high_risk_orders.csv",

    "kpi_summary.csv",

    "late_delivery_probability.csv",

    "model_comparison.csv",

    "model_metrics.csv",

    "risk_category_distribution.csv",

    "top15_features.csv"

]


for file_name in export_files:

    path = os.path.join(

        "exports",

        file_name

    )

    if os.path.exists(path):

        st.write(f"• {file_name}")

        download_file(

            path,

            f"Download {file_name}"

        )


st.divider()


#=========================================================
# MODEL FILES
#=========================================================

st.subheader("Machine Learning Models")


model_files = [

    "random_forest.pkl",

    "logistic_regression.pkl",

    "gradient_boosting.pkl"

]


for file_name in model_files:

    path = os.path.join(

        "models",

        file_name

    )

    if os.path.exists(path):

        st.write(f"• {file_name}")

        download_file(

            path,

            f"Download {file_name}"

        )


st.divider()


#=========================================================
# REPORTS
#=========================================================

st.subheader("Project Reports")


report_files = [

    "Executive_Summary.txt",

    "Project_Results.txt",

    "Final_Project_Report.pdf"

]


for file_name in report_files:

    path = os.path.join(

        "reports",

        file_name

    )

    if os.path.exists(path):

        st.write(f"• {file_name}")

        download_file(

            path,

            f"Download {file_name}"

        )


st.divider()


#=========================================================
# GRAPHS
#=========================================================

st.subheader("Project Graphs")


graphs_path = "graphs"


if os.path.exists(graphs_path):

    graph_files = os.listdir(

        graphs_path

    )

    for file_name in graph_files:

        path = os.path.join(

            graphs_path,

            file_name

        )

        st.write(f"• {file_name}")

        download_file(

            path,

            f"Download {file_name}"

        )


st.divider()


#=========================================================
# KPI SUMMARY PREVIEW
#=========================================================

st.subheader("KPI Summary")


try:

    kpi_df = pd.read_csv(

        os.path.join(

            "exports",

            "kpi_summary.csv"

        )

    )

    st.dataframe(

        kpi_df,

        use_container_width=True

    )

except:

    st.warning(

        "KPI Summary not available."

    )


st.divider()


#=========================================================
# MODEL METRICS PREVIEW
#=========================================================

st.subheader("Model Metrics")


try:

    metrics_df = pd.read_csv(

        os.path.join(

            "exports",

            "model_metrics.csv"

        )

    )

    st.dataframe(

        metrics_df,

        use_container_width=True

    )

except:

    st.warning(

        "Model Metrics not available."

    )


st.divider()


#=========================================================
# FOOTER
#=========================================================

st.caption(

    "Project Resources Center | "

    "Supply Chain Analytics | "

    "Late Delivery Risk Prediction"

)
