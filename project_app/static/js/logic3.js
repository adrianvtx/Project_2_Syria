const API_KEY = "pk.eyJ1IjoiYW5kZXJzamgiLCJhIjoiY2sxODNlMDBzMDZ6cTNvcDFwZTh0eGJnNyJ9.UOYs4mSt5CSEuifzIxu1tA";

var link = https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson";


function chooseColor(mag) {
  return (mag >= 5) ? "red"
        : (mag >= 4) ? "orange"
        : (mag >= 3) ? "blue"
        : (mag >= 2) ? "yellow"
        : (mag >= 1) ? "green"
        : "cyan"
  };

function markerSize(mag) {
  return (mag*.2)**10;
}
// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a GeoJSON layer with the retrieved data
  let earthquakeData = data;
  createFeatures(earthquakeData);
});

var legend = L.control({ position: "bottomleft"});
legend.onAdd = function(grades) {
  var div = L.DomUtil.create("div", "legend"),
  grades = [0, 1, 2, 3, 4, 5],
  labels = ["less than 1", "1 - 2", "2 - 3", "3 - 4", "4 - 5", "5 <"];

  // loop through our magnitudes and generate a label with a colored square for each mag
for (var i = 0; i < grades.length; i++) {
    div.innerHTML += '<i style="background:' + chooseColor(grades[i] + 1) + '"></i> ' +	grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
  }
  return div;
  };


function createFeatures(earthquakeData) {
  // Run the onEachFeature function once for each piece of data in the array
  var earthquakes = L.geoJSON(earthquakeData, {
    pointToLayer: function(feature, latlng) {
      return L.circleMarker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], {
        fillOpacity: 1,
        color: chooseColor(feature.properties.mag),
        fillColor: chooseColor(feature.properties.mag),
        radius:  markerSize(feature.properties.mag)
      })
    .bindPopup("<h3>" + feature.properties.place + "</h3><hr><p>" + new Date(feature.properties.time) + "</p><hr><p>Magnitude: " + feature.properties.mag + "</p>");
  },
});
  createMap(earthquakes)
};



// Sending our earthquakes layer to the createMap function
function createMap(earthquakes) {

// Define streetmap and darkmap layers
var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
});

// var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//   maxZoom: 18,
//   id: "mapbox.dark",
//   accessToken: API_KEY
// });

// // Define a baseMaps object to hold our base layers
// var baseMaps = {
//   "Street Map": streetmap,
//   "Dark Map": darkmap
// };

// Create overlay object to hold our overlay layer
var overlayMaps = {
  Earthquakes: earthquakes
};

// Create our map, giving it the streetmap and earthquakes layers to display on load
var myMap = L.map("map", {
  center: [
    37.09, -95.71
  ],
  zoom: 1,
  layers: [streetmap, earthquakes]
});


// Create a layer control
// Pass in our baseMaps and overlayMaps
// Add the layer control to the map
// L.control.layers(baseMaps, overlayMaps, {
//   collapsed: true
// }).addTo(myMap);
legend.addTo(myMap);
}
