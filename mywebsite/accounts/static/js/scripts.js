//Menu buttom animation
function menuAnimation(x) {
  x.classList.toggle("change");
}

//Opens and Closes Navbar
var sideNavOpen = 0;
function changeNav() {
  var width = window.innerWidth;
  if (sideNavOpen == 0) {
    if (width > 570) {
      document.getElementById("mySidenav").style.width = "250px";
      document.getElementById("main").style.marginLeft = "250px";
    }
    else {
      document.getElementById("mySidenav").style.width = "250px";
    }
    sideNavOpen = 1
  }
  else if (sideNavOpen == 1) {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    sideNavOpen = 0;
  }
}

//Navbar disapears on scroll
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("customNav").style.top = "0";
  } else {
    document.getElementById("customNav").style.top = "-100px";
  }
  prevScrollpos = currentScrollPos;
}
