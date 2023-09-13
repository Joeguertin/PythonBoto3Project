from importlib.resources import path
import boto3
import random
import logging
import os

from botocore.exceptions import ClientError

AWS_REGION = "us-east-1"
s3 = boto3.resource('s3')
ec2 = boto3.client('ec2')
ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)
ec2_client = boto3.client("ec2", region_name=AWS_REGION)


def createkeypair():
    running = True
    while running:
        try:
            global key_pair_name
            key_pair_name = input("What would you like to name your keypair?")    
            response = ec2.create_key_pair(KeyName=key_pair_name)
            print(key_pair_name , "successfully made!")
            private_key_file=open(key_pair_name,"w")
            private_key_file.write(response['KeyMaterial'])
            private_key_file.close
            filename = key_pair_name
            os.chmod(filename, 0o664)
            running = False
        except:
            print("Keypair" , key_pair_name, "already exists, please try again.")
        
createkeypair()

def createec2instance():
    looploop1 = 0
    while looploop1 == 0:
            try:
                
                    print(f"Instance {ec2_client_name} is being created")
                    
                    instances = ec2_client.run_instances(
                        ImageId="ami-0c02fb55956c7d316",
                        MinCount=1,
                        MaxCount=1,
                        InstanceType="t2.micro",
                        KeyName=key_pair_name,
                        TagSpecifications = [
                            {
                                'ResourceType': 'instance',
                                'Tags': [
                                    {
                                        'Key': 'Name',
                                        'Value': ec2_client_name
                                    }
                                        ]
                            }
                        ]
                        )

                    print(instances["Instances"][0]["InstanceId"])
                    print(ec2_client_name)
                
                    looploop1 = looploop1 + 1

            except:
                print("Something broke dawg")
                




def checkforinstance():
    checkfor = True
    while checkfor:
        try:
            
            global ec2_client_name
            ec2_client_name = input(str("Please enter desired instance tag name?"))
            
            testprint = 0
            omegalul = True
            
            if omegalul == True:
                instances = ec2_resource.instances.filter(
                    Filters=[
                        {
                            'Name': 'tag:Name',
                            'Values': [
                                ec2_client_name
                            ]
                        }
                    ]
                )


            for instance in instances:
                testprint = instance.id
                print("*ERROR CHECKING #1*", ec2_client_name)
            if testprint == instance.id:
                print("This instance already exists, choose another name")      
                print(testprint)  
                print(ec2_client_name)
            else:
                print("*else statement", ec2_client_name)
                
                print(f"Instance {ec2_client_name} will now be created")
                createec2instance()
                checkfor = False
            



        except:
            print(f"Instance {ec2_client_name} will now be created")
            createec2instance()
            checkfor = False

checkforinstance()




    




#createec2instance()

#def get_running_instances():
#    AWS_REGION = "us-east-1"
#    EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
#    INSTANCE_NAME_TAG_VALUE = 'my-ec2-instance'
#
#    instances = EC2_RESOURCE.instances.filter(
#        Filters=[
#            {
#                'Name': 'tag:Name',
#                'Values': [
#                    INSTANCE_NAME_TAG_VALUE
#                ]
#            }
#        ]
#    )
#
#    print(f'Instances with Tag "Name={INSTANCE_NAME_TAG_VALUE}":')
#
#    for instance in instances:
#        print(f'  - Instance ID: {instance.id}')        
#
#
#
#
#get_running_instances()