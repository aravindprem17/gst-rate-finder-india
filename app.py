import streamlit as st
import pandas as pd

# --- Page Configuration (must be the first Streamlit command) ---
st.set_page_config(
    page_title="GST Rate Finder India",
    page_icon="🇮🇳",
    layout="centered"
)

# --- Data Loading (with caching for performance) ---
@st.cache_data
def load_data():
    """Loads the GST item data from the CSV file."""
    df = pd.read_csv('data/items.csv')
    return df

gst_data = load_data()

# --- App UI ---
st.title("🇮🇳 GST Rate Finder")
st.markdown("A tool to help consumers check the latest GST rates on items in India.")

# --- Search Functionality ---
search_term = st.text_input(
    "Search for an item or category",
    placeholder="e.g., Curd, Electronics, Lassi"
).lower()

# --- Filtering and Displaying Data ---
if search_term:
    # Filter the dataframe based on the search term
    results_df = gst_data[
        gst_data['itemName'].str.lower().str.contains(search_term) |
        gst_data['category'].str.lower().str.contains(search_term)
    ]
else:
    # Show all data if search is empty
    results_df = gst_data

st.subheader("Search Results")

if results_df.empty:
    st.warning("No items found. Please try another search term.")
else:
    # Display each item as a card with a calculator
    for index, row in results_df.iterrows():
        st.markdown("---")
        col1, col2 = st.columns([3, 2]) # Create columns for layout

        with col1:
            st.markdown(f"#### {row['itemName']}")
            st.caption(f"Category: {row['category']}")
            st.markdown(f"Old GST: **{row['oldRate']}%** → New GST: **{row['newRate']}%**")

        with col2:
            base_price = st.number_input(
                "Enter Base Price (₹)",
                min_value=0.0,
                format="%.2f",
                key=f"price_{index}" # Unique key for each input box
            )
            if base_price > 0:
                final_price = base_price * (1 + row['newRate'] / 100)
                st.success(f"Final Price: **₹{final_price:,.2f}**")

# --- Footer ---
st.markdown("---")
st.info("**Disclaimer:** This tool is for informational purposes only. Data is based on public announcements from the GST Council.")
