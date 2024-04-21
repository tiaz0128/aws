import pytest

from services.ec2.sg.script import hello_ec2


class TestEC2:
    @pytest.fixture(autouse=True)
    def setup(self, session):
        self.session = session
        self.ec2_resource = session.resource("ec2")

    def test_hello_ec2(self):
        hello_ec2(self.ec2_resource)
