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
rate = 0.05 / 12
nper = to_year * 12
pmt = month_contr
pv = 0  # No initial investment

# Calculate future value
future_value = npf.fv(rate, nper, pmt, pv)


st.header(f"FV in {to_year} is {future_value}", divider="gray")
