setInterval(function () {
  var myImageElement = document.getElementById('frame');
  myImageElement.src = '/frame?rand=' + Math.random();
}, 500);

