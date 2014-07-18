var GET_INFO_PATH = '/locate/'
var map = null;
var position = null;

function init(){
  var mapOptions = {
      zoom: 8,
    };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  position = new GeolocationMarker(map);
  position.addListener('position_changed', function() {
    map.setCenter(position.getPosition());
  });
  if(!window.location.pathname == "/"){
    updateLocation();
  }
}

function updateLocation(){
  var key = window.location.pathname.split('/');
  if(key[key.length-1] == ''){
    key = key[key.length-2];
  }
  else {
    key = key[key.length-1];
  }
  $.ajax({
    url: GET_INFO_PATH + key + '/'
  }).complete(function(d){
    var lat = d.responseJSON.lat;
    var lng = d.responseJSON.lng;
    console.log(lat);
    console.log(lng);
    var p = new google.maps.LatLng(lat, lng);
    var marker = new google.maps.Marker( {
      position: p,
      map: map
    });
  });
}


google.maps.event.addDomListener(window, 'load', init);

