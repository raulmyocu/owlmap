var map = L.map('map-template').setView([29.08377, -110.96405], 17);

L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);

navigator.geolocation.getCurrentPosition(function(position) {
  const coords = [position.coords.latitude, position.coords.longitude];
  const locMarker = L.marker(coords);
  locMarker.bindPopup('Aquí estás').openPopup();
  map.addLayer(locMarker);
});
