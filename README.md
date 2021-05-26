## email-approved-sender

This is a repository for OCI sample code to add an email approved sender. Both solutions share the same "config" file 

- Add multiple approved senders from a file createsenderfile.py The program, reads a "file.txt" or "file.csv" containing a list of email addresses. For each email address in the file, an approved sender address is configured in OCI tenancy's region and compartment.  

- Add a single approved sender by using createsenderwithemail.py and defining the approved sender address to be configured in the OCI tenancy's region and compartment.


## Step-by-step guide

1. Clone the GitHub.
```
https://github.com/igfasouza/email-approved-sender.git
```

2. Update the de "config" with your specific details

For more details on the config file parameters and where to find the values, refer to the [technical documentation](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm).

3. Update or create the "email_file.csv" with the emails that you want to be added as an approved sender

3. Run the Python code.
```
python3 createsenderfile.py
```

4. The second example "createsenderemail.py" adds one email and expects an email as a parameter. Replace "user1@test.com" with the email that you want to add.
```
python3 createsenderemail.py user1@test.com
```

## Rest API

the folder "restAPI" contains the same examples but using the REST API. 

