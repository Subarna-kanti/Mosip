from behave import given, when, then, step
import requests

@given('A user with valid access token')
def set_access_token_in_header(context):
    context.header = {"Authorization": "Bearer " + "b3c1e915bc7874d30e268e8de481322ed3b97e454ff0a82c63ec53d07c066b91"}
    
@step('the user has email as "subornosamonto@gmail.com"')
def set_mail(context):
    context.request_body = {"email": "subornosamo@gmail.com"}

@step('the user wants to create a record with name as "Subarna"')
def set_first_name(context):
    context.request_body['name'] = "Subarna"

@step('the gender is "male"')
def set_last_name(context):
   context.request_body['gender'] = "Male"

@step('the user status is "active"')
def set_user_status(context):
    context.request_body['status'] = "Active"

@when('user submits the user data in "https://gorest.co.in/public-api/users"')
def execute_post_request_for_user_creation(context):
    print(context.request_body)
    response = requests.post('https://gorest.co.in/public-api/users', headers=context.header, json=context.request_body)
    context.response_body = response.json()
    context.status_code = response.status_code
    print(context.status_code)
    print(context.response_body)

@then('you should receive a "200" status code')
def check_status_code(context):
    assert context.status_code == 200

@step('mail is "subornosamonto@gmail.com"')
def check_mail(context):
    assert context.response_body['data']['email'] == "subornosamo@gmail.com"

@step('first name "Subarna" should be in response body')
def check_first_name(context):
    assert context.response_body['data']['name'] == "Subarna"

@step('gender "male" should be in response body')
def check_gender(context):
    assert context.response_body['data']['gender'] == "Male"


@step('user status "active" should be in response body')
def check_user_status(context):
    assert context.response_body['data']['status'] == "Active"

