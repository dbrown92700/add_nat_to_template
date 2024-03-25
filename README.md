# Overview
Adds static NAT entries to a VPN feature template
# Install
Requires python 3.9 or later

Clone repository:
> git clone https://github.com/dbrown92700/configGroups

Recommend creating a virtual environment:
> python -m venv venv \
> source venv/bin/activate

Install python dependencies
> pip install -r requirements.txt

# Execute

- The script will copy an existing template and add the number of specified NATs 
to the end of the existing list.
- There must be at least 1 static NAT already configured in the template.
- The new template name and description will be prefixed with COPY_OF_
- Edit the varables at the beginning of main.py
  - You can find the templateId of the template you wish to copy in the URL of vManage by editing the template
  - The variable names will be appended with the sequence number


> ./main.py

or

> python main.py

# Author
Dave Brown, Cisco SDWAN TSA, davibrow@cisco.com

