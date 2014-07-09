var GET_INFO_PATH = '/locate/'
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
  });
}


google.maps.event.addDomListener(window, 'load', init);

