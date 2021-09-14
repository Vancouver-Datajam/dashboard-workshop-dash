import pandas as pd
import plotly.express as px

def graph_region(region_df, graph_type: str, dimension1: str, dimension2: str) -> None:
    """
    Parameters
    ----------
        region_df: (dataframe object) reshaped data frame object with mortage, delinquency and population data
        graph_type: (string) "box", "violin", "scatter", "line"
        dimension1: (str) one of 'Time' or 'Geography'
        dimension2: (str) one of 'AverageMortgageAmount', 'AverageMortgageAmount' or 'PopulationSize'
        
    Returns:
    --------
        None
    """
    
    plot_dict = {'box': px.box,'violin': px.violin, 'scatter': px.scatter, 'line':px.line}
        
    try:
        # Initialize function
        fig = plot_dict[graph_type](region_df, 
                                    x=dimension1, 
                                    y=dimension2, 
                                    color = "Geography",
                                   hover_name = "Time")
        # Format figure 
        title_string = f'Chart: {graph_type} plot of {dimension1} and {dimension2} by Geography'
        fig.update_layout(title = title_string)
        fig.update_xaxes(tickangle=-45)
        fig.show()
    
    except KeyError:
        print("Key not found. Make sure that 'graph_type' is in ['box','violin', 'scatter', 'line']")
    except ValueError:
        print("Dimension is not valid. dimension1 is one of 'Time' or 'Geography'")
        print("dimension2 is one of 'AverageMortgageAmount', 'DelinquencyRate', 'PopulationSize'")
        
        
if __name__ == '__main__':  
    
    # Read the data into a dataframe 
    url = 'https://raw.githubusercontent.com/Vancouver-Datajam/dashboard-workshop-dash/main/data/delinquency_mortgage_population_2021_2020.csv'
    data_pop_del_mort_df = pd.read_csv(url, index_col=0)
    
    # See the first few rows
    display(data_pop_del_mort_df.head(10))
    
    # Visualize
    graph_region(data_pop_del_mort_df, 'line', "Time", "AverageMortgageAmount")
    graph_region(data_pop_del_mort_df, 'box', "Geography", "AverageMortgageAmount")
    graph_region(data_pop_del_mort_df, 'scatter', "AverageMortgageAmount", "DelinquencyRate")