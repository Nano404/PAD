function initMap() {
  // The location
  const uluru = { lat: 52.354320, lng: 4.912691 };
  // The map
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: uluru,
  });
  // IC101-c5
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}