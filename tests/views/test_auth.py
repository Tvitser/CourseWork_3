import os

from project.implemented import user_service


class TestAuthViewlogin:
    url = "/auth/login"

    def test_get_auth(self, client):
        auth_d = {
            "email": "test@vasya1",
            "password": "my_little_pony"
        }
        response = client.post(self.url, json=auth_d)
        assert response.json['access_token'] is not None
        assert response.status_code == 201


class TestAuthViewReg:
    url = "/auth/register"

    def test_get_auth_reg(self, client):
        auth_d = {
            "email": "SkyUser3@test.ru",
            "name": "SkyUser1",
            "password": "eGGPtRKS51",
            "role": "user"
        }
        response = client.post(self.url, json=auth_d)
        user = user_service.get_by_email(auth_d['email'])
        assert user.email == auth_d['email']
        assert response.status_code == 201


if __name__ == "__main__":
    os.system("pytest")
