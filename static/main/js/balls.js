let powerBallElements = document.querySelectorAll(".numberCellPB");
let selectedPB = undefined;

let ballElements = document.querySelectorAll(".numberCell");
let ballValues = document.querySelectorAll(".ballValue");
let selectedBalls = [];

let gridElement = document.querySelectorAll(".numberGrid");

function addToNumberList(x) {
  if (selectedBalls.length >= 5) {
    //If length > or equal to 5 remove first num then unselect
    const removedNumber = selectedBalls.shift();
    ballElements[removedNumber - 1].removeAttribute("data-clicked");
    ballElements[removedNumber - 1].removeAttribute("style");
  }
  selectedBalls.push(x);
}
//Borrowed from
//https://www.30secondsofcode.org/js/s/all-unique
const allUnique = (arr) => arr.length === new Set(arr).size;

//Borrowed from
//https://stackoverflow.com/questions/5767325/how-can-i-remove-a-specific-item-from-an-array#:~:text=Find%20the%20index%20of%20the,and%2For%20adding%20new%20elements.&text=The%20second%20parameter%20of%20splice%20is%20the%20number%20of%20elements%20to%20remove.
function removeItemAll(arr, value) {
  var i = 0;
  while (i < arr.length) {
    if (arr[i] === value) {
      arr.splice(i, 1);
    } else {
      ++i;
    }
  }
  return arr;
}
function submitForm() {
  if (
    selectedPB != undefined &&
    selectedBalls.length == 5 &&
    allUnique(selectedBalls)
  ) {
    document.getElementById("id_ball1").value = selectedBalls[0];
    document.getElementById("id_ball2").value = selectedBalls[1];
    document.getElementById("id_ball3").value = selectedBalls[2];
    document.getElementById("id_ball4").value = selectedBalls[3];
    document.getElementById("id_ball5").value = selectedBalls[4];

    document.getElementById("id_powerBall").value = selectedPB;

    //Here make sure boxes being filled then once are uncomment to submit form
    document.getElementById("playLottoForm").submit();
  } else {
    throw "Error: bad input for lotto balls";
  }
}

function sortAndPrint() {
  //Sort before printing
  //Wierd js sort
  selectedBalls = selectedBalls.sort((a, b) => {
    if (a < b) {
      return -1;
    }
    if (a > b) {
      return 1;
    }
    return 0;
  });

  if (selectedBalls[0] === undefined) {
    if (ballValues[0].style.display === "block") {
      ballValues[0].style.display = "none";
    }
    //ballValues[0].getElementsByClassName("innerBallText")[0].innerHTML = "";
  } else {
    ballValues[0].style.display = "block";
    ballValues[0].getElementsByClassName("innerBallText")[0].innerHTML =
      selectedBalls[0];
  }

  if (selectedBalls[1] === undefined) {
    //ballValues[1].getElementsByClassName("innerBallText")[0].innerHTML = "";
    if (ballValues[1].style.display === "block") {
      ballValues[1].style.display = "none";
    }
  } else {
    ballValues[1].style.display = "block";
    ballValues[1].getElementsByClassName("innerBallText")[0].innerHTML =
      selectedBalls[1];
  }

  if (selectedBalls[2] === undefined) {
    if (ballValues[2].style.display === "block") {
      ballValues[2].style.display = "none";
    }
    //ballValues[2].getElementsByClassName("innerBallText")[0].innerHTML = "";
  } else {
    ballValues[2].style.display = "block";
    ballValues[2].getElementsByClassName("innerBallText")[0].innerHTML =
      selectedBalls[2];
  }

  if (selectedBalls[3] === undefined) {
    if (ballValues[3].style.display === "block") {
      ballValues[3].style.display = "none";
    }
    //ballValues[3].getElementsByClassName("innerBallText")[0].innerHTML = "";
  } else {
    ballValues[3].style.display = "block";
    ballValues[3].getElementsByClassName("innerBallText")[0].innerHTML =
      selectedBalls[3];
  }

  if (selectedBalls[4] === undefined) {
    if (ballValues[4].style.display === "block") {
      ballValues[4].style.display = "none";
    }
    //ballValues[4].getElementsByClassName("innerBallText")[0].innerHTML = "";
  } else {
    ballValues[4].style.display = "block";
    ballValues[4].getElementsByClassName("innerBallText")[0].innerHTML =
      selectedBalls[4];
  }

  if (selectedPB === undefined) {
    if (ballValues[5].style.display === "block") {
      ballValues[5].style.display = "none";
    }
    //ballValues[5].getElementsByClassName("innerBallText")[0].innerHTML = "";
  } else {
    ballValues[5].style.display = "block";
    ballValues[5].getElementsByClassName("innerBallText")[0].innerHTML =
      selectedPB;
  }
  //If grid is full collapse
  if (selectedBalls.length == 5) {
    gridElement[0].style.display = "none";
  } else {
    gridElement[0].style.display = "block";
  }

  if (selectedPB != undefined) {
    gridElement[1].style.display = "none";
  } else {
    gridElement[1].style.display = "block";
  }

  if (selectedPB != undefined && selectedBalls.length == 5) {
    document.getElementById("playTheLotto").removeAttribute("hidden");
  } else {
    document.getElementById("playTheLotto").setAttribute("hidden", "hidden");
  }
}

