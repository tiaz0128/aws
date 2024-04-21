import logging


def hello_ec2(ec2_resource):
    logging.info("Hello, Amazon EC2! Let's list up to 10 of your security groups:")
    for sg in ec2_resource.security_groups.limit(10):
        logging.info(f"\t{sg.id}: {sg.group_name}")
