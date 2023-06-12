function showTaskStatus() {
    
    if (fitnessStatus) {
        textElement = document.getElementById("fitnessText");
        textElement.classList.toggle("finish");
    }
    
    if (ticketStatus) {
        textElement = document.getElementById("ticketText");
        textElement.classList.toggle("finish");
    }

    if (errandStatus) {
        textElement = document.getElementById("errandText");
        textElement.classList.toggle("finish");
    }

}



function updateTask(buttonId) {
    var textId = "";
    var complete = false;
    switch(buttonId) {
        case "fitnessButton":
            textId = "fitnessText";
            fitnessStatus = !fitnessStatus;
            complete = fitnessStatus;
            break;
        case "ticketButton":
            textId = "ticketText";
            ticketStatus = !ticketStatus;
            complete = ticketStatus;
            break;
        case "errandButton":
            textId = "errandText";
            errandStatus = !errandStatus;
            complete = errandStatus;
            break;
        default:
            return;
    }
    textElement = document.getElementById(textId);
    textElement.classList.toggle("finish");
    updateBackEnd(buttonId, complete);
}


function callBackEnd() {

    //const url = "http://127.0.0.1:5000/api/status";
    const get_url = "http://172.105.3.93:5000/api/status";

    return fetch(get_url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Current-Date': formattedDate
        },
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Request failed with status ' + response.status);
        }
    }).then(data => {
        // Handle the response data
        console.log("Made contact!!");
        //console.log(data);
        return data
    }).catch(error => {
        // Handle any errors
        console.error('Error:', error);
        throw error;
    });
}


function updateBackEnd(buttonPressed, complete) {

    const post_url = "http://172.105.3.93:5000/api/update";

    fetch(post_url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Current-Date': formattedDate
        },
        body: JSON.stringify({"task": buttonPressed, "complete": complete})
    }).then(response => response.json()).then(data => {
        // Handle the response data
        console.log("Made contact!!");
        console.log(data);
    }).catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });
}

var currentDate = new Date();

var year = currentDate.getFullYear();
var month = currentDate.getMonth() + 1;
var day = currentDate.getDate();

var formattedDate = year + '-' + month + '-' + day;

var fitnessStatus = false;
var ticketStatus = false;
var errandStatus = false;

(async function() {
    try {
        const currentStatus = await callBackEnd();
        console.log("Current status:", currentStatus);
        fitnessStatus = currentStatus["gym"];
        ticketStatus = currentStatus["ticket"];
        errandStatus = currentStatus["errand"];
        showTaskStatus();
    } catch (error) {
        console.error('Error:', error);
    }
})();