//On click of big number grid
for (element of ballElements) {
  element.addEventListener("click", function () {
    if (!this.dataset.clicked) {
      //add to list of numbers
      addToNumberList(parseInt(this.outerText));
      this.setAttribute("data-clicked", "true");
      this.style.backgroundColor = "#555";
      this.style.color = "#fff";
    } else {
      //remove from list and deselect
      removeItemAll(selectedBalls, parseInt(this.outerText));
      this.removeAttribute("data-clicked");
      this.removeAttribute("style");
    }
    sortAndPrint();
  });
}

for (elementPB of powerBallElements) {
  //On click of small number grid
  elementPB.addEventListener("click", function () {
    if (!this.dataset.clicked) {
      //remove if alraeady set
      if (typeof selectedPB !== "undefined") {
        powerBallElements[selectedPB - 1].removeAttribute("data-clicked");
        powerBallElements[selectedPB - 1].removeAttribute("style");
      }
      //then update varible and select
      selectedPB = parseInt(this.outerText);
      this.setAttribute("data-clicked", "true");
      this.style.backgroundColor = "#555";
      this.style.color = "#fff";
    } else {
      //remove from list and deselect
      selectedPB = undefined;
      this.removeAttribute("data-clicked");
      this.removeAttribute("style");
    }
    sortAndPrint();
  });
}

//On click of balls
for (elementBall of ballValues) {
  //Remove element from list on click of balls
  elementBall.addEventListener("click", function () {
    if (!this.dataset.clicked) {
      //If powerball is clicked
      if (
        this.getElementsByClassName("innerBallText")[0].classList.contains(
          "powerBallClass"
        )
      ) {
        if (this.getElementsByClassName("innerBallText")[0].innerHTML !== "") {
          selectedPB = undefined;
          powerBallElements[
            this.getElementsByClassName("innerBallText")[0].innerHTML - 1
          ].removeAttribute("data-clicked");
          powerBallElements[
            this.getElementsByClassName("innerBallText")[0].innerHTML - 1
          ].removeAttribute("style");
          sortAndPrint();
        }
      } else {
        //If normal ball is clicked
        if (this.getElementsByClassName("innerBallText")[0].innerHTML !== "") {
          removeItemAll(
            selectedBalls,
            parseInt(this.getElementsByClassName("innerBallText")[0].innerHTML)
          );
          ballElements[
            this.getElementsByClassName("innerBallText")[0].innerHTML - 1
          ].removeAttribute("data-clicked");
          ballElements[
            this.getElementsByClassName("innerBallText")[0].innerHTML - 1
          ].removeAttribute("style");
          sortAndPrint();
        }
      }
    }
  });
}
