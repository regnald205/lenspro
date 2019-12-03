const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
  $('#message').fadeOut('slow');}
,3000);


$('.carousel').carousel();

// MDB Lightbox Init
$(function () {
    $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
    });
    //Multi item carousel gallery 





let mainNavLinks = document.querySelectorAll("nav ul li a");

mainNavLinks.forEach(link => {
    link.addEventListener("click", event => {
        event.preventDefault();
        let target = document.querySelector(event.target.hash);
        target.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      });
    });

//video
//$('#html5-videos').lightGallery(); 



