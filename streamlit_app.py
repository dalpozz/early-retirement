import math

import numpy_financial as npf
import streamlit as st
from er.utils import format_Mk, get_data

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title="Early Retirement dashboard",
    page_icon=":dollar:",  # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------

cfg = get_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
"""
# :earth_americas: ER dashboard

This website allows one to simulate how much money we can put asside with monthly investments.
"""

# Add some spacing
""
""


min_value = cfg["min_horizon"]
max_value = cfg["max_horizon"]

to_year = st.slider(
    "How many years do you have before retirment?",
    min_value=min_value,
    max_value=max_value,
    value=20,
)

min_contr = cfg["min_contribution"]
max_contr = cfg["max_contribution"]
avg_contr = cfg["avg_contribution"]

month_contr = st.slider(
    "How much can you save monthly?",
    min_value=min_contr,
    max_value=max_contr,
    value=avg_contr,
)

savings = st.number_input("Enter your current saving:", min_value=0, max_value=10000000, step=1000)

interest = st.slider(
    "Yearly return on investment (%)",
    min_value=1,
    max_value=10,
    value=4,
)

""
""
""

# Parameters
rate = interest / 100 / 12
nper = to_year * 12
pmt = -month_contr
pv = -savings

# Calculate future value
future_value = round(npf.fv(rate, nper, pmt, pv))


st.header(f"Retirement amount in {to_year} year is {format_Mk(future_value)}", divider="gray")

""
""
""

# st.header("Net worth over time", divider="gray")

# ""

# st.line_chart(
#     filtered_gdp_df,
#     x="Year",
#     y="GDP",
#     color="Country Code",
# )

# ""
# ""
