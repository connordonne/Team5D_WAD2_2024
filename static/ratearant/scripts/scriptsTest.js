//alert("Script loaded");

// simple functions to show some javascript functionality

// Function to change the image when the button is clicked

 
var counter = 0;

    function changeImageLeft() {

        var imageOne = document.getElementById("changeImageLeft");

        if (counter == 0) {
            counter++;
        } else if (counter == 1) {
            imageOne.src = "/static/ratearant/images/cake.jpeg";
            counter++;
        } else if (counter == 2) {
            counter++;
        } else if (counter == 3) {
            imageOne.src = "/static/ratearant/images/curry.jpeg";
            counter++;
        } else if (counter == 4) {
            counter++; 
        } else if (counter == 5) { 
            imageOne.src = "/static/ratearant/images/soup.jpeg";
            counter++;
        } else if (counter == 6) { 
            counter++;
        } else if (counter == 7) { 
            imageOne.src = "/static/ratearant/images/fajitas.jpeg";
            counter++;
        } else if (counter == 8) { 
            counter++;
        } else if (counter == 9) { 
            imageOne.src = "/static/ratearant/images/burger.jpeg";
            counter++;
        } else if (counter == 10) { 
            counter++;
        } else if (counter == 11) { 
            imageOne.src = "/static/ratearant/images/bread.jpeg";
            counter=0;
        }
        
        
        
    }

  
    var index = 1;

    function changeImageRight() {

        var imageTwo = document.getElementById("changeImageRight");
        
        if (index == 0) {
            imageTwo.src = "/static/ratearant/images/ratatouille.jpeg";
            index=index+1;
        } else if (index== 1) {
            index++;
        } else if (index == 2) {
            imageTwo.src = "/static/ratearant/images/pasta.jpg";
            index++;
        } else if (index == 3) {
            index++;
        } else if (index == 4) {
            imageTwo.src = "/static/ratearant/images/rice.jpg";
            index++;
        } else if (index == 5) {
            index++;
        } else if (index== 6) {
            imageTwo.src = "/static/ratearant/images/pancakes.jpg";
            index++;
        } else if (index== 7) {
            index++;
        } else if (index== 8) {
            imageTwo.src = "/static/ratearant/images/pizza.jpg";
            index++;
        } else if (index== 9) {
            index=index+1;
        } else if (index== 10) {
            imageTwo.src = "/static/ratearant/images/th.jpg";
            index=0;
        } 
    }

    setInterval(changeImageLeft, 3000);
    setInterval(changeImageRight, 3000);

