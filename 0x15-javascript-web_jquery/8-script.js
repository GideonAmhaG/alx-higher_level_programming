$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (r) => {
  for (const film of r.results) {
    $('#list_movies').append($('<li></li>').text(film.title));
  }
});
