$(document).ready(function (){
    const cardImages = document.querySelectorAll('[attrrestaurantpic]');
    cardImages.forEach(cardImage => {
        var pathToImage = staticUrl + "rateArant_";
        //get a number between 1-19
        var nums=19;
        var random=Math.floor(Math.random()*nums)+1;
        var image=pathToImage+random+".jpg";
        console.log(image);
        cardImage.src = image;
    });
});

