Locate me API
====
So all methods return the same JSON. lol.
  {key: session key,
   lat: latitude,
   lng: longitude
  }
- *POST* /locate/ : Creates a new session and returns the session ID in a JSON object.

- *POST* /locate/\<key\>/ : Updates the apprpriate record and returns the above object.

Both POST requests require the same JSON data, and ensure your content-type is application/json: {lat: latitude, lng: longitude}

- *GET* /locate/\<key\>/: Retrieve seturns the aforementioned object


- *DELTE???* lol
