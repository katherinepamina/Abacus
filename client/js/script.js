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
  var falseMap = {};

  $scope.one = "5";
  $scope.two = "60";
  $scope.three = "16";
  $scope.four = "7920";

  valToIndex[$scope.one] = "五";
  valToIndex[$scope.two] = "六十";
  valToIndex[$scope.three] = "十六";
  valToIndex[$scope.four] = "七千九百二十";

  falseMap["4"] = "4";
  falseMap["69"] = "69";
  falseMap["7"] = "7";
  falseMap["42"] = "42";
  falseMap["35"] = "35";
  falseMap["6535"] = "6535";

  if (Object.keys(foundMap).length == 4) {
    document.getElementsByTagName("body")[0].style.backgroundImage = "url('img/open.png')";
  }

  channel.bind('updated', function(data) {
    var number = data
    $scope.number = number;
    if (number in valToIndex) {
      foundMap[number] = number;
      if (number == $scope.one){
        document.getElementById('number_1').style.backgroundColor = "#00FF00";
        document.getElementById('number_1').firstChild.style.visibility = "visible";
        document.getElementById('5').style.color = "#00FF00";
      }
      else if (number == $scope.two){
        document.getElementById('number_2').style.backgroundColor = "#00FF00";
        document.getElementById('number_2').firstChild.style.visibility = "visible";
        document.getElementById('60').style.color = "#00FF00";

      }
      else if (number == $scope.three){
        document.getElementById('number_3').style.backgroundColor = "#00FF00";
        document.getElementById('number_3').firstChild.style.visibility = "visible";
        document.getElementById('16').style.color = "#00FF00";
      }
      else if (number == $scope.four){
        document.getElementById('number_4').style.backgroundColor = "#00FF00";
        document.getElementById('number_4').firstChild.style.visibility = "visible";
        document.getElementById('7920').style.color = "#00FF00";
      }

    }
    else if (number in falseMap) {
      if (number == "4") {
        document.getElementById("4").style.color = "red";
      }
      else if (number == "69") {
        document.getElementById("69").style.color = "red";
      }
      else if (number == "7") {
        document.getElementById("7").style.color = "red";
      }
      else if (number == "42") {
        document.getElementById("42").style.color = "red";
      }
      else if (number == "35") {
        document.getElementById("35").style.color = "red";
      }
      else if (number == "6535") {
        document.getElementById("6535").style.color = "red";
      }
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