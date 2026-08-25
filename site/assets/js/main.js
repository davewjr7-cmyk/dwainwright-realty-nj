// Mobile nav toggle
document.addEventListener('click', function (e) {
  var t = e.target.closest('.nav-toggle');
  if (t) {
    var nav = document.querySelector('.main-nav');
    if (nav) nav.classList.toggle('open');
  }
  // Search widget tabs
  var tab = e.target.closest('.search-tabs button');
  if (tab) {
    document.querySelectorAll('.search-tabs button').forEach(function (b) { b.classList.remove('active'); });
    tab.classList.add('active');
    var ph = tab.getAttribute('data-ph');
    var input = document.querySelector('.search-body input');
    if (ph && input) input.setAttribute('placeholder', ph);
  }
});
// Listing carousel arrows
document.addEventListener('click', function (e) {
  var arrow = e.target.closest('.lc-arrow');
  if (!arrow) return;
  var wrap = arrow.closest('.listing-carousel');
  var track = wrap && wrap.querySelector('.lc-track');
  if (!track) return;
  var dist = Math.min(track.clientWidth * 0.85, 720);
  track.scrollBy({ left: arrow.classList.contains('lc-next') ? dist : -dist, behavior: 'smooth' });
});
// Prevent submit on demo search
document.addEventListener('submit', function (e) {
  if (e.target.matches('.demo-form')) {
    e.preventDefault();
    alert('This is a visual demo of the search. Connect your IDX/MLS provider to enable live results.');
  }
});
