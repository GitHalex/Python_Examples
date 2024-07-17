class AgendaPersonal:
    def __init__(self):
        """Initialize the StudentManager with empty lists for names and grades."""
        self.names: str = []
        self.telefonos: int = []
        self.mails: str = []

    def menu(self) -> None:
        """Display the menu and process user choices."""
        while True:
            print("1- CARGA DE UN CONTACTO")
            print("2- LISTA COMPLETA DE LA AGENDA")
            print("3- CONSULTA EL NOMBRE DE CONTACTO")
            print("4- MODIFICACION DE SU TELEFONO Y EMAIL")
            print("5- FINALIZAR PROGRAMA")
            try:
                option = int(input("Enter your option: "))
                if option == 1:
                    self.add_contactos()
                elif option == 2:
                    self.list_contactos()
                elif option == 3:
                    self.list_consultaName()
                elif option == 4:
                    self.list_modificacion()
                elif option == 5:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def add_contactos(self) -> None:
        """Add constactos' names and grades to the lists."""
        num_students = int(input("How many students do you want to add? "))
        for _ in range(num_students):
            name = input("Enter the Contact's name: ")
            while True:
                try:
                    phone = int(input("Ingrese su telefono: "))
                    mail = input("Ingrese su correo: ")
                    break
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            self.names.append(name)
            self.telefonos.append(phone)
            self.mails.append(mail)

    def list_contactos(self) -> None:
        """List all students with their grades."""
        print("Complete list of contactos")
        for name, telefono, mail in zip(self.names, self.telefonos, self.mails):
            print(f"{name} => {telefono} => {mail}")
        print("_____________________")

    def list_consultaName(self) -> None:
        print("Consulta de nombre: ")
        nombreConsulta = input("Ingrese un nombre a consultar: ")

        if nombreConsulta in self.names:
            for name, telefono, mail in zip(self.names, self.telefonos, self.mails):
              if name == nombreConsulta:
                  print("El nombre existe!!! ")
                  print(f"{name} => {telefono} => {mail}")
        else:
            print(f"El nombre: {nombreConsulta} no existe en la lista: {self.names}")
        
          
    
    def list_modificacion(self) -> list:
        print("Ingrese le nombre y si hay lo vamos a modificar")
        nombreModificar = input("Ingrese el nombre para modificar solo si existe: ")
        if nombreModificar in self.names:
            print("El nombre existe!!! ")
            for i in range(len(self.names)):
              if self.names[i] == nombreModificar:
                  self.telefonos[i] = int(input("Ingrese su telefono actual: "))
                  self.mails[i] = input("Ingrese su nuevo correo")
        else:
            print(f"El nombre: {nombreModificar} no existe en la lista: {self.names}")
        

    

    """def list_high_grades(self) -> None:
        # List students with grades greater than or equal to 7.
        print("Students with grades >= 7:")
        for name, grade in zip(self.names, self.grades):
            if grade >= 7:
                print(f"{name}: {grade}")
        print("_____________________")"""


if __name__ == "__main__":
    manager = AgendaPersonal()
    manager.menu()
