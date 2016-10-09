from TTT.exemples import super_additionneur
from TTT.application import application
import webtest

def test_addition_de_deux_nombres():
    #Arrange
    app = webtest.TestApp(application)

    #Act
    response = app.post_json('/super-additionneur', dict(param1=1, param2=2))

    #Assert
    assert response.status == '200 OK'
    assert response.content_type == 'application/json'
    assert response.json == {"result": 3}
