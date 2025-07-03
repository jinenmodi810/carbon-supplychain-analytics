import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px

# -------------------------------
# Set up Streamlit page with modern layout
# -------------------------------
st.set_page_config(
    page_title="🌍 Carbon Emissions Dashboard",
    page_icon="🌿",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #F5F5F5;
    }
    .stDataFrame {
        background-color: #1E1E1E;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌿 Carbon Emissions Dashboard")
st.markdown(
    """
    <p style="font-size:18px; color:#DDDDDD;">
        Visualizing supplier-level carbon emissions and sustainability performance.
    </p>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Connect to Snowflake
# -------------------------------
conn = snowflake.connector.connect(
    user="JMODI6",
    password="Kaiwalmodi810@",
    account="QKXVORB-YVB74511",
    warehouse="TRANSFORMING",
    database="RAW",
    schema="SUPPLY_CHAIN",
    role="ACCOUNTADMIN"
)

# -------------------------------
# Query the mart
# -------------------------------
query = """
SELECT
    SUPPLIER_ID,
    SUPPLIER_NAME,
    SUPPLIER_COUNTRY,
    SUSTAINABILITY_RATING,
    TOTAL_SHIPMENTS,
    TOTAL_CO2_GRAMS,
    AVG_CO2_GRAMS
FROM FCT_SUPPLIER_EMISSIONS
ORDER BY TOTAL_CO2_GRAMS DESC
"""

df = pd.read_sql(query, conn)

# -------------------------------
# Metrics - custom styled block
# -------------------------------
total_shipments = df["TOTAL_SHIPMENTS"].sum()
total_co2 = df["TOTAL_CO2_GRAMS"].sum()
avg_co2 = df["AVG_CO2_GRAMS"].mean()

st.markdown(
    f"""
    <div style="display: flex; justify-content: space-around; padding: 20px 0;">
        <div style="background-color:#1E1E1E; padding:20px; border-radius:10px; width:30%;">
            <h3 style="color:#00FFAA; text-align:center;">🚚 Total Shipments</h3>
            <p style="font-size:32px; text-align:center; color:white;">{total_shipments:,}</p>
        </div>
        <div style="background-color:#1E1E1E; padding:20px; border-radius:10px; width:30%;">
            <h3 style="color:#00FFAA; text-align:center;">🌍 Total CO2 Emissions (g)</h3>
            <p style="font-size:32px; text-align:center; color:white;">{total_co2:,.0f}</p>
        </div>
        <div style="background-color:#1E1E1E; padding:20px; border-radius:10px; width:30%;">
            <h3 style="color:#00FFAA; text-align:center;">⚖️ Avg CO2 per Shipment (g)</h3>
            <p style="font-size:32px; text-align:center; color:white;">{avg_co2:,.0f}</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------
# Bar chart
# -------------------------------
st.subheader("📊 CO2 Emissions by Supplier")

fig = px.bar(
    df,
    x="SUPPLIER_NAME",
    y="TOTAL_CO2_GRAMS",
    color="SUSTAINABILITY_RATING",
    color_discrete_sequence=px.colors.qualitative.Vivid,
    template="plotly_dark",
    title="Total CO2 Emissions by Supplier"
)
fig.update_layout(
    plot_bgcolor="#121212",
    paper_bgcolor="#121212",
    font=dict(color="#F5F5F5"),
    xaxis=dict(title="Supplier Name", color="#F5F5F5"),
    yaxis=dict(title="Total CO2 (g)", color="#F5F5F5")
)
st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Data preview
# -------------------------------
st.subheader("🗂️ Supplier Emissions Data Preview")

st.dataframe(df.style.highlight_max(
    axis=0,
    subset=["TOTAL_CO2_GRAMS"],
    color="#00FFAA"
))

# -------------------------------
# Close connection
# -------------------------------
conn.close()