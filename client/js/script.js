var abacus = angular.module('abacusApp', ['ngRoute']);

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

abacus.controller('HomeCtrl', function ($scope) {
  $scope.cow = "moo";
});