/* CloudCart front end: plain JavaScript, no framework. Talks to the JSON API under /api. */
'use strict';
const $ = (s, el = document) => el.querySelector(s);
const main = $('#main');
const money = c => '$' + (c / 100).toFixed(2);
const esc = s => String(s).replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch]));
let state = { me: { signedIn: false }, cart: { items: [], count: 0 }, products: [], categories: [] };
let uid = 0;

/* ---------- API ---------- */
async function api(method, path, body) {
  const res = await fetch('api' + path, {
    method, headers: body ? { 'Content-Type': 'application/json' } : {},
    body: body ? JSON.stringify(body) : undefined, credentials: 'same-origin'
  });
  let data = null;
  try { data = await res.json(); } catch (e) { /* empty body */ }
  if (!res.ok) { const err = new Error((data && data.error) || 'Something went wrong (' + res.status + ')'); err.status = res.status; throw err; }
  return data;
}

/* ---------- helpers ---------- */
let toastTimer;
function toast(msg, bad) {
  const t = $('#toast'); t.textContent = msg; t.className = 'toast show' + (bad ? ' bad' : '');
  clearTimeout(toastTimer); toastTimer = setTimeout(() => t.className = 'toast', 2600);
}
function stars(r) {
  const full = Math.round(r); return '<span class="stars" aria-label="Rated ' + r + ' out of 5">' + '★'.repeat(full) + '☆'.repeat(5 - full) + '<span>' + r.toFixed(1) + '</span></span>';
}
function stockTag(p) {
  if (p.stock === 0) return '<span class="tag out">Out of stock</span>';
  if (p.stock <= 5) return '<span class="tag low">Only ' + p.stock + ' left</span>';
  return '<span class="tag in">In stock</span>';
}
function setBadge() {
  const b = $('#badge'); b.hidden = state.cart.count === 0; b.textContent = state.cart.count;
  $('.cartlink').setAttribute('aria-label', 'Cart, ' + state.cart.count + ' items');
}
function setAccount() {
  const a = $('#account');
  a.textContent = state.me.signedIn ? state.me.name.split(' ')[0] + ' · Sign out' : 'Sign in';
  a.href = state.me.signedIn ? '#/signout' : '#/signin';
}
function markNav(name) {
  document.querySelectorAll('[data-nav]').forEach(a => a.classList.toggle('on', a.dataset.nav === name));
}
function go(route) { location.hash = route; }

