$(document).ready(function(){
    $("#loading").css('visibility','visible');
    $("#root").css('visibility','hidden');
    setTimeout(function(){
      $("body").css({"margin-top":"200px"});
      $("#loading").remove();
      $("#root").css('visibility','visible');
    },1000);
    
    
    $("h2","#header1").on('click',function(){
        window.open("https://github.com/vikrantdeshpande09876/XML_to_CSV_Rep/","_blank");
    });
    $("i","#gotogithub").on('click',function(){
        window.open("https://github.com/vikrantdeshpande09876/XML_to_CSV_Rep/","_blank");
    });

      $("#gototop").on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop:0}, '300');
      });
      $(window).scroll(function() {
        if ($(window).scrollTop() > 300) {
          $("#gototop").addClass('show');
        } else {
          $("#gototop").removeClass('show');
        }
      });
});