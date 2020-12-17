# DistributedSystems
Repository for a Distributed systems class.

**Hands-on class 1 - EC2**
--------------
Web application written in Python using Flask. FlaskPlot displays plots of mathematical functions submitted by users.
The application also shows the number of functions plotted until now and the last plotted function at the end of the page.

**Contents**
* `flaskplot/`: Python code to run the web app.
* `ec2/`: The `flaskplot.service` file contains a script to automatically run the web app at the instance start-up. This is done through a systemd service. This file needs to be save in the path `/etc/systemd/system/flaskplot.service` on the EC2 instance.

**Run the web app**
Run the web app locally.
* Run `./run.sh`.
* Go to your localhost page.

This application needs to be manually deployed on an AWS EC2 instance.


**Hands-on class 2 - Ansible (static inventory)**
--------------
Web application written in Python using Flask. PhotoGallery displays some pictures on a web page. At the moment the pictures URL are hard-coded on the web server code (but it's just a demo, they'll be retrived as S3 items in a bucket in the next version).

**Contents**
* `photogallery_v1/`: Python code to run the web app.
* `photogallery_ansible/`: Ansible playbook and inventory.

**Run the web app**
This application can be deployed on AWS using Ansible to automate the process. At the moment the a static in inventory is being used.


**Hands-on class 3 - S3, Dynamo, Ansible (dynamic inventory)**
--------------
Web application written in Python using Flask. PhotoGallery displays some pictures on a web page. Pictures are downloaded from an S3 bucket. Users can also upload pictures, and give them a title and some tags. These pieces of information are stored as key-value pairs in a AWS Dynamo instance.

**Contents**
* `photogallery_v4/`: Python code to run the web app.
* `ansible/`: Ansible playbook and inventory.

**Run the web app**
This application can be deployed on AWS using Ansible (with dynamic inventory) to automate the process.


**Hands-on class 4 - SQS, Lambda, Terraform**
--------------
Examples for AWS SQS, AWS Lambda and Terraform.

**Contents**
* `terraform/`: Terraform example to start an EC2 instance.
* `sqs/`: Contains two Python scripts to put and get messages from an SQS queue.
* `lambda/sqss3/`: Lambda function that reads messages from a SQS queue and save the message content ad a file on an S3 bucket. Messagges are sent to the SQS queue from the `producer.py` code. The Lambda function is deployed using Terraform.
