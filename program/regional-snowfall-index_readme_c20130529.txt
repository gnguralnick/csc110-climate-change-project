Readme file for the Regional Snowfall Index (RSI) and the Northeast Snowfall Impact Scale (NESIS) results files.

-------------------------------------------------------------------------
-------------------------------------------------------------------------

I. CONTENTS OF ftp://ftp.ncdc.noaa.gov/pub/data/surface-snow-products

     - regional-snowfall-index_readme_c20130529.txt (this file)
   
     - snowstorm-db_shapefile-readme_c20130529.txt

     - regional-snowfall-index_c20130529.csv

     - ne-snowfall-impact-scale_c20130529.csv

     - Snowfall Database shapefiles.  TAR file of the GZIP-compressed storm specific     	  shapefiles

-------------------------------------------------------------------------
-------------------------------------------------------------------------


II. RSI RESULTS

This file contains the RSI value for each snowstorm along with snowfall area and population information for that storm.  There is a seperate record for each storm.  The references are found at 'http://www.ncdc.noaa.gov/snow-and-ice/rsi/references'.

   REGION     ; NCDC Climate region
   START      ; start date of storm (year-month-day)
   END        ; end date of storm (year-month-day)
   RSI        ; raw Regional Snowfall Index value ( 0.000 � 35.000)
   CATEGORY   ; Regional Snowfall Index category (1 � 5)
   TERM1PCT   ;	percent of final RSI value from term 1 of RSI equation (see references)
   TERM2PCT   ; percent of final RSI value from term 2 of RSI equation (see references)
   TERM3PCT   ; percent of final RSI value from term 3 of RSI equation (see references)
   TERM4PCT   ;	percent of final RSI value from term 4 of RSI equation (see references)
   AREA0      ; area of snowfall for entire storm
   POP0       ; population for entire storm
   AREA1      ;	area of snowfall greater than the first region specific threshold (see                                        	           reference)
   POP1       ; population in an area with snowfall greater than the first region  	   	           specific threshold (see reference)
   AREA2      ; area of snowfall greater than the second region specific threshold (see                                       	           reference)
   POP2       ; population in an area with snowfall greater than the second region 	   	           specific threshold (see reference)
   AREA3      ;	area of snowfall greater than the third region specific threshold (see                                        	           reference)
   POP3       ; population in an area with snowfall greater than the third region 	  	           specific threshold (see reference)
   AREA4      ; area of snowfall greater than the fourth region specific threshold (see                                       	           reference)
   POP4       ; population in an area with snowfall greater than the fourth region 	 	           specific threshold (see reference)
   STORM_ID   ;	unique string for each storm � concatenation of starting and ending 	 	           dates
   REGION_CODE;	numeric code associated with region
   YEAR       ; year of storm
   MONTH      ; month of storm

-------------------------------------------------------------------------
-------------------------------------------------------------------------

III. NESIS RESULTS

This file contains the NESIS results for each storm.

   Rank    ; rank of this storm (1 = highest NESIS value)
   START   ; start date of storm (year-month-day)
   END     ; end date of storm (year-month-day)
   NESIS   ; raw Northeast Snowfall Impact Scale value ( 0.000 � 25.000)
   CATEGORY; Northeast Snowfall Impact Scale category (1 � 5)
