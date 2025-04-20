import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("Business Case Data.xlsx")
superm = data[data['CHANNEL'] == 'Supermarket']
conv = data[data['CHANNEL'] == 'Convenience']
chan_s_b = superm['BRAND1_BIG_post']-superm['BRAND1_BIG_pre']
chan_s_m = superm['BRAND1_MEDIUM_post']-superm['BRAND1_MEDIUM_pre']
chan_c_b = conv['BRAND1_BIG_post']-conv['BRAND1_BIG_pre']
chan_c_m = conv['BRAND1_MEDIUM_post']-conv['BRAND1_MEDIUM_pre']
avg_sup_b = chan_s_b.mean()
avg_sup_m = chan_s_m.mean()
avg_conv_b = chan_c_b.mean()
avg_conv_m = chan_c_m.mean()
import plotly.express as px
mean_values = [avg_sup_b, avg_sup_m, avg_conv_b, avg_conv_m]
labels = ['Big-Supermarket', 'Medium-Supermarket', 'Big-Convenience', 'Medium-Convenience']
colors = ['blue', 'green', 'yellow', 'purple']

df_plot = pd.DataFrame({
    'Segment': labels,
    'Change': mean_values,
    'Color': colors
})

fig = px.bar(df_plot,
             x='Segment',
             y='Change',
             color='Segment',
             color_discrete_sequence=colors,
             title='Average change in Supermarkets and Convenience Stores',
             labels={'Change': 'Avg Change (Post - Pre)'}
            )

fig.update_layout(showlegend=False)
fig.show()
