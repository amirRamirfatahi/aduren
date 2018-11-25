// JavaScript Document
var animation = bodymovin.loadAnimation({
  container: document.getElementById('bm'),
  renderer: 'svg',
  loop:false,
  autoplay: false,
  path: 'data.json'
})
var anim;

anim = bodymovin.loadAnimation(animation);