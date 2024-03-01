//alert("Script loaded");

// simple functions to show some javascript functionality

// Function to change the image when the button is clicked
function changeImage(){
    // select the item on the page using the DOM model
    var imageOne=document.getElementById("img1");
    // use the src attribute to change the image
    imageOne.src="/static/ratearant/images/th.jpg";
}

// function to change the image back
function revertImage(){
    // Select the image again
    var imageOne=document.getElementById("img1");
    // change to the original image
    imageOne.src="{% static 'ratearant/images/ratearanticon.jpeg' %}"
}