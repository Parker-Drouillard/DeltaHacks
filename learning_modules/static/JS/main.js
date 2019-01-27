window.onscroll = function (e) {
    var vertical_position = 0;
    if (pageYOffset)//usual
      vertical_position = pageYOffset;
    else if (document.documentElement.clientHeight)//ie
      vertical_position = document.documentElement.scrollTop;
    else if (document.body)//ie quirks
      vertical_position = document.body.scrollTop;
  
    var your_div = document.getElementById('whiteout');
    your_div.top = (vertical_position + 200) + 'px';//200 is arbitrary.. just to show you could now position it how you want
  }


window.onload = function(){
  var loadingScreen = document.getElementById("loadingScreen");
  if(loadingScreen){
    loadingScreen.style.display = "none";
  }
}