//Create map and load map overlay from openstreetmap

const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  minZoom: 4,
  noWrap: true, // disables multiple side by side maps
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60.319120, 24.955821], 9); //set start view
map.setMaxBounds(
    [[84.67351256610522, -174.0234375], [-75.995311187950925, 250.2421875]]); //Sets dragging borders so player cant lose sight of map

// Player circle = red, available flights should = blue

// This monster fetches json from the specified address and passes it on to the function appendData
async function asynchronousFunction(player_name) {

  console.log('asynchronous download begins');
  try {
    fetch(`http://127.0.0.1:15486/get_player/${player_name}`).
        then(function(response) {
          return response.json();
        }).
        then(function(data) {
          appendData(data);
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

// This function will parse the fetched json data and log it to console for now
// TODO: Add functionality to this shit
function appendData(jsonData) {

  console.log(JSON.stringify(jsonData, null, 2));

  for (let i = 0; i < jsonData['flights'].length; i++) {

    const availableFlights =
        L.circle(
            [jsonData['flights'][i][1], jsonData['flights'][i][2]], { // Available flights TODO: Add real flights...
              color: 'blue',
              fillColor: 'blue',
              fillOpacity: 0.8,
              radius: 5000,
            }).addTo(map);

    availableFlights.bindPopup(`Location: ${jsonData['flights'][i][0]}`); // sets parameters for popup
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

//TODO: adding circles to available airport connections and player location

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

//Guide modal code ends here

let player = 'make';

let temp = asynchronousFunction(player);
