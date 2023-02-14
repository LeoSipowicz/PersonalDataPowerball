var path = window.location.pathname;
var page = path.split("/").pop();
console.log(page);

window.onload = function () //executes when the page finishes loading
{
  setTimeout(func1, 6000); //sets a timer which calls function func1 after 2,000 milliseconds = 2 secs.
};
function func1() {
  document.getElementById("results").className = "show";
}
