---
tags:
    - Analytics Function
    - ChatGPT
---

# Natural Language Analytics and Visualization

We can generate datasets using ChatGPT prompts. Then we can combine use these datasets for visualization and analytics.

``` yaml title="ChatGPT Prompt"
What are the house price trends over last 10 years in Sunnyvale, CA? 
Only provide historically factual data and cite source of data. 
In response create a markdown table starting # (1)!
with "```" markdown and closing with "```". 
```

1. :bulb: Note that in the prompt "```" needs to be mentioned without enclosing quotes. We have used the enclosing quotes to ensure it renders as-is in our code block. You can also skip this part of the prompt if you do not want to copy-paste the markdown code for the table.

This generates a table of data and citing source of the data. Note that as you run this query a few times, the source of data and the values may vary. Asking for the source of the data along with the data ensures that the data is historically factual and not made up. You could even perform a sanity check by comparing the data with the source of data.

!!! note "ChatGPT Completion"

    | Year | Median House Price in Sunnyvale, CA |
    |------|------------------------------------|
    | 2011 | $756,000                           |
    | 2012 | $833,750                           |
    | 2013 | $940,000                           |
    | 2014 | $1,148,000                         |
    | 2015 | $1,360,000                         |
    | 2016 | $1,450,000                         |
    | 2017 | $1,555,000                         |
    | 2018 | $1,710,000                         |
    | 2019 | $1,730,000                         |
    | 2020 | $1,900,000                         |

    Source: Zillow Home Value Index. (n.d.). Sunnyvale home values. 
    Zillow. https://www.zillow.com/sunnyvale-ca/home-values/


Next we instruct ChatGPT within the same chat session to generate code for [vegalite charts](https://vega.github.io/vega-lite/). Vega-Lite is a high-level grammar of interactive graphics. It provides a concise, declarative JSON syntax to create an expressive range of visualizations for data analysis and presentation.

``` yaml title="ChatGPT Prompt"
Visualize this table data by generating code for vegalite charts 
using bar charts.
```

Here is the visualization for the code that ChatGPT generates.

``` vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "values": [
      {"Year": 2011, "Median House Price in Sunnyvale, CA": 756000},
      {"Year": 2012, "Median House Price in Sunnyvale, CA": 833750},
      {"Year": 2013, "Median House Price in Sunnyvale, CA": 940000},
      {"Year": 2014, "Median House Price in Sunnyvale, CA": 1148000},
      {"Year": 2015, "Median House Price in Sunnyvale, CA": 1360000},
      {"Year": 2016, "Median House Price in Sunnyvale, CA": 1450000},
      {"Year": 2017, "Median House Price in Sunnyvale, CA": 1555000},
      {"Year": 2018, "Median House Price in Sunnyvale, CA": 1710000},
      {"Year": 2019, "Median House Price in Sunnyvale, CA": 1730000},
      {"Year": 2020, "Median House Price in Sunnyvale, CA": 1900000}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "y": {"field": "Year", "type": "nominal"},
    "x": {"field": "Median House Price in Sunnyvale, CA", "type": "quantitative"},
    "tooltip": [
      {"field": "Year", "type": "nominal"},
      {"field": "Median House Price in Sunnyvale, CA", "type": "quantitative", "format": "$,.0f"}
    ],
    "color": {"field": "Median House Price in Sunnyvale, CA", "type": "quantitative", "scale": {"scheme": "bluepurple"}}
  },
  "config": {
    "axis": {
      "labelFontSize": 14,
      "titleFontSize": 16,
      "labelFontWeight": "bold"
    }
  }
}
```

As you can see vegalite is an awesome library for visualizing data and the chart is interactive. You can hover over the bars to see the values. ChatGPT takes care of generating styled charts with gradients, colors, and legends, without any need for us to provide these instructions as part of the prompt.

In summary, you can now use natural language to query world knowledge learnt by a large language model like ChatGPT and generate visualizations and analytics. No databases, no SQL, no programming, no coding, no data engineering, no JavaScript knowledge required!




