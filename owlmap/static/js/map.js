bounds = L.latLngBounds(L.latLng(29.088027, -110.973668), L.latLng(29.079270, -110.953851));
let locMarker = null;
let ubMarker = null;
let ruta = null;

var map = L.map('map-template', {
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

var buhoIcono = L.icon({
    iconUrl: 'static/images/owlmapPuntero.png',

    iconSize:     [46, 53], // size of the icon
    iconAnchor:   [23, 52], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
});

navigator.geolocation.getCurrentPosition(function(position) {
  if (ubMarker != null){
    map.removeLayer(ubMarker);
  }
  coords = [position.coords.latitude, position.coords.longitude];
  ubMarker = L.marker(coords, {icon: buhoIcono});
  ubMarker.bindPopup('Aquí estás').openPopup();
  map.addLayer(ubMarker);
});
