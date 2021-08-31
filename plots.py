import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    st.header('Visualise data')
    # Remove deprecation warning.
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Subheader for scatter plot.
    st.subheader("Scatter plot")
    # Choosing x-axis values for scatter plots.
    features_list = st.multiselect("Select the x-axis values:", 
                                            ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
    # Create scatter plots.
    for feature in features_list:
        st.subheader(f"Scatter plot between {feature} and price")
        plt.figure(figsize = (12, 6))
        sns.scatterplot(x = feature, y = 'price', data = car_df)
        st.pyplot()

    # Add a multiselect widget to allow the user to select multiple visualisation.
    # Add a subheader in the sidebar with label "Visualisation Selector"
    st.subheader("Visualisation Selector")

    # Add a multiselect in the sidebar with label 'Select the charts or plots:'
    # and pass the remaining 3 plot types as a tuple i.e. ('Histogram', 'Box Plot', 'Correlation Heatmap').
    # Store the current value of this widget in a variable 'plot_types'.
    plot_types = st.multiselect("Select charts or plots:", ('Histogram', 'Box Plot', 'Correlation Heatmap'))

    # Display box plot using the 'matplotlib.pyplot' module and the 'st.pyplot()' function.
    if 'Histogram' in plot_types:
        st.subheader("Histogram")
        columns = st.selectbox("Select the column to create its histogram",
                                      ('carwidth', 'enginesize', 'horsepower'))
        # Note: Histogram is generally created for continous values not for discrete values.
        plt.figure(figsize = (12, 6))
        plt.title(f"Histogram for {columns}")
        plt.hist(car_df[columns], bins = 'sturges', edgecolor = 'black')
        st.pyplot()



    if 'Box Plot' in plot_types:
        st.subheader("Box plot")
        columns = st.selectbox("Select the column to create its Box plot",
                                      ('carwidth', 'enginesize', 'horsepower'))
        # Note: Histogram is generally created for continous values not for discrete values.
        plt.figure(figsize = (12, 6))
        plt.title(f"Box plot for {columns}")
        sns.boxplot(car_df[columns])
        st.pyplot()    


    if 'Correlation Heatmap' in plot_types:
        st.subheader('Correlation Heatmap')
        plt.figure(figsize=(10,5))
        sns.heatmap(car_df.corr(),annot=True)
        st.pyplot()    