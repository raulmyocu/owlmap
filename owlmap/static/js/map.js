var map = L.map('map-template', { zoomControl: false }).setView([29.08377, -110.96405], 17);

L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    detectRetina: true,
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);

var buhoIcono = L.icon({
    iconUrl: 'static/images/owlmapPuntero.png',

    iconSize:     [46, 53], // size of the icon
    iconAnchor:   [23, 52], // point of the icon which will correspond to marker's location
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

navigator.geolocation.getCurrentPosition(function(position) {
  const coords = [position.coords.latitude, position.coords.longitude];
  const locMarker = L.marker(coords, {icon: buhoIcono});
  locMarker.bindPopup('Aquí estás').openPopup();
  map.addLayer(locMarker);
});
