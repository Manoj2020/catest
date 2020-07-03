from behave import *
import requests
import jsonschema
from jsonschema import validate
import json
from schemas import PoliticianSchema as ps


# validate response schema
def schema_validator(json_payload, schema):
    try:
        validate(instance=json_payload, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


@given("I have access to the politician API Service Environment")
def initialise(context):
    pass


@step('I build the endpoint to access politician API')
def build_endpoint(context):
    context.endpoint = 'http://qa-test.data-playground-1.ivxs.uk/peps'


@step('I build the HTTP header details')
def build_headers(context):
    context.type_header = {"Content-Type": "application/json"}


@step('I build create peps POST http body with "{name}", "{country}", "{yob}", "{position}" and "{risk}" details')
def build_body(context, name, country, yob, position, risk):
    context.request_body = {"name": name, "country": country, "yob": int(yob), "position": position, "risk": int(risk)}


@when('I send the POST request')
def step_impl(context):
    response = requests.post(context.endpoint, headers=context.type_header, json = context.request_body)
    context.response_body = response.json()
    context.status_code = response.status_code


@when('I send the GET request')
def step_impl(context):
    response = requests.get(context.endpoint, headers=context.type_header)
    context.response_body = response.json()
    context.status_code = response.status_code


@when('I send the GET peps by "{id}" request')
def step_impl(context, id):
    response = requests.get(context.endpoint + '/' + id, headers=context.type_header)
    context.response_body = response.json()
    context.status_code = response.status_code


@then('I verify the response http code 201')
def verify_response(context):
    assert context.status_code == 201


@step("I validate response message ok is true")
def step_impl(context):
    assert context.response_body["ok"] == True


@step("I validate message field value")
def step_impl(context):
    assert context.response_body["message"] == 'Entity created successfully!'


@step("I validate response id value is not null")
def step_impl(context):
    assert context.response_body["id"]


@then("I validate POST response json schema")
def step_impl(context):
    json_body = json.dumps(context.response_body)
    assert schema_validator(json.loads(json_body), ps.post_response)


@then("I validate GET response json schema")
def step_impl(context):
    json_body = json.dumps(context.response_body)
    assert schema_validator(json.loads(json_body), ps.get_response)


@then("I validate GET by ID response json schema")
def step_impl(context):
    json_body = json.dumps(context.response_body)
    assert schema_validator(json.loads(json_body), ps.getbyid_response)


@then("I verify the response http code is not 201")
def step_impl(context):
    assert context.status_code != 201, 'The HTTP status code should not be 201'


@step("I validate response message ok is not true")
def step_impl(context):
    assert context.response_body["ok"] == False, 'The value of Ok field should be false'


@step("I validate message field value is not successful")
def step_impl(context):
    assert context.response_body["message"] != 'Entity created successfully!', 'Entity should not have been created'


@step("I validate response id value is null")
def step_impl(context):
    assert not context.response_body["id"]


@then("I verify the response http code is 200")
def step_impl(context):
    assert context.status_code == 200


@then('I validate the "{name}" in the response')
def step_impl(context, name):
    assert context.response_body["name"] == name


@then("I validate the response has 5 politicians records")
def step_impl(context):
    records = len(context.response_body)
    assert records == 5, 'There should be only 5 records, it returned: ' + str(records)


@then("I validate that they are in descending order by date of creation")
def step_impl(context):
    created_dates = [politician["createdAt"] for politician in context.response_body]
    assert all(former >= latter for former, latter in zip(created_dates, created_dates[1:])), 'Records should be in ' \
                                                                                              'descending order '


@step("I validate response message generated id is not null")
def step_impl(context):
    assert context.response_body["id"], 'Generated id should not be null'


@step('I validate the returned "{name}" in the response')
def step_impl(context, name):
    returned = context.response_body["name"]
    assert returned == name, 'Response returned: ' + returned + ' expected: ' + name


@step('I check the "{country}" in the response')
def step_impl(context, country):
    returned = context.response_body["country"]
    assert returned == country, 'Response returned: ' + returned + ' expected: ' + country


@step('I validate the "{position}" returned in the response')
def step_impl(context, position):
    returned = context.response_body["position"]
    assert returned == position, 'Response returned: ' + returned + ' expected: ' + position


@step('I validate the "{risk}" in the returned response')
def step_impl(context, risk):
    returned = context.response_body["risk"]
    assert returned == int(risk), 'Response returned: ' + str(returned) + ' expected: ' + risk


@step('I examine the returned "{yob}" in the response')
def step_impl(context, yob):
    returned = context.response_body["yob"]
    assert returned == int(yob), 'Response returned: ' + str(returned) + ' expected: ' + yob
