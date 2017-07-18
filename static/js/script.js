$(document).ready(function(){
  console.log("Admit One");

  var nav = $('#navigate');

  $(window).scroll(function(){
    var height = $(window).height();
    var point = height / 4;
    var top = $(window).scrollTop();

    if( top > point ) {
      nav.css("background", "black");
      //nav.css("border-bottom", "none");
    }
    else {
      nav.css("background", "transparent");
      //nav.css("border-bottom", "1px solid white");
    }

  });
});
