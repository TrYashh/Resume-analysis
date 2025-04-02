const wrapper = document.getElementById('wrapper');
const registerBtn = document.getElementById('registerBtn');
const loginBtn = document.getElementById('loginBtn');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');

registerBtn.addEventListener('click', () => {
  wrapper.classList.add('active');
});

loginBtn.addEventListener('click', () => {
  wrapper.classList.remove('active');
});