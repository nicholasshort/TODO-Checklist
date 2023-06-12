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
    callBackEnd(buttonId);
}

const url = "http://127.0.0.1:5000/api/update";
//const url = "http://172.105.3.93:5000/api/update";

function callBackEnd(buttonPressed) {
    fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
        // body: JSON.stringify({"task": buttonPressed, "complete": true})
        body: JSON.stringify({"date": "2023-06-11"})
    }).then(response => response.json()).then(data => {
        // Handle the response data
        console.log("Made contact!!");
        console.log(data);
    }).catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });
}

