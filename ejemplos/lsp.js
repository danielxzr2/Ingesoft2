class Bird {
  eat() { console.log("Comiendo..."); }
}

class FlyingBird extends Bird {
  fly() { console.log("Volando..."); }
}

// El Águila puede volar, así que hereda de FlyingBird
class Eagle extends FlyingBird { }

// El Pingüino no vuela, así que solo hereda de Bird
class Penguin extends Bird {
  swim() { console.log("Nadando..."); }
}

function makeBirdFly(bird) {
  bird.fly();
}

const eagle = new Eagle();
makeBirdFly(eagle);

// const penguin = new Penguin();
// makeBirdFly(penguin); // Esto lanzaría un error a nivel de diseño antes, ahora simplemente no se lo permitimos porque no es un FlyingBird.
