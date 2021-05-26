import oci
from oci.config import from_file

# Create a default config using DEFAULT profile in default location Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
try:
    config = from_file("./config")
except oci.exceptions.ConfigFileNotFound as e:
    config = from_file()


# Initialize service client with default config file
email_client = oci.email.EmailClient(config)

out = open('log.txt', 'a+')
for line in open(config['file'], 'r'):
    for email in line.strip().split(config['delimited']):
        try:
            # Send the request to service, some parameters are not required, see API doc for more info
            create_sender_response = email_client.create_sender(
                create_sender_details=oci.email.models.CreateSenderDetails(
                    compartment_id=config['compartment_id'],
                    email_address=email))
        except Exception as e:
            out.write(str(e) + '\n')
            print(e)
        # Get the data from response
        out.write(str(create_sender_response.data) + '\n')
        print(create_sender_response.data)