//Cada clase tiene un único propósito.

class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }
}

class UserRepository {
  saveToDatabase(user) {
    console.log(`Guardando a ${user.name} en la BD...`);
  }
}

class EmailService {
  sendWelcomeEmail(user) {
    console.log(`Enviando correo de bienvenida a ${user.email}...`);
  }
}

const user = new User("Daniel", "daniel@ejemplo.com");
const repo = new UserRepository();
const emailer = new EmailService();

repo.saveToDatabase(user);
emailer.sendWelcomeEmail(user);
