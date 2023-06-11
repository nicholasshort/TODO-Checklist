function finishTask(buttonId) {
    var textId = "";
    switch(buttonId) {
        case "fitnessButton":
            textId = "fitnessText";
            break;
        case "ticketButton":
            textId = "ticketText";
            break;
        case "errandButton":
            textId = "errandText";
            break;
        default:
            return;
    }
    textElement = document.getElementById(textId);
    textElement.classList.toggle("finish");
}

const url = "http://127.0.0.1:5000/api/";
const data = {key: "value"};

function callBackEnd() {
    fetch(url + "gym", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => response.json()).then(data => {
        // Handle the response data
        console.log("Made contact!!");
        console.log(data);
    }).catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });
}

callBackEnd();

