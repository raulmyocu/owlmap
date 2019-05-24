bounds = L.latLngBounds(L.latLng(29.088027, -110.973668), L.latLng(29.079270, -110.953851));
var locMarker = null;

var map = L.map('map-select', {
    zoomControl: false,
    maxBounds: bounds,
    maxBoundsViscosity: 0.6
}).setView([29.08377, -110.96405], 16);

L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    detectRetina: true,
    minZoom: 16,
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);

map.on('click', function(ev) {
  cambiaInput(ev.latlng.lat, ev.latlng.lng);
});

function muestraUbicacion(el) {
  var key = el.options[el.selectedIndex].value;
  var edif = document.getElementById(key);
  cambiaInput(parseFloat(edif.attributes[1].value), parseFloat(edif.attributes[2].value));
}

function cambiaInput(lat, lng) {
  console.log("y");
  document.getElementById("latitud").value = lat;
  document.getElementById("longitud").value = lng;
  verUbicacion(lat, lng);
}

function verUbicacion(latitud, longitud) {
  if (locMarker != null) {
    map.removeLayer(locMarker); //si hay marcador de localización, se borra
  }
  const locCoords = [latitud, longitud];
  locMarker = L.marker(locCoords);
  locMarker.bindPopup('¿Aquí está el lugar que quieres agregar?').openPopup();
  map.addLayer(locMarker);
}
