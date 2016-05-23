var abacus = angular.module('abacusApp', ['ngRoute', 'pusher-angular']);

abacus.config(function($routeProvider){
  $routeProvider.when('/',
    {
      templateUrl: "views/home.html",
      controller: "HomeCtrl"
    })
    .otherwise({
        redirectTo: '/'
    });
});

abacus.controller('HomeCtrl', function ($scope, $pusher, $http) {
  var client = new Pusher('3a07e26ad5dafe9ae4ca');
  var pusher = $pusher(client);
  var channel = pusher.subscribe('abacus_channel');

  channel.bind('updated', function(data) {
    //console.log(data);
    $scope.number = data;
  });

  var getNumber = function() {
    $http.get("http://127.0.0.1:5000")
    .then(function(response) {
        alert("response");
        $scope.number = response.data;
    });
  }

  //getNumber();
});