$(document).ready(function () {
  $("#des").click(function () {
    $("#des").hide();
    $(".show").show();
  });
  $(".show").click(function () {
    $("#des").show();
    $(".show").hide();
  });
});