/* ---------- product art: drawn SVG illustrations ---------- */
const ART = {
  keyboard: ['#1d5560', '#0f3038', () => {
    let k = ''; for (let r = 0; r < 4; r++) for (let c = 0; c < 10; c++) k += `<rect x="${86 + c * 22.5}" y="${118 + r * 22}" width="19" height="18" rx="4" fill="${r === 3 && c > 1 && c < 8 ? '#19c3b1' : '#cfe9e6'}"/>`;
    return `<rect x="70" y="100" width="260" height="106" rx="14" fill="#2c7b86"/><rect x="70" y="100" width="260" height="106" rx="14" fill="none" stroke="#8fe3d9" stroke-width="2" opacity=".5"/>${k}`; }],
  hub: ['#2a4f6b', '#122a3d', () => `<path d="M120 110c-30 0-50 20-50 40" fill="none" stroke="#8fb9d6" stroke-width="7" stroke-linecap="round"/><rect x="120" y="105" width="190" height="80" rx="16" fill="#cfd9e0"/><rect x="134" y="120" width="34" height="14" rx="3" fill="#2a3a46"/><rect x="178" y="120" width="34" height="14" rx="3" fill="#2a3a46"/><rect x="222" y="120" width="50" height="14" rx="3" fill="#19c3b1"/><rect x="134" y="150" width="60" height="12" rx="3" fill="#2a3a46"/><circle cx="288" cy="156" r="6" fill="#f5b942"/>`],
  monitor: ['#233b66', '#0f1c33', () => `<rect x="76" y="62" width="248" height="150" rx="10" fill="#0b1222" stroke="#aab7cc" stroke-width="6"/><rect x="86" y="72" width="228" height="130" rx="4" fill="url(#g)"/><path d="M96 190l50-60 36 40 30-28 70 48z" fill="#0fa597" opacity=".8"/><circle cx="268" cy="104" r="14" fill="#f5b942"/><rect x="186" y="212" width="28" height="30" fill="#aab7cc"/><rect x="150" y="240" width="100" height="10" rx="5" fill="#aab7cc"/><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1f5ea8"/><stop offset="1" stop-color="#0c2a52"/></linearGradient></defs>`],
  mouse: ['#35305e', '#1a1733', () => `<path d="M200 70c-40 0-62 30-62 80 0 52 24 82 62 82s62-30 62-82c0-50-22-80-62-80z" fill="#d7d3f2"/><path d="M200 70v78" stroke="#7a72b8" stroke-width="3"/><path d="M138 148h124" stroke="#7a72b8" stroke-width="3"/><rect x="192" y="90" width="16" height="34" rx="8" fill="#19c3b1"/>`],
  headphones: ['#4d2f5f', '#25142f', () => `<path d="M104 170v-18a96 96 0 0 1 192 0v18" fill="none" stroke="#e5d3f2" stroke-width="14" stroke-linecap="round"/><rect x="84" y="156" width="46" height="84" rx="20" fill="#b58ad6"/><rect x="270" y="156" width="46" height="84" rx="20" fill="#b58ad6"/><rect x="94" y="170" width="26" height="56" rx="12" fill="#6e3f94"/><rect x="280" y="170" width="26" height="56" rx="12" fill="#6e3f94"/>`],
  speaker: ['#5f3a2a', '#2c170f', () => `<rect x="100" y="86" width="200" height="130" rx="30" fill="#e8c7a8"/><circle cx="200" cy="135" r="34" fill="#5f3a2a"/><circle cx="200" cy="135" r="16" fill="#f5b942"/><circle cx="200" cy="190" r="9" fill="#5f3a2a"/><path d="M100 150h-14M300 150h14" stroke="#e8c7a8" stroke-width="6" stroke-linecap="round"/>`],
  mic: ['#5a2d3a', '#2a121b', () => `<rect x="170" y="52" width="60" height="110" rx="30" fill="#f0c9d2"/><path d="M178 80h44M178 100h44M178 120h44" stroke="#9c4a5f" stroke-width="3"/><path d="M142 130v14a58 58 0 0 0 116 0v-14" fill="none" stroke="#f0c9d2" stroke-width="9" stroke-linecap="round"/><path d="M200 202v32M162 240h76" stroke="#f0c9d2" stroke-width="9" stroke-linecap="round"/>`],
  backpack: ['#2f5a3d', '#142a1c', () => `<rect x="120" y="70" width="160" height="170" rx="40" fill="#8fd1a2"/><path d="M160 72c0-24 80-24 80 0" fill="none" stroke="#8fd1a2" stroke-width="10"/><rect x="146" y="150" width="108" height="64" rx="16" fill="#4b9a65"/><path d="M154 172h92" stroke="#8fd1a2" stroke-width="4"/><rect x="190" y="166" width="20" height="14" rx="3" fill="#f5b942"/><rect x="140" y="104" width="120" height="8" rx="4" fill="#4b9a65"/>`],
  bottle: ['#1c4f6b', '#0c2433', () => `<rect x="172" y="50" width="56" height="26" rx="8" fill="#19c3b1"/><rect x="180" y="76" width="40" height="22" fill="#9cd8ec"/><path d="M166 104c0-8 10-8 34-8s34 0 34 8v128c0 10-8 18-18 18h-32c-10 0-18-8-18-18z" fill="#bfe8f5"/><rect x="176" y="150" width="48" height="54" rx="8" fill="#1c4f6b"/><circle cx="200" cy="177" r="10" fill="#19c3b1"/>`],
  notebook: ['#5c5230', '#2b2514', () => { let d = ''; for (let r = 0; r < 7; r++) for (let c = 0; c < 6; c++) d += `<circle cx="${156 + c * 22}" cy="${96 + r * 22}" r="2.2" fill="#a69a62"/>`; return `<rect x="124" y="56" width="152" height="196" rx="8" fill="#f4eccb"/><rect x="124" y="56" width="22" height="196" rx="6" fill="#19c3b1"/>${d}<rect x="236" y="56" width="10" height="46" fill="#f5b942"/>`; }],
  lamp: ['#5e4a1f', '#2b200b', () => `<circle cx="256" cy="120" r="70" fill="#f5b942" opacity=".18"/><ellipse cx="148" cy="236" rx="58" ry="12" fill="#e9d6a4"/><path d="M148 232l40-92 70-34" fill="none" stroke="#e9d6a4" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M236 92l50 14-18 36z" fill="#f5d27a"/><circle cx="272" cy="134" r="8" fill="#fff6d6"/>`],
  webcam: ['#2a4a52', '#101f24', () => `<path d="M172 250h56l-12-48h-32z" fill="#9cc4cc"/><circle cx="200" cy="130" r="74" fill="#cfe4e8"/><circle cx="200" cy="130" r="52" fill="#16282e"/><circle cx="200" cy="130" r="30" fill="#1f5ea8"/><circle cx="188" cy="118" r="9" fill="#ffffff" opacity=".7"/><circle cx="262" cy="70" r="6" fill="#5be0a3"/>`]
};
function art(key) {
  const a = ART[key] || ART.keyboard, id = 'bg' + (uid++);
  return `<svg viewBox="0 0 400 300" role="img" aria-label="Illustration of ${esc(key)}" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="${id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${a[0]}"/><stop offset="1" stop-color="${a[1]}"/></linearGradient></defs><rect width="400" height="300" fill="url(#${id})"/><ellipse cx="200" cy="262" rx="120" ry="12" fill="#000" opacity=".25"/>${a[2]()}</svg>`;
}

