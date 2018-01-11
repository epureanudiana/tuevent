$(document).ready(function(){
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
    
    
    $(document).on('click', '.browse', function(){
  var file = $(this).parent().parent().parent().find('.file');
  file.trigger('click');
});
$(document).on('change', '.file', function(){
  $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
});
    $('.remove_button').click(function(){
       $(this).closest('.card2').hide(); 
    });
});