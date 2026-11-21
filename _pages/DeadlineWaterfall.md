---
layout: page
permalink: /DeadlineWaterfall/
title: 
nav: false
---

<style>
#dw{overflow-x:auto;margin-top:1rem;padding-bottom:1rem;--dw-line:var(--global-divider-color,rgba(128,128,128,.25));--dw-muted:var(--global-text-color-light,#888)}
#dw *{box-sizing:border-box}
.dw-inner{position:relative}
.dw-header{display:flex;padding-left:64px}
.dw-cat{padding:0 8px}
.dw-catbody{display:flex;height:100%}
.dw-catname{text-align:center;font-weight:700;padding-bottom:4px}
.dw-bracket{height:12px;border:2px solid var(--c);border-bottom:0;border-radius:14px 14px 0 0}
.dw-body{position:relative}
.dw-row{height:28px;border-bottom:1px solid var(--dw-line)}
.dw-row.dw-weekend{background:rgba(128,128,128,.06)}
.dw-row.dw-month{border-top:1px solid var(--dw-muted)}
.dw-row.dw-pastrow{opacity:.45}
.dw-row.dw-todayrow{background:rgba(255,82,82,.10);border-bottom-color:transparent}
.dw-num{display:block;width:56px;text-align:right;line-height:27px;font-size:12px;color:var(--dw-muted)}
.dw-month .dw-num{font-weight:700;color:var(--global-text-color,inherit)}
.dw-todayrow .dw-num{color:#ff5252;font-weight:700}
.dw-cats{position:absolute;left:64px;right:0;top:0;bottom:0;display:flex;z-index:1}
.dw-col{flex:1 1 0;position:relative;min-width:44px}
.dw-seg{position:absolute;left:50%;width:2px;margin-left:-1px;background:var(--c)}
.dw-arrow{position:absolute;left:50%;margin-left:-6px;width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:9px solid var(--c)}
.dw-date{position:absolute;left:50%;transform:translateX(-50%);font-size:11px;font-weight:600;white-space:nowrap;color:var(--c)}
.dw-label{position:absolute;left:50%;writing-mode:vertical-rl;transform:translateX(-50%) rotate(180deg);white-space:nowrap;font-size:12px;font-weight:600;padding:6px 1px;background:var(--global-bg-color,#fff);color:var(--global-text-color,inherit);text-decoration:none;z-index:2}
.dw-dim{opacity:.28}
.dw-label.dw-dim{opacity:1;color:var(--dw-muted)}
.dw-today{position:absolute;left:0;right:0;height:2px;background:#ff5252;box-shadow:0 0 6px 1px rgba(255,82,82,.9),0 0 18px 4px rgba(255,82,82,.45);z-index:3;pointer-events:none}
</style>
<div id="dw"></div>
<script>
(function () {
  var DATA = {{ site.data.deadlines | jsonify }};
  var ROW = 28, GUT = 64, COLW = 44, DAY = 86400000;
  var PALETTE = ['#29b6f6', '#ffa726', '#66bb6a', '#ab47bc', '#ec407a', '#8d6e63'];
  var MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var root = document.getElementById('dw');
  if (!root || !DATA || !DATA.categories) return;
  var PAST = DATA.past_days != null ? +DATA.past_days : 7;
  var TAIL = DATA.tail_days != null ? +DATA.tail_days : 5;
  var now = new Date();
  var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  var start = new Date(today.getFullYear(), today.getMonth(), today.getDate() - PAST);
  function parse(s) { var p = String(s).slice(0, 10).split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function idx(d) { return Math.round((d - start) / DAY); }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  var todayY = PAST * ROW + ROW / 2;
  var labels = [];
  var cats = [];
  var last = new Date(today.getFullYear(), today.getMonth(), today.getDate() + 14);
  DATA.categories.forEach(function (c, ci) {
    var items = (c.items || []).map(function (it) {
      return { name: it.name, url: it.url, date: parse(it.date) };
    }).filter(function (it) { return !isNaN(it.date.getTime()) && it.date >= start; });
    if (!items.length) return;
    items.sort(function (a, b) { return a.date - b.date; });
    items.forEach(function (it) { if (it.date > last) last = it.date; });
    cats.push({ name: c.name, color: c.color || PALETTE[ci % PALETTE.length], items: items });
  });
  if (!cats.length) { root.textContent = 'No upcoming deadlines to show. Add some in _data/deadlines.yml.'; return; }
  function buildItem(it) {
    var col = el('div', 'dw-col');
    var endY = idx(it.date) * ROW + ROW / 2;
    var isPast = endY < todayY;
    var above = el('div', 'dw-seg dw-dim');
    above.style.top = '0px';
    above.style.height = Math.min(endY, todayY) + 'px';
    col.appendChild(above);
    if (endY > todayY) {
      var below = el('div', 'dw-seg');
      below.style.top = todayY + 'px';
      below.style.height = (endY - todayY) + 'px';
      col.appendChild(below);
    }
    var arrow = el('div', 'dw-arrow' + (isPast ? ' dw-dim' : ''));
    arrow.style.top = (endY - 9) + 'px';
    col.appendChild(arrow);
    var dateTxt = MON[it.date.getMonth()] + ' ' + it.date.getDate();
    var dl = el('div', 'dw-date' + (isPast ? ' dw-dim' : ''), dateTxt);
    dl.style.top = (endY + 2) + 'px';
    col.appendChild(dl);
    var lab = el(it.url ? 'a' : 'div', 'dw-label' + (isPast ? ' dw-dim' : ''), it.name);
    if (it.url) { lab.href = it.url; lab.target = '_blank'; lab.rel = 'noopener'; }
    lab.title = it.name + ' (' + dateTxt + ', ' + it.date.getFullYear() + ')';
    col.appendChild(lab);
    labels.push({ lab: lab, endY: endY });
    return col;
  }
  function placeLabels() {
    labels.forEach(function (o) {
      var h = o.lab.offsetHeight;
      var anchor = Math.min(o.endY, todayY);
      var fits = o.endY > todayY && h <= (o.endY - todayY - 30);
      var top = fits ? todayY + 14 : Math.max(0, anchor - 12 - h);
      o.lab.style.top = top + 'px';
    });
  }
  var n = idx(last) + TAIL + 1;
  var inner = el('div', 'dw-inner');
  var header = el('div', 'dw-header');
  var body = el('div', 'dw-body');
  var rows = el('div', 'dw-rows');
  var box = el('div', 'dw-cats');
  var minTotal = GUT;
  body.style.height = (n * ROW) + 'px';
  cats.forEach(function (c) {
    var k = c.items.length;
    var minW = Math.max(k * COLW + 16, 110);
    minTotal += minW;
    var head = el('div', 'dw-cat');
    head.style.flex = k + ' 1 0px';
    head.style.minWidth = minW + 'px';
    head.style.setProperty('--c', c.color);
    head.appendChild(el('div', 'dw-catname', c.name));
    head.appendChild(el('div', 'dw-bracket'));
    header.appendChild(head);
    var cat = el('div', 'dw-cat dw-catbody');
    cat.style.flex = k + ' 1 0px';
    cat.style.minWidth = minW + 'px';
    cat.style.setProperty('--c', c.color);
    c.items.forEach(function (it) { cat.appendChild(buildItem(it)); });
    box.appendChild(cat);
  });
  for (var i = 0; i < n; i++) {
    var d = new Date(start.getFullYear(), start.getMonth(), start.getDate() + i);
    var cls = 'dw-row';
    if (i < PAST) cls += ' dw-pastrow';
    if (i === PAST) cls += ' dw-todayrow';
    if (d.getDay() === 0 || d.getDay() === 6) cls += ' dw-weekend';
    if (d.getDate() === 1) cls += ' dw-month';
    var row = el('div', cls);
    var txt = i === PAST ? 'Today' : ((d.getDate() === 1 || i === 0) ? MON[d.getMonth()] + ' ' + d.getDate() : String(d.getDate()));
    row.appendChild(el('span', 'dw-num', txt));
    rows.appendChild(row);
  }
  var tl = el('div', 'dw-today');
  tl.style.top = (todayY - 1) + 'px';
  body.appendChild(rows);
  body.appendChild(box);
  body.appendChild(tl);
  inner.appendChild(header);
  inner.appendChild(body);
  inner.style.minWidth = minTotal + 'px';
  root.appendChild(inner);
  placeLabels();
  window.addEventListener('load', placeLabels);
})();
</script>