/* ---------- views ---------- */
function card(p) {
  return `<article class="card"><a class="art" href="#/product/${p.id}" aria-label="View ${esc(p.name)}">${art(p.art)}</a>
  <div class="body"><span class="cat">${esc(p.category)}</span><h3><a href="#/product/${p.id}">${esc(p.name)}</a></h3>
  <div class="row">${stars(p.rating)}${stockTag(p)}</div>
  <div class="row actions"><span class="price">${money(p.priceCents)}</span>
  <button class="btn sm" data-add="${p.id}" ${p.stock === 0 ? 'disabled' : ''}>${p.stock === 0 ? 'Sold out' : 'Add to cart'}</button></div></div></article>`;
}

async function shop(params) {
  markNav('shop');
  const q = params.get('q') || '', cat = params.get('category') || '', sort = params.get('sort') || '';
  $('#q').value = q;
  main.innerHTML = '<div class="grid"><div class="skel"></div><div class="skel"></div><div class="skel"></div></div>';
  const qs = new URLSearchParams(); if (q) qs.set('q', q); if (cat) qs.set('category', cat); if (sort) qs.set('sort', sort);
  const list = await api('GET', '/products' + (qs.toString() ? '?' + qs : ''));
  const hero = (!q && !cat) ? `<section class="hero"><div><h1>Gear for people who <em>build things</em></h1><p>Keyboards, audio and desk upgrades picked for engineers. Free shipping over $75.</p><a class="btn" href="#grid">Start shopping</a> <a class="btn ghost" href="#/signin">Sign in to order</a></div><div class="art">${art('keyboard')}</div></section>` : '';
  const chip = (label, val) => `<button class="chip" data-cat="${esc(val)}" aria-pressed="${cat === val}">${esc(label)}</button>`;
  main.innerHTML = `${hero}<div class="bar" id="grid"><div class="chips" role="group" aria-label="Filter by category">${chip('All', '')}${state.categories.map(c => chip(c, c)).join('')}</div>
   <label class="count">Sort <select id="sort"><option value="">Featured</option><option value="price-asc">Price: low to high</option><option value="price-desc">Price: high to low</option><option value="rating">Top rated</option><option value="name">Name A to Z</option></select></label></div>
   <p class="count" aria-live="polite">${list.length} product${list.length === 1 ? '' : 's'}${q ? ' for “' + esc(q) + '”' : ''}${cat ? ' in ' + esc(cat) : ''}</p>
   ${list.length ? '<div class="grid">' + list.map(card).join('') + '</div>' : `<div class="empty"><svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#9bbdc0" stroke-width="1.6" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5M9 11h4"/></svg><h2>Nothing matches “${esc(q)}”</h2><p>Try a shorter word, or clear the filters.</p><a class="btn" href="#/">Show all products</a></div>`}`;
  $('#sort').value = sort;
  const nav = patch => { const n = new URLSearchParams({ q, category: cat, sort, ...patch }); [...n].forEach(([k, v]) => { if (!v) n.delete(k); }); go('#/' + (n.toString() ? '?' + n : '')); };
  main.querySelectorAll('[data-cat]').forEach(b => b.onclick = () => nav({ category: b.dataset.cat }));
  $('#sort').onchange = e => nav({ sort: e.target.value });
}

