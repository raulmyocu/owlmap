var map = L.map('map-template').setView([29.08377, -110.96405], 17);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

L.marker([29.08331, -111.96398]).addTo(map)
    .bindPopup('Universidad de Sonora<br> Campus Hermosillo')
