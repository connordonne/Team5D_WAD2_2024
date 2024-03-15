//alert("Script loaded");

// simple functions to show some javascript functionality

// Function to change the image when the button is clicked

 
    var counter = 1;

    function changeImageLeft() {

        console.log("hello")
        
        var imageOne = document.getElementById("changeImageLeft");
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

  
    var index = 1;

    function changeImageRight() {

    
        var imageOne = document.getElementById("changeImageRight");
        if (index == 0) {
            imageOne.src = "/static/ratearant/images/ratearanticon.jpeg";
            index++;
        } else if (index== 1) {
            imageOne.src = "/static/ratearant/images/pizza.jpg";
            index++;
        } else if (index == 2) {
            imageOne.src = "/static/ratearant/images/pasta.jpg";
            index++;
        } else if (index == 3) {
            imageOne.src = "/static/ratearant/images/pancakes.jpg";
            index++;
        } else if (index == 4) {
            imageOne.src = "/static/ratearant/images/rice.jpg";
            index++; 
        } else if (index == 5) {
            imageOne.src = "/static/ratearant/images/th.jpg";
            index = 0;
        }
    }

    document.getElementById("changeImageLeft").addEventListener("click", changeImageLeft)
    document.getElementById("changeImageRight").addEventListener("click", changeImageRight)

