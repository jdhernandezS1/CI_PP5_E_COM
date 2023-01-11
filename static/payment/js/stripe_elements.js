/* 
Set your publishable key: remember to change this to your live publishable key in production
See your keys here: https://dashboard.stripe.com/apikeys
*/

var stripe_public_key = $('#id_strippe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'

        }
    },
    invalid: {
        color: '#000000',
        iconColor: '#000000'
    }
}
card.mount('#card-element', {
    style: style
});