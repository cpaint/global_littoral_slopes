"Global distribution of nearshore slopes"

date of publication: 30/04/2019

Institutes: Deltares/TU Twente

Contributors:
Panagiotis Athanasiou
Ap van Dongeren 
Alessio Giardino
Michalis Vousdoukas
Sandra Gaytan Aguilar
Roshanka Ranasinghe

Global nearshore slope estimations using an interpolated MERIT+GEBCO merged dataset with the Open Street Maps (OSM) coastline as MSL. 
The slope was calculated from elevation profiles that were created by transects perpendicular to the OSM coastline, positioned every 1 km in the alongshore direction.
The depths of closure that were used for the slope estimation are also provided.

X -->			Longitude (WGS84)
				Given as decimal degrees

Y -->			Latitude (WGS84)
				Given as decimal degrees			

dc -->			Depth of closure  estimated at an offshore location according to Nicholls (1998) formula using the wave time series
				from Vousdoukas et al. 2018 reanalysis
				Given as positive depth value (meters)
			
slope --> 		Nearshore slope calculated as the Depth of Closure (dc) devided by the horizontal length from the dc to the shoreline (MSL=0)
				Given as tan(beta)
			

error_code --> 	Error or Warning code from the calculation:
				0: No errors or warnings
				1: Error- Number of cross-shore underwater points not enough for analysis
				2: Warning - DoC deeper that most deep offshore point (used that one as DoC)
				3: Error - Shoreline point not found
				4: Error - DoC point not found
				5: Warning - Negative calculated  slope 
				6: Warning - Really steep slope (step) close to MSL
				7: Error - No DoC estimation available
				8: Warning 1 and 6
