// Módulos de bajo nivel
class StripeProcessor {
  pay(amount) { console.log(`Pagando $${amount} procesado vía Stripe.`); }
}

class PayPalProcessor {
  pay(amount) { console.log(`Pagando $${amount} procesado vía PayPal.`); }
}

// Módulo de alto nivel
class Store {
  // Inyectamos el procesador a través del constructor.
  // La tienda no sabe qué procesador es, solo sabe que tiene un método pay().
  constructor(paymentProcessor) {
    this.paymentProcessor = paymentProcessor;
  }

  purchase(item, amount) {
    console.log(`Comprando ${item}...`);
    this.paymentProcessor.pay(amount);
  }
}

// Uso: Podemos cambiar de Stripe a PayPal sin tocar el código de la clase Store.
const stripe = new StripeProcessor();
const miTienda = new Store(stripe);
miTienda.purchase("Teclado Mecánico", 120);

// Si mañana cambiamos a PayPal, es transparente:
// const paypal = new PayPalProcessor();
// const miTienda = new Store(paypal);
