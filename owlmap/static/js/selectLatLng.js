
var map = L.map('map-select', {
    zoomControl: false,
    maxBounds: bounds,
    maxBoundsViscosity: 0.6
}).setView([29.08377, -110.96405], 17);

L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    detectRetina: true,
    minZoom: 16,
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);

map.on('click', function(ev) {
  document.getElementById("latitud").value = ev.latLng.lat;
  document.getElementById("longitud").value = ev.latLng.lng;
  console.log(ev.latlng);
});
