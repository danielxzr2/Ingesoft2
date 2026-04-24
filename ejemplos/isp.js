// Comportamientos aislados
const canPrint = {
  print() { console.log("Imprimiendo documento..."); }
};

const canScan = {
  scan() { console.log("Escaneando documento..."); }
};

// Impresora básica: solo imprime. No la forzamos a tener un método scan() inútil.
const BasicPrinter = () => {
  return Object.assign({}, canPrint);
};

// Impresora multifunción: componemos ambos comportamientos.
const MultiFunctionPrinter = () => {
  return Object.assign({}, canPrint, canScan);
};

const miImpresora = BasicPrinter();
miImpresora.print();
// miImpresora.scan(); // Dará error porque no lo necesita ni lo tiene.
