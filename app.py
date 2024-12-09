# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Startbucks Dataset Explorer", page_icon="☕")

# Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis"])

#Load the dataset
df = pd.read_csv('data/cleaned_starbucks.csv')

# Home Page
if page == "Home":
    st.write("👈 Use the sidebar to navigate between different sections.")
    st.title("☕ Starbucks Dataset Explorer")
    st.subheader("Welcome to our Starbucks dataset explorer app!")
    st.write("""
        Welcome to the Starbucks Dataset Explorer! This app lets you dive into the nutritional data of Starbucks beverages. 
        Explore the breakdown of calories, fat, sugar, and more, and visualize how different drinks compare across various categories.
        Use the sidebar to navigate through the sections and start exploring!
    """)

    st.image('https://1000logos.net/wp-content/uploads/2023/04/Starbucks-logo-500x281.png', caption="Starbucks' Siren Logo")



# Data Overview
elif page == "Data Overview":
    st.title("💚 Data Overview")

    # Subheader and introduction
    st.subheader("About the Data")
    st.write("""
        People have been drinking Starbucks since 1971, when it started in Seattle, 
        Washington. You may have thought about what you're going to order in the morning, 
        but have you ever considered the nutritional value of what you're drinking? 
    """)

    # Image with caption
    st.image(
        'https://starbucksjobs.de/assets/Uploads/4d7e59639c/002-de.jpg', 
        caption="Starbucks Motto: To inspire and nurture the human spirit - one person, one cup, and one neighborhood at a time."
    )

    # Dataset Display
    st.subheader("Quick Glance at the Data")

    # Data Dictionary
    if st.checkbox("Show Data Dictionary"):
        st.subheader("Data Dictionary")
        st.write("""
        - `Beverage_category` (Object): Type of beverage (e.g., coffee, tea, smoothie).  
        - `Beverage` (Object): Name of the drink (e.g., Caramel Macchiato, Green Tea Latte).  
        - `Beverage_prep` (Object): Preparation method (e.g., hot, cold, toppings).  
        - `Calories` (Int): Total calories in the beverage.  
        - `Total Fat (g)` (Float): Total fat content in grams.  
        - `Trans Fat (g)` (Float): Trans fat content in grams.  
        - `Saturated Fat (g)` (Float): Saturated fat content in grams.  
        - `Sodium (mg)` (Int): Sodium content in milligrams.  
        - `Total Carbohydrates (g)` (Float): Total carbohydrates, including sugars, in grams.  
        - `Cholesterol (mg)` (Int): Cholesterol content in milligrams.  
        - `Dietary Fibre (g)` (Float): Dietary fiber content in grams.  
        - `Sugars (g)` (Float): Sugar content in grams.  
        - `Protein (g)` (Float): Protein content in grams.  
        - `Vitamin A (% DV)` (Float): % Daily Value of Vitamin A.  
        - `Vitamin C (% DV)` (Float): % Daily Value of Vitamin C.  
        - `Calcium (% DV)` (Float): % Daily Value of Calcium.  
        - `Iron (% DV)` (Float): % Daily Value of Iron.  
        - `Caffeine (mg)` (Int): Caffeine content in milligrams.  
        """)

        st.write("""
        **Description**: This dataset provides a nutritional breakdown of Starbucks beverages.
        """)

    if st.checkbox("Show DataFrame"):
        st.dataframe(df)

    # Shape of Dataset
    if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Exploratory Data Analysis (EDA)
elif page == "Exploratory Data Analysis":
    st.title("📊 Exploratory Data Analysis (EDA)")
    # Display the .webp image
    st.image("images/databarista.webp", use_column_width=True)
    st.subheader("Be a Data Barista: Select Your Visualization Ingredients:")
    eda_type = st.multiselect("Visualization Options", ['Histograms', 'Box Plots', 'Scatterplots', 'Count Plots'])

    obj_cols = df.select_dtypes(include='object').columns.tolist()
    num_cols = df.select_dtypes(include='number').columns.tolist()

    if 'Histograms' in eda_type:
        st.subheader("Histograms - Visualizing Numerical Distributions")
        h_selected_col = st.selectbox("Select a numerical column for the histogram:", num_cols)
        if h_selected_col:
            chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
            if st.checkbox("Show by Category"):
                category_col = st.selectbox("Select a categorical column for coloring:", obj_cols)
                if category_col:
                    st.plotly_chart(px.histogram(df, x=h_selected_col, color=category_col, title=chart_title, barmode='overlay'))
            else:
                st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))

    if 'Box Plots' in eda_type:
        st.subheader("Box Plots - Visualizing Numerical Distributions")
        b_selected_col = st.selectbox("Select a numerical column for the box plot:", num_cols)
        if b_selected_col:
            chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
            category_col = st.selectbox("Select a categorical column for coloring:", obj_cols)
            if category_col:
                st.plotly_chart(px.box(df, x=category_col, y=b_selected_col, title=chart_title, color=category_col))

    if 'Scatterplots' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        selected_col_x = st.selectbox("Select x-axis variable:", num_cols)
        selected_col_y = st.selectbox("Select y-axis variable:", num_cols)
        if selected_col_x and selected_col_y:
            chart_title = f"{selected_col_x.title().replace('_', ' ')} vs. {selected_col_y.title().replace('_', ' ')}"
            category_col = st.selectbox("Select a categorical column for coloring:", obj_cols)
            if category_col:
                st.plotly_chart(px.scatter(df, x=selected_col_x, y=selected_col_y, color=category_col, title=chart_title))

    if 'Count Plots' in eda_type:
        st.subheader("Count Plots - Visualizing Categorical Distributions")
        selected_col = st.selectbox("Select a categorical variable:", obj_cols)
        if selected_col:
            chart_title = f'Distribution of {selected_col.title()}'
            st.plotly_chart(px.histogram(df, x=selected_col, color=selected_col, title=chart_title))


