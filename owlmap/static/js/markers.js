function verUbicacion(latitud, longitud) {
  if (locMarker != null) {
    map.removeLayer(locMarker); //si hay marcador de localización, se borra
  }
  const locCoords = [latitud, longitud];
  locMarker = L.marker(locCoords);
  locMarker.bindPopup('¡Aquí está el lugar que buscas!').openPopup();
  map.addLayer(locMarker);
}

function verRuta(latitud, longitud) {
  if (ubMarker != null) { //ya hay alguna ubicación actual guardada
    if (ruta != null) {
      map.removeLayer(ruta); //si hay una ruta, se borra
    }

    verUbicacion(latitud, longitud);

    var url = "https://api.mapbox.com/directions/v5/mapbox/walking/" //url del api de mapbox
    + coords[1] + "," + coords[0] + ";"
    + longitud + "," + latitud +
    "?geometries=geojson&access_token=pk.eyJ1IjoicmF1bG15b2N1IiwiYSI6ImNqdnNma2pyZzBxcnQ0NG9lY2tnemZvaGgifQ.Xk8K-zL1ylQ4tV_QbolARg";

    var req = new XMLHttpRequest();
    req.responseType = 'json';
    req.open('GET', url, true);
    req.onload = function() {
      var steps = req.response.routes[0].geometry.coordinates;
      steps.forEach(function(point) { //se intercambian las coordenadas desordenadas
        var aux = point[0];
        point[0] = point[1];
        point[1] = aux;
      });
      steps.unshift([coords[0], coords[1]]); //se agrega el inicio y el final
      steps.push([latitud, longitud]);

      ruta = L.polyline(steps, {color: 'red'});
      ruta.addTo(map);
    };
    req.send();
  }
}
