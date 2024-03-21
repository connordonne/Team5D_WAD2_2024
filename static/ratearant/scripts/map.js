function loadMapScenario() {
    var searchQuery = document.getElementById('restaurantAddress').innerHTML;   
    var name = document.getElementById('restaurantName').innerHTML;                 
    var map = new Microsoft.Maps.Map(document.getElementById('map'), {
        /* No need to set credentials if already passed in URL */
        center: new Microsoft.Maps.Location(55.860916, -4.251433),
        zoom: 19
    });

    Microsoft.Maps.loadModule('Microsoft.Maps.Search', function () {
        var searchManager = new Microsoft.Maps.Search.SearchManager(map);
        var requestOptions = {
            bounds: map.getBounds(),
            where: searchQuery,
            callback: function (answer, userData) {
                map.setView({ bounds: answer.results[0].bestView });
                var pin = new Microsoft.Maps.Pushpin(answer.results[0].location, {
                    color: 'red', title: name
                });
                map.entities.push(pin);
            }
        };
        searchManager.geocode(requestOptions);
    });
}