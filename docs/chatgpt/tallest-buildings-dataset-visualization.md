
# Tallest Buildings Dataset Visualization

Let us pull a dataset of tallest buildings.

``` yaml title="ChatGPT Prompt"
Create a table of tallest buildings in the world with 
various attributes like height, year built, location, and others. 
Draw the table in markdown enclosing in "```".
```

Generates this table with extra attributes including the ones specified in the prompt.

!!! info "ChatGPT Completion"
  
    | Rank | Building Name            | Height (m) | Height (ft) | Year Completed | City              | Country           | Primary Use             |
    |------|-------------------------|------------|-------------|----------------|-------------------|-------------------|-------------------------|
    | 1    | Burj Khalifa            | 828        | 2,716       | 2010           | Dubai             | United Arab Emirates | Mixed Use               |
    | 2    | Shanghai Tower          | 632        | 2,073       | 2015           | Shanghai          | China             | Office                  |
    | 3    | Abraj Al Bait Clock Tower | 601        | 1,971       | 2012           | Mecca             | Saudi Arabia      | Mixed Use               |
    | 4    | Ping An Finance Center   | 599        | 1,965       | 2017           | Shenzhen          | China             | Office                  |
    | 5    | Lotte World Tower        | 555        | 1,819       | 2017           | Seoul             | South Korea       | Mixed Use               |
    | 6    | One World Trade Center   | 541        | 1,776       | 2014           | New York City     | United States     | Office                  |
    | 7    | Guangzhou CTF Finance Centre | 530        | 1,739       | 2016           | Guangzhou         | China             | Hotel/Residential/Office |
    | 8    | Tianjin CTF Finance Centre | 530        | 1,739       | 2019           | Tianjin           | China             | Hotel/Office            |
    | 9    | CITIC Tower              | 528        | 1,732       | 2018           | Beijing           | China             | Office                  |
    | 10   | TAIPEI 101               | 508        | 1,667       | 2004           | Taipei            | Taiwan            | Office                  |

Now we define a prompt for visualizing the table using vegalite charts.

``` yaml title="ChatGPT Prompt"
Visualize this table choosing appropriate vegalite chart 
and generate the code for the visualization.
```

The generated code handles mixed data types intelligently and is able to identify appropriate chart design based on given attributes and types.

``` vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "values": [
      {"Building Name": "Burj Khalifa", "Height (m)": 828, "Height (ft)": 2716, "Year Completed": 2010, "City": "Dubai", "Country": "United Arab Emirates", "Primary Use": "Mixed Use"},
      {"Building Name": "Shanghai Tower", "Height (m)": 632, "Height (ft)": 2073, "Year Completed": 2015, "City": "Shanghai", "Country": "China", "Primary Use": "Office"},
      {"Building Name": "Abraj Al Bait Clock Tower", "Height (m)": 601, "Height (ft)": 1971, "Year Completed": 2012, "City": "Mecca", "Country": "Saudi Arabia", "Primary Use": "Mixed Use"},
      {"Building Name": "Ping An Finance Center", "Height (m)": 599, "Height (ft)": 1965, "Year Completed": 2017, "City": "Shenzhen", "Country": "China", "Primary Use": "Office"},
      {"Building Name": "Lotte World Tower", "Height (m)": 555, "Height (ft)": 1819, "Year Completed": 2017, "City": "Seoul", "Country": "South Korea", "Primary Use": "Mixed Use"},
      {"Building Name": "One World Trade Center", "Height (m)": 541, "Height (ft)": 1776, "Year Completed": 2014, "City": "New York City", "Country": "United States", "Primary Use": "Office"},
      {"Building Name": "Guangzhou CTF Finance Centre", "Height (m)": 530, "Height (ft)": 1739, "Year Completed": 2016, "City": "Guangzhou", "Country": "China", "Primary Use": "Hotel/Residential/Office"},
      {"Building Name": "Tianjin CTF Finance Centre", "Height (m)": 530, "Height (ft)": 1739, "Year Completed": 2019, "City": "Tianjin", "Country": "China", "Primary Use": "Hotel/Office"},
      {"Building Name": "CITIC Tower", "Height (m)": 528, "Height (ft)": 1732, "Year Completed": 2018, "City": "Beijing", "Country": "China", "Primary Use": "Office"},
      {"Building Name": "TAIPEI 101", "Height (m)": 508, "Height (ft)": 1667, "Year Completed": 2004, "City": "Taipei", "Country": "Taiwan", "Primary Use": "Office"}
    ]
  },
  "mark": "bar",
  "encoding": {
    "y": {
      "field": "Building Name",
      "type": "nominal",
      "sort": {"field": "Height (m)", "order": "descending"}
    },
    "x": {"field": "Height (m)", "type": "quantitative"},
    "color": {
      "field": "Primary Use",
      "type": "nominal",
      "scale": {
        "range": ["#1f77b4",
                "#ff7f0e",
                "#2ca02c",
                "#d62728",
                "#9467bd",
                "#8c564b",
                "#e377c2",
                "#7f7f7f",
                "#bcbd22",
                "#17becf"
            ]
            },
            "tooltip": [
            {"field": "Building Name", "type": "nominal"},
            {"field": "Height (m)", "type": "quantitative"},
            {"field": "Year Completed", "type": "ordinal"},
            {"field": "City", "type": "nominal"},
            {"field": "Country", "type": "nominal"},
            {"field": "Primary Use", "type": "nominal"}
            ]
},
"config": {
"view": {"continuousHeight": 400, "continuousWidth": 600}
}
}
}
```