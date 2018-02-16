function addImage(activity) {
    var img = document.createElement("img");
    switch(activity) {
        case 'play':
        img.src = "{% static "images/Toys.png" %}";
        break;
        case 'snack':
        img.src = "{% static "images/Apple.png" %}";
        break;
        case 'outside':
        img.src = "{% static "images/Park.png" %}";
        break;
        default:
        console.log("Error: Activity not found.");
    }
    img.height = 100;
    img.width = 100;

    document.body.appendChild(img);
}
