        // find template and compile it
        /*

        var templateSource = document.getElementById('results-template').innerHTML,
            template = Handlebars.compile(templateSource),
            resultsPlaceholder = document.getElementById('results'),
            playingCssClass = 'playing',
            audioObject = null;

        */
$(function () {
  console.log("spotify");



        var fetchTracks = function (albumId, callback) {
            $.ajax({
                url: 'https://api.spotify.com/v1/albums/' + albumId,
                success: function (response) {
                    console.log(response);
                }
            });
        };

        var searchAlbums = function (query) {
            query = "king kunta";
            //console.log("searching:" + query);
            $.ajax({
                url: 'https://api.spotify.com/v1/search',
                contentType: "application/json",
                crossOrigin: true,
                data: {
                    q: query,
                    type: 'track'
                     
                },
               
                success: function (response) {
                    console.log("Success");
                    console.log(response)
                },
                error: function (response) {
                    console.log("Failed");
                    console.log(response);


                }
            });
        };
        /*
        $('#search').on('click', function () {
            console.log("clicked");
            search_query = $('#query').value;
            console.log(search_query);
            searchAlbums('king kunta');
            

        });
        */
         $('#search-form').on('submit', function () {
           console.log("submit")
           console.log($('#query').value);
           searchAlbums($('#query').value);
        });


});