import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load forecast data (update path if needed)
df = pd.read_csv('inventory_forecast_product_267_store_50.csv')

# Set page config
st.set_page_config(page_title="Sales Forecast Dashboard", layout="wide")

# Title
st.title('📈 Sales Forecast & Reorder Dashboard')
st.markdown("This dashboard shows the 30-day forecasted sales and recommended reorder quantities for **Product 267** at **Store 50** using ARIMA.")

# Show raw data checkbox
with st.expander("📊 Show Forecast Data"):
    st.dataframe(df)

# Key Metrics
st.subheader("🔹 Forecast Summary (Next 30 Days)")

col1, col2, col3 = st.columns(3)
col1.metric("Total Forecasted Units", f"{df['Forecast_Units'].sum():,}")
col2.metric("Avg. Daily Demand", f"{df['Forecast_Units'].mean():.1f}")
col3.metric("Total Reorder Units (20% buffer)", f"{df['Reorder_Quantity'].sum():,}")

# Line Chart
st.subheader("📆 Forecast vs. Reorder Quantity")

fig = px.line(df, x='Date', y=['Forecast_Units', 'Reorder_Quantity'],
              labels={'value': 'Units', 'variable': 'Metric'},
              title='Forecasted Sales and Reorder Plan (Product 267 @ Store 50)',
              markers=True)
fig.update_layout(xaxis_title="Date", yaxis_title="Units", legend_title="Legend")
st.plotly_chart(fig, use_container_width=True)

# Download button
st.subheader("⬇️ Download Forecast CSV")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Inventory Forecast CSV",
    data=csv,
    file_name='inventory_forecast_product_267_store_50.csv',
    mime='text/csv'
)

# 📸 Images Section (Add Here)
# 📸 Images Section
st.subheader("📸 Model and Forecast Insights")

col1, col2 = st.columns(2)

with col1:
    st.image("screenshot/dashboard.png", caption="Dashboard View", use_column_width=True)

with col2:
    st.image("screenshot/Screenshot 2025-05-25 173353.png", caption="Forecast Plot", use_column_width=True)


# Footer
st.markdown("---")
st.markdown("💡 *Model used: ARIMA (2,1,2). Reorder Quantity = Forecast + 20% Safety Stock.*")
st.caption("Built with ❤️ using Streamlit | Project by Akshaya M.")


import joblib

# Load the ARIMA model
model = joblib.load("model/arima_model.pkl")

# Predict using the model (example, update based on your needs)
forecast = model.forecast(steps=10)
st.write("📈 Forecast Results", forecast)
