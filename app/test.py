
from serviceapi import app
from flask import json

def testRowdata():        
    response = app.test_client().get(
        '/getRowsdata?row=6'
    )

    data = json.loads(response.get_data(as_text=True))
    print(data['data'])
    assert response.status_code == 200
    assert len(data['data']) == 6

def testData():        
    response = app.test_client().get(
        '/getRequestedKeydata?KeyValue={"title":"Introduction to African Oral Literature and Performance"}'
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['title']== "Introduction to African Oral Literature and Performance"


