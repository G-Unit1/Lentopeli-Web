
//Create map and load mapsoverlay from openstreetmap
let map = L.map('map').setView([60.319120, 24.955821], 13); /*needs to be set by players locations*/

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 9,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
//TODO: adding circles to available airport connections and