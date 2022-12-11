//Create map and load map overlay from google
const map = L.map('map', {tap: false});

// Create a new marker grou called airportMarkers
const airportMarkers = L.featureGroup().addTo(map);

L.tileLayer('https://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  minZoom: 4,
  noWrap: true, // disables multiple side by side maps
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60.317222, 24.963333], 0); //set start view
map.setMaxBounds(
    [[84.67351256610522, -174.0234375], [-75.995311187950925, 250.2421875]]); //Sets dragging borders so player cant lose sight of map

// This checks if username and password are correct and returns the response in json fromat
async function fetch_login(username, password) {
  try {
    return fetch(
        `https://make-s.duckdns.org:15486/continue_game/${username},${password}`).
        then(response => response.json());
  } catch (error) {
    console.log(error.message);
  }
}

// This function fetches json from the specified address and returns the response in json fromat
async function fetch_player(player_name) {
  try {
    return fetch(`https://make-s.duckdns.org:15486/get_player/${player_name}`).
        then(response => response.json());

  } catch (error) {
    console.log(error.message);
  }
}

// This function will fly you to the airport you selected
async function fly_to(username, airport) {
  try {
    await fetch(
        `https://make-s.duckdns.org:15486/fly_to/${username},${airport}`).
        then(response => response.json());
  } catch (error) {
    console.log(error.message);
  }
}

// This function will show the available flights on the map as blue dots and the player as a red dot
function set_map_points(jsonData, username) {

  // We clear the map of any markers
  airportMarkers.clearLayers();

  // We set the view to the player location
  map.setView([
    jsonData['player_data']['location'][1],
    jsonData['player_data']['location'][2]], 9);

  let player_name = document.getElementById('player_name');
  player_name.innerText = jsonData['player_data']['screen_name'];

  let co2_consumed = document.getElementById('co2_consumed');
  co2_consumed.innerText = `CO2 consumed: ${jsonData['player_data']['co2_consumed']}`;

  // We test if the player has any flights available
  if (jsonData['flights'][0] != null) {

    // We set the blue pins on the map
    for (let i = 0; i < jsonData['flights'].length; i++) {
      const marker = L.marker(
          [jsonData['flights'][i][1], jsonData['flights'][i][2]]).addTo(map);

      // We add the blue markers to a group called airportMarkers
      airportMarkers.addLayer(marker);

      // This part of code handles the marker pin and button
      const popupContent = document.createElement('div');

      const h4 = document.createElement('h4');
      h4.innerHTML = jsonData['flights'][i][0];
      h4.innerHTML += `<br>${jsonData['flights'][i][3]}`
      h4.innerHTML += `<br>${jsonData['flights'][i][4]}`
      h4.innerHTML += `<br>${jsonData['flights'][i][5]}`
      h4.innerHTML += `<br>${jsonData['flights'][i][6]}`
      popupContent.append(h4);

      const goButton = document.createElement('button');
      goButton.classList.add('button');
      goButton.innerHTML = 'Fly here';
      popupContent.append(goButton);

      marker.bindPopup(popupContent);

      // We add a click event listener to the button inside the marker pin
      goButton.addEventListener('click', function() {

        // Debug log the airport ICAO code
        console.log(jsonData['flights'][i][0]);

        // We move the player to the location they clicked
        fly_to(username, jsonData['flights'][i][0]).then(null);

        // We again fetch the player data from the Flask server
        fetch_player(username).then(player_data => {

          // We again set the map pins and zoom
          set_map_points(player_data, username);
        });
      });
    }
  }

  // If the player has no flights available, we give them the option to fly back to Helsinki Airport
  else {
    const marker = L.marker([60.317222, 24.963333]).addTo(map);

    // We add the blue markers to a group called airportMarkers
    airportMarkers.addLayer(marker);

    // This part of code handles the marker pin and button
    const popupContent = document.createElement('div');
    const h4 = document.createElement('h4');
    h4.innerHTML = 'EFHK';
    popupContent.append(h4);

    const goButton = document.createElement('button');
    goButton.classList.add('button');
    goButton.innerHTML = 'Fly here';
    popupContent.append(goButton);

    marker.bindPopup(popupContent);

    // We add a click event listener to the button inside the marker pin
    goButton.addEventListener('click', function() {

      // We move the player to the location they clicked
      fly_to(username, 'EFHK').then(null);

      // We again fetch the player data from the Flask server
      fetch_player(username).then(player_data => {

        // We again set the map pins and zoom
        set_map_points(player_data, username);
      });
    });
  }

  // We set the player location on the map
  let playerLocation = L.circle([
    jsonData['player_data']['location'][1],
    jsonData['player_data']['location'][2]], { //Player location
    color: 'red',
    fillColor: 'red',
    fillOpacity: 0.8,
    radius: 10500,
  }).addTo(map);
  playerLocation.bindPopup(`You are here`);

  airportMarkers.addLayer(playerLocation);
}

//Guide modal code starts here
let modal_button = document.getElementById('guide_modal');

//Adding click-event listener to button
modal_button.addEventListener('click', function handleClick(evt) {

  //Prevent the default action of the button element
  evt.preventDefault();

  //debug console log
  console.log('Guide button pressed');

  let modal = document.querySelector('dialog');

  modal.showModal();

  let span = modal.getElementsByTagName('span');

  //Adding the closing function to X-button inside the modal
  for (let btn of span) {
    btn.addEventListener('click', () => {

      //another debug console log
      console.log('close guide modal');

      modal.close();
    });
  }
});
// Guide modal code ends here

// Login starts here
const login_button = document.getElementById('login_button');

// Add a click event listener to login button
login_button.addEventListener('click', function(evt) {

  // Prevent the default action of the button
  evt.preventDefault();

  let username = document.querySelector('input[name="username"]').value;
  let password = document.querySelector('input[name="password"]').value;

  // We fetch the login data from Flask server
  fetch_login(username, password).then(login_data => {

    // We test if the Flask server responds with true
    if (login_data['value'] === 'true') {

      // We fetch the player data from the Flask server
      fetch_player(username).then(player_data => {

        // We set the map pins and zoom
        set_map_points(player_data, username);
      });

      // If the server returns anything other than true, we pop an alert box with the message from the Flask server
    } else {
      alert(login_data['message']);
    }

  });

});