async function product(id) {
  markNav('shop');
  let p; try { p = await api('GET', '/products/' + id); } catch (e) { return notFound(e.message); }
  const inCart = (state.cart.items.find(i => i.productId === p.id) || {}).quantity || 0;
  let qty = 1; const max = Math.min(p.stock, 10);
  main.innerHTML = `<p class="crumbs"><a href="#/">Shop</a> / <a href="#/?category=${encodeURIComponent(p.category)}">${esc(p.category)}</a> / ${esc(p.name)}</p>
  <div class="detail"><div class="art">${art(p.art)}</div><div><span class="cat">${esc(p.category)}</span><h1>${esc(p.name)}</h1><div class="row" style="justify-content:flex-start;gap:14px">${stars(p.rating)}${stockTag(p)}</div>
  <div class="price">${money(p.priceCents)}</div><p>${esc(p.description)}</p>
  <div class="row" style="justify-content:flex-start;gap:14px"><div class="qty" role="group" aria-label="Quantity"><button id="dec" aria-label="Fewer">−</button><output id="qv" aria-live="polite">1</output><button id="inc" aria-label="More">+</button></div>
  <button class="btn" id="add" ${p.stock === 0 ? 'disabled' : ''}>${p.stock === 0 ? 'Sold out' : 'Add to cart'}</button></div>
  ${inCart ? `<p class="hint">You already have ${inCart} in your cart. <a href="#/cart">View cart</a></p>` : ''}
  <ul class="facts"><li>Free shipping over $75</li><li>Up to 10 per order line</li><li>Demo store: nothing is charged</li></ul></div></div>`;
  const out = $('#qv');
  $('#dec').onclick = () => { qty = Math.max(1, qty - 1); out.textContent = qty; };
  $('#inc').onclick = () => { qty = Math.min(max, qty + 1); out.textContent = qty; };
  $('#add').onclick = () => addToCart(p.id, qty);
}

async function addToCart(id, qty = 1) {
  try {
    state.cart = await api('POST', '/cart/items', { productId: id, quantity: qty });
    setBadge(); toast('Added to cart');
  } catch (e) { toast(e.message, true); }
}

function cartLines(c, editable) {
  return c.items.map(i => `<div class="line"><div class="art">${art(i.art)}</div><div><h3><a href="#/product/${i.productId}">${esc(i.name)}</a></h3><div class="sub">${money(i.priceCents)} each</div>
  ${editable ? `<div style="margin-top:8px"><div class="qty" role="group" aria-label="Quantity of ${esc(i.name)}"><button data-q="${i.productId}" data-d="-1" aria-label="Fewer">−</button><output>${i.quantity}</output><button data-q="${i.productId}" data-d="1" aria-label="More" ${i.quantity >= i.maxQuantity ? 'disabled' : ''}>+</button></div><button class="rm" data-rm="${i.productId}">Remove</button></div>` : `<div class="sub">Quantity ${i.quantity}</div>`}</div>
  <strong>${money(i.lineCents)}</strong></div>`).join('');
}
function summary(c) {
  const pct = Math.min(100, Math.round(c.subtotalCents / 75));
  return `<div class="sum"><div class="r"><span>Subtotal</span><span>${money(c.subtotalCents)}</span></div><div class="r"><span>Shipping</span><span>${c.shippingCents ? money(c.shippingCents) : 'Free'}</span></div><div class="r"><span>Tax (8%)</span><span>${money(c.taxCents)}</span></div><div class="r t"><span>Total</span><span>${money(c.totalCents)}</span></div></div>
  ${c.subtotalCents ? `<div class="meter" aria-hidden="true"><i style="width:${pct}%"></i></div><p class="hint">${c.freeShippingGapCents ? 'Add ' + money(c.freeShippingGapCents) + ' more for free shipping' : 'You unlocked free shipping'}</p>` : ''}`;
}

function cartView() {
  markNav('cart'); const c = state.cart;
  if (!c.count) { main.innerHTML = `<div class="empty"><svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="#9bbdc0" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2.5l2 11h11l2-8H7"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/></svg><h2>Your cart is empty</h2><p>Add something you like and it will wait here.</p><a class="btn" href="#/">Browse products</a></div>`; return; }
  main.innerHTML = `<h1 class="page">Your cart</h1><div class="layout"><section class="panel" aria-label="Cart items">${cartLines(c, true)}</section><aside class="panel"><h2>Order summary</h2>${summary(c)}<div style="margin-top:16px;display:grid;gap:10px"><a class="btn" href="#/checkout">Checkout</a><a class="btn ghost" href="#/">Keep shopping</a></div></aside></div>`;
  main.querySelectorAll('[data-q]').forEach(b => b.onclick = async () => {
    const it = c.items.find(i => i.productId == b.dataset.q), n = it.quantity + Number(b.dataset.d);
    try { state.cart = await api('PUT', '/cart/items/' + it.productId, { quantity: n }); setBadge(); cartView(); } catch (e) { toast(e.message, true); }
  });
  main.querySelectorAll('[data-rm]').forEach(b => b.onclick = async () => { state.cart = await api('DELETE', '/cart/items/' + b.dataset.rm); setBadge(); cartView(); toast('Removed from cart'); });
}

