import logging
import pytest

import os
from dotenv import load_dotenv

import boto3
from boto3 import Session

# .env 파일 로드
load_dotenv()


@pytest.fixture(scope="session", name="aws_user_session")
def setup_user_session():
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    region_name = os.getenv("REGION_NAME")

    return boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name,
    )


@pytest.fixture(scope="session", name="session")
def setup_role_credentials(aws_user_session):
    aws_account_id = os.getenv("AWS_ACCOUNT_ID")
    role_arn = os.getenv("ROLE_ARN")

    credentials = assume_role(aws_user_session, role_arn)

    session = boto3.Session(
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
        region_name=os.getenv("AWS_REGION"),
    )

    logging.info("Role credentials are generated successfully")

    sts = session.client("sts")
    logging.info(sts.get_caller_identity())

    return session


def assume_role(aws_user_session: Session, role_arn):
    sts_client = aws_user_session.client("sts")

    response = sts_client.assume_role(
        RoleArn=role_arn, RoleSessionName="boto3-assume-session"
    )

    return response["Credentials"]
