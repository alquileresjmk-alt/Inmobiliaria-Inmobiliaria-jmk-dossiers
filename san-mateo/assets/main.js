// Visor de imágenes: abre la foto ampliada sin salir de la página.
(function () {
  var dialog = document.querySelector('dialog.lb');
  if (!dialog || typeof dialog.showModal !== 'function') return; // sin soporte: el enlace abre la imagen
  var img = dialog.querySelector('img');
  document.querySelectorAll('a[data-lb]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      var thumb = link.querySelector('img');
      img.src = link.href;
      img.alt = thumb ? thumb.alt : '';
      dialog.showModal();
    });
  });
  dialog.addEventListener('click', function (event) {
    if (event.target === dialog || event.target === img) dialog.close();
  });
  dialog.addEventListener('close', function () { img.removeAttribute('src'); });
})();
