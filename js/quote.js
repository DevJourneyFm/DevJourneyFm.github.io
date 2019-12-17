getText();

function populateArrayOfTips(response){
    var allRecords = [];

    if(response != '')
    {
        var ar = response.split('\n');
        ar.forEach(function(record) {
            if(record != '') allRecords.push(record.split('|'));
        })
    }

    if(allRecords != undefined){
        i = getRandomIndex(allRecords);
        
        if(recordsFormatIsIncorrect(allRecords)){
            console.log("No records found or missing data, reloading the doc!")
            location.reload();
            return;
        }

        var guest = getGuest(allRecords, i);

        var link = getGuestLink(guest);

        document.getElementById("tip").innerHTML = getCurrentTip(allRecords, i);
        document.getElementById("author").innerHTML = link;
    }
}

function getCurrentTip(allRecords, index){
    return allRecords[i][0].toString();
}

function getGuest(allRecords, index){
    return allRecords[i][1].toString();
}

function getCurrentGuestPage(allRecords, index){
    return allRecords[i][2].toString().replace(/\s/g, '');
}

function populateArrayOfShowsLinks(response, guest){
    var links = [];
    
    if(response != '')
    {
        var m;
        var regex1 = "(Guests\\/\\d{1,2}_";
        var regex2 = "\\.html)";
        var guestWOSpaces = guest.replace(/\s/g,'');
        var regexString = regex1.concat(guestWOSpaces, regex2)
        var regex = new RegExp(regexString);
        var extractedLink = regex.exec(response);
        return extractedLink;
    }

    return "";
}

function createGuestLink(currentAuthorsHandle, currentAuthor){
    //find the page in the index.html page
    if(currentAuthorsHandle == ''){
        return currentAuthor;
    } else {
        return ''.concat(
            "<a href=\"https://www.twitter.com/", 
            currentAuthorsHandle,
            "\">",
            currentAuthorsHandle,
            "</a>");
    }
}

function recordsFormatIsIncorrect(allRecords){
    return allRecords[i] == undefined || allRecords[i].length != 3;
}

function getRandomIndex(allRecords){
    return Math.floor((Math.random() * allRecords.length)); 
}

function getText(){
    var request = new XMLHttpRequest();
    request.open('GET', 'https://raw.githubusercontent.com/DevJourneyFm/DevJourneyFm.github.io/master/tips.txt', true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var type = request.getResponseHeader('Content-Type');
            if (type.indexOf("text") !== 1) {
                populateArrayOfTips(request.responseText);
            }
        }
    }
}

function getGuestLink(guest){
    var request = new XMLHttpRequest();
    request.open('GET', 'https://raw.githubusercontent.com/DevJourneyFm/DevJourneyFm.github.io/master/index.html', true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var type = request.getResponseHeader('Content-Type');
            if (type.indexOf("text") !== 1) {
                return populateArrayOfShowsLinks(request.responseText, guest);
            }
        }
    }
}