#!/usr/bin/env python3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/12/2023
# Purpose:                      HTTP GET Request

# got help from chatgpt

# in terminal "pip3 install requests"

# For the given URL, print response header information to the screen.
import requests

# Prompt the user to type a string input as the variable for your destination URL.
def get_user_input():
    url = input("Enter your destination URL: ") # GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS

    http_method = input("Enter the HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
    return url, http_method

def confirm_request(url, http_method):
    print(f"\nRequest about to be sent:\nURL: {url}\nHTTP Method: {http_method}")
    confirmation = input("Do you want to proceed? (yes/no): ").lower()
    return confirmation == 'yes'
# Prompt the user to select a HTTP Method of the following options:
# GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS
def send_request(url, http_method):
    if http_method == 'GET':
        response = requests.get(url)
    elif http_method == 'POST':
        response = requests.post(url)
    elif http_method == 'PUT':
        response = requests.put(url)
    elif http_method == 'DELETE':
        response = requests.delete(url)
    elif http_method == 'HEAD':
        response = requests.head(url)
    elif http_method == 'PATCH':
        response = requests.patch(url)
    elif http_method == 'OPTIONS':
        response = requests.options(url)
    else: # For invalid 
        print("Invalid HTTP Method.")
        return None
    
    return response
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.

def print_response_info(response):
    if response is not None:
        print("\nResponse Header Information:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

        print("\nStatus Code Translation:")
        if response.status_code in status_code_translations:
            print(status_code_translations[response.status_code])
        else:
            print(f"Status Code: {response.status_code}")

status_code_translations = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Site not found",
    500: "Internal Server Error",
}

if __name__ == "__main__":
    url, http_method = get_user_input()

    if confirm_request(url, http_method):
        response = send_request(url, http_method)
        print_response_info(response)