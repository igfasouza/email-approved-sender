import oci
from oci.config import from_file
import sys


print(sys.argv[1])

# Create a default config using DEFAULT profile in default location Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
try:
    config = from_file("./config")
except oci.exceptions.ConfigFileNotFound as e:
    config = from_file()


# Initialize service client with default config file
email_client = oci.email.EmailClient(config)

try:
    # Send the request to service, some parameters are not required, see API doc for more info
    create_sender_response = email_client.create_sender(
        create_sender_details=oci.email.models.CreateSenderDetails(
            compartment_id=config['compartment_id'],
            email_address=sys.argv[1]))
except Exception as e:
    print(e)
# Get the data from response
print(create_sender_response.data)