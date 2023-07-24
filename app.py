import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

def main():
    st.title("Dynamic Plotly Visualizations with Streamlit")
    
    with st.sidebar:
        # Add user input elements (e.g., text input, slider, etc.)
        data_type = st.selectbox("Select Data Type", ["Scatter",
                                                      "Bar",
                                                      "Line", 
                                                      "Heatmap",
                                                      "Boxplot",
                                                      "Areachart",
                                                      "Violinplot",
                                                      "3DSurfaceplot",
                                                      "Sunburstplot",
                                                      "Chorpleth"])
        
    if data_type == "Scatter":
        show_scatter_plot()
    elif data_type == "Bar":
        show_bar_chart()
    elif data_type == "Line":
        show_line_chart()
    elif data_type == "Heatmap":
        show_heatmap()
    elif data_type == "Boxplot":
        show_boxplot()
    elif data_type == "Areachart":
        show_areachart()
    elif data_type == "Violinplot":
        show_Violinplot()
    elif data_type == "3DSurfaceplot":
        show_3DSurfaceplot()
    elif data_type == "Sunburstplot":
        show_Sunburstplot()
    elif data_type == "Chorpleth":
        show_Choropleth_Map()

# Define the functions for each type of plot
def show_scatter_plot():
    st.header("Scatter Plot")
    # Add user input elements if needed
    # For example, get x_data and y_data from user input
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 12, 8, 15, 11]
    
    # Create the Scatter Plot
    fig = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='markers'))
    st.plotly_chart(fig)


def show_bar_chart():
    st.header("Bar Chart")
    # Add user input elements if needed
    # For example, get categories and values from user input
    categories = ['A', 'B', 'C', 'D']
    values = [25, 40, 30, 55]
    
    # Create the Bar Chart
    fig = go.Figure(data=go.Bar(x=categories, y=values))
    st.plotly_chart(fig)


def show_line_chart():
    st.header("Line Chart")
    # Add user input elements if needed
    # For example, get x_data and y_data from user input
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 12, 8, 15, 11]
    
    # Create the Line Chart
    fig = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='lines+markers'))
    st.plotly_chart(fig)


def show_heatmap():
    st.header("Heatmap")
    # Add user input elements if needed
    # For example, get data from user input or a CSV file
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Create the Heatmap
    fig = go.Figure(data=go.Heatmap(z=data))
    st.plotly_chart(fig)
    
def show_boxplot():
    # Sample data
    data = [10, 15, 20, 25, 30, 35, 40, 45, 50]

    # Create the Box Plot
    fig = go.Figure(go.Box(y=data))
    st.plotly_chart(fig)

def show_areachart():
    # Sample data
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 12, 8, 15, 11]

    # Create the Area Chart
    fig = go.Figure(go.Scatter(x=x_data, y=y_data, fill='tozeroy'))
    st.plotly_chart(fig)
    
def show_Violinplot():
    # Sample data
    data = [10, 12, 8, 15, 11, 9, 13, 14, 7]

    # Create the Violin Plot
    fig = go.Figure(go.Violin(y=data))
    st.plotly_chart(fig)
    
def show_Violinplot():
    # Sample data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # Create the 3D Surface Plot
    fig = go.Figure(go.Surface(z=Z))
    st.plotly_chart(fig)
    
def show_3DSurfaceplot():
    # Sample data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # Create the 3D Surface Plot
    fig = go.Figure(go.Surface(z=Z))
    st.plotly_chart(fig)

def show_Sunburstplot():
    # Sample data
    labels = ["A", "B", "C", "D", "E", "F", "G", "H"]
    parents = ["", "A", "A", "B", "C", "C", "D", "D"]
    values = [16, 4, 8, 2, 6, 4, 2, 4]

    # Create the Sunburst Chart
    fig = go.Figure(go.Sunburst(labels=labels, parents=parents, values=values))
    st.plotly_chart(fig)

def show_Choropleth_Map():
    # Sample data
    data = [
        dict(type='choropleth', locations=['USA', 'Canada', 'Mexico'],
            locationmode='country names', z=[10, 20, 30], colorscale='Viridis')
    ]

    # Create the Choropleth Map
    fig = go.Figure(data=data)
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()

