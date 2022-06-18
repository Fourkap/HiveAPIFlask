import flask

import requests


def read_all():
    return flask.redirect('/getall')


def read_one(id):
    return flask.redirect('/get/' + id)


def create(employe):
    _name = employe.get("name", None)
    _country = employe.get("country", None)
    _department = employe.get("department", None)
    _salary = employe.get("salary", None)
    _id = employe.get("id", None)

    params = {"id": _id, "name": _name, "country": _country, "department": _department, "salary": _salary}
    response = requests.post('http://127.0.0.1:5000/add', json=params)
    return flask.redirect('/getall')


def update(id, employe):
    _name = employe.get("name", None)
    _country = employe.get("country", None)
    _department = employe.get("department", None)
    _salary = employe.get("salary", None)

    params = {"name": _name, "country": _country, "department": _department, "salary": _salary}
    response = requests.post('http://127.0.0.1:5000/update/' + id, json=params)
    return flask.redirect('/get/' + id)


def delete(id):
    return flask.redirect('/delete/' + id)
