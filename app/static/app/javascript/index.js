$(document).ready(function(){
$("#lei").hover(
  // Mouse Over
  function(){

    $("#ed").css("opacity","0.5"),
    $("#prf").css("opacity","0.5"),
    $("#per").css("opacity","0.5");

  },
  // Mouse Out
  function(){

      $("#prf").css("opacity","1"),
      $("#per").css("opacity","1"),
      $("#ed").css("opacity","0.5");
});

$("#per").hover(
  // Mouse Over
  function(){

    $("#ed").css("opacity","0.5"),
    $("#prf").css("opacity","0.5"),
    $("#lei").css("opacity","0.5");

  },
  // Mouse Out
  function(){

      $("#prf").css("opacity","1"),
      $("#ed").css("opacity","1"),
      $("#lei").css("opacity","1");
});
$("#ed").hover(
  // Mouse Over
  function(){

    $("#lei").css("opacity","0.5"),
    $("#prf").css("opacity","0.5"),
    $("#per").css("opacity","0.5");

  },
  // Mouse Out
  function(){
      $("#lei").css("opacity","1"),
      $("#prf").css("opacity","1"),
      $("#per").css("opacity","1");
});

$("#prf").hover(
  // Mouse Over
  function(){

    $("#ed").css("opacity","0.5"),
    $("#lei").css("opacity","0.5"),
    $("#per").css("opacity","0.5");

  },
  // Mouse Out
  function(){
      $("#ed").css("opacity","1"),
      $("#lei").css("opacity","1"),
      $("#per").css("opacity","1");
});

  $(".slide-section").click(function(e){

      var linkHref = $(this).attr("href");
      $('html,body').animate({
         scrollTop: $(linkHref).offset().top
      }, 1000);
      e.preventDefault();
  });

    $(document).ready(function(){
    $('.hb-button').on('click', function(){
        $('nav ul').toggleClass('show');
        $('.hb-button').css('z-index','1');

    });
});

});
