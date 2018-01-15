$(document).ready(function(){
    $(".slide-section").click(function(e){

      var linkHref = $(this).attr("href");
      $('html,body').animate({
         scrollTop: $(linkHref).offset().top
      }, 1000);
      e.preventDefault();
  });

  $("#console").keyup(function(event){
    if(event.keyCode == 13) {
        $("#submitField").click();
    }
});

    $(document).ready(function(){
    $('.hb-button').on('click', function(){
        $('nav ul').toggleClass('show');
        $('.hb-button').css('z-index','1');

    });
    $('.btn-group>.btn').click(function(){
       $(this).addClass("active").siblings().removeClass("active");
    });

});
});
