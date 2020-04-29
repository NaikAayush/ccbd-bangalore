/**
 * Adds a polygon to the map
 *
 * @param  {H.Map} map      A HERE Map instance within the application
 */
/*
 var points = [{'lat': 13.019121, 'lng': 77.3801937},
 {'lat': 12.96214, 'lng': 77.38071},
 {'lat': 12.93555, 'lng': 77.37777},
 {'lat': 12.99586, 'lng': 77.37314}];
*/
//var points = JSON.parse('{{  final | tojson  }}');
//var no_of_outputs=appConfig.no_of_outputs;
var points=appConfig.final;
//var no_of_outputs=appConfig.no_of_outputs;
function addPolygonToMap(map,points) {
	var lineString = new H.geo.LineString();
	points.forEach(function(point) {
		lineString.pushPoint(point);
	});

	map.addObject(
		new H.map.Polygon(lineString, {
			style: {
				fillColor: '#126C2B',
				strokeColor: '#126C2B',
				lineWidth: 10
			}
		})
	);
}

/**
 * Boilerplate map initialization code starts below:
 */

//Step 1: initialize communication with the platform
// In your own code, replace variable window.apikey with your own apikey
var platform = new H.service.Platform({
	apikey: 'NV894oRoVT9hPq5Ywn01TrNm_q48u5SRtlLYpP8hLDs'
});
var defaultLayers = platform.createDefaultLayers();

//Step 2: initialize a map - this map is centered over Europe

var map = new H.Map(document.getElementById('map'), defaultLayers.vector.normal.map, {
	center: { lat: 12.979075, lng:77.585747},
	zoom: 12,
	pixelRatio: window.devicePixelRatio || 1
});

// add a resize listener to make sure that the map occupies the whole container
window.addEventListener('resize', () => map.getViewPort().resize());
//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// Create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);

// Now use the map as required...
//for (i = 0; i < no_of_outputs; i++) {
	//addPolygonToMap(map,points);
  //text += "The number is " + i + "<br>";
//}
addPolygonToMap(map,points)
