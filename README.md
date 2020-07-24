## This repository is 3 step process that helps you in framing an ETL process from the field data. 

## Requirement: 

Our field team has compiled a database of all the mushrooms they have found in the wild on a specific day. The team has recorded the physical characteristics of the specimen found, its coordinates and the time. We want to load the dataset in the above url into a relational database as our team will want to run a number of queries on this dataset. 

Because our field team has very little time, some fields will need to be translated before loading into the database:

1. cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s 
3. cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y 
5. odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s 
8. gill-size: broad=b,narrow=n 
9. gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y 
14. stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y 
17. veil-color: brown=n,orange=o,white=w,yellow=y 
19. ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z 
20. spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y 
21. population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y 
22. habitat: grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d

We want you to create a relational database schema representing the data described, a script to clean, translate and load the data from the csv into the database, and write the queries our team will run:
-	How many different species of mushroom are there, if a species is identified by the attributes 1-20?
-	Does habitat and cap-color correlate?
-	Considering a specific geographical point, what colours should we be able to see in the 10 km around it?


## Operating System: 

Linux

## Framework Infrastructure : 

CLI, Mysql workbench

## Progamming Language : 

Python, Mysql

## Knowledge 

This is a data engineer excercise on the Extract, Transform and Load process  by creating a database with mysql and load the data into mysql and then perform the transformation on top it to validate the results with sql queries.

## Usage & Instrunctions to test :

once you sucesfully git clone the repository please follow the below steps

initialise the database from CLI using  sudo launchctl load -F com.oracle.oss.mysql.mysqld.plist

a.execute the db script in pycharm 

b.execute the etl script in the pycharm after ensuring the db is created Pleas be informed the data given is agaricus-lepiota.csv and the processed is trns-file.txt
that has the mapping done

c.execute the mysql scripts in mysql workbench to validate the requirment criteria
