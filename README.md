# AWS Study

AWS 를 사용하는 3가지 방법으로 공부한다. services 폴더에 서비스별로 공부한 내용을 정리한다.

1. AWS console
    - `console.md` 파일에 내용을 정리
2. awscli
    - `cli.md` 파일에 내용을 정리
    - [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest)
3. boto3(python)
    - `script.py` 파일에 내용을 정리
    - [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - [AWS SDK Code Examples](https://github.com/awsdocs/aws-doc-sdk-examples)

## 테스트를 위한 임시 자격 증명(Assume-Role)

AWS 사용권한은 유출시 치명적이므로, 반드시 임시 자격 증명을 통해서 최소한의 권한을 설정 테스트를 수행한다.

## aws-cli 설치

```bash
$ apt update

$ apt install awscli
```

```bash
$ awscli configure
```

## boto3 assume-role 이용

- `.env` 파일에 필요한 정보를 입력
- pytest fixture 에서 `assume-role` 로직을 통해서 동적으로 토큰을 발급 받아서 테스트를 진행

```text
AWS_ACCOUNT_ID=...
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
REGION_NAME=ap-northeast-2

ROLE_NAME=테스트에_사용할_ROLE_NAME
```
