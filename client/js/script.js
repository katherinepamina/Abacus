var abacus = angular.module('abacusApp', ['ngRoute', 'pusher-angular']);

abacus.config(function($routeProvider){
  $routeProvider.when('/',
    {
      templateUrl: "views/home.html",
      controller: "HomeCtrl"
    })
    .otherwise({
        redirectTo: '/home'
    });
});

abacus.controller('HomeCtrl', function ($scope, $pusher, $http) {
  var client = new Pusher('3a07e26ad5dafe9ae4ca');
  var pusher = $pusher(client);
  var channel = pusher.subscribe('abacus_channel');
  var valToIndex = {}
  var foundMap = {};
  $scope.one = "5";
  $scope.two = "7";
  valToIndex[$scope.one] = $scope.one;
  valToIndex[$scope.two] = $scope.two;

  channel.bind('updated', function(data) {
    $scope.number = data;
    if ($scope.number in valToIndex) {
      found[$scope.number] = $scope.number;
    }
  });

  $scope.found = function(number) {
    if (number in foundMap) {
      return true;
    }
    else {
      return false;
    }
  }

});