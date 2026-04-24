class Shape {
  area() {
    throw new Error("El método area() debe ser implementado");
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }
  area() { return this.width * this.height; }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }
  area() { return Math.PI * (this.radius ** 2); }
}

// Esta función NUNCA tendrá que ser modificada, incluso si agregamos Triángulos despues.
function calculateTotalArea(shapes) {
  return shapes.reduce((total, shape) => total + shape.area(), 0);
}

const shapes = [new Rectangle(10, 5), new Circle(5)];
console.log(calculateTotalArea(shapes));
