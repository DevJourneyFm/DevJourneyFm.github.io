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

/// Used to display one random quote on the homepage
function pickOneTipInTheListAndDisplayIt(response){
    var allRecords = populateArrayOfTips(response);
    if(allRecords != undefined){
        i = getRandomIndex(allRecords);
        
        if(recordsFormatIsIncorrect(allRecords)){
            console.log("No records found or missing data, reloading the doc!")
            location.reload();
            return;
        }

        document.getElementById("tip").innerHTML = "<i>".concat(getCurrentTip(allRecords[i][0]), "</i>");
        document.getElementById("author").innerHTML = "<a href=\"".concat(getCurrentGuestPage(allRecords[i][2]), "\">", getGuest(allRecords[i][1]), "</a>");
    }
}

/// Used to display all the quotes in the advice page
function displayAllQuotes(response){
    var allRecords = populateArrayOfTips(response);
    if(allRecords != undefined){
        allRecords.forEach(function(record){
            var author = " by <a href=\"".concat(getCurrentGuestPage(record[2]), "\">", getGuest(record[1]), "</a>");
            var quote = "<li><i class=\"tip\">\"".concat(getCurrentTip(record[0]), "\"</i>", author, "</li>");
            document.getElementById("tip").innerHTML += quote;
        });
    }
}

function getCurrentTip(record){
    return record.toString().trim();
}

function getGuest(record){
    return record.toString().trim();
}

function getCurrentGuestPage(record){
    return record.toString().replace(/\s/g, '');
}

function recordsFormatIsIncorrect(allRecords){
    return allRecords[i] == undefined || allRecords[i].length != 3;
}

function getRandomIndex(allRecords){
    return Math.floor((Math.random() * allRecords.length)); 
}

function getGuestQuotes(multiple){
    var request = new XMLHttpRequest();
    request.open('GET', 'https://raw.githubusercontent.com/DevJourneyFm/DevJourneyFm.github.io/master/tips.txt', true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var type = request.getResponseHeader('Content-Type');
            if (type.indexOf("text") !== 1) {
                if(multiple)
                    displayAllQuotes(request.responseText)
                else
                    pickOneTipInTheListAndDisplayIt(request.responseText);
            }
        }
    }
}