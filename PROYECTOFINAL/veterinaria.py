class Fisica:
    dni=''
    def __init__(self,dni):
        self.dni=dni
    
    #get de un atributo
    @property
    def dni(self):
         return self.__dni

    #Simular un set
    @dni.setter
    def dni(self, dni):
        self.__dni = dni


    def __str__(self):
        return f'Objeto Fisica : {self.dni}'

class Juridica:
    cif=''    
    def __init__(self,cif):
        self.cif=cif
    
    #get de un atributo
    @property
    def cif(self):
        return self.__cif

    #Simular un set
    @cif.setter
    def cif(self, cif):
        self.__cif = cif


    def __str__(self):
        return f'Objeto Juridica : {self.cif}' 

class Veterinario:
    
    def __init__(self):
        pass
    def __str__(self):
        return f'Objeto Veterinario :' 


class Auxiliar:
    
    def __init__(self):
        pass

    def __str__(self):
        return f'Objeto Veterinario '  


class ElementoHistorico:
    
    def __init__(self):
        pass
    def __str__(self):
        return f'Objeto Elemento Histórico'  
    
        

class Historico(ElementoHistorico):
    def __init__(self,refHistorico):
        super().__init__()
        self.refHistorico=refHistorico

#get de un atributo
    @property
    def refHistorico(self):
         return self.__refHistorico

    #Simular un set
    @refHistorico.setter
    def refHistorico(self, refHistorico):
        self.__refHistorico = refHistorico


    def __str__(self):
        return f'Objeto Historico : {self.refHistorico}'
         
class Personal(Veterinario,Auxiliar):
    
    def __init__(self,nombre_personal,apellidos,fecha_contratacion):
        Veterinario().__init__()
        Auxiliar().__init__()
        self.nombre_personal=nombre_personal
        self.apellidos=apellidos
        self.fecha_contratacion=fecha_contratacion

    @property
    def nombre_personal(self): 
        return self.__nombre_personal

    @nombre_personal.setter
    def nombre_personal(self,nombre_personal):
        self.__nombre_personal=nombre_personal 

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self,apellidos):
        self.__apellidos=apellidos

    @property
    def fecha_contratacion(self):
        return self.__fecha_contratacion

    @fecha_contratacion.setter
    def fecha_contratacion(self,fecha_contratacion):
        self.__fecha_contratacion=fecha_contratacion   

    def __str__(self):
        return f"Este es un objeto de tipo Personal: {self.nombre_personal} {self.apellidos} {self.fecha_contratacion}"        

class Persona(Juridica,Fisica):
    email=''
    direccion=''
    telefono=''
    def __init__(self, dni,cif,email,direccion,telefono):
        Juridica.__init__(self,cif)
        Fisica.__init__(self,dni)
        self.email=email
        self.direccion=direccion
        self.telefono=telefono
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email=email 

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self,direccion):
        self.__direccion=direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono           

    def __str__(self):
        return f'Objeto Persona : {self.email} {self.direccion} {self.telefono}{self.cif} {self.dni}'  

class Animal(Persona,Historico):
    def __init__(self, dni, cif, email, direccion, telefono,refHistorico,tipo,nombre,edad):
        Persona.__init__(self, dni, cif, email, direccion, telefono)
        Historico.__init__(self,refHistorico)
        self.tipo=tipo
        self.nombre=nombre
        self.edad=edad
    

    @property
    def tipo(self):
        return self.__tipo 

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        self.__edad=edad                       

    def __str__(self):
        return f'Objeto de tipo Animal: {self.tipo} {self.nombre} {self.edad} {self.direccion} {self.dni} {self.cif} {self.email} {self.telefono} {self.refHistorico} ' 


class Diagnostico(Personal,Animal):
    
    def __init__(self,personal,animal,fecha,descripcion):
        self.animal=animal
        self.personal=personal
        self.fecha=fecha
        self.descripcion=descripcion


    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self,fecha):
        self.__fecha=fecha

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion=descripcion
            
    def __str__(self):
        #return f'Objeto de tipo Diagnóstico: {self.nombre} {self.tipo} {self.edad} {self.dni} {self.cif}{self.nombre_personal} {self.email} {self.direccion} {self.descripcion} {self.fecha}' 
         return f'Objeto de tipo Diagnóstico: {self.animal} {self.personal} {self.fecha} {self.descripcion}'
class Factura(Diagnostico):
    def __init__(self,diagnostico,ref_factura):
        #super().__init__(self,personal, animal, fecha, descripcion)
        self.diagnostico=diagnostico
        self.ref_factura=ref_factura
        
    @property
    def ref_factura(self):
        return self.__ref_factura

    @ref_factura.setter
    def ref_factura(self,ref_factura):
        self.__ref_factura=ref_factura

    @property
    def diagnostico(self):
        return self.__diagnostico

    @diagnostico.setter
    def diagnostico(self,diagnostico):
        self.__diagnostico=diagnostico    

    def __str__(self):
        return f"Objeto de tipo Factura: {self.ref_factura} {self.diagnostico}"          

class ElementoFactura(Factura):
    def __init__(self, diagnostico, ref_factura,elemento,precio,cantidad):
        Factura.__init__(self,diagnostico, ref_factura)
        self.elemento=elemento
        self.precio=precio
        self.cantidad=cantidad
   
    @property
    def elemento(self):
        return self.__elemento

    @elemento.setter
    def elemento(self,elemento):
        self.__elemento=elemento

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,precio):
        self.__precio=precio     
     
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad=cantidad

    def __str__(self):
        return f'Objeto de tipo detalle factura:{self.ref_factura} {self.diagnostico} {self.elemento} {self.precio} {self.cantidad}'  

fisica_1=Fisica('1234567890')
juridica_1=Juridica('ee')

persona_1=Persona(dni=fisica_1.dni,cif=juridica_1.cif,email='ramiro.salas@gamil.com',direccion='Quito',telefono='121323')
elemento_historico=ElementoHistorico()
historico=Historico('ref')
vaterinario=Veterinario()
auxiliar=Auxiliar()
personal_1=Personal(nombre_personal='Roberto',apellidos='Bolaños',fecha_contratacion='2019-01-01')
animal_1=Animal(dni=persona_1.dni,cif=persona_1.cif,email=persona_1.email,direccion=persona_1.direccion,telefono=persona_1.telefono,tipo="Mestizo",nombre="Zeus",edad=12,refHistorico='asasad')
diagnostico_1=Diagnostico(personal=personal_1,animal=animal_1,fecha='2021-09-09',descripcion='Patita fracturada')
factura=Factura(diagnostico=diagnostico_1,ref_factura='ads')
detalle_Factura=ElementoFactura(diagnostico=diagnostico_1,ref_factura=factura.ref_factura,elemento='1',precio='50.00',cantidad=2)

print(detalle_Factura)