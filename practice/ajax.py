'''
Using AJAX to send data to flask asynchronously, i.e. without a page refresh:
1. XMLHttpRequest - obsolete = manual handling
2. Fetch - modern = using JQuery libary
'''

#XMLHttpRequest
var xhttp = new XMLHttpRequest();
description = document.getElementById("description").value;
xhttp.open("GET", "/todos/create?description=" + description);
xhttp.send();


#XMLHttpRequest on success
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      // on successful response
      console.log(xhttp.responseText);
    }
};


#Using fetch to send HTTP requests. fetch(<url-route>, <object of request parameters>)

fetch('/my/request', {
  method: 'POST', #GET by default
  body: JSON.stringify({
    'description': 'some description here'
  }),
  headers: {
    'Content-Type': 'application/json'
  }
});
