# gst-rate-finder-india
A tool to help Indian consumers check the latest GST rates and verify product prices after recent government changes.

# GST Rate Finder India 🇮🇳

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

An interactive web application built with Python and Streamlit to help Indian consumers understand the latest GST rate changes, check impacted items, and verify product prices.

**🚀 Live Demo:** [**https://your-streamlit-app-url.streamlit.app/**](https://your-streamlit-app-url.streamlit.app/)

---

### 💡 About The Project

As of October 2025, navigating changes in India's Goods and Services Tax (GST) can be challenging for the average person. This project provides a simple, fast, and user-friendly tool to bring clarity. It offers a searchable database of items with their old and new GST rates and includes an integrated calculator to ensure consumers are paying the correct price.

This tool is designed for public awareness and to make financial information more accessible.

### ✨ Features

* **Live Search:** Instantly filter through a comprehensive list of items and categories.
* **Clear Rate Comparison:** See the old and new GST rates side-by-side for easy understanding.
* **Integrated Price Calculator:** Enter the base price for any item to calculate its final cost with the new GST applied.
* **Responsive Design:** Works seamlessly on desktops, tablets, and mobile devices.
* **Constantly Updated:** The data can be easily updated in the `items.csv` file as new changes are announced.

### 🛠️ Technology Stack

* **Python:** The core programming language.
* **Streamlit:** For creating and serving the interactive web application.
* **Pandas:** For efficient data loading and manipulation.

---

### Local Development

To run this project on your local machine, follow these steps:

#### **Prerequisites**
* Python 3.8 or newer
* pip package manager

#### **Installation & Setup**

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/gst-rate-finder-india.git](https://github.com/your-username/gst-rate-finder-india.git)
    cd gst-rate-finder-india
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```
    Your browser should open with the application running locally!

### 🚀 Deployment

This app is perfect for deployment on **Streamlit Community Cloud** for free.

1.  Push your code (including `requirements.txt`) to your GitHub repository.
2.  Sign up or log in to [Streamlit Community Cloud](https://share.streamlit.io/).
3.  Click "New app" and select your repository.
4.  Ensure the main file path is set to `app.py`.
5.  Click "Deploy!" and your app will be live in minutes.

### 📊 Data Source

The GST data is compiled from public announcements by the GST Council of India and the Central Board of Indirect Taxes and Customs (CBIC).

**Disclaimer:** This tool is for informational purposes only. For legal and financial decisions, please consult official government sources.

### 📜 License

This project is distributed under the MIT License. See `LICENSE` for more information.
