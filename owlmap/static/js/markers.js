function verUbicacion(latitud, longitud) {
  const coords = [latitud, longitud];
  const locMarker = L.marker(coords, {icon: buhoIcono});
  locMarker.bindPopup('Aquí está el punto').openPopup();
  map.addLayer(locMarker);
}
