const cart = document.getElementById('cart');
const cart_box = document.getElementById('cart_box');

cart.addEventListener('click', open_cart);

function open_cart(){
    if (cart_box.style.display==='none'){
        cart_box.style.display = 'flex';
    }
    else{
        cart_box.style.display = 'none';
    }
}
open_cart()