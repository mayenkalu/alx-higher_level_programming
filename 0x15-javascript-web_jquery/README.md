# Javascript - Web JQuery
## About
📝 **JQuery** is a popular JavaScript library that simplifies front-end programming by providing a concise syntax for selecting and manipulating HTML elements, handling DOM events, and making Ajax requests.
JQuery's syntax is straightforward, and it makes selecting and manipulating HTML elements much more comfortable than traditional JavaScript methods. jQuery makes front-end programming easy by simplifying DOM manipulation, event handling, and Ajax requests. Its concise syntax and chainable methods make it a go-to choice for many developers. #ilovejquery 😍
Here's an example of selecting HTML elements in JavaScript:
```
document.getElementById("id"); // by ID
document.getElementsByClassName("class"); // by class
document.getElementsByTagName("tag"); // by tag name
```
Selecting HTML elements with jQuery:
```
$("#id"); // by ID
$(".class"); // by class
$("tag"); // by tag name
ID, Class, and Tag Name Selectors:
ID: Unique identifier for an element, used with #.
Class: Can be applied to multiple elements, used with ..
Tag Name: Represents the element type (e.g. div, p).
```
JQuery makes it easy to modify an HTML element style:
```
$("selector").css("property", "value");
$('#myElement').css('color', 'red'); #an example
```
To get and update an HTML element content:
```
# using text() method
$("selector").text(); // get content
$("selector").text("new content"); // update content
# using html() method
var content = $('#myElement').html(); // get the content
$('#myElement').html('new content'); // update the content
```
JQuery simplifies DOM manipulation by providing methods like append(), prepend(), and remove(). To modify the DOM:
```
$("selector").append(content); // add content
$("selector").remove(); // remove element
```
To make a GET request with jQuery Ajax:
```
$.get("URL", data, successFunction, "dataType");
```
To make an Ajax request with JQuery, using the $.ajax() method. Here's an example of making a GET request:
```
$.ajax({
    url: 'http://example.com/data',
    method: 'GET',
    success: function(response) {
        // handle the response
    },
    error: function() {
        // handle the error
    }
});
```
Make a POST request with jQuery Ajax:
```
$.post("URL", data, successFunction, "dataType");
```
Making the POST request using $.ajax() method
```
$.ajax({
    url: 'http://example.com/data',
    method: 'POST',
    data: {name: 'John', age: 30},
    success: function(response) {
        // handle the response
    },
    error: function() {
        // handle the error
    }
});
```
To listen/bind to DOM events using the on() function:
```
$("selector").on("event", function() {
  // event handler
});
# example
$('#myElement').on('click', function() {
    // handle the click event
});
```
JQuery makes front-end programming more accessible and more comfortable. It simplifies common tasks like selecting HTML elements, modifying their styles and content, manipulating the DOM, and making Ajax requests.
Happy coding! 🚀 #ilovejquery

## Requirements
- jQuery 3.x
- Chrome 57.0

## File Descriptions
**[0-script.js](0-script.js)** - Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):
- You must use `document.querySelector` to select the HTML tag
- You can’t use the jQuery API

Please test with this [HTML file](html_files/0-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```
**[1-script.js](1-script.js)** - Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/1-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
```

**[2-script.js](2-script.js)** - Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/2-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
```

**[3-script.js](3-script.js)** - Write a Javascript script that adds the class red to the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/3-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
```

**[4-script.js](-script.js)** - Write a Javascript script that toggles the class of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#toggle_header`:
- The `HEADER` tag must always have one class: `red` or `green`. Never both at the same time and never empty.
- If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green`, and vice-versa.
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/4-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green">
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
```

**[5-script.js](5-script.js)** - Write a Javascript script that adds a `LI` element to a list when the user clicks on the tag `DIV#add_item`:
- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/5-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
```

**[6-script.js](6-script.js)** - Write a Javascript script that updates the text of the HTML tag `HEADER` to `New Header!!!` when the user clicks on `DIV#update_header`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/6-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
```

**[7-script.js](7-script.js)** - Write a Javascript script that fetches the name from this URL: `https://swapi.co/api/people/5/?format=json`
- The name must be displayed in the HTML tag `DIV#character`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/7-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header>
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
```

**[8-script.js](8-script.js)** - Write a Javascript script that fetches and lists all movie titles by using this URL: `https://swapi.co/api/films/?format=json`
- All movie titles must be listed in the HTML tag `UL#list_movies`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this [HTML file](html_files/8-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header>
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
```

**[9-script.js](9-script.js)** - Write a Javascript script that fetches and prints the San Francisco wind speed by using this URL: `https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json`
- The wind speed must be displayed in the HTML tag `DIV#sf_wind_speed`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the `HEAD` tag

Please test with this [HTML file](html_files/9-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header>
      San Francisco - wind speed
    </header>
    <br />
    <div id="sf_wind_speed"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

**[100-script.js](100-script.js)** - Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):
- You must use `document.querySelector` to select the HTML tag
- You can’t use the jQuery API
- Your script must work when it is imported from the `HEAD` tag

Please test with this [HTML file](html_files/100-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

**[101-script.js](101-script.js)** - Write a Javascript script that adds, removes and clears `LI` elements from a list when the user clicks:
- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- When the user clicks on `DIV#add_item`: a new element is added to the list
- When the user clicks on `DIV#remove_item`: a last element is removed to the list
- When the user clicks on `DIV#clear_list`: all elements of the list are removed
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the `HEAD` tag

Please test with this [HTML file](html_files/101-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

**[102-script.js](102-script.js)** - Write a Javascript script that fetches and prints the wind speed by using this URL: `https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json`
- The wind speed must be displayed in the HTML tag `DIV#wind_speed`
- The city name must be the value of the tag `INPUT#city_search`
- The wind speed must be fetched when the user clicks on `INPUT#btn_search`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the `HEAD` tag

Please test with this [HTML file](html_files/102-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header>
      Wind speed
    </header>
    <br />
    <input id="city_search" type="text" placeholder="City"/>
    <input id="btn_search" type="button" value="Search"/>
    <br />
    <div id="wind_speed"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

**[103-script.js](103-script.js)** - Write a Javascript script that fetches and prints the wind speed by using this URL: `https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json`
- The wind speed must be displayed in the HTML tag `DIV#wind_speed`
- The city name must be the value of the tag `INPUT#city_search`
- The wind speed must be fetched when the user clicks on `INPUT#btn_search` OR presses `ENTER` when the focus is on `INPUT#city_search`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the `HEAD` tag

Please test with this [HTML file](html_files/103-main.html) in your browser:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header>
      Wind speed
    </header>
    <br />
    <input id="city_search" type="text" placeholder="City"/>
    <input id="btn_search" type="button" value="Search"/>
    <br />
    <div id="wind_speed"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
