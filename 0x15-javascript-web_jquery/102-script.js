document.addEventListener('DOMContentLoaded', () =>
  $('INPUT#btn_translate').click(() =>
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' +
    $('INPUT#language_code').val(), (data) =>
      $('DIV#hello').html(data.hello))));
