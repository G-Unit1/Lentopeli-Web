//Create map and load map overlay from google
const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  minZoom: 4,
  noWrap: true, // disables multiple side by side maps
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60.317222, 24.963333], 0); //set start view
map.setMaxBounds(
    [[84.67351256610522, -174.0234375], [-75.995311187950925, 250.2421875]]); //Sets dragging borders so player cant lose sight of map

// This checks if username and password are correct


async function fetch_login(username, password) {
  return fetch(`https://make-s.duckdns.org:15486/log_in/${username},${password}`)
      .then(response => response.json())
}

/*
// This function fetches json from the specified address and passes it on to the function appendData
async function fetch_player(player_name) {

  console.log('asynchronous download begins');
  try {
    await fetch(`https://make-s.duckdns.org:15486/get_player/${player_name}`).
        then(function(response) {
          return response.json();
        }).
        then(function(data) {
          set_map_points(data);
        }).
        catch(function(err) {
          console.log(err);
        });

  } catch (error) {
    console.log(error.message);
  } finally {
    console.log('asynchronous load complete');
  }
}

// This function will show the available flights on the map as blue dots and the player as a red dot
async function set_map_points(jsonData) {

  map.setView([
    jsonData['player_data']['location'][1],
    jsonData['player_data']['location'][2]], 9); //set start view

  console.log(JSON.stringify(jsonData, null, 2));

  for (let i = 0; i < jsonData['flights'].length; i++) {

    const availableFlights =
        L.circle(
            [jsonData['flights'][i][1], jsonData['flights'][i][2]], { // Available flights
              color: 'blue',
              fillColor: 'blue',
              fillOpacity: 0.8,
              radius: 5000,
            }).addTo(map);

    availableFlights.bindPopup(
        `Location: ${jsonData['flights'][i][0]}<br><button type="submit" id="fly_here">Fly Here</button>`); // sets parameters for popup
  }

  let playerLocation = L.circle([
    jsonData['player_data']['location'][1],
    jsonData['player_data']['location'][2]], { //Player location
    color: 'red',
    fillColor: 'red',
    fillOpacity: 0.8,
    radius: 10500,
  }).addTo(map);
  playerLocation.bindPopup(`You are here`);
}

 */


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
})

// Guide modal code ends here

// Login starts here

const login_button = document.getElementById('login_button');

login_button.addEventListener('click', function(evt) {
  evt.preventDefault();

  let username = 'make';// document.querySelector('input[name="username"]').value;
  let password = '1234';// document.querySelector('input[name="password"]').value;

  // asynchronousFunction(username).then(r => {r = null;});

  fetch_login(username, password).then(data => {
    console.log(data)
  })

});
















