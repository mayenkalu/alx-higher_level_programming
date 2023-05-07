$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/hello/';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
