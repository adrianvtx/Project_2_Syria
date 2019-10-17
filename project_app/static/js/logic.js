
// Set up initial map center and zoom level
var map = L.map('map', {
  center: [36, 36], // EDIT latitude, longitude to re-center map
  zoom: 8,  // EDIT from 1 to 18 -- decrease to zoom out, increase to zoom in
  scrollWheelZoom: false
});

// display Carto basemap tiles with light features and labels
L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>'
}).addTo(map); // EDIT - insert or remove ".addTo(map)" before last semicolon to display by default

// display Stamen basemap tiles with colored terrain and labels
L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png', {
  attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
}); // EDIT - insert or remove ".addTo(map)" before last semicolon to display by default

// upload CSV file from local directory and display latitude and longitude coordinates as default blue markers on map

var customLayer = L.geoJson(null, {
  onEachFeature: function (feature, layer) {
    layer.bindPopup(feature.properties.event_type);
  }
});

var runLayer = omnivore.csv('../static/data/data.csv', null, customLayer)
  .on('ready', function () {
    // http://leafletjs.com/reference.html#map-fitbounds
    map.fitBounds(runLayer.getBounds());
  })
  .addTo(map);
