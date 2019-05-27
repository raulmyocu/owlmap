function searchString() {
  var str = document.getElementById("searchfield").value;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("results").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "search="+str, true);
  xhttp.send();
}
