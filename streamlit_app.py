import math

import numpy_financial as npf
import streamlit as st
from er.utils import get_data

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title="Early Retirement dashboard",
    page_icon=":earth_americas:",  # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------

cfg = get_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
"""
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
"""

# Add some spacing
""
""


min_value = cfg["min_horizon"]
max_value = cfg["max_horizon"]

from_year, to_year = st.slider(
    "How many years do you have before retirment?",
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value],
)

min_contr = cfg["min_contribution"]
max_contr = cfg["max_contribution"]


""
""
""


st.header("Net worth over time", divider="gray")

""

# st.line_chart(
#     filtered_gdp_df,
#     x="Year",
#     y="GDP",
#     color="Country Code",
# )

""
""


# Parameters
rate = 0.05  # 5% annual interest rate
nper = 10  # Number of years
pmt = 1000  # Annual payment
pv = 0  # No initial investment

# Calculate future value
future_value = npf.fv(rate, nper, pmt, pv)


st.header(f"FV in {to_year} is {future_value}", divider="gray")
