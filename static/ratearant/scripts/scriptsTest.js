//alert("Script loaded");

// simple functions to show some javascript functionality

// Function to change the image when the button is clicked

    var counter = 1;

    function changeImage() {
        
        var imageOne = document.getElementById("changeImage");
        if (counter == 0) {
            imageOne.src = "/static/ratearant/images/ratearanticon.jpeg";
            counter++;
        } else if (counter == 1) {
            imageOne.src = "/static/ratearant/images/pizza.jpg";
            counter++;
        } else if (counter == 2) {
            imageOne.src = "/static/ratearant/images/pasta.jpg";
            counter++;
        } else if (counter == 3) {
            imageOne.src = "/static/ratearant/images/pancakes.jpg";
            counter++;
        } else if (counter == 4) {
            imageOne.src = "/static/ratearant/images/rice.jpg";
            counter++; 
        } else if (counter == 5) {
            imageOne.src = "/static/ratearant/images/th.jpg";
            counter = 0;
        }
    }
setInterval(changeImage, 2000);
