# Linode-instance-price-monitoring-robot
A robot that monitors the current price of a provisioned Linode instance, and sends email alert to the appropriate personnels whenever the price exceeds their budget 

__Note__

The first version of this code uses Heroku Dynamo and a custom python module for scheduling jobs. However since Heroku services are no longer free at the moment I decided to integrate 
Github actions to this repository for running the robot to keep monitoring for changes in the dynamic website containing resources of Linode services and their price tag
