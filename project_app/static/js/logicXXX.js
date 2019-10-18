const API_KEY = "pk.eyJ1IjoiYW5kZXJzamgiLCJhIjoiY2sxODNlMDBzMDZ6cTNvcDFwZTh0eGJnNyJ9.UOYs4mSt5CSEuifzIxu1tA";

// Set up initial map center and zoom level
var map = L.map('map', {
  center: [36, 36], // EDIT latitude, longitude to re-center map
  zoom: 8,  // EDIT from 1 to 18 -- decrease to zoom out, increase to zoom in
  scrollWheelZoom: false
});

// // display Carto basemap tiles with light features and labels
// L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', {
//   attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>'
// }).addTo(map); // EDIT - insert or remove ".addTo(map)" before last semicolon to display by default

// display Stamen basemap tiles with colored terrain and labels
L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png', {
  attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
}).addTo(map); // EDIT - insert or remove ".addTo(map)" before last semicolon to display by default

// upload CSV file from local directory and display latitude and longitude coordinates as default blue markers on map

var customLayer = L.geoJson(null, {
  onEachFeature: function (feature, layer) {
    layer.bindPopup(feature.properties.event_type);
  }
});

const runLayer = omnivore.csv('../static/data/data.csv', null, customLayer)
  .on('ready', function () {
    // http://leafletjs.com/reference.html#map-fitbounds
    map.fitBounds(runLayer.getBounds());
  })
  .addTo(map);



// function createFeatures(earthquakeData) {
//   // Run the onEachFeature function once for each piece of data in the array
//   var earthquakes = L.geoJSON(earthquakeData, {
//     pointToLayer: function(feature, latlng) {
//       return L.circleMarker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], {
//         fillOpacity: 1,
//         color: chooseColor(feature.properties.event_type),
//         fillColor: chooseColor(feature.properties.event_type),
//         radius:  markerSize(feature.properties.event_type)
//       })
//     .bindPopup("<h3>" + feature.properties.event_type + "</h3><hr><p>" + new Date(feature.properties.event_date) + "</p><hr><p>Magnitude: " + feature.properties.event_type + "</p>");
//   },
// });
//   createMap(earthquakes)
// };

// // Sending our earthquakes layer to the createMap function
// function createMap(earthquakes) {

//   // Define streetmap and darkmap layers
//   var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//     attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//     maxZoom: 18,
//     id: "mapbox.satellite",
//     accessToken: API_KEY
//   });
  
//   // var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//   //   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//   //   maxZoom: 18,
//   //   id: "mapbox.dark",
//   //   accessToken: API_KEY
//   // });
  
//   // // Define a baseMaps object to hold our base layers
//   // var baseMaps = {
//   //   "Street Map": streetmap,
//   //   "Dark Map": darkmap
//   // };
  
//   // Create overlay object to hold our overlay layer
//   var overlayMaps = {
//     Earthquakes: earthquakes
//   };
  
//   // Create our map, giving it the streetmap and earthquakes layers to display on load
//   var myMap = L.map("map", {
//     center: [
//       36, 36
//     ],
//     zoom: 1,
//     layers: [streetmap, earthquakes]
//   });
  
  
//   // Create a layer control
//   // Pass in our baseMaps and overlayMaps
//   // Add the layer control to the map
//   // L.control.layers(baseMaps, overlayMaps, {
//   //   collapsed: true
//   // }).addTo(myMap);
//   legend.addTo(myMap);
//   }
