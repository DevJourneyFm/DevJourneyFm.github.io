
function getEpisodeNumberFromUrl(currentUrl){
    return currentUrl.match(".*devjourney\.info\/190346\/.*-(\d\d)-.*");
}

function tryGetEpisodeNumber(){
    var episodeNumber = getEpisodeNumberFromUrl(window.location.href);
}


var currentUrl = "https://podcast.devjourney.info/190346/UID-71-irwin-williams-found-his-perfect-spot";

document.querySelector("#URL").innerHTML = currentUrl;


document.querySelector("#Guess").innerHTML = episodeNumber;

podcast.devjourney.info/190346/UID-71-irwin-williams-found-his-perfect-spot

http://podcast.devjourney.info/190346/1833373