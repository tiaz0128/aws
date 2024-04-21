#!/bin/bash

# aws sts assume-role 명령을 실행하고 출력을 저장합니다.
output=$(aws sts assume-role --role-arn $ROLE_ARN --role-session-name cli-assume-session)

# 출력에서 필요한 정보를 추출하고 이를 환경 변수에 설정합니다.
export AWS_ACCESS_KEY_ID=$(echo $output | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $output | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $output | jq -r '.Credentials.SessionToken')