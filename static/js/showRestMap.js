



const lat = Number(document.querySelector('#map').getAttribute('data-lat'))
const lng = Number(document.querySelector('#map').getAttribute('data-lng'))

function initMap(){
    
    let options = {
        zoom: 12,
        center:{lat:lat, lng:lng}
    }

    let map = new google.maps.Map(
        document.getElementById('map'), options);

    let marker = new google.maps.Marker({
        position:{lat:lat, lng:lng},
        map:map, 
    });
}

window.initMap = initMap;
