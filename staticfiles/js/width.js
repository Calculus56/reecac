$( document ).ready(function() {
   function resize(){
   document.documentElement.style.setProperty('--height-var', window.innerHeight+'px');
   }
   window.onorientationchange = function() {
           window.location.reload();
       };
   resize()
   });