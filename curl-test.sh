#!/bin/bash

api_url="http://localhost:5000/api/timeline_post"
name="Joni Park"
email="zeepada0623@gmail.com"
content="Test Content"

# POST Request
echo "POST request..."
response=$(curl -s -X POST $api_url -H "Content-Type: application/x-www-form-urlencoded" -d "name=$name&email=$email&content=$content")
echo "Response from server: $response"

# GET Request
echo "GET request..."
response=$(curl -s $api_url)
echo "Response from server: $response"
