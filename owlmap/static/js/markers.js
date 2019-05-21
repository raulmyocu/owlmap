function verUbicacion(latitud, longitud) {
  if (locMarker != null) {
    map.removeLayer(locMarker);
  }
  const coords = [latitud, longitud];
  locMarker = L.marker(coords);
  locMarker.bindPopup('¡Aquí está el lugar que buscas!').openPopup();
  map.addLayer(locMarker);
}