function checkout() {
  markNav('cart');
  if (!state.cart.count) return go('#/cart');
  if (!state.me.signedIn) { sessionStorage.setItem('after', '#/checkout'); toast('Please sign in to place your order'); return go('#/signin'); }
  const c = state.cart;
  main.innerHTML = `<h1 class="page">Checkout</h1><div class="layout"><form class="panel form" id="co" novalidate><h2>Shipping details</h2>
  <div class="demo"><b>Demo store.</b> Use any made-up address. No payment is taken and nothing is shipped.</div>
  <label>Full name<input class="f" name="name" autocomplete="name" value="${esc(state.me.name)}" required></label>
  <label>Street address<input class="f" name="address" autocomplete="street-address" placeholder="1 Main Street" required></label>
  <div class="two"><label>City<input class="f" name="city" autocomplete="address-level2" required></label><label>ZIP code<input class="f" name="zip" inputmode="numeric" maxlength="5" placeholder="78701" required></label></div>
  <p class="err" id="err" role="alert"></p><button class="btn" id="place">Place order · ${money(c.totalCents)}</button></form>
  <aside class="panel"><h2>Your items</h2>${cartLines(c, false)}<hr style="border:0;border-top:1px solid var(--line)">${summary(c)}</aside></div>`;
  $('#co').onsubmit = async e => {
    e.preventDefault(); const f = e.target, err = $('#err'); err.textContent = '';
    f.querySelectorAll('input').forEach(i => i.classList.remove('fieldErr'));
    const body = Object.fromEntries(new FormData(f));
    const missing = ['name', 'address', 'city'].find(k => !body[k].trim());
    if (missing) { f[missing].classList.add('fieldErr'); f[missing].focus(); err.textContent = 'Please fill in your ' + (missing === 'name' ? 'full name' : missing) + '.'; return; }
    if (!/^\d{5}$/.test(body.zip.trim())) { f.zip.classList.add('fieldErr'); f.zip.focus(); err.textContent = 'ZIP code must be 5 digits.'; return; }
    $('#place').disabled = true; $('#place').textContent = 'Placing order...';
    try {
      const o = await api('POST', '/orders', body); state.cart = await api('GET', '/cart'); setBadge(); confirmation(o);
    } catch (ex) { err.textContent = ex.message; $('#place').disabled = false; $('#place').textContent = 'Place order · ' + money(c.totalCents); if (ex.status === 401) go('#/signin'); }
  };
}

function confirmation(o) {
  main.innerHTML = `<div class="panel narrow done"><div class="tick"><svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#5be0a3" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>
  <h1 class="page" style="margin-bottom:6px">Thank you, order placed!</h1><p>Your order number is <b>${o.id}</b>.<br>Total ${money(o.totalCents)} for ${o.lines.reduce((n, l) => n + l.quantity, 0)} item(s), shipping to ${esc(o.city)}.</p>
  <p class="hint">Demo store: nothing was charged or shipped.</p><div style="display:flex;gap:10px;justify-content:center;margin-top:16px"><a class="btn" href="#/orders">View my orders</a><a class="btn ghost" href="#/">Keep shopping</a></div></div>`;
  window.scrollTo(0, 0);
}

async function ordersView() {
  markNav('orders');
  if (!state.me.signedIn) { sessionStorage.setItem('after', '#/orders'); return go('#/signin'); }
  const list = await api('GET', '/orders');
  if (!list.length) { main.innerHTML = `<div class="empty"><h2>No orders yet</h2><p>Orders you place will show up here.</p><a class="btn" href="#/">Browse products</a></div>`; return; }
  main.innerHTML = '<h1 class="page">Your orders</h1>' + list.map(o => `<section class="panel order"><header><h2>${o.id}</h2><span class="hint">${new Date(o.placedAt).toLocaleString()}</span></header>
  <table><thead><tr><th>Item</th><th>Qty</th><th>Price</th></tr></thead><tbody>${o.lines.map(l => `<tr><td>${esc(l.name)}</td><td>${l.quantity}</td><td>${money(l.priceCents * l.quantity)}</td></tr>`).join('')}</tbody></table>
  <div class="row" style="margin-top:12px"><span class="hint">Ships to ${esc(o.name)}, ${esc(o.address)}, ${esc(o.city)} ${esc(o.zip)}</span><strong>Total ${money(o.totalCents)}</strong></div></section>`).join('');
}

