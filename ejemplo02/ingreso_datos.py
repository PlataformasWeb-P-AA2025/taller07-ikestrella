from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Lee lo datos de los txt para clubes y jugadores
# Primero se ingresan los clubes
with open("data/datos_clubs.txt", 'r', encoding="utf-8") as a:
    # Se iteran las lineas
    for l in a:
        # Se separa por los delimitadores
        data = l.split(";")
        # Se crea el objeto tipo Club
        club = Club(nombre=data[0], deporte=data[1], fundacion=int(data[2]))
        # Se lo agrega a las session para subir la informacion
        session.add(club)

session.commit()

# Luego ingresan los jugadores
with open("data/datos_jugadores.txt", 'r', encoding="utf-8") as a:
    # Itera las lineas del txt de jugadores
    for l in a:
        data = l.split(";")
        # Se hace una consulta de los clubes segun el club del txt
        club = session.query(Club).filter_by(nombre=data[0]).one()
        # Se agrega el objeto obtenido de la consulta
        jugador = Jugador(nombre=data[3], dorsal=int(data[2]), posicion=data[1], club=club)
        session.add(jugador)

session.commit()