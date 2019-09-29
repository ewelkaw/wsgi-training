from app import application


class MockedInput:
    def __init__(self, string):
        self.string = string.encode()

    def read(self):
        return self.string


def test_app_root_path():
    input = MockedInput("")

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "GET",
        "QUERY_STRING": "",
        "PATH_INFO": "/",
    }
    assert (
        "".join(map(lambda x: x.decode("UTF-8"), application(env, lambda x, y: None)))
        == """<html>

<body>
  <a href="/users">Users</a>
</body>

</html>"""
    )


def test_app_users_path():
    input = MockedInput("")

    env = {
        "wsgi.input": input,
        "REQUEST_METHOD": "GET",
        "QUERY_STRING": "",
        "PATH_INFO": "/users",
    }

    assert (
        "".join(map(lambda x: x.decode("UTF-8"), application(env, lambda x, y: None)))
        == """<html>

<body>
  <form action="/users" method="POST">
    <input type="text" name="username" placeholder="username" />
    <input type="text" name="email" placeholder="email" />
    <input type="submit" />
  </form>


  <table>
    
    <tr>
      <td>user1</td>
      <td>email1</td>
    </tr>
    
    <tr>
      <td>user2</td>
      <td>email2</td>
    </tr>
    
    <tr>
      <td>user3</td>
      <td>email3</td>
    </tr>
    
  </table>
</body>

</html>"""
    )