function signin() {
  markNav('signin');
  let mode = 'login';
  const draw = () => {
    main.innerHTML = `<div class="panel narrow"><div class="tabs" role="tablist"><button role="tab" aria-selected="${mode === 'login'}" data-m="login">Sign in</button><button role="tab" aria-selected="${mode === 'register'}" data-m="register">Create account</button></div>
    <div class="demo">Try the demo account:<br><b>student@cloudcart.test</b> / <b>learn-cloudcart</b> <button class="rm" id="fill" type="button">Fill it in</button></div>
    <form class="form" id="af" novalidate>${mode === 'register' ? '<label>Your name<input class="f" name="name" autocomplete="name" required></label>' : ''}
    <label>Email<input class="f" type="email" name="email" autocomplete="email" required></label>
    <label>Password${mode === 'register' ? ' (8+ characters)' : ''}<input class="f" type="password" name="password" autocomplete="${mode === 'login' ? 'current-password' : 'new-password'}" required></label>
    <p class="err" id="err" role="alert"></p><button class="btn">${mode === 'login' ? 'Sign in' : 'Create account'}</button></form></div>`;
    main.querySelectorAll('[data-m]').forEach(b => b.onclick = () => { mode = b.dataset.m; draw(); });
    $('#fill').onclick = () => { const f = $('#af'); f.email.value = 'student@cloudcart.test'; f.password.value = 'learn-cloudcart'; };
    $('#af').onsubmit = async e => {
      e.preventDefault(); const body = Object.fromEntries(new FormData(e.target));
      try {
        state.me = await api('POST', '/auth/' + mode, body); setAccount(); toast('Welcome, ' + state.me.name.split(' ')[0] + '!');
        const after = sessionStorage.getItem('after') || '#/'; sessionStorage.removeItem('after'); go(after);
      } catch (ex) { $('#err').textContent = ex.message; }
    };
  };
  draw();
}

async function signout() { await api('POST', '/auth/logout'); state.me = { signedIn: false }; setAccount(); toast('You are signed out'); go('#/'); }
function notFound(msg) { main.innerHTML = `<div class="empty"><h2>Page not found</h2><p>${esc(msg || 'That page does not exist.')}</p><a class="btn" href="#/">Back to the shop</a></div>`; }

/* ---------- router ---------- */
async function route() {
  const h = location.hash.slice(1) || '/', [path, qs] = h.split('?'), params = new URLSearchParams(qs || '');
  try {
    if (path === '/' || path === '') await shop(params);
    else if (path.startsWith('/product/')) await product(path.split('/')[2]);
    else if (path === '/cart') cartView();
    else if (path === '/checkout') checkout();
    else if (path === '/orders') await ordersView();
    else if (path === '/signin') signin();
    else if (path === '/signout') await signout();
    else notFound();
  } catch (e) { main.innerHTML = `<div class="empty"><h2>We could not load this page</h2><p>${esc(e.message)}</p><button class="btn" onclick="location.reload()">Try again</button></div>`; }
  document.title = 'CloudCart' + ({ '/cart': ' · Cart', '/checkout': ' · Checkout', '/orders': ' · Orders', '/signin': ' · Sign in' }[path] || '');
  if (!path.startsWith('/') || path !== '/' || !qs) window.scrollTo(0, 0);
}

document.addEventListener('click', e => { const b = e.target.closest('[data-add]'); if (b) addToCart(Number(b.dataset.add)); });
$('#search').onsubmit = e => { e.preventDefault(); const q = $('#q').value.trim(); go('#/' + (q ? '?q=' + encodeURIComponent(q) : '')); };

(async function start() {
  try {
    [state.me, state.cart, state.categories] = await Promise.all([api('GET', '/me'), api('GET', '/cart'), api('GET', '/categories')]);
    fetch('health').then(r => r.json()).then(h => { $('#ver').textContent = 'v' + h.version; }).catch(() => { });
  } catch (e) { /* the router shows the error */ }
  setAccount(); setBadge(); window.addEventListener('hashchange', route); route();
})();
