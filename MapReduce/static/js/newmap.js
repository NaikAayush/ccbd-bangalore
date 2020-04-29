var locations;
var coord;

function addCountryOutline(map,shape) {

    // clear map
    //markerGroup.removeAll();

    // set up polygon style
    var customStyle = {
        strokeColor: 'black',
        fillColor: 'rgba(0,175,170,0.5)',
        lineWidth: 2,
        lineJoin: 'bevel'
    };

    // the shape is returned as WKT and we need to convert it a Geometry
    var geometry = H.util.wkt.toGeometry(shape);
    // geometry is either a single or multi-polygon
    if (geometry instanceof H.geo.MultiGeometry) {
        var geometryArray = geometry.getGeometries();
        for (var i = 0; i < geometryArray.length; i++) {
            markerGroup.addObject(new H.map.Polygon(geometryArray[i].getExterior(), { style: customStyle }));
        }
    } else { // instanceof H.geo.Polygon
        markerGroup.addObject(new H.map.Polygon(geometry.getExterior(), { style: customStyle }));
    }
}

// step 1: initialize communication with the platform
var platform = new H.service.Platform({
    apikey: 'NV894oRoVT9hPq5Ywn01TrNm_q48u5SRtlLYpP8hLDs'
});
var defaultLayers = platform.createDefaultLayers();

// step 2: initialize a map - this map is centered over California
var map = new H.Map(
    document.getElementById('map'),
    defaultLayers.vector.normal.map,
    {
        zoom: 12,
        center: { lat: 12.972070, lng:  77.593949 }
});

// step 3: make the map interactive
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// step 4: create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);
var markerGroup = new H.map.Group();
map.addObject(markerGroup);

var i;
function start(){
for (i = 0; i < shapex.length; i++) {
  var shape=shapex[i];
  addCountryOutline(map,shape);
}
};

start();
