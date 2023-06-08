I am going to explain my project in the next steps in very detail.

Tools used: Python,PostgreSQL,Amazon EC2(Ubuntu instance),RDS(postgres instance),Cron(scheduling),PowerBi

=== Phase-1(python scripting) ===

1. I have requested openweathermap api for weather data of 10 cities Ahmedabad,Kochi,Hyderabad,Delhi,Kolkata,Pune,Mumbai,Chennai,Bangalore and Jaipur.
2. I have converted this data into json format and then extracted required information like City Name, Temp, Humidity and Pressure.
3. Then I have connected to my postgresql database(locally) using psycopg2 library.
4. Utilized date and time functions and wrote a python script to write data into table in database.
5. The table columns would be like Date,Time,City,Temperature,Humidity and Pressure

=== Phase-2(scheduling with cron on my local machine) ===

1. After contionusly trying and improving phase-1, I moved to phase-2 that is to run the program for every 30 mins.(From here on Google became my very best friend)
2. I have installed ubuntu in my local machine with wsl and moved my python script from windows to ubuntu.
3. scheduled with cron to run every 30 minutes.
4. Hurray! Everything went fine. But, the real question i asked myself is how can I run this program if my system is turned off? Even if system is turned off, does postgresql db run some where? These kind of noob questions i have googled and after 1 day i got the soultion that is to run this entire set up in a cloud enivronment.
5. I figured out to complete this project I need two things one is a cloud database and the other one is a computer that runs 24/7,365 days a year(techincally speaking a server).

=== Phase-3(setting up a postgres instance on Amazon RDS) ===

1. After googling and youtube I have set up a cloud database in AWS(why aws? I'll clear this in the last point of phase-3).
2. connected to this database using python script(very easy in phase-1 we have connected to local db right? just changing database name and host I have connected to aws instance)
3. Executed python script. with pgadmin tool i have connected to database instance and qureied the table. Result? I got 10 rows that shows temperatures of cities. That means programm is running fine.
4. Tested again by shecudling with cron this time to run for every minute. Everything went well.
5. Now the only thing left is deploying code in cloud server so that I do not want to bother about keeping my system on.
6. Now we go to final phase but before going why AWS? Because after going through lot of articles learning aws is easy as a begineer compared to other clouds. Also AWS offers freetier for 12 months, that means I can use this service for my next project as well free of cost.

=== Final Phase ===

1. Intially i tried to go through serverless route that is running my python with AWS lambda and scheduling with cloudwatch. But, Lambda gave me atough time because to run psycogp2 library we need to create additional lamda layers.
2. I have tried everything followed lots of articles but running script on lambda did not work. Gave me a lot of errors. I gave up and explored other options that is to create a server.
3. This is just 2 steps, creating an instance and moving python script from local machine to this instance and scheduling with cron.
4. create an ubuntu instance and used filezilla to transfer python script from local machine to ubuntu instance. After transferring scheduled this script to run for every 30 mins, ofcourse by using cron.
5. Everything went well and after 8 days with the collected data here I am writing this post.


Adding snapshots of the process:
1. Running on AWS
![Aws-Ec2-1](https://github.com/manisharanthota/weatherapi/assets/116102968/38a817f6-8d3c-4778-afc9-0f230f93022b)
2. AWS server instance
![Aws-Ec2-2](https://github.com/manisharanthota/weatherapi/assets/116102968/379a8be9-bc0a-4502-a0f8-6a92882e6472)
3. snapshot of Datbase Instance
![Database-Instance](https://github.com/manisharanthota/weatherapi/assets/116102968/fe01430a-d34c-4f6f-8651-f68a03fb9b41)
4.cron job status
![cron-status](https://github.com/manisharanthota/weatherapi/assets/116102968/e4514289-ef6f-4a75-87d6-bd0fa7e25559)




