getSingleQuote();

function populateArrayOfTips(response){
    var allRecords = [];

    if(response != '')
    {
        var ar = response.split('\n');
        ar.forEach(function(record) {
            if(record != '') allRecords.push(record.split('|'));
        })
    }

    return allRecords;
}

function pickOneTipInTheListAndDisplayIt(response){
    var allRecords = populateArrayOfTips(response);
    if(allRecords != undefined){
        i = getRandomIndex(allRecords);
        
        if(recordsFormatIsIncorrect(allRecords)){
            console.log("No records found or missing data, reloading the doc!")
            location.reload();
            return;
        }

        document.getElementById("tip").innerHTML = "<i>".concat(getCurrentTip(allRecords, i), "</i>");
        document.getElementById("author").innerHTML = "<a href=\"".concat(getCurrentGuestPage(allRecords, i), "\">", getGuest(allRecords, i), "</a>");
    }
}

function getCurrentTip(allRecords, index){
    return allRecords[i][0].toString().trim();
}

function getGuest(allRecords, index){
    return allRecords[i][1].toString().trim();
}

function getCurrentGuestPage(allRecords, index){
    return allRecords[i][2].toString().replace(/\s/g, '');
}

function recordsFormatIsIncorrect(allRecords){
    return allRecords[i] == undefined || allRecords[i].length != 3;
}

function getRandomIndex(allRecords){
    return Math.floor((Math.random() * allRecords.length)); 
}

function getSingleQuote(){
    var request = new XMLHttpRequest();
    request.open('GET', 'https://raw.githubusercontent.com/DevJourneyFm/DevJourneyFm.github.io/master/tips.txt', true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var type = request.getResponseHeader('Content-Type');
            if (type.indexOf("text") !== 1) {
                pickOneTipInTheListAndDisplayIt(request.responseText);
            }
        }
    }
}