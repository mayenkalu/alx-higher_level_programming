# Python - Network

A **URL** (Uniform Resource Locator) is a string of characters that is used to identify a web resource, such as a webpage, a file, an image, or a video. URLs are used to navigate the internet and are composed of different parts that provide information about the location and type of the resource.

**HTTP** (Hypertext Transfer Protocol) is a protocol used for transmitting data over the internet. It is the foundation of data communication for the World Wide Web and is used to deliver web pages, images, videos, and other resources to web browsers.

Reading a URL involves understanding its different components. A typical URL has the following parts:
```
scheme://domain:port/path?query_string#fragment_id
```
The scheme for a HTTP URL is usually "http://" or "https://", which indicates the protocol used to access the resource. The domain name is the unique identifier for a website, while a sub-domain is a part of the domain that is used to organize and categorize content. For example, "blog.example.com" is a sub-domain of "example.com".

A **port number** is used to identify a specific process to which data should be sent. In a URL, the port number is defined by adding a colon followed by the port number after the domain name. For example, **"http://example.com:8080"** would indicate that the resource is being accessed via port 8080.

Here's Python code that shows how to parse a URL and extract its different components:
```
from urllib.parse import urlparse

url = "http://www.example.com:8080/path/to/resource?query=string#fragment"

parsed_url = urlparse(url)

print("Scheme:", parsed_url.scheme)
print("Domain:", parsed_url.netloc)
print("Path:", parsed_url.path)
print("Query String:", parsed_url.query)
print("Fragment ID:", parsed_url.fragment)
```
The above code will output the following:
```
Scheme: http
Domain: www.example.com:8080
Path: /path/to/resource
Query String: query=string
Fragment ID: fragment
```
Note that the `urlparse` function is part of the built-in Python urllib library and can be used to parse and manipulate URLs.

A **query string** is a portion of a URL that contains data that is sent to the server as part of an HTTP request. It follows the "?" character in a URL and is typically used to pass parameters to a web application.
Example: `https://example.com/search?q=apple`
Here, `?q=apple` is the query string, and it contains the parameter `q` with the value `apple`.

An **HTTP request** is a message sent by a client (such as a web browser) to a server requesting some action to be performed.
Example code:
```
GET /index.html HTTP/1.1
Host: example.com
```
This is a GET request for the file "index.html" on the server example.com.

An **HTTP response** is a message sent by a server in response to an HTTP request. It contains the data requested by the client and other information such as headers and status codes.
```
HTTP/1.1 200 OK
Content-Type: text/html

<html>
  <head>
    <title>Hello, World!</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```
This is a response with status code 200 (OK) and the HTML code for a basic webpage.

**HTTP headers** are additional information sent along with an HTTP request or response. They provide metadata about the message, such as content type, encoding, and cache control.
Example code:
```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
```
This request has three headers: Host, User-Agent, and Accept.

**HTTP Message Body** contains the data being sent in an HTTP request or response. For example, in a GET request, the message body is usually empty, while in a POST request, the message body contains the data being sent to the server.
Example code:
```
POST /submit-form HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Mary",
  "age": 13
}
```
This is a POST request with a JSON message body containing data about a person's name and age.

**An HTTP request** method is a verb that tells the server what action to perform. The most common methods are GET, POST, PUT, and DELETE.
Example code:
```
POST /submit-form HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "John",
  "age": 30
}
```
This is a POST request, which tells the server to submit data to the URL `/submit-form`.

**HTTP response** status codes indicate the outcome of an HTTP request. They are three-digit numbers that represent the response sent by a server to a client. Each status code begins with a digit that represents the class of the status code. The most common status codes are:
      - 2xx: Success
      - 3xx: Redirection
      - 4xx: Client error
      - 5xx: Server error
Code example:
```
import requests

response = requests.get('https://www.example.com')
print(response.status_code)  # prints the status code of the response
```

**An HTTP cookie** (also called a web cookie or a browser cookie) is a small piece of data sent from a website to a user's web browser. Cookies are used to store information about a user's session or preferences on a website, such as login credentials, language settings, and shopping cart contents. Cookies are sent back to the server with subsequent requests, allowing the server to remember the user's preferences or perform authentication.

**cURL (curl)** is a command-line tool for transferring data using various protocols, including HTTP. Here's an example of making a GET request with cURL:
```
curl https://www.example.com
```

This command sends a GET request to https://www.example.com and outputs the response to the terminal.

Pactical:
When you type google.com in your browser and press enter, your browser sends a request to Google's servers using the HTTP protocol. The request includes information such as the URL, any headers, and any cookies associated with the domain. Google's servers respond with an HTTP response, which includes the HTML content of the page, as well as any other resources required to render the page, such as images and JavaScript files. Your browser then interprets the HTML and renders the page on your screen. During this process, various other things happen, such as DNS resolution and TLS negotiation, but at a high level, this is what happens at the application level.

## Tests :heavy_check_mark:                                         
  * [tests](./tests): Folder of test files. Provided by Holberton School.

## Task Description

NOTE: The `curl` behavior in all Bash scripts were written to interact with a
server set up on a container provided by Holberton School.

1. [0-body_size.sh](./0-body_size.sh)
      Bash script that sends a `GET` request to a given URL and displays the size of the response body in bytes.

2. [1-body.sh](./1-body.sh)
      Bash script that sends a `GET` request to a given URL and displays the response body for a `200` status code response.

3. [2-delete.sh](./2-delete.sh)
      Bash script that sends a `DELETE` request to a given URL and displays the response body.

4. [3-methods.sh](./3-methods.sh)
      Bash script that displays all HTTP methods the server of a given URL will accept.

5. [4-header.sh](./4-header.sh)
      Bash script that sends a `GET` request to a given URL with a header variable `X-HolbertonSchool-User-Id=98` and displays the response body.

6. [5-post_params.sh](./5-post_params.sh)
      Bash script that sends a `POST` request to a given URL with the variables `email=hr@holbertonschool.com` and `subject=I will always be here for PLD` and displays the response body.

7. [6-peak.py](./6-peak.py)
      [Technical interview preparation] - Python program that finds a peak in a list of unsorted integers.
   [6-peak.txt](./6-peak.txt)
      Text file containing the complexity of the algorithm.

8. [100-status_code.sh](./100-status_code.sh)
      Bash script that sends a `GET` request to a given URL without using pipes, redirections, `;`, or `&&` and displays the status code of the response.

9. [101-post_json.sh](./101-post_json.sh)
      Bash script that sends a JSON `POST` request with the contents of a provided file to a given URL, and displays the response body.

10. [102-catch_me.sh](./102-catch_me.sh)
      Bash script that sends a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!` in the repsonse body.
