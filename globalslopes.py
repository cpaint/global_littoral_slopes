### Plotting global slope data from Athanasiou et al 2019
#Crystal Painter 5/25/23
import numpy as np
import pandas as pd
import matplotlib as plt
#import matplotlib.cm as cm
import plotly.express as px
import plotly

filename = 'nearshore_slopes.csv'
data = pd.read_csv(filename)

#_______________
#pdf of global data
# slope_limited = data.slope
# ceiling = 1
# slope_limited = data.slope.copy()
# slope_limited[slope_limited > ceiling] = ceiling
# data['slope_limited'] = slope_limited
# plt.pyplot.hist(slope_limited,bins = 30)


#clip out the nans
notnan = ~np.isnan(data.slope)
clip_data = data.loc[notnan,:].copy()
# clip_data["slope"].quantile(0.5)


#TODO 
# thin the data out for figures clip_data.sample()

#Global
fig = px.scatter_mapbox(clip_data, lat="Y", lon="X", hover_name="slope", hover_data=["slope", "dc"],
                        color='slope',range_color=[0,.1],
                          zoom=3, height=400, color_continuous_scale=px.colors.sequential.Viridis)
fig.update_layout(mapbox=dict(style="carto-positron")) 
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

#Taiwan
is_taiwan = (clip_data.Y <=25) & (clip_data.Y >=21) & (clip_data.X<=122) &(clip_data.X >=120)
taiwan_df = clip_data.loc[is_taiwan,:].copy()
fig = px.scatter_mapbox(taiwan_df, lat="Y", lon="X", hover_name="slope", hover_data=["slope", "dc"],
                        color='slope',range_color=[.001,.1],
                          zoom=3, height=800, color_continuous_scale=px.colors.sequential.Viridis)
# fig.update_layout(mapbox_style="mapbox-dark") #This one looks the nicest on the comp but not for a paper lit review
fig.update_layout(mapbox=dict(style="carto-positron")) # grayscale simple )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

#Japan
is_schwab = (clip_data.Y <= 26.8) & (clip_data.Y >= 25.5) & (clip_data.X <= 128.5) & (clip_data.X >= 128)
japan_df = clip_data.loc[is_schwab, :].copy()
fig = px.scatter_mapbox(japan_df, lat="Y", lon="X", hover_name="slope", hover_data=["slope", "dc"],
                        color='slope',range_color=[.001,.1],
                          zoom=3, height=800, color_continuous_scale=px.colors.sequential.Viridis)
# fig.update_layout(mapbox_style="mapbox-dark")
fig.update_layout(mapbox=dict(style="carto-positron")) # grayscale simple )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
#South China Sea
is_scs = (clip_data.Y <= 20.5) & (clip_data.Y >= 8) & (clip_data.X <= 119) & (clip_data.X >= 103.05)
scs_df = clip_data.loc[is_scs, :].copy()
fig = px.scatter_mapbox(scs_df, lat="Y", lon="X", hover_name="slope", hover_data=["slope", "dc"],
                        color='slope',range_color=[.001,.1],
                          zoom=3, height=800, color_continuous_scale=px.colors.sequential.Viridis)
# fig.update_layout(mapbox_style="mapbox-dark")
fig.update_layout(mapbox=dict(style="carto-positron")) # grayscale simple )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

#California
is_cali = (clip_data.Y <= 48) & (clip_data.Y >= 31) & (clip_data.X <= -116) & (clip_data.X >= -133)
cali_df = clip_data.loc[is_cali, :].copy()
fig = px.scatter_mapbox(cali_df, lat="Y", lon="X", hover_name="slope", hover_data=["slope", "dc"],
                        color='slope',range_color=[.001,.04],
                          zoom=3, height=800, color_continuous_scale=px.colors.sequential.Viridis)
# fig.update_layout(mapbox_style="mapbox-dark")
fig.update_layout(mapbox=dict(style="carto-positron")) # grayscale simple )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

#East Coast
is_east = (clip_data.Y <= 38) & (clip_data.Y >= 33) & (clip_data.X <= -75) & (clip_data.X >= -78)
east_df = clip_data.loc[is_east, :].copy()
fig = px.scatter_mapbox(east_df, lat="Y", lon="X", hover_name="slope", hover_data=["slope", "dc"],
                        color='slope',range_color=[.001,.1],
                          zoom=3, height=800, color_continuous_scale=px.colors.sequential.Viridis)
# fig.update_layout(mapbox_style="mapbox-dark")
fig.update_layout(mapbox=dict(style="carto-positron")) # grayscale simple )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

#Pendleton 
pen = cali_df.loc[(cali_df.X >-117.592)&(cali_df.X<-117.412)&(cali_df.Y>33.223)&(cali_df.Y<33.386)]
print(pen.slope.mean(),pen.dc.mean())
print(' ')









# for i in range(len(cali_df.Y)):
#     folium.CircleMarker([cali_df.Y.values[i], cali_df.X.values[i]], 
#                         color= plt.colors.rgb2hex(slope_color.to_rgba(cali_df.slope.values[i])),
#                         fill_color= plt.colors.rgb2hex(slope_color.to_rgba(cali_df.slope.values[i])),
#                         popup = f'Depth of closure: {cali_df.dc.values[i]},Slope:{cali_df.slope.values[i]},Lat: {cali_df.Y.values[i]}, Lon:{cali_df.X.values[i]}').add_to(map),


# for i in range(len(east_df.Y)):
#     folium.CircleMarker([east_df.Y.values[i], east_df.X.values[i]],
#                         color= plt.colors.rgb2hex(slope_color.to_rgba(east_df.slope.values[i])),
#                         fill_color= plt.colors.rgb2hex(slope_color.to_rgba(east_df.slope.values[i])),
#     popup = f'Depth of closure: {east_df.dc.values[i]}, Slope:{east_df.slope.values[i]}').add_to(map)

# map.save("nearshore_slopes.html")

# print(data)
# #X (lon),Y (lat),dc (depth of closure),slope,error_code
# norm = plt.colors.Normalize(vmin = .0001,vmax=.1)
# cmap = cm.winter
# slope_color  = cm.ScalarMappable(norm = norm, cmap = cmap)
