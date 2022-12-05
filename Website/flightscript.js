//Create map and load map overlay from openstreetmap

const map = L.map('map', {tap: false});
L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
  maxZoom: 9,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60.319120, 24.955821], 13);
//TODO: adding circles to available airport connections and

//Guide modal code starts here
let modal_button = document.getElementById('guide_modal');

//Adding click-event listener to button
modal_button.addEventListener('click', function handleClick(evt) {

  //Prevent the default action of the button element
  evt.preventDefault();

  //debug console log
  console.log('button pressed');

  let modal = document.querySelector('dialog');

  modal.showModal();

  let span = modal.getElementsByTagName('span');

  //Adding the closing function to X-button inside the modal
  for (let btn of span) {
    btn.addEventListener('click', () => {

      //another debug console log
      console.log('close modal');

      modal.close();
    });

  }

});

//Guide modal code ends here
