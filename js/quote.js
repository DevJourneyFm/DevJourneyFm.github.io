//getText();

function populateArray(response){
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

        document.getElementById("tip").innerHTML = getCurrentTip(allRecords, i);
        document.getElementById("author").innerHTML = createAuthorSnippet(getCurrentAuthorsHandle(allRecords, i), getCurrentAuthor(allRecords, i))
    }
}

function getCurrentTip(allRecords, index){
    return allRecords[i][0].toString();
}

function getCurrentAuthor(allRecords, index){
    return allRecords[i][1].toString();
}

function getCurrentAuthorsHandle(allRecords, index){
    return allRecords[i][2].toString().replace(/\s/g, '');
}

function createAuthorSnippet(currentAuthorsHandle, currentAuthor){
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
    request.open('GET', 'https://raw.githubusercontent.com/Timothep/howtokillaproject/master/tips', true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var type = request.getResponseHeader('Content-Type');
            if (type.indexOf("text") !== 1) {
                populateArray(request.responseText);
            }
        }
    }
}