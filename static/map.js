function init(){
  var mapOptions = {
      zoom: 8,
    };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  var position = new GeolocationMarker(map);
  position.addListener('position_changed', function() {
    map.setCenter(position.getPosition());
  });
}

google.maps.event.addDomListener(window, 'load', init);

