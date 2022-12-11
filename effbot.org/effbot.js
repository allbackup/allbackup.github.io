// effbot.js

function effbot_download() {
 function platform(cx) {
  var div = document.getElementById('effbot_download');
  var els = div.getElementsByTagName('div');
  for (var i = 0; i < els.length; i++) {
   var e = els[i];
   var c = e.getAttribute("class") || e.getAttribute("className");
   if (c == cx) {
    e.setAttribute("class", cx + " highlight");
    e.setAttribute("className", cx + " highlight");
    if (i != 0)
     div.insertBefore(div.removeChild(e), els[0]);
    return;
   }
  }
  if (cx != "source")
    platform("source"); // fallback
 }
 var p = navigator.platform;
 if (p.indexOf("Win") != -1)
  platform("windows");
 else if (p.indexOf("Mac") != -1)
  platform("mac");
 else if (p.indexOf("Linux") != -1)
  platform("linux");
 else
  platform("source");
}

