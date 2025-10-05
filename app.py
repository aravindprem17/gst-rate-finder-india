import streamlit as st
import pandas as pd

# --- Page Configuration (must be the first Streamlit command) ---
# Sets the title and icon that appear in the browser tab.
st.set_page_config(
    page_title="GST Rate Finder India",
    page_icon="🇮🇳",
    layout="wide"
)

# --- Data Loading and Caching ---
# @st.cache_data ensures that the data is loaded only once, making the app faster.
@st.cache_data
def load_data(file_path):
    """Loads the GST item data from the specified CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file {file_path} was not found. Please make sure it's in the correct directory.")
        return None

# Load the data from the 'data' subfolder
gst_data = load_data('data/items.csv')

# --- Main Application UI ---

# Header Section
st.title("🇮🇳 GST Rate Finder India")
st.markdown("Your guide to understanding recent changes in the Goods and Services Tax. Search for an item to see its updated rate and calculate the final price.")

# Search bar
search_term = st.text_input(
    "Search for an item or category (e.g., 'Curd', 'Electronics', 'Lassi')",
    placeholder="Type here to search..."
).lower()

st.markdown("---") # Visual separator

# --- Logic for Filtering and Displaying Data ---

if gst_data is not None:
    # Filter the dataframe based on the search term
    if search_term:
        results_df = gst_data[
            gst_data['itemName'].str.lower().str.contains(search_term) |
            gst_data['category'].str.lower().str.contains(search_term)
        ]
    else:
        # Show all data if search is empty
        results_df = gst_data

    # Display search results or a message if no results are found
    if results_df.empty:
        st.warning("No items found matching your search term. Please try again.")
    else:
        st.subheader(f"Found {len(results_df)} matching items")

        # Display each item using Streamlit's layout features
        for index, row in results_df.iterrows():
            # Use an expander to keep the UI clean
            with st.expander(f"{row['itemName']} ({row['category']})"):
                col1, col2 = st.columns([2, 2]) # Create two columns

                with col1:
                    st.markdown(f"**Previous GST Rate:** `{row['oldRate']}%`")
                    st.markdown(f"**New GST Rate:** `{row['newRate']}%`")
                    if pd.notna(row['remarks']) and row['remarks']:
                        st.info(f"**Note:** {row['remarks']}")

                with col2:
                    # Integrated Price Calculator
                    st.markdown("**Price Calculator**")
                    base_price = st.number_input(
                        "Enter Base Price (₹)",
                        min_value=0.01,
                        step=10.0,
                        format="%.2f",
                        key=f"price_{index}" # Unique key for each number input
                    )
                    
                    if base_price > 0:
                        final_price = base_price * (1 + row['newRate'] / 100)
                        st.success(f"Final Price (incl. GST): **₹{final_price:,.2f}**")

# --- Footer ---
st.markdown("---")
st.caption("Disclaimer: This tool is for informational purposes only. Data is based on public announcements from the GST Council. Always verify with official sources.")
