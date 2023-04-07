# Python Network II
Python provides several built-in packages to handle HTTP requests and responses. Two of the most commonly used packages are `urllib` and `requests`.

**Fetching Internet Resources with urllib**
`urllib` is a package that provides several modules to interact with web pages and URLs. It can be used to fetch resources from the internet.
```
import urllib.request

url = "https://www.example.com"
response = urllib.request.urlopen(url)
print(response.read().decode('utf-8'))
```
This code will fetch the resource from the URL and decode it using UTF-8.

**Decoding urllib Body Response**
In the above example, the `response.read() `method returns the response body as bytes, which needs to decoded to convert it into a human-readable format. This is done by calling the `decode()` method on the bytes object, passing the appropriate encoding (e.g. UTF-8) as an argument.

**Using the requests Package**
`requests` is a third-party package that simplifies making HTTP requests. It is often preferred over `urllib` due to its simpler syntax and richer functionality.
```
import requests

url = "https://www.example.com"
response = requests.get(url)
print(response.text)
```
This code performs an HTTP GET request to the specified URL and prints the response body.

**Making HTTP GET Request**
To make an HTTP GET request using `requests`, we can use the `requests.get()` method.
```
import requests

url = "https://www.example.com"
response = requests.get(url)
print(response.text)
```

**Making HTTP POST/PUT/etc. Request**
To make an HTTP POST, PUT, or other type of request, use the appropriate method in `requests`. For example, to make an HTTP POST request, using `requests.post()`:
```
import requests

url = "https://www.example.com"
data = {'key': 'value'}
response = requests.post(url, data=data)
print(response.text)
```
**Fetching JSON Resources**
Many web APIs return data in JSON format. We can use `requests` to fetch JSON data and convert it into a Python object.
```
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
data = response.json()
print(data)
```
In this example, we fetch a JSON resource and convert it into a Python object using the `json()` method.

**Manipulating Data from an External Service**
Once we have fetched data from an external service, we can manipulate it using Python's built-in data manipulation tools (e.g. lists, dictionaries, etc.). Here's an example:
```
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
```
# Filter the data to only include posts with an ID less than 10
filtered_data = [post for post in data if post['id'] < 10]

# Print the filtered data
for post in filtered_data:
    print(post['title'])
```

In this example, we fetch a collection of posts from an external service, filter the data to only include posts with an ID less than 10, and print the titles of the filtered posts.

## Task Description :card_index:
* [0-hbtn_status.py](./0-hbtn_status.py): Python script that fetches
  `https://alx-intranet.hbtn.io/status`.
  * Uses `urllib`.

* [1-hbtn_header.py](./1-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./1-hbtn_header.py <URL>`
	* Uses `urllib`.

* [2-post_email.py](./2-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./2-post_email.py <URL> <email>`.
	* Uses `urllib`.

* [3-error_code.py](./3-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `urllib`.

* [4-hbtn_status.py](./4-hbtn_status.py): Python script that fetches
  `https://alx-intranet.hbtn.io/status`.
  * Uses `requests`.


* [5-hbtn_header.py](./5-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./5-hbtn_header.py <URL>`
	* Uses `requests`.

* [6-post_email.py](./6-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./6-post_email.py <URL> <email>`.
	* Uses `requests`.


* [7-error_code.py](./7-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `requests`.


* [8-json_api.py](./8-json_api.py): Python script that sends a `POST` request
  to `http://0.0.0.0:5000/search_user` with a letter passed as parameter.
  * Usage: `./8-json_api.py <letter>`
	* The letter is sent as the value of the variable `q`.
	* If no letter is given, sets `q=""`.
	* If the response body is properly formatted and non-empty, displays it as
  `[<id>] <name>`.
  * Uses `requests`.

* [10-my_github.py](./10-my_github.py): Python script that takes GitHub
  credentials (username and password) and uses the Github API to display the
  corresponding ID.
  * Usage: `./10-my_github.py <username> <password>`
	* Uses `requests`.

* [100-github_commits.py](./100-github_commits.py): Python script that lists
  the 10 most recent comments of a given GitHub repository using the GitHub API.
  * Usage: `./100-github_commits.py <repository name> <owner name>`
	* Uses `requests`.